import boto3

ec2 = boto3.resource("ec2")
try:
    running_instance = ec2.instances.filter(
        Filters=[{
            "Name": "instance-state-name",
            "Values": ["running"]
        }
        ]
        
    )
    print("running instance list")
    count = 0
    for instance in running_instance:
        print(f"instance id: {instance.id}")
        count+=1

    if count == 0:
        print("no instance is running currently")
except Exception as e:
    print("unable to connect to aws EC2 service", e)

