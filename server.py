#server
import socket
import re
def main():
    host = 'localhost'
    port = 5000
    permitted_numbers = []
    client_count = 0
    client_port = 0
    unwanted_characters = '()[]_+!,;:.&$#£>{§½}*'

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    client_count = 0

    while client_count < 4:
        # Receive the next message from the same client
        data, addr = server_socket.recvfrom(1024)
        message = data.decode()
        if client_port != addr[1]:
            client_count += 1
        client_port = addr[1]
        print(f"Message: '{message}'")
        print(f"Client Address: {addr}")

        if client_port == 1234:
            if message.lower().startswith("permission") and message[-1].isdigit() and not any(c in message for c in unwanted_characters)and ' ' not in message[10:]:
      
                num = int(''.join(filter(str.isdigit, message)))
                if num in permitted_numbers:
                    server_socket.sendto("Already Permitted".encode(), addr)
                else:
                    permitted_numbers.append(num)
                    server_socket.sendto("Permission Accepted".encode(), addr)
            else:
                server_socket.sendto("Invalid Message".encode(), addr)
        elif client_port == 3333:
            if message.lower().startswith("request") and message[-1].isdigit() and ' ' not in message[7:] and not re.search(r'[()\[\]_+]', message):
                num = int(''.join(filter(str.isdigit, message)))
                if num in permitted_numbers:
                    server_socket.sendto("Request Accepted".encode(), addr)
                else:
                  server_socket.sendto("Request Rejected".encode(), addr)
            else:
                 server_socket.sendto("Invalid Message".encode(), addr)
                

        else:
            server_socket.sendto("Port is not allowed to communicate".encode(), addr)


    print("The number of connected clients is:", client_count)
    server_socket.close()

if __name__ == '__main__':
    main()