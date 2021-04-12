import boto3
import pprint
session=boto3.Session(profile_name="aws_ec2_iam_user",region_name="us-east-1")
ec2_re=session.resource(service_name="ec2")

print("Instance info with resource")
for each_in in ec2_re.instances.all():
	print(each_in.id,each_in.state['Name'])
print("Instances info with client")
for each in ec2_cli.describe_instances()['Reservations']:
	for each_in in each['Instances']:
		print(each_in['InstanceId'],each_in['State]['Name'])
