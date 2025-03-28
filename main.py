from pprint import pprint
from Google import Create_Service

CLIENT_SECRET_FILE = 'client-secret.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

part_string = 'contentDetails, statistics, snippet '
video_ids = 'lBvbNxiVmZA'

response =service.videos().list(
    part=part_string, 
    id=video_ids
).execute()

pprint(response)
print("Video CommentCount: " ,response['items'][0]['statistics']['commentCount'])

print("Video Duration: " ,response['items'][0]['contentDetails']['duration'])

print("Video ViewCount: " ,response['items'][0]['statistics']['viewCount'])

print("Video LikeCount: " ,response['items'][0]['statistics']['likeCount'])

print("Video channelTitle : " ,(response['items'][0]['snippet']['channelTitle']))

print("Video channelId : " ,response['items'][0]['snippet']['channelId'])

