import json
from collections import namedtuple
from Profile import Post

DataTuple = namedtuple('DataTuple', ['response', 'token'])

def extract_json(json_msg: str) -> DataTuple:
    '''
    Parses a JSON string and converts it to a DataTuple object.
    '''
    try:
        json_obj = json.loads(json_msg)
        # print('-------------')
        # print(json_obj)
        # print("----------")

        response = json_obj.get('response', {})
        token = response.get('token', None)

        # print('....respond:', response)
        print('....token:', token)
        
        return DataTuple(response, token)
    except json.JSONDecodeError:
        print("JSON cannot be decoded.")
        return DataTuple({}, None)

def join(username, password):
    '''
    Formats the join message to follow the DSP protocol.
    '''
    join_msg = json.dumps({
        "join": {
            "username": username,
            "password": password,
            "token": ""
        }
    })
    return join_msg

def post(token, message):

    '''
    Formats the post message to follow the DSP protocol.

    '''
    new_post = Post(entry=message)
    post_format = json.dumps({
        "token": token,
        "post": {
            "entry": message,
            "timestamp": new_post.timestamp  
        }
    })
    return post_format

def bio(token, bio):
    '''
    Formats the bio message to follow the DSP protocol.
    '''

    new_bio = Post(entry=bio)
    bio_format = json.dumps({
        "token": token,
        "bio": {
            "entry": bio,
            "timestamp": new_bio.timestamp 
        }
    })
    return bio_format