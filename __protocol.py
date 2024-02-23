# ds_protocol.py

# Ana Gao
# gaomy@uci.edu
# 26384258

import socket
import json
from collections import namedtuple
from Profile import Post

# Namedtuple to hold the values retrieved from json messages.
# TODO: update this named tuple to use DSP protocol keys
Connection = namedtuple('Connection', ['socket','send', 'recv'])

def extract_json(json_msg:str) -> Connection:
    '''
    Call the json.loads function on a json string and convert it to a DataTuple object
  
    TODO: replace the pseudo placeholder keys with actual DSP protocol keys
    '''
    try:
        json_obj = json.loads(json_msg)
        foo = json_obj['foo']
        baz = json_obj['bar']['baz']
    except json.JSONDecodeError:
        print("Json cannot be decoded.")

    return Connection(foo, baz)


class ProtocolError(Exception):
    pass


def join(username, password):
    join_msg = json.dumps({
        "join": {
            "username": username,
            "password": password,
            "token": ""
        }
    })
    return join_msg


def post(token, message):
    new_post = Post(entry=message)
    post_msg = json.dumps({
        "token": token,
        "post": {
            "entry": message,
            "timestamp": new_post.timestamp  
        }
    })
    return post_msg


def bio(token, bio):
    new_bio = Post(entry=bio)
    bio_msg = json.dumps({
        "token": token,
        "bio": {
            "entry": bio,
            "timestamp": new_bio.timestamp 
        }
    })
    return bio_msg