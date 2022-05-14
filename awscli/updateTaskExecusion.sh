#!/bin/sh

# before run this script, we need start a task. For example.
# aws datasync start-task-execution --cli-input-json file://override_start.json

taskArn="arn:aws:datasync:ap-northeast-1:911679503813:task/task-0c026111a1d2225f8"
taskExecutionArn=`aws datasync list-task-executions --task-arn $taskArn --query 'TaskExecutions[?Status==\`TRANSFERRING\`].TaskExecutionArn[]' --output text`

cat << EOM > override_update.json
{
    "TaskExecutionArn": "${taskExecutionArn}",
    "Options": {
        "BytesPerSecond": -1
    }
}
EOM

# aws datasync update-task-execution --cli-input-json file://override_update.json
