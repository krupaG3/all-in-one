import requests
import json
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/'
import time 
# time.sleep(5)
# print('get request started.....')
# def get_resource(id=None):
#     data={}
#     if id is not None:
#         data={
#             'id':id
#         }
#     resp=requests.get(BASE_URL+ENDPOINT,data=json.dumps(data))
#     print(resp.status_code)
#     print(resp.json())
# get_resource()
# time.sleep(5)
# print('post request started... ')

# def create_resource():
#     data={
#         'eno':105,
#         'ename':'Python World',
#         'esal':1000000,
#         'eaddr':'ROLLA'
#     }
#     resp=requests.post(BASE_URL+ENDPOINT,data=json.dumps(data))
#     print(resp.status_code)
#     print(resp.json())

# create_resource()
# time.sleep(5)
# print('update process started...')
def update_resource(id):
    data={
        'id':id,
        'ename':' KHAIF',
        'esal':99999,
        
    }
    resp=requests.put(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())
update_resource(1)
# time.sleep(5)
# print('delete process completed..')

# def delete_resource(id):
#     data={
#         'id':id
#     }
#     resp=requests.delete(BASE_URL+ENDPOINT,data=json.dumps(data))
#     print(resp.status_code)
#     print(resp.json())
# delete_resource(3)