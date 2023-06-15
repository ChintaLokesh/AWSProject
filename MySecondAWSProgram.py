import boto3
s3=boto3.resource("s3",aws_access_key_id="AKIAVQRYFTDWKYVT6DGL",aws_secret_access_key="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")

for bucket in s3.buckets.all():
    print(bucket.name)