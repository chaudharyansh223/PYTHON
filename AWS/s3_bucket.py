import boto3
s3 = boto3.client("s3")

def create_bucket():
    bucket_name = "24-10-py-bucket"
    try:
        s3.create_bucket(Bucket = bucket_name,CreateBucketConfiguration={
            "LocationConstraint": "ap-south-1"
        })
        print(f"bucket {bucket_name} has created")
        return bucket_name
    except Exception as e:
        print("failed to create bucket", e)
        
def upload_object(bucket_name):
    local_file_path = r"C:\Users\HP\Desktop\python\python_learning\file.txt"
    object_to_upload = "file.txt"
    try:
        s3.upload_file(
            Filename = local_file_path,
            Bucket = bucket_name,
            Key = object_to_upload
        )
        print(f"object {object_to_upload} has uploaded")
    except Exception as e:
        print("failed to upload object in bucket", e)


bucket_name = create_bucket()
if bucket_name:
    upload_object(bucket_name)
