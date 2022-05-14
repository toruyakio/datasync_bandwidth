import boto3

datasync = boto3.client('datasync')

def get_running_task_execution_arn(task_arn):
  response = datasync.list_task_executions(TaskArn=task_arn)
  task_executions = response["TaskExecutions"]
  for task_execution in task_executions:
    task_execution_arn = task_execution["TaskExecutionArn"]
    task_execution_status = task_execution["Status"]
    #
    # getting task execution from a given taskARN where TRANSFERRING only.
    # We can expect only one, since DataSync allow one task execution for each task 
    #
    if task_execution_status == "TRANSFERRING":
        return task_execution_arn

def get_task_execution_bandwidth(task_execution_arn):
    response = datasync.describe_task_execution(TaskExecutionArn=task_execution_arn)
    bytes_per_sec = response["Options"]["BytesPerSecond"]
    return bytes_per_sec

response = datasync.list_tasks()
tasks = response["Tasks"]

for task in tasks:
    task_arn = task["TaskArn"]
    print (task_arn)
    task_execution_arn = get_running_task_execution_arn(task_arn)
    if task_execution_arn == None:
        print ('nothing to do for this task at this stage')
        continue
    print (task_execution_arn)
    before_bw = get_task_execution_bandwidth(task_execution_arn)
    #
    # -1 means no limitation. That mean user want to release bandwidth limitation since something critical workload finished anymore.
    # if 20MB bandwidth limit, 20 * 1024 * 1024 = 20971520 as exaple
    # args={'BytesPerSecond': 20971520}
    #
    args={'BytesPerSecond': -1}
    response = datasync.update_task_execution(TaskExecutionArn=task_execution_arn, Options=args)
    after_bw = get_task_execution_bandwidth(task_execution_arn)
    print ('bandwidth limmit has been updated from {} to {}'.format(before_bw, after_bw))
