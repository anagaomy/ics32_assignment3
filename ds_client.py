# ds_client.py


import socket
import ds_protocol as dp



def send(server: str, port: int, username: str, password: str, message: str, bio: str = None):

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
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((server, port))
            print(f'Connected to {server} on port {port}')

            # Join
            join_msg = dp.join(username, password)  # Ensure this function returns the correct JSON payload
            client.sendall(join_msg.encode())
            response = client.recv(4096).decode()
            success, token = dp.extract_json(response)  # Adjusted to directly unpack success and token

            if not success:
                print('Join command was not successful')
                return False

            # Message
            if message and not message.isspace():
                post_msg = dp.post(token, message)  # Ensure this function returns the correct JSON payload
                client.sendall(post_msg.encode())
                print(client.recv(4096).decode())

            # Bio
            if bio and not bio.isspace():
                bio_msg = dp.bio(token, bio)  # Ensure this function returns the correct JSON payload
                client.sendall(bio_msg.encode())
                print(client.recv(4096).decode())

            return True

    except Exception as e:
        print(f'Error: {e}')
        return False

if __name__ == "__main__":
    server = "168.235.86.101"
    port = 3021
    username = "blackpink"
    password = "123"
    message = "blackpink in your area!!"
    bio = "yoooooo"

    if send(server, port, username, password, message, bio):
        print("Operation completed successfully.")
    else:
        print("Failed to complete the operation.")