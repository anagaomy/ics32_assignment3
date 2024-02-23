# ds_client.py

# Ana Gao
# gaomy@uci.edu
# 26384258


import socket 
import ds_protocol


def send(server:str, port:int, username:str, password:str, message:str, bio:str=None):
    '''
    The send function joins a ds server and sends a message, bio, or both

    :param server: The ip address for the ICS 32 DS server.
    :param port: The port where the ICS 32 DS server is accepting connections.
    :param username: The user name to be assigned to the message.
    :param password: The password associated with the username.
    :param message: The message to be sent to the server.
    :param bio: Optional, a bio for the user.
    '''
    #TODO: return either True or False depending on results of required operation

    try:
        client = connect_to_server(server, port)
        if client == None:
            print("ERROR")
            return False
        print("Client succeffully connected to " + f"{server} on {port}")

        while True:
            join_msg = ds_protocol.join(username, password)
            client.send.write(join_msg.encode())
            response = client.recv(8000).decode()
            _type, _token = ds_protocol.extract_json(response)

            if _type == "error":
                print(response)
                return False
            elif _type == "ok":
                if message and not message.isspace():
                    post_msg = ds_protocol.post(_token, message)
                    client.send.write(post_msg.encode())
                    print(client.recv(8000).decode())
                
                if bio and not bio.isspace():
                    bio_msg = ds_protocol.bio(_token, bio)
                    client.send.write(bio_msg.encode())
                    print(client.recv(8000).decode())

                return True
            
    except Exception:
        print("ERROR")
        return False


def connect_to_server(server, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((server, port))
            return client
    except:
        return None


if __name__ == "__main__":
    username = "blackpink"
    password = "123"
    message = "blackpink in your area!!"
    bio = "yoooooo"    
    server = input("Enter server IP address   : ")
    port = input("Enter server port         : ")

    if send(server, port, username, password, message, bio):
        print("Operation completed")
    else:
        print("Operation failed")
    
