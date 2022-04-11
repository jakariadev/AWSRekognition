import csv
import boto3
from botocore.exceptions import ClientError
import time
start_time = time.time()

try:
    start_time = time.time()
    # taking keys from the file
    with open('aws_access_keys.csv', 'r') as input:
        next(input)
        reader = csv.reader(input)
        for line in reader:
            access_key_id = line[0]
            secret_access_key = line[1]
    # Given photo to analysis
    ref_photo = 'jakaria.jpg'
    client = boto3.client('rekognition', aws_access_key_id = access_key_id,
    aws_secret_access_key = secret_access_key, region_name='ap-southeast-1')
    print("client created at: {}".format(client))

    #create collection
    def create(COLLECTION_NAME):
        print('Creating collection: {}'.format(COLLECTION_NAME))
        try:
            response = client.create_collection(CollectionId=COLLECTION_NAME)
            print('Colletion ARN: {}'.format(response['CollectionArn']))
            print('Status code: {}'.format(str(response['StatusCode'])))
            print('Collection: {} has been created.'.format(COLLECTION_NAME))
            st1 ='Collection: {} has been created.'.format(COLLECTION_NAME)
            return st1
        except client.exceptions.ResourceAlreadyExistsException:
            print('Collection: {} already exists.'.format(COLLECTION_NAME))
            st1='Collection: {} already exists.'.format(COLLECTION_NAME)
            return st1
        except ClientError as e:
            st="Cannot create / Don't give space for collection Name"
            return st

    # list of all collections
    def list_collections():
        try:
            print('Displaying collections...')
            response = client.list_collections()
            collections = response['CollectionIds']
            print(len(collections),collections)
            return len(collections),collections
        except ClientError as e:
            return 0,"Problem in client"

    create("FR_Collection_XXXXX")
    # list of all the collections
    list_collections()
    print("--- %s seconds ---" % (time.time() - start_time))

except ClientError as error:
    print("ERROR CODE: {} & MESAGE: {}".format(error.response, error.response['Error']['Message'] ))
