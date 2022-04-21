import socket, datetime, time
library = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
adr = ('127.0.0.1', 8000)
app = socket.socket()
app.connect(adr)
while True:
    a = time.perf_counter()
    try:
        for i in library:
            for h in library:
                for g in library:
                    for k in library:
                        app.send((i + h + g + k).encode())
                        data = app.recv(1024)
                        if data.decode() == "You connect to PyWorkshop!!":
                            with open('checked.txt', 'a', encoding='utf-8') as file:
                                now = datetime.datetime.now()
                                b = time.perf_counter()
                                file.write(f"{now.strftime('%b %d, %Y')} - {adr} - {i + h + g + k} - {b - a} sec \n")
                            raise ConnectionResetError
        app.close()

    except ConnectionResetError:
        print("successful!")