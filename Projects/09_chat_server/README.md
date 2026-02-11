# 💬 Project 9: Chat Server (CLI)

Build a multi-client chat server with chat rooms, nicknames, and private messaging. This project teaches you the fundamentals of network programming, threading, and real-time communication.

---

## 📋 Project Overview

This project helps you practice:
- TCP socket programming
- Multi-threading for concurrent clients
- Client-server architecture
- Protocol design and message parsing
- Real-time event broadcasting
- State management for multiple connections

### Features to Build

1. ✅ **TCP Socket Server**
   - Listen for client connections
   - Handle multiple clients simultaneously
   - Graceful client disconnection

2. ✅ **User Management**
   - Nickname registration
   - Unique nickname enforcement
   - User list tracking

3. ✅ **Chat Rooms**
   - Join/leave rooms
   - Room-specific messaging
   - List available rooms

4. ✅ **Messaging System**
   - Broadcast messages to all users
   - Room-specific messages
   - Private messages (whisper)

5. ✅ **Command System**
   - `/nick` - Change nickname
   - `/join` - Join a room
   - `/leave` - Leave current room
   - `/rooms` - List all rooms
   - `/users` - List users in current room
   - `/whisper` - Send private message
   - `/quit` - Disconnect from server

---

## 💻 Requirements

### Prerequisites

Complete these modules before starting:
- [00_getting_started](../../00_getting_started/README.md)
- [01_foundations](../../01_foundations/README.md)
- [04_oop_concepts](../../04_oop_concepts/README.md)
- [12_concurrency](../../12_concurrency/README.md)

### Skills You'll Use

- **socket Module** — TCP server and client connections
- **threading Module** — Handle multiple clients concurrently
- **Queue Module** — Thread-safe message passing
- **select Module** — Monitor multiple socket connections
- **Classes** — Organize server and client logic
- **String Parsing** — Parse commands and messages

---

## 🚀 Development Steps

### Step 1: Understanding the Architecture (15 minutes)

The chat server uses a client-server model:

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Client 1  │────▶│             │◀────│   Client 2  │
└─────────────┘     │    Chat     │     └─────────────┘
                    │   Server    │
┌─────────────┐     │             │     ┌─────────────┐
│   Client 3  │────▶│  (Threads)  │◀────│   Client 4  │
└─────────────┘     └─────────────┘     └─────────────┘
```

**Key Components:**
- **Server Socket** — Listens for new connections
- **Client Threads** — One thread per connected client
- **Message Queue** — Thread-safe message distribution
- **Room Manager** — Tracks users and rooms

### Step 2: Basic Server Setup (20 minutes)

Create a basic TCP server that accepts connections:

```python
import socket
import threading

class ChatServer:
    """Multi-client chat server."""
    
    def __init__(self, host='localhost', port=5555):
        self.host = host
        self.port = port
        self.server_socket = None
        self.clients = {}  # socket -> client_info
        self.running = False
    
    def start(self):
        """Start the chat server."""
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        self.running = True
        
        print(f"Chat server started on {self.host}:{self.port}")
        
        while self.running:
            try:
                client_socket, address = self.server_socket.accept()
                print(f"New connection from {address}")
                
                # Start new thread for client
                thread = threading.Thread(
                    target=self.handle_client,
                    args=(client_socket, address)
                )
                thread.daemon = True
                thread.start()
            except Exception as e:
                if self.running:
                    print(f"Error accepting connection: {e}")
    
    def handle_client(self, client_socket, address):
        """Handle a single client connection."""
        # Will be implemented in later steps
        pass
    
    def stop(self):
        """Stop the chat server."""
        self.running = False
        if self.server_socket:
            self.server_socket.close()
        print("Server stopped.")
