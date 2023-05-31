from dotenv import load_dotenv
import boto3
import pandas as pd
import os
import sys

load_dotenv()

aws_access_key_id_01=os.getenv('aws_access_key_id_01')
aws_secret_access_key_01=os.getenv('aws_secret_access_key_01')

print(f"aws_access_key_id_01 is {aws_access_key_id_01}")
print(f"aws_secret_access_key_01 is {aws_secret_access_key_01}")




# aws_access_key_id_01=os.environ["aws_access_key_id_01"]
# aws_secret_access_key_01=os.environ["aws_secret_access_key_01"]

# print(sys.argv[1])
# print(sys.argv[2])

# 1 st Argument="<your access key id>"
# 2nd Argument ="<your aws secret access key>" 

# aws_access_key_id_01=sys.argv[1]
# aws_secret_access_key_01=sys.argv[2]


# print(f"aws_access_key_id_01 is {aws_access_key_id_01}")
# print(f"aws_secret_access_key_01 is {aws_secret_access_key_01}")

#  upload the file to S3 Bucket

def uploadFile(awsFilePath:str,filename:str,aws_access_key_id:str,aws_secret_access_key:str,
            bucket_name:str,file_key:str):   
    s3 = boto3.client("s3",aws_access_key_id=aws_access_key_id,aws_secret_access_key=aws_secret_access_key)
    result = s3.list_objects_v2(Bucket=bucket_name, Prefix=file_key)
    if 'Contents' in result:
        print("file exists in the bucket.")
    else:
        s3.put_object(
    
            Bucket=bucket_name,
            Key=file_key,
            Body=filename,
        )
        print("file is uploaded successfully")


df=pd.read_excel("Files/Sample Spreadsheet.xlsx")
# print(df.head())
rows=df.shape[0]
cols=df.shape[1]

print(f"shape is {df.shape}")
print(f"rows is {rows}")
print(f"cols is {cols}")
for col in range(cols):
    print(f" first row {col+1 }  col is {df.iloc[0,col]}")
    print("---------")





#  Get the S3 Bucket Names

s3=boto3.resource("s3",aws_access_key_id=aws_access_key_id_01,aws_secret_access_key=aws_secret_access_key_01)

for bucket in s3.buckets.all():
    print(f"bucket name is {bucket.name}")

bucket_name="s301myawsbucket"
awsFilePath=df.iloc[0,0]+"/"+df.iloc[0,0+1]
file_key=awsFilePath+'/Test.xlsx'


print(f"boto3 version is {boto3.__version__}")
print(f"pandas version is {pd.__version__}")



uploadFile(awsFilePath,df.iloc[0,0+2],aws_access_key_id_01,aws_secret_access_key_01,bucket_name,file_key)