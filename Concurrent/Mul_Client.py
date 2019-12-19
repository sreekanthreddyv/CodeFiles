from multiprocessing.connection import Client
from array import array


address = ('localhost', 6000)

with Client(address, authkey=b'hacker') as conn:
    print(conn.recv())
    print(conn.recv_bytes())
