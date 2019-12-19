from multiprocessing.connection import Listener
from array import array


address = ('10.131.12.236', 6000)  # Family is deduced to be 'AF_INET'

with Listener(address, authkey=b'hacker') as listener:
    with listener.accept() as conn:
        print(f"Connection accepted from {listener.last_accepted}")
        conn.send([2, 25, None, 'junk', float])
        conn.send_bytes(b'hello')
        conn.send_bytes(array('i', [42, 345]))
