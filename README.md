# UDP Server-Client Communication

This project demonstrates a simple UDP server-client communication setup in Python. The server listens for messages from clients on specific ports and processes the messages based on predefined rules. Clients send either permission or request messages and receive responses from the server.

## Requirements

- Python 3.x

## Server

The server listens on `localhost` and port `5000`. It processes messages from clients on specific ports (1234 and 3333) and maintains a list of permitted numbers.

### Rules for Server:

1. **Port 1234:**
   - Accepts messages starting with "permission".
   - Message should end with a digit and contain no unwanted characters (`()[]_+!,;:.&$#£>{§½}*`) or spaces after the keyword.
   - If the number is already permitted, it responds with "Already Permitted".
   - If the number is new, it adds the number to the list and responds with "Permission Accepted".
   - Otherwise, it responds with "Invalid Message".

2. **Port 3333:**
   - Accepts messages starting with "request".
   - Message should end with a digit and contain no unwanted characters (`()[]_+`) or spaces after the keyword.
   - If the number is in the list of permitted numbers, it responds with "Request Accepted".
   - Otherwise, it responds with "Request Rejected".
   - If the message does not meet the criteria, it responds with "Invalid Message".

3. **Other Ports:**
   - Responds with "Port is not allowed to communicate".

### Usage:

To start the server, run:
```bash
python server.py
```

## Client

The client allows users to send messages to the server and receive responses. The client prompts the user to enter a port number and a message.

### Usage:

To start the client, run:
```bash
python client.py
```

The client will ask for:
1. Port number to bind.
2. Messages to send to the server.

### Example Interaction:

1. Enter port number: `1234`
2. Enter a message: `permission123`
   - Response: `Permission Accepted` (if 123 is not already permitted)
   - Response: `Already Permitted` (if 123 is already permitted)

3. Enter port number: `3333`
4. Enter a message: `request123`
   - Response: `Request Accepted` (if 123 is in the permitted list)
   - Response: `Request Rejected` (if 123 is not in the permitted list)

## Notes

- The server accepts up to 4 different clients.
- If a message is invalid or from a non-allowed port, appropriate error messages are sent.
- Ensure the port numbers and message formats are correct for successful communication.
## Group Members:
- Feride Betül Çuhadar
- İrem Sıla Madenli 
- Doğa Durmaz 


