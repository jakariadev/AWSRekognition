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
    ref_photo = 'sakib.jpg'
    comp_photo = 'musfiq.png'
    client = boto3.client('rekognition', aws_access_key_id = access_key_id,
    aws_secret_access_key = secret_access_key, region_name='ap-southeast-1')
    # detection portion with given image.
    with open(ref_photo, 'rb') as source_image:
        ref_source_bytes = source_image.read()
    with open(comp_photo, 'rb') as source_image2:
        comp_source_bytes = source_image2.read()

    # Compare faces
    response = client.compare_faces(
        SourceImage={'Bytes': ref_source_bytes},
        TargetImage={'Bytes': comp_source_bytes},
        QualityFilter='AUTO'
    )
    print("Response: ", response)
    for key, value in response.items():
        if key in ('FaceMatches','UnmatchedFaces'):
            print(key)
            for att in value:
                print(att)


except ClientError as error:
    print("ERROR CODE: {} & MESAGE: {}".format(error.response, error.response['Error']['Message'] ))
