#client
import socket

def main():
     host = 'localhost'
     server_port = 5000

     while True:
          client_port = int(input("Enter port no: "))
          client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
          client_socket.bind((host, client_port))

          while True:
               message = input("Enter a message: ")
               client_socket.sendto(message.encode(), (host, server_port))

               data,addr = client_socket.recvfrom(1024)
               message=data.decode()
               
               if message == "Permission Accepted":
                    print("Permission Accepted")
               elif message == "Invalid Message":
                    print("Invalid Message")
               elif message == "Already Permitted":
                    print("Already Permitted")
               elif message == "Request Rejected":
                    print("Request Rejected")
               elif message == "Request Accepted":
                    print("Request Accepted")
               else:
                    print("Port is not allowed to communicate")
                    break

          client_socket.close()
          break

if __name__ == '__main__':
    main()