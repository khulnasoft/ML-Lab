<!-- markdownlint-disable -->

<a href="https://github.com/khulnasoft/docknet/blob/main/components/lab-job-scheduler/backend/src/lab_job_scheduler/app.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `lab_job_scheduler.app`




**Global Variables**
---------------
- **CREATE_RESOURCE_RESPONSES**
- **JOB_INTERVAL**
- **DOCKNET_API_ENDPOINT**
- **cached_scheduled_jobs**
- **lock**

---

<a href="https://github.com/khulnasoft/docknet/blob/main/components/lab-job-scheduler/backend/src/lab_job_scheduler/app.py#L41"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `on_startup`

```python
on_startup() → None
```






---

<a href="https://github.com/khulnasoft/docknet/blob/main/components/lab-job-scheduler/backend/src/lab_job_scheduler/app.py#L70"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `create_schedule`

```python
create_schedule(
    project_id: str,
    job_input: ScheduledJobInput,
    component_manager: ComponentOperations = Depends(get_component_manager)
) → Any
```






---

<a href="https://github.com/khulnasoft/docknet/blob/main/components/lab-job-scheduler/backend/src/lab_job_scheduler/app.py#L98"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `list_schedules`

```python
list_schedules(project_id: str) → Any
```






---

<a href="https://github.com/khulnasoft/docknet/blob/main/components/lab-job-scheduler/backend/src/lab_job_scheduler/app.py#L116"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `list_schedule`

```python
list_schedule(project_id: str, job_id: str) → Any
```






---

<a href="https://github.com/khulnasoft/docknet/blob/main/components/lab-job-scheduler/backend/src/lab_job_scheduler/app.py#L138"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `delete_schedules`

```python
delete_schedules(
    project_id: str,
    component_manager: ComponentOperations = Depends(get_component_manager)
) → Any
```






---

<a href="https://github.com/khulnasoft/docknet/blob/main/components/lab-job-scheduler/backend/src/lab_job_scheduler/app.py#L155"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `delete_schedule`

```python
delete_schedule(
    project_id: str,
    job_id: str,
    component_manager: ComponentOperations = Depends(get_component_manager)
) → Any
```






---

<a href="https://github.com/khulnasoft/docknet/blob/main/components/lab-job-scheduler/backend/src/lab_job_scheduler/app.py#L179"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `update_schedule`

```python
update_schedule(
    project_id: str,
    job_input: ScheduledJobInput,
    job_id: str,
    component_manager: ComponentOperations = Depends(get_component_manager)
) → Any
```






---

<a href="https://github.com/khulnasoft/docknet/blob/main/components/lab-job-scheduler/backend/src/lab_job_scheduler/app.py#L209"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `executor_info`

```python
executor_info() → Any
```






---

<a href="https://github.com/khulnasoft/docknet/blob/main/components/lab-job-scheduler/backend/src/lab_job_scheduler/app.py#L221"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_all_scheduled_jobs_from_db`

```python
get_all_scheduled_jobs_from_db(
    component_manager: ComponentOperations,
    project_id: str
) → List[ScheduledJob]
```

Returns all jobs from the database. 


---

<a href="https://github.com/khulnasoft/docknet/blob/main/components/lab-job-scheduler/backend/src/lab_job_scheduler/app.py#L230"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_job_from_job_input`

```python
get_job_from_job_input(
    job_schedule: ScheduledJobInput,
    job_id: Optional[str] = None
) → ScheduledJob
```






---

<a href="https://github.com/khulnasoft/docknet/blob/main/components/lab-job-scheduler/backend/src/lab_job_scheduler/app.py#L242"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_next_run_time`

```python
get_next_run_time(job_schedule: ScheduledJobInput) → datetime
```

Returns the next run time of a job. 




---

_This file was automatically generated via [docsai](https://github.com/khulnasoft/docsai)._
