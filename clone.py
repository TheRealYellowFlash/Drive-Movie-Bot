import re
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from oauth2client.service_account import ServiceAccountCredentials
from httplib2 import Http
import random
from urllib.parse import quote, unquote, urlparse

def getid(url):
   folder_id = None

   pattern = r'https://drive\.google\.com/(?:' \
             r'drive/(?:u/[\d]+/)?(?:mobile/)?folders/([\w.\-_]+)(?:\?[\=\w]+)?|' \
             r'folderview\?id=([\w.\-_]+)(?:\&[=\w]+)?|' \
             r'open\?id=([\w.\-_]+)(?:\&[=\w]+)?|' \
             r'(?:a/[\w.\-_]+/)?file/d/([\w.\-_]+)|' \
             r'(?:a/[\w.\-_]+/)?uc\?id\=([\w.\-_]+)&?' \
             r')'

   x = re.search(pattern, url)
   if x:
       folder_id = ''.join(filter(None, x.groups()))
   return folder_id

def clonev1(url):  
    try:
        url = url.replace('/u/0','')
        id = getid(url)
        scopes = ['https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(f'Accounts/{random.randint(0, 99)}.json', scopes)
        http_auth = credentials.authorize(Http())
        service = build('drive', 'v3', http=http_auth)
        file = service.files().get(fileId=id,supportsAllDrives=True).execute()
        title = file.get("name")
        file2 = service.files().copy(fileId=id, body={"parents": ['0AJtbwLEZZtnjUk9PVA'], 'name': title},supportsAllDrives=True).execute()
        return f"https://clone2.yellowflash-cloud7775.workers.dev/0:/{quote(title)}"
    except Exception as e:
        print(e)
        print("bad link")


def details(url):
    url = url.replace('/u/0','')
    id = getid(url)
    scopes = ['https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(f'Accounts/{random.randint(0, 99)}.json', scopes)
    http_auth = credentials.authorize(Http())
    service = build('drive', 'v3', http=http_auth)
    file = service.files().get(fileId=id,supportsAllDrives=True).execute()
    title = file.get("name")
    
    return title
