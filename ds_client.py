# ds_client.py

# Ana Gao
# gaomy@uci.edu
# 26384258


import json
import socket
import ds_protocol


def send(server: str, port: int, username: str,
         password: str, message: str, bio: str = None):
    '''
    The send function joins a ds server and sends a message, bio, or both

    :param server: The ip address for the ICS 32 DS server.
    :param port: The port where the ICS 32 DS server is accepting connections.
    :param username: The user name to be assigned to the message.
    :param password: The password associated with the username.
    :param message: The message to be sent to the server.
    :param bio: Optional, a bio for the user.
    '''

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((server, port))
            if client is None:
                print("Error! Fail to connect to the server!")
                return False
            print("Client succeffully connected to " + f"{server} on {port}")

            join_msg = ds_protocol.join(username, password)
            client.sendall(join_msg.encode())
            response = client.recv(8000).decode()
            _type, _msg, _token = ds_protocol.extract_json(response)

            if _type == "error":
                print(_msg)
                return False

            elif _type == "ok":
                if message and not message == '' and not message.isspace():
                    post_msg = ds_protocol.post(_token, message)
                    client.sendall(post_msg.encode())
                    MSG = client.recv(8000).decode()
                    msg = json.loads(MSG)['response']['message']
                    print(msg)
                else:
                    print("ERROR! INVALID POST MESSAGE!")
                    return False

                if bio and not bio == '' and not bio.isspace():
                    bio_msg = ds_protocol.bio(_token, bio)
                    client.sendall(bio_msg.encode())
                    MSG = client.recv(8000).decode()
                    msg = json.loads(MSG)['response']['message']
                    print(msg)
                else:
                    print("ERROR! INVALID BIO!")
                    return False

                return True

    except Exception:
        print("ERROR")
        return False


# if __name__ == "__main__":
    # username = "ALBUM"
    # password = "123"
    # message = "HI"
    # bio = "cooool"
    # server = "168.235.86.101"
    # port = 3021
    # server = str(input("Enter server IP address   : "))
    # port = int(input("Enter server port         : "))

    # if send(server, port, username, password, message, bio):
        # print("Operation completed")
    # else:
        # print("Operation failed")
        # exit()
