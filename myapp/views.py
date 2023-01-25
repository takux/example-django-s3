# 追加
from django.http import HttpResponse
import boto3
from myconfig import settings

s3 = boto3.resource('s3')
bucket_name = settings.AWS_STORAGE_BUCKET_NAME
bucket = s3.Bucket(bucket_name)

filename = 'screenshot.png'
filepath = settings.BASE_DIR / filename


def upload_to_s3(request):
    bucket.upload_file(filepath, filename)
    return HttpResponse('upload complete')
