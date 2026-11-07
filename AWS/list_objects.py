import boto3

s3 = boto3.client("s3")
bucket_name = "1-11-bucket"

def get_object():
    try:
        response = s3.list_objects_v2(
            Bucket = "python-bucket"
        )
        object_list = response.get("content", [])
    
        if not object_list:
            print(f"Bucket '{bucket_name}' is totally empty")
        else:
            print(f"Bucket '{bucket_name}' objets")
        for object in object_list:
            object_name = object["Key"]
            object_size = object["Size"]
            print(f"Naam: {object_name} | Size: {object_size} bytes")
    except Exception:
        print("unable to connect to aws s3 microservcie", Exception)

get_object()
