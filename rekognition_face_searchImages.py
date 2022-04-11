import csv
import boto3
from botocore.exceptions import ClientError
import time
start_time = time.time()
# print("--- %s seconds ---" % (time.time() - start_time))
try:
    # taking keys from the file
    with open('aws_access_keys.csv', 'r') as input:
        next(input)
        reader = csv.reader(input)
        for line in reader:
            access_key_id = line[0]
            secret_access_key = line[1]
    # Given photo to analysis
    # ref_photo2 = 'jakaria.jpg' 
    ref_photo = 'opencv_frame_0.png'
    client = boto3.client('rekognition', aws_access_key_id = access_key_id,
    aws_secret_access_key = secret_access_key, region_name='ap-southeast-1')
    print("client created at: {}".format(client))

    # detection portion with provied image.
    with open(ref_photo, 'rb') as source_image:
        source_bytes = source_image.read()

    # For s3 Image link as input for indexing
    # ref_photo_name = 'public/rekognition_test/sny2.png'
    # Image={
    #     'S3Object': {
    #         'Bucket': 'XXXXXXXXXXXXXXXXXXX',
    #         'Name': ref_photo_name,
    #     },
    # },

    #Search by image
    response = client.search_faces_by_image(
        CollectionId="XXXXXXXXXXX",
        Image={'Bytes': source_bytes},
        MaxFaces=5,
        FaceMatchThreshold=70,
        QualityFilter='AUTO'
    )
    print("Search Image Response: {}".format(response))

    #search by faceid
    # response = client.search_faces(
    #     CollectionId='XXXXXXXXXXX',
    #     FaceId='d1554a5f-b0a8-4c00-8244-c0117dad9d75',
    #     MaxFaces=2,
    #     FaceMatchThreshold=80
    #     )
    # print("Search Image Response2: {}".format(response))

except ClientError as error:
    print("ERROR CODE: {} & MESAGE: {}".format(error.response, error.response['Error']['Message'] ))

print("--- %s seconds ---" % (time.time() - start_time))
