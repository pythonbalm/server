'''  ಊ
'''
# _____________________________My:

# _____________________________Or:
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('0.0.0.0',2222))
s.listen(10)
while True:
    conn, addr = s.accept()
    print(conn, addr)
    data = conn.recv(1024)
    if not data or data == "close":
        conn.close()
        break
    conn.send(data.upper())
    conn.close()
# _____________________________Or:
import socket
import os
s = socket.socket()
s.bind(('0.0.0.0', 2222))
s.listen(5)
for i in range(10):
    child = os.fork()
    if child == 0:
        while True:
            conn, addr = s.accept()
            data = conn.recv(1024)
            conn.send(data)
            conn.close()

# ______________________ Проверка:

# ==============================================================================================================