```

### Step 3: Client Handler (25 minutes)

Implement the client handler that receives and processes messages:

```python
def handle_client(self, client_socket, address):
    """Handle a single client connection.
    
    Args:
        client_socket: Socket object for the client
        address: Tuple of (host, port) for the client
    """
    # Assign temporary nickname
    temp_nick = f"guest_{len(self.clients) + 1}"
    client_info = {
        'nickname': temp_nick,
        'room': 'lobby',
        'address': address
    }
    self.clients[client_socket] = client_info
    
    # Send welcome message
    self.send_to_client(client_socket, 
        f"Welcome! Your nickname is '{temp_nick}'. Use /nick <name> to change it.")
    
    # Broadcast join notification
    self.broadcast_message(f"{temp_nick} has joined the chat!", 
                          exclude=client_socket)
    
    # Main client loop
    while self.running:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            
            message = message.strip()
            if message.startswith('/'):
                self.handle_command(client_socket, message)
            else:
                # Regular chat message
                nick = self.clients[client_socket]['nickname']
                room = self.clients[client_socket]['room']
                self.broadcast_message(f"[{room}] {nick}: {message}")
                
        except ConnectionResetError:
            break
        except Exception as e:
            print(f"Error handling client {address}: {e}")
            break
    
    # Client disconnected
    self.remove_client(client_socket)

def remove_client(self, client_socket):
    """Remove a client from the server."""
    if client_socket in self.clients:
        nick = self.clients[client_socket]['nickname']
        del self.clients[client_socket]
        self.broadcast_message(f"{nick} has left the chat.")
        client_socket.close()
```

### Step 4: Command System (30 minutes)

Implement the command handling system:

```python
def handle_command(self, client_socket, command):
    """Process a command from a client.
    
    Args:
        client_socket: Socket that sent the command
        command: Command string starting with /
    """
    parts = command.split(' ', 1)
    cmd = parts[0].lower()
    args = parts[1] if len(parts) > 1 else ''
    
    client_info = self.clients.get(client_socket)
    if not client_info:
        return
    
    if cmd == '/nick':
        self.cmd_nick(client_socket, args)
    elif cmd == '/join':
        self.cmd_join(client_socket, args)
    elif cmd == '/leave':
        self.cmd_leave(client_socket)
    elif cmd == '/rooms':
        self.cmd_rooms(client_socket)
    elif cmd == '/users':
        self.cmd_users(client_socket)
    elif cmd == '/whisper':
        self.cmd_whisper(client_socket, args)
    elif cmd == '/help':
        self.cmd_help(client_socket)
    elif cmd == '/quit':
        self.cmd_quit(client_socket)
    else:
        self.send_to_client(client_socket, 
            f"Unknown command: {cmd}. Type /help for available commands.")

def cmd_nick(self, client_socket, nickname):
    """Change nickname."""
    nickname = nickname.strip()
    if not nickname:
        self.send_to_client(client_socket, "Usage: /nick <nickname>")
        return
    
    # Check if nickname is taken
    for info in self.clients.values():
        if info['nickname'].lower() == nickname.lower():
            self.send_to_client(client_socket, 
                f"Nickname '{nickname}' is already taken.")
            return
    
    old_nick = self.clients[client_socket]['nickname']
    self.clients[client_socket]['nickname'] = nickname
    self.send_to_client(client_socket, f"Nickname changed to '{nickname}'.")
    self.broadcast_message(f"{old_nick} is now known as {nickname}.",
                          exclude=client_socket)

def cmd_join(self, client_socket, room_name):
    """Join a chat room."""
    room_name = room_name.strip()
    if not room_name:
        self.send_to_client(client_socket, "Usage: /join <room>")
        return
    
    old_room = self.clients[client_socket]['room']
    nick = self.clients[client_socket]['nickname']
    
    # Leave current room
    self.broadcast_to_room(old_room, f"{nick} has left the room.")
    
    # Join new room
    self.clients[client_socket]['room'] = room_name
    self.send_to_client(client_socket, f"You joined room '{room_name}'.")
    self.broadcast_to_room(room_name, f"{nick} has joined the room.",
                          exclude=client_socket)

