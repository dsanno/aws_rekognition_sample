# AWS Rekognition sample

see https://aws.amazon.com/jp/rekognition/getting-started/ for detail.

# Requirements

Python 2.7

# Set up environment

## Set up AWS Account

See "Step 1" of
https://aws.amazon.com/jp/rekognition/getting-started/

## Set up AWS credentials and config file

### Credentials file

Example: ~/.aws/credentials

```
[default]
aws_access_key_id = YOUR_KEY
aws_secret_access_key = YOUR_SECRET
```

### Config file

Example: ~/.aws/config

```
[default]
region=us-east-1
```

## Install [Boto 3 (AWS SDK for Python)](https://github.com/boto/boto3)

```
$ pip install boto3
```

# Usage

## Detect labels

```
$ python detect_labels.py [-f image_file_path] [-b s3_bucket] [-n s3_name] [-v s3_version]
```
