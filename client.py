import time
import socket

HOST = 'localhost'
PORT = 50007


def send():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b'>')
        data = s.recv(8)

    print('Received', repr(data))


start_process = time.process_time()
send()
print(f'Time process: {time.process_time() - start_process}')


start_perf = time.perf_counter()
send()
print(f'Time perf: {time.perf_counter() - start_perf}')


start_monotonic = time.monotonic()
send()
print(f'Time monotonic: {time.monotonic() - start_monotonic}')