def cmd_leave(self, client_socket):
    """Leave current room and return to lobby."""
    old_room = self.clients[client_socket]['room']
    nick = self.clients[client_socket]['nickname']
    
    if old_room == 'lobby':
        self.send_to_client(client_socket, "You are already in the lobby.")
        return
    
    self.broadcast_to_room(old_room, f"{nick} has left the room.")
    self.clients[client_socket]['room'] = 'lobby'
    self.send_to_client(client_socket, "You returned to the lobby.")

def cmd_rooms(self, client_socket):
    """List all active rooms."""
    rooms = set(info['room'] for info in self.clients.values())
    if rooms:
        room_list = ', '.join(sorted(rooms))
        self.send_to_client(client_socket, f"Active rooms: {room_list}")
    else:
        self.send_to_client(client_socket, "No active rooms.")

def cmd_users(self, client_socket):
    """List users in current room."""
    current_room = self.clients[client_socket]['room']
    users = [info['nickname'] for info in self.clients.values() 
             if info['room'] == current_room]
    user_list = ', '.join(sorted(users))
    self.send_to_client(client_socket, 
        f"Users in {current_room}: {user_list}")

def cmd_whisper(self, client_socket, args):
    """Send private message."""
    parts = args.split(' ', 1)
    if len(parts) < 2:
        self.send_to_client(client_socket, "Usage: /whisper <user> <message>")
        return
    
    target_nick, message = parts
    target_nick = target_nick.strip()
    
    # Find target user
    target_socket = None
    for sock, info in self.clients.items():
        if info['nickname'].lower() == target_nick.lower():
            target_socket = sock
            break
    
    if not target_socket:
        self.send_to_client(client_socket, f"User '{target_nick}' not found.")
        return
    
    sender = self.clients[client_socket]['nickname']
    self.send_to_client(target_socket, f"[Whisper from {sender}]: {message}")
    self.send_to_client(client_socket, f"[Whisper to {target_nick}]: {message}")

def cmd_help(self, client_socket):
    """Show available commands."""
    help_text = """
Available commands:
  /nick <name>     - Change your nickname
  /join <room>     - Join a chat room
  /leave           - Leave current room
  /rooms           - List active rooms
  /users           - List users in current room
  /whisper <user> <msg> - Send private message
  /help            - Show this help
  /quit            - Disconnect from server
"""
    self.send_to_client(client_socket, help_text)

def cmd_quit(self, client_socket):
    """Disconnect from server."""
    self.send_to_client(client_socket, "Goodbye!")
    self.remove_client(client_socket)
```

### Step 5: Message Broadcasting (20 minutes)

Implement message distribution methods:

```python
def send_to_client(self, client_socket, message):
    """Send a message to a specific client.
    
    Args:
        client_socket: Target client socket
        message: Message string to send
    """
    try:
        client_socket.send(message.encode('utf-8'))
    except Exception as e:
        print(f"Error sending to client: {e}")

def broadcast_message(self, message, exclude=None):
    """Broadcast message to all connected clients.
    
    Args:
        message: Message string to broadcast
        exclude: Optional socket to exclude from broadcast
    """
    for client_socket in list(self.clients.keys()):
        if client_socket != exclude:
            self.send_to_client(client_socket, message)

def broadcast_to_room(self, room, message, exclude=None):
    """Broadcast message to all clients in a room.
    
    Args:
        room: Room name to broadcast to
        message: Message string to broadcast
        exclude: Optional socket to exclude
    """
    for client_socket, info in list(self.clients.items()):
        if info['room'] == room and client_socket != exclude:
            self.send_to_client(client_socket, message)
```

### Step 6: Chat Client (30 minutes)

Create the client application:

```python
import socket
import threading
import sys

