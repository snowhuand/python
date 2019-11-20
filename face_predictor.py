import os
import sys
import requests
import json
import getpass
#Get username, password and applicationid
username = input('Please input username: ')
#use getpass.getpass to hide user inputted password
password = getpass.getpass(prompt='Please input password: ')
appid = input('Please input appid: ')
#create authentication request URL, message and header
authenMsg = {'CreateServiceToken_Request_1': { 'ApplicationID':appid, 'Username':username,'Password':password }}
authenURL = 'https://hackattic.com/challenges/basic_face_detection'
headers = {'content-type': 'application/json;charset=utf-8'}
# send request
result = requests.post(authenURL, data = json.dumps(authenMsg), headers=headers)
# request success
if result.status_code == 200:
    print('Request success')
    print('response status %s'%(result.status_code))
    # get Token
    token = result.json()['CreateServiceToken_Response_1']['Token']
    print('Token: %s'%(token))
    # get expiraion
    expire = result.json()['CreateServiceToken_Response_1']['Expiration']
    print('Expire: %s'%(expire))
# handle error
else:
    print('Request fail')
    print('response status %s'%(result.status_code))
    if result.status_code == 500: # if username or password or appid is wrong
        print('Error: %s'%(result.json()))
    result.raise_for_status()