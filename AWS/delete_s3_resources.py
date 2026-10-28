import boto3

s3 = boto3.client("s3")

def delete_object():
    s3.delete_object(
          Bucket = "28-10-bucket",
          Key = "cloud-data.txt"
    )
    print("object deleted")
def delete_bucket():
        s3.delete_bucket(
              Bucket = "28-10-bucket"
        )
        print("bucket deleted")

delete_object()
delete_bucket()
