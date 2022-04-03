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
    ref_photo = 'jakaria.jpg'
    photo2 = 'jkr.jpg'
    ref_photo2 = 'jakariaWCM1.jpg'
    client = boto3.client('rekognition', aws_access_key_id = access_key_id,
    aws_secret_access_key = secret_access_key, region_name='ap-southeast-1')
    print("client created at: {}".format(client))

    # detection portion with provied image.
    with open(ref_photo2, 'rb') as source_image:
        source_bytes = source_image.read()

    #Search by image
    response = client.search_faces_by_image(
        CollectionId="XXXXXXXXXXXX",
        Image={'Bytes': source_bytes},
        MaxFaces=5,
        FaceMatchThreshold=70,
        QualityFilter='AUTO'
    )
    print("Search Image Response: {}".format(response))
    
except ClientError as error:
    print("ERROR CODE: {} & MESAGE: {}".format(error.response, error.response['Error']['Message'] ))
