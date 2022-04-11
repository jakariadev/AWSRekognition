import csv
import boto3
from botocore.exceptions import ClientError
import time
start_time = time.time()

try:
    # taking keys from the file
    with open('aws_access_keys.csv', 'r') as input:
        next(input)
        reader = csv.reader(input)
        for line in reader:
            access_key_id = line[0]
            secret_access_key = line[1]

    # CLient ready with AWS Rekognition
    client = boto3.client('rekognition', aws_access_key_id = access_key_id,
        aws_secret_access_key = secret_access_key, region_name='ap-southeast-1')

    # Given photo to analysis
    # ref_photo_name = 'jakaria.jpg'
    ref_photo_name = 'opencv_frame_0.png' #it has taken from camera [manual way]

    # Image to byte string convertion
    with open(ref_photo_name, 'rb') as source_image:
        source_bytes = source_image.read()

    # For s3 Image link as input for indexing
    # ref_photo_name = 'public/rekognition_test/sny2.png'
    # Image={
    #     'S3Object': {
    #         'Bucket': 'XXXXXXXXXXXXXXXXXXX',
    #         'Name': ref_photo_name,
    #     },
    # },


    # Image Indexing by s3/byte string image 
    response = client.index_faces(
        CollectionId= "XXXXXXXXXXXXXXXX", # Actually Collection Name
        Image={'Bytes': source_bytes},
        ExternalImageId='myphotoid',
        DetectionAttributes=[
            'ALL',
        ],
        MaxFaces=5,
        QualityFilter='AUTO'
        )

    print("indexed output: {}".format(response))
    print("--- %s seconds ---" % (time.time() - start_time))


except ClientError as error:
    print("ERROR CODE: {} & MESAGE: {}".format(error.response, error.response['Error']['Message'] ))
