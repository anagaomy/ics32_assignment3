# ds_protocol.py

# Ana Gao
# gaomy@uci.edu
# 26384258

import socket
import json
from collections import namedtuple

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


def init(sock:socket) -> Connection:
    try:
        f_send = sock.makefile('w')
        f_recv = sock.makefile('r')
    except:
        raise ProtocolError("Invalid socket connection")

    return Connection(
        socket = sock,
        send = f_send,
        recv = f_recv
    )


def disconnect(_conn: Connection):
    _conn.send.close()
    _conn.recv.close()


def listen(_conn: Connection) -> str:
    return _read_command(_conn)


def error(_conn: Connection):
    return False


def complete(_conn: Connection):
    _write_command(_conn, str(1))


def _write_command(_conn: Connection, cmd: str):
    try:
        _conn.send.write(cmd + '\n')
        _conn.send.flush()
    except:
        raise ProtocolError
    

def send(_conn: Connection, cmd):
    _write_command(_conn, cmd)


def _read_command(_conn: Connection) -> str:
    cmd = _conn.recv.readline()[:-1]
    return cmd


def start_server(host_address: str, host_port: int):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv:
        srv.bind((host_address, host_port))
        srv.listen()

        print(f"Server listening on IP: {host_address} and port {host_port}")
        while True:
            connection, address = srv.accept()

            with connection:
                print(f"client connected from {address[0]}")
                _conn = init(connection)

                while True:
                    rec_msg = listen(_conn)
                    if rec_msg == '':
                        break

                    print("Message received from client: ", rec_msg)
                    try:
                        pass

                    except Exception:
                        print("ERROR")
                        break

                print("client disconnected")




if __name__ == "__main__":
    PORT = 3021
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    start_server(IPAddr, PORT)

