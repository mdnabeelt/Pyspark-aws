import boto3
import json

client = boto3.client('emr', region_name='us-east-1')

response = client.run_job_flow(
    Name="Boto3 test cluster",
    ReleaseLabel='emr-6.3.0',
    Instances={
        'MasterInstanceType': 'm1.medium',
        'InstanceCount': 1,
        'KeepJobFlowAliveWhenNoSteps': True,
        'TerminationProtected': False,
        'Ec2KeyName': 'EMR Key Pair'
    },
    VisibleToAllUsers=True,
    ServiceRole='EMR_DefaultRole',
    JobFlowRole='EMR_EC2_DefaultRole',
    AutoScalingRole="EMR_AutoScaling_DefaultRole"
)

print(json.dumps(response, indent=4, sort_keys=True, default=str))