# bzt-s3-reader
[Taurus](https://gettaurus.org) plugin to load files from s3

## Installation

```bash
git clone https://github.com/cezkuj/bzt-s3-reader.git
cd bzts3reader/
pip install .
```
## Example of configuration file

```yaml
execution:
- executor: encarno
  concurrency: 5
  hold-for: 2m
  ramp-up: 1m
  throughput: 5
  scenario: simplest
scenarios:
  simplest:
    default-address: https://example.com
    requests: my_file.txt

services:
  - module: s3reader

modules:
    s3reader:
      #required
      bucket: my-bucket
      #required
      file: my_file.txt
```

## Configuration

bucket and file settings are required, [AWS credentials](#aws-authentication) will be read directly by boto3

## AWS Authentication

Plugin uses [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) as its depenedency and AWS credentials need to be configured according to their [docs](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html#configuring-credentials)