class ChatClient:
    """Chat client for connecting to the chat server."""
    
    def __init__(self, host='localhost', port=5555):
        self.host = host
        self.port = port
        self.socket = None
        self.running = False
    
    def connect(self):
        """Connect to the chat server."""
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.host, self.port))
            self.running = True
            
            # Start receiving thread
            receive_thread = threading.Thread(target=self.receive_messages)
            receive_thread.daemon = True
            receive_thread.start()
            
            print(f"Connected to chat server at {self.host}:{self.port}")
            print("Type /help for available commands.\n")
            
            # Main input loop
            self.input_loop()
            
        except ConnectionRefusedError:
            print("Could not connect to server. Is it running?")
        except Exception as e:
            print(f"Connection error: {e}")
    
    def receive_messages(self):
        """Receive messages from the server (runs in separate thread)."""
        while self.running:
            try:
                message = self.socket.recv(1024).decode('utf-8')
                if not message:
                    print("\nDisconnected from server.")
                    self.running = False
                    break
                print(f"\n{message}")
                print("> ", end='', flush=True)
            except ConnectionResetError:
                print("\nConnection lost.")
                self.running = False
                break
            except Exception as e:
                if self.running:
                    print(f"\nError receiving message: {e}")
                break
    
    def input_loop(self):
        """Main input loop for sending messages."""
        while self.running:
            try:
                message = input("> ")
                if message.strip():
                    self.socket.send(message.encode('utf-8'))
                    
                    if message.strip().lower() == '/quit':
                        self.running = False
                        break
                        
            except KeyboardInterrupt:
                print("\nDisconnecting...")
                self.socket.send("/quit".encode('utf-8'))
                self.running = False
                break
            except Exception as e:
                print(f"Error sending message: {e}")
                break
        
        self.disconnect()
    
    def disconnect(self):
    """Disconnect from the server."""
        self.running = False
        if self.socket:
            self.socket.close()
        print("Disconnected.")


def main():
    """Entry point for the chat client."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Chat Client')
    parser.add_argument('--host', default='localhost', help='Server host')
    parser.add_argument('--port', type=int, default=5555, help='Server port')
    args = parser.parse_args()
    
    client = ChatClient(args.host, args.port)
    client.connect()


if __name__ == "__main__":
    main()
```

---

## 🧪 Testing

Test your chat server with these scenarios:

### 1. Basic Connection
```bash
# Terminal 1 - Start server
python chat_server.py

# Terminal 2 - Connect client
python chat_client.py

# Terminal 3 - Connect another client
python chat_client.py
```

### 2. Test Commands
```
> /nick alice
> /join general
> /rooms
> /users
> Hello everyone!
> /whisper bob Hi Bob!
> /leave
> /quit
```

### 3. Test Multiple Clients
- Connect 3+ clients
- Test broadcasting messages
- Test room isolation
- Test private messaging

### 4. Test Edge Cases
- Duplicate nicknames
- Invalid commands
- Empty messages
- Client disconnection
- Server shutdown with connected clients

---

## 🎯 Learning Checkpoints

After completing this project, you should understand:

- ✅ How TCP sockets work for client-server communication
- ✅ How to use threading for concurrent client handling
- ✅ How to design a simple text-based protocol
- ✅ How to manage shared state across threads
- ✅ How to broadcast messages to multiple clients
- ✅ How to handle client disconnections gracefully

---

## 🏆 Challenges

Complete these challenges to enhance your chat server:

1. **Message History** — Store and display recent messages when joining a room
2. **File Transfer** — Allow users to send files to each other
3. **Moderation** — Add kick/ban commands for room moderators
4. **Emojis** — Support emoji shortcodes like `:smile:` → 😄
5. **Logging** — Log all messages to a file with timestamps
6. **Authentication** — Add password-protected nicknames
7. **Server Admin** — Add admin commands for server management
8. **Rate Limiting** — Prevent spam by limiting message rate

See [challenges.md](challenges.md) for detailed instructions.

---

## 📁 File Structure

```
09_chat_server/
├── README.md              # This file
├── chat_server.py         # Server implementation
├── chat_client.py         # Client implementation
└── challenges.md          # Additional challenge tasks
```

---

## 🔧 Running the Project

### Start the Server
```bash
python chat_server.py
# Or with custom settings:
python chat_server.py --host 0.0.0.0 --port 8080
```

### Connect a Client
```bash
python chat_client.py
# Or connect to specific server:
python chat_client.py --host 192.168.1.100 --port 8080
```

---

**Ready to start?** Create `chat_server.py` and begin building! 🚀
