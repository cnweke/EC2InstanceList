import boto3


def list_ec2_instances():
    session = boto3.Session(
        aws_access_key_id='YOUR_ACCESS_KEY',
        aws_secret_access_key='SECRET_KEY',
        region_name='REGION'
        # we're creating a session
    )

    ec2 = session.resource('ec2')

    instances = ec2.instances.all()

    # Print every instance ID and state
    for instance in instances:
        print(f'Instance ID: {instance.id}, State: {instance.state["Name"]} ')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    list_ec2_instances()


