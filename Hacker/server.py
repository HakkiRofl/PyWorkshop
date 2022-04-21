import socket, random
app = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
app.bind (('127.0.0.1',8000))
app.listen(5)
client, (ip, port) = app.accept()

library = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while True:
    num = [random.choices(library) for _ in range(4)]
    num = num[0] + num[1] + num[2] + num[3]
    num = "".join(num)
    num = "zzzz"
    print(num)
    while True:
        data = client.recv(1024)
        if data.decode() == str(num):
            client.send("You connect to PyWorkshop!!".encode())
            break
        if not data:
            print("client connected: ", ip, port)
        else:
            client.send("WRONG".encode())



'''  
    'hello'.encode()
    data = data.decode()

    import socket

    with socket.socket() as client_socket:
        hostname = '127.0.0.1'
        port = 5000

        client_socket.connect((hostname, port))

        data = 'Wake up Neo'

        client_socket.send(data.encode())

        buffer = 1024
        response = client_socket.recv(buffer)
        response = response.decode()

        print(response)'''
