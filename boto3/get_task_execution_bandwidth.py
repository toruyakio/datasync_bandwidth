import boto3

datasync = boto3.client('datasync')

task_execution_arn = "arn:aws:datasync:ap-northeast-1:911679503813:task/task-0c026111a1d2225f8/execution/exec-0ba70503645fbb4eb"
task_execution_arn = "arn:aws:datasync:ap-northeast-1:911679503813:task/task-0c026111a1d2225f8/execution/exec-061a490da01a93ee1"
response = datasync.describe_task_execution(TaskExecutionArn=task_execution_arn)
#options = response["Options"]
#bytes_per_sec = options["BytesPerSecond"]
bytes_per_sec = response["Options"]["BytesPerSecond"]
print (bytes_per_sec)
