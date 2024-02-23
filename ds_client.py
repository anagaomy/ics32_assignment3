# ds_client.py

# Ana Gao
# gaomy@uci.edu
# 26384258


import socket 


def _send_(server:str, port:int, username:str, password:str, message:str, bio:str=None):
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
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((server, port))

        send = client.makefile("w")
        recv = client.makefile("r")

        print("Client succeffully connected to " + f"{server} on {port}")

        while True:
            msg = message
            send.write(msg + "\r\n")
            send.flush()

            srv_msg = recv.readline()[:-1]
            print("Response received from server: ", srv_msg)

    return 


if __name__ == "__main__":
    print("Welcome! \n")
    srv_ip = input("Enter server IP address   : ")
    srv_port = input("Enter server port         : ")
    
