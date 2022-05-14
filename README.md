# Changing DataSync bandwidth
learning how to change datasync bandwidth on the fly

This repo is for a sample which enable me to change DataSync bandwidth value for a given task execution which has been already started. 

How to use:

Python 3 environment with AWS credential for boto3.
- https://aws.amazon.com/jp/sdk-for-python/
- https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html

1. download or clone this repository
2. run your DataSync task execution (manually or scheduled)
3. ```% python3 updateTaskExecution.py```

使い方

前提：任意のタスクを作成する

AWS CLIは、1タスクに対応している。

override_start.json
タスクを実行するときに、事前に定義したものを上書きして実行したい場合に利用。
意図としては、スケジュール化すると1hに一回なので待っていられないから、マニュアル実行して、かつ、帯域を狭く、またALLにして更新がなくてもファイルを送るようにしている。

```
% aws datasync start-task-execution --cli-input-json file://override_start.json
```

この例ではあえて帯域幅を狭くして実行するもの。そして、

```
% aws datasync list-task-executions --task-arn $taskArn

% aws datasync list-task-executions --task-arn arn:aws:datasync:ap-northeast-1:911679503813:task/task-0c026111a1d2225f8
```

でそのタスクにおけるtask execution一覧が見れる。

これを実行している最中にTransferingになったら、帯域をもとに戻す。

CLIの場合が、updateTaskExecution.sh で override_update.jsonを得てから、

```
% aws datasync update-task-execution --cli-input-json file://override_update.json
```

SDK（python）の場合が、
```
% python3 updateTaskExecution.py
```
こちらは、存在するタスクすべてから、今動いているものを探して帯域を変更する
