import csv
import boto3
from botocore.exceptions import ClientError

try:
    # taking keys from the file
    with open('aws_access_keys.csv', 'r') as input:
        next(input)
        reader = csv.reader(input)
        for line in reader:
            access_key_id = line[0]
            secret_access_key = line[1]
    # Given photo to analysis
    ref_photo = 'musfiq.png'
    client = boto3.client('rekognition', aws_access_key_id = access_key_id,
    aws_secret_access_key = secret_access_key, region_name='ap-southeast-1')
    # detection portion with given image.
    with open(ref_photo, 'rb') as source_image:
        ref_source_bytes = source_image.read()
    # Compare faces
    response = client.detect_text(
        Image={'Bytes': ref_source_bytes},
    )
    print("Response: ", response)

except ClientError as error:
    print("ERROR CODE: {} & MESAGE: {}".format(error.response, error.response['Error']['Message'] ))
