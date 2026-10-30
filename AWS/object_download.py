import boto3

s3 = boto3.client("s3")

def download_object():
    try:
        s3.download_file(
            Bucket = "30-10-download",
            Key = "1111Screenshot_Timestamps.xlsx",
            Filename = "bucket-file"
        )
        print("object downloaded")
    except Exception:
        print("couldn't download object")

download_object()
