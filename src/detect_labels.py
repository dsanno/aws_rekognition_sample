import argparse
import base64
import boto3

parser = argparse.ArgumentParser('Detect labels')
parser.add_argument('--file-path', '-f', type=str, default=None, help='Image file path')
parser.add_argument('--bucket', '-b', type=str, default=None, help='S3 bucket')
parser.add_argument('--name', '-n', type=str, default=None, help='S3 name')
parser.add_argument('--version', '-v', type=str, default=None, help='S3 version')
args = parser.parse_args()

client = boto3.client('rekognition')

image = {}

if args.file_path:
    with open(args.file_path, 'rb') as f:
        image['Bytes'] = f.read()

s3_object = {}
if args.bucket:
    s3_object['Bucket'] = args.bucket
if args.name:
    s3_object['Name'] = args.name
if args.version:
    s3_object['Version'] = args.version
if s3_object:
    image['S3Object'] = s3_object

res = client.detect_labels(Image=image)
print(res)
