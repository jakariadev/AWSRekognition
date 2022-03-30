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
            print(access_key_id,secret_access_key)
    # Given photo to analysis
    photo = 'isfe.jpeg'
    client = boto3.client('rekognition', aws_access_key_id = access_key_id,
    aws_secret_access_key = secret_access_key, region_name='ap-southeast-1')
    # detection portion with provied image.
    with open(photo, 'rb') as source_image:
        source_bytes = source_image.read()
        # print("SOURCE BYTES:",source_bytes)
    # face detection
    response = client.detect_faces(Image={'Bytes': source_bytes}, Attributes=['ALL',])
    print("Response:", response)
    for key, value in response.items():
        if key == 'FaceDetails':
            for people_att in value:
                print(people_att)
                print("++++++++++++")

except ClientError as error:
    print("ERROR CODE: {} & MESAGE: {}".format(error.response, error.response['Error']['Message'] ))
