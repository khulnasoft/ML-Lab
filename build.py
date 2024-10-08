"""Root build.py for the ML Lab project. Will also execute the build.py in sub-directories."""

import os
import re
from argparse import ArgumentParser

from ml_buildkit import build_utils
from ml_buildkit.helpers import build_docker, build_python, openapi_utils

HERE = os.path.abspath(os.path.dirname(__file__))

LAB_COMPONENTS = "components"
WEBAPP_COMPONENT = "webapp"
DOCS_COMPONENT = "docs"

PROJECT_NAME = "lab-backend"


def update_docknet_version(file_path, docknet_version):
    with open(file_path, "r+") as f:
        data = f.read()
        f.seek(0)
        f.write(re.sub(r'\"docknet([^=]*)==[^\"]*\"', fr'"docknet\1=={docknet_version}"', data))
        f.truncate()


def update_mllab_version_in_docker_compose_file(file_path, mllab_version):
    with open(file_path, "r+") as f:
        content = f.read()
        f.seek(0)
        updated_content = re.sub(
            r'ghcr.io/khulnasoft/ml-lab/(.*):.*',
            fr'ghcr.io/khulnasoft/ml-lab/\1:{mllab_version}', content
        )
        f.write(updated_content)
        f.truncate()


def main(args: dict) -> None:
    """Execute all component builds."""

    # set script path as working dir
    os.chdir(HERE)

    version = args.get(build_utils.FLAG_VERSION)

    docknet_version = args.get("docknet-version")
    if docknet_version:
        update_docknet_version("./Dockerfile", docknet_version)

    # Build all ML Lab components
    build_utils.build(LAB_COMPONENTS, args)

    # Build the webapp
    build_utils.build(WEBAPP_COMPONENT, args)

    # Build the docs
    build_utils.build(DOCS_COMPONENT, args)

    # Build ML Lab docker image
    if args.get(build_utils.FLAG_MAKE):
        build_docker.build_docker_image(PROJECT_NAME, version, exit_on_error=True)

    # TODO: Uncomment when dockerfile is finalized
    # if args.get(build_utils.FLAG_CHECK):
    # build_docker.lint_dockerfile(exit_on_error=True)

    if args.get(build_utils.FLAG_RELEASE):
        update_mllab_version_in_docker_compose_file("deployment/mllab-docker/docker-compose.yml", version)
        build_docker.release_docker_image(
            PROJECT_NAME,
            args[build_utils.FLAG_VERSION],
            "ghcr.io/khulnasoft/ml-lab",
        )


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        f"--docknet-version", help="Version of the docknet library to use."
    )
    args = build_utils.parse_arguments(argument_parser=parser)

    if args.get(build_utils.FLAG_RELEASE):
        # Run main without release to see whether everything can be built and all tests run through
        args = dict(args)
        args[build_utils.FLAG_RELEASE] = False
        main(args)
        # Run main again without building and testing the components again
        args = {
            **args,
            build_utils.FLAG_MAKE: False,
            build_utils.FLAG_CHECK: False,
            build_utils.FLAG_TEST: False,
            build_utils.FLAG_RELEASE: True,
            build_utils.FLAG_FORCE: True,
        }
    main(args)
