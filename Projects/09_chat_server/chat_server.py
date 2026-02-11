"""
Chat Server - Multi-client TCP Chat Server
==========================================

A multi-threaded chat server that supports multiple clients,
chat rooms, nicknames, and private messaging.

Run: python chat_server.py [--host HOST] [--port PORT]
"""

import socket
import threading
import argparse
from datetime import datetime


class ChatServer:
    """
    Multi-client chat server with rooms and private messaging.
    
    Features:
    - Multiple concurrent clients via threading
    - Chat rooms with join/leave
    - Nickname management
    - Private messaging (whisper)
    - Command-based interface
    
    Attributes:
        host (str): Server host address
        port (int): Server port number
        server_socket: Main server socket
        clients (dict): Maps client sockets to their info
        rooms (dict): Maps room names to sets of client sockets
        running (bool): Server running state
        lock: Thread lock for shared state
    """
    
    def __init__(self, host='localhost', port=5555):
        """Initialize the chat server.
        
        Args:
            host: Host address to bind to (default: localhost)
            port: Port number to listen on (default: 5555)
        """
        self.host = host
        self.port = port
        self.server_socket = None
        self.clients = {}  # socket -> {'nickname': str, 'room': str, 'address': tuple}
        self.rooms = {'lobby': set()}  # room_name -> set of sockets
        self.running = False
        self.lock = threading.Lock()
        self.message_history = {}  # room -> list of recent messages
        self.max_history = 50  # Max messages to keep per room
    
    # =========================================================================
    # SERVER LIFECYCLE
    # =========================================================================
    
    def start(self):
        """Start the chat server and begin accepting connections."""
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(10)
            self.running = True
            
            print("=" * 60)
            print("        💬 CHAT SERVER STARTED 💬")
            print("=" * 60)
            print(f"Host: {self.host}")
            print(f"Port: {self.port}")
            print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print("=" * 60)
            print("\nWaiting for connections... (Ctrl+C to stop)\n")
            
            # Main accept loop
            while self.running:
                try:
                    client_socket, address = self.server_socket.accept()
                    
                    # Start new thread for client
                    thread = threading.Thread(
                        target=self.handle_client,
                        args=(client_socket, address),
                        daemon=True
                    )
                    thread.start()
                    
                except OSError:
                    # Socket closed during shutdown
                    break
                except Exception as e:
                    if self.running:
                        print(f"Error accepting connection: {e}")
                        
        except OSError as e:
            print(f"Failed to start server: {e}")
        except KeyboardInterrupt:
            print("\n\nShutdown signal received...")
        finally:
            self.stop()
    
    def stop(self):
        """Stop the chat server and disconnect all clients."""
        if not self.running:
            return
            
        print("\nShutting down server...")
        self.running = False
        
        # Disconnect all clients
        with self.lock:
            for client_socket in list(self.clients.keys()):
                try:
                    self.send_to_client(client_socket, "Server is shutting down. Goodbye!")
                    client_socket.close()
                except:
                    pass
            self.clients.clear()
            self.rooms = {'lobby': set()}
        
        # Close server socket
        if self.server_socket:
            try:
                self.server_socket.close()
            except:
                pass
        
        print("Server stopped.")
    
    # =========================================================================
    # CLIENT HANDLING
    # =========================================================================
    
    def handle_client(self, client_socket, address):
        """Handle a single client connection.
        
        This method runs in a separate thread for each client.
        It receives messages, processes commands, and handles disconnection.
        
        Args:
            client_socket: Socket object for the connected client
            address: Tuple of (host, port) for the client's address
        """
        # Assign temporary nickname
        with self.lock:
            guest_num = len(self.clients) + 1
            temp_nick = f"guest_{guest_num}"
            
            # Ensure unique nickname
            while any(info['nickname'] == temp_nick for info in self.clients.values()):
                guest_num += 1
                temp_nick = f"guest_{guest_num}"
            
            client_info = {
                'nickname': temp_nick,
                'room': 'lobby',
                'address': address,
                'joined_at': datetime.now()
            }
            self.clients[client_socket] = client_info
            self.rooms['lobby'].add(client_socket)
        
        # Log connection
        print(f"[CONNECT] {temp_nick} connected from {address[0]}:{address[1]}")
        
        # Send welcome message
        welcome = f"\n{'='*50}"
        welcome += f"\n  Welcome to the Chat Server!"
        welcome += f"\n  Your nickname: {temp_nick}"
        welcome += f"\n  Type /help for available commands"
        welcome += f"\n{'='*50}\n"
        self.send_to_client(client_socket, welcome)
        
        # Broadcast join notification
        self.broadcast_message(f"➡️ {temp_nick} has joined the lobby!", 
                              exclude=client_socket)
        
        # Main client loop
        while self.running:
            try:
                message = client_socket.recv(4096)
                if not message:
                    break
                
                message = message.decode('utf-8').strip()
                if not message:
                    continue
                
                if message.startswith('/'):
                    self.handle_command(client_socket, message)
                else:
                    # Regular chat message
                    self.handle_chat_message(client_socket, message)
                    
            except ConnectionResetError:
                break
            except ConnectionAbortedError:
                break
            except UnicodeDecodeError:
                self.send_to_client(client_socket, "Error: Invalid message encoding.")
            except Exception as e:
                if self.running:
                    print(f"Error handling client {address}: {e}")
                break
        
        # Client disconnected
        self.remove_client(client_socket)
    
    def remove_client(self, client_socket):
        """Remove a client from the server.
        
        Args:
            client_socket: Socket of the client to remove
        """
        with self.lock:
            if client_socket not in self.clients:
                return
                
            client_info = self.clients[client_socket]
            nickname = client_info['nickname']
            room = client_info['room']
            
            # Remove from structures
            del self.clients[client_socket]
            if room in self.rooms:
                self.rooms[room].discard(client_socket)
            
            # Clean up empty rooms (except lobby)
            empty_rooms = [r for r, clients in self.rooms.items() 
                          if not clients and r != 'lobby']
            for r in empty_rooms:
                del self.rooms[r]
        
        # Log disconnection
        print(f"[DISCONNECT] {nickname} disconnected")
        
        # Broadcast leave notification
        self.broadcast_message(f"⬅️ {nickname} has left the chat.")
        
        # Close socket
        try:
            client_socket.close()
        except:
            pass
    
    # =========================================================================
    # MESSAGE HANDLING
    # =========================================================================
    
    def handle_chat_message(self, client_socket, message):
        """Process a regular chat message from a client.
        
        Args:
            client_socket: Socket that sent the message
            message: Chat message content
        """
        with self.lock:
            if client_socket not in self.clients:
                return
            client_info = self.clients[client_socket]
            nickname = client_info['nickname']
            room = client_info['room']
        
        # Format message with timestamp
        timestamp = datetime.now().strftime('%H:%M:%S')
        formatted = f"[{timestamp}] [{room}] {nickname}: {message}"
        
        # Store in history
        self.add_to_history(room, formatted)
        
        # Broadcast to room
        self.broadcast_to_room(room, formatted)
    
    def handle_command(self, client_socket, command):
        """Process a command from a client.
        
        Args:
            client_socket: Socket that sent the command
            command: Command string starting with /
        """
        parts = command.split(' ', 1)
        cmd = parts[0].lower()
        args = parts[1].strip() if len(parts) > 1 else ''
        
        # Command routing
        commands = {
            '/nick': self.cmd_nick,
            '/join': self.cmd_join,
            '/leave': self.cmd_leave,
            '/rooms': self.cmd_rooms,
            '/users': self.cmd_users,
            '/whisper': self.cmd_whisper,
            '/w': self.cmd_whisper,  # Alias
            '/help': self.cmd_help,
            '/quit': self.cmd_quit,
            '/me': self.cmd_me,
            '/history': self.cmd_history,
            '/whois': self.cmd_whois,
        }
        
        handler = commands.get(cmd)
        if handler:
            handler(client_socket, args)
        else:
            self.send_to_client(client_socket, 
                f"❓ Unknown command: {cmd}. Type /help for available commands.")
    
    # =========================================================================
    # COMMANDS
    # =========================================================================
    
    def cmd_nick(self, client_socket, nickname):
        """Change nickname command.
        
        Usage: /nick <nickname>
        """
        nickname = nickname.strip()
        
        if not nickname:
            self.send_to_client(client_socket, "Usage: /nick <nickname>")
            return
        
        # Validate nickname
        if len(nickname) < 2 or len(nickname) > 20:
            self.send_to_client(client_socket, 
                "Nickname must be 2-20 characters long.")
            return
        
        if not nickname.replace('_', '').isalnum():
            self.send_to_client(client_socket, 
                "Nickname can only contain letters, numbers, and underscores.")
            return
        
        if nickname.lower().startswith('guest_'):
            self.send_to_client(client_socket, 
                "Cannot use 'guest_' prefix. Choose another nickname.")
            return
        
        # Check if nickname is taken
        with self.lock:
            for info in self.clients.values():
                if info['nickname'].lower() == nickname.lower():
                    self.send_to_client(client_socket, 
                        f"❌ Nickname '{nickname}' is already taken.")
                    return
            
            # Change nickname
            old_nick = self.clients[client_socket]['nickname']
            self.clients[client_socket]['nickname'] = nickname
        
        print(f"[NICK] {old_nick} -> {nickname}")
        self.send_to_client(client_socket, f"✅ Nickname changed to '{nickname}'.")
        self.broadcast_message(f"📝 {old_nick} is now known as {nickname}.",
                              exclude=client_socket)
    
    def cmd_join(self, client_socket, room_name):
        """Join a chat room command.
        
        Usage: /join <room>
        """
        room_name = room_name.strip().lower()
        
        if not room_name:
            self.send_to_client(client_socket, "Usage: /join <room>")
            return
        
        # Validate room name
        if len(room_name) > 30:
            self.send_to_client(client_socket, "Room name too long (max 30 chars).")
            return
        
        if not room_name.replace('_', '').replace('-', '').isalnum():
            self.send_to_client(client_socket, 
                "Room name can only contain letters, numbers, underscores, and hyphens.")
            return
        
        with self.lock:
            old_room = self.clients[client_socket]['room']
            nick = self.clients[client_socket]['nickname']
            
            if old_room == room_name:
                self.send_to_client(client_socket, 
                    f"You are already in room '{room_name}'.")
                return
            
            # Leave old room
            if old_room in self.rooms:
                self.rooms[old_room].discard(client_socket)
                # Clean up empty rooms
                if not self.rooms[old_room] and old_room != 'lobby':
                    del self.rooms[old_room]
            
            # Join new room
            if room_name not in self.rooms:
                self.rooms[room_name] = set()
            self.rooms[room_name].add(client_socket)
            self.clients[client_socket]['room'] = room_name
        
        print(f"[JOIN] {nick} -> {room_name}")
        
        # Notify rooms
        self.broadcast_to_room(old_room, f"⬅️ {nick} has left the room.")
        self.send_to_client(client_socket, f"✅ You joined room '{room_name}'.")
        self.broadcast_to_room(room_name, f"➡️ {nick} has joined the room.",
                              exclude=client_socket)
        
        # Show recent history
        self.show_history(client_socket, room_name, count=5)
    
    def cmd_leave(self, client_socket, args):
        """Leave current room and return to lobby.
        
        Usage: /leave
        """
        with self.lock:
            old_room = self.clients[client_socket]['room']
            nick = self.clients[client_socket]['nickname']
            
            if old_room == 'lobby':
                self.send_to_client(client_socket, 
                    "You are already in the lobby. Use /join <room> to join a room.")
                return
            
            # Leave room
            if old_room in self.rooms:
                self.rooms[old_room].discard(client_socket)
                if not self.rooms[old_room]:
                    del self.rooms[old_room]
            
            # Return to lobby
            self.rooms['lobby'].add(client_socket)
            self.clients[client_socket]['room'] = 'lobby'
        
        print(f"[LEAVE] {nick} left {old_room}")
        self.broadcast_to_room(old_room, f"⬅️ {nick} has left the room.")
        self.send_to_client(client_socket, "✅ You returned to the lobby.")
    
    def cmd_rooms(self, client_socket, args):
        """List all active rooms.
        
        Usage: /rooms
        """
        with self.lock:
            if not self.rooms:
                self.send_to_client(client_socket, "No active rooms.")
                return
            
            room_list = []
            for room_name, clients in sorted(self.rooms.items()):
                count = len(clients)
                room_list.append(f"  {room_name} ({count} user{'s' if count != 1 else ''})")
        
        message = "\n📋 Active Rooms:\n" + "\n".join(room_list)
        self.send_to_client(client_socket, message)
    
    def cmd_users(self, client_socket, args):
        """List users in current room or specified room.
        
        Usage: /users [room]
        """
        args = args.strip()
        
        with self.lock:
            if args:
                # List users in specified room
                if args not in self.rooms:
                    self.send_to_client(client_socket, 
                        f"Room '{args}' does not exist.")
                    return
                room = args
            else:
                # List users in current room
                room = self.clients[client_socket]['room']
            
            users = []
            for sock, info in self.clients.items():
                if info['room'] == room:
                    marker = " (you)" if sock == client_socket else ""
                    users.append(f"  {info['nickname']}{marker}")
        
        message = f"\n👥 Users in {room}:\n" + "\n".join(sorted(users))
        self.send_to_client(client_socket, message)
    
    def cmd_whisper(self, client_socket, args):
        """Send private message to a user.
        
        Usage: /whisper <user> <message>
        """
        parts = args.split(' ', 1)
        
        if len(parts) < 2:
            self.send_to_client(client_socket, 
                "Usage: /whisper <user> <message>")
            return
        
        target_nick, message = parts
        target_nick = target_nick.strip()
        message = message.strip()
        
        if not message:
            self.send_to_client(client_socket, "Message cannot be empty.")
            return
        
        # Find target user
        target_socket = None
        with self.lock:
            sender_nick = self.clients[client_socket]['nickname']
            for sock, info in self.clients.items():
                if info['nickname'].lower() == target_nick.lower():
                    target_socket = sock
                    break
        
        if not target_socket:
            self.send_to_client(client_socket, 
                f"❌ User '{target_nick}' not found.")
            return
        
        if target_socket == client_socket:
            self.send_to_client(client_socket, 
                "You can't whisper to yourself!")
            return
        
        # Send whisper
        timestamp = datetime.now().strftime('%H:%M:%S')
        self.send_to_client(target_socket, 
            f"[{timestamp}] 💬 [Whisper from {sender_nick}]: {message}")
        self.send_to_client(client_socket, 
            f"[{timestamp}] 💬 [Whisper to {target_nick}]: {message}")
        
        print(f"[WHISPER] {sender_nick} -> {target_nick}")
    
    def cmd_me(self, client_socket, action):
        """Send an action message.
        
        Usage: /me <action>
        """
        action = action.strip()
        
        if not action:
            self.send_to_client(client_socket, "Usage: /me <action>")
            return
        
        with self.lock:
            nick = self.clients[client_socket]['nickname']
            room = self.clients[client_socket]['room']
        
        timestamp = datetime.now().strftime('%H:%M:%S')
        formatted = f"[{timestamp}] [{room}] * {nick} {action}"
        
        self.broadcast_to_room(room, formatted)
    
    def cmd_history(self, client_socket, args):
        """Show message history for current room.
        
        Usage: /history [count]
        """
        try:
            count = int(args.strip()) if args.strip() else 10
            count = min(count, 50)  # Max 50 messages
        except ValueError:
            count = 10
        
        with self.lock:
            room = self.clients[client_socket]['room']
        
        self.show_history(client_socket, room, count)
    
    def cmd_whois(self, client_socket, nickname):
        """Show information about a user.
        
        Usage: /whois <nickname>
        """
        nickname = nickname.strip()
        
        if not nickname:
            self.send_to_client(client_socket, "Usage: /whois <nickname>")
            return
        
        with self.lock:
            target_info = None
            for info in self.clients.values():
                if info['nickname'].lower() == nickname.lower():
                    target_info = info
                    break
        
        if not target_info:
            self.send_to_client(client_socket, 
                f"❌ User '{nickname}' not found.")
            return
        
        # Show user info
        info_lines = [
            f"\n📋 User Info: {target_info['nickname']}",
            f"  Room: {target_info['room']}",
            f"  Address: {target_info['address'][0]}",
            f"  Joined: {target_info['joined_at'].strftime('%H:%M:%S')}",
        ]
        self.send_to_client(client_socket, "\n".join(info_lines))
    
    def cmd_help(self, client_socket, args):
        """Show available commands.
        
        Usage: /help
        """
        help_text = """
╔══════════════════════════════════════════════════════════╗
║                    AVAILABLE COMMANDS                     ║
╠══════════════════════════════════════════════════════════╣
║  /nick <name>      Change your nickname                  ║
║  /join <room>      Join a chat room                      ║
║  /leave            Leave current room (return to lobby)  ║
║  /rooms            List all active rooms                 ║
║  /users [room]     List users in room                    ║
║  /whisper <u> <m>  Send private message                  ║
║  /me <action>      Send an action message                ║
║  /history [n]      Show last n messages (default: 10)    ║
║  /whois <user>     Show information about a user         ║
║  /help             Show this help message                ║
║  /quit             Disconnect from server                ║
╚══════════════════════════════════════════════════════════╝
"""
        self.send_to_client(client_socket, help_text)
    
    def cmd_quit(self, client_socket, args):
        """Disconnect from server.
        
        Usage: /quit
        """
        self.send_to_client(client_socket, "👋 Goodbye!")
        self.remove_client(client_socket)
    
    # =========================================================================
    # BROADCASTING
    # =========================================================================
    
    def send_to_client(self, client_socket, message):
        """Send a message to a specific client.
        
        Args:
            client_socket: Target client socket
            message: Message string to send
        """
        try:
            client_socket.send(message.encode('utf-8'))
        except Exception as e:
            # Client likely disconnected
            pass
    
    def broadcast_message(self, message, exclude=None):
        """Broadcast message to all connected clients.
        
        Args:
            message: Message string to broadcast
            exclude: Optional socket to exclude from broadcast
        """
        with self.lock:
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
        with self.lock:
            if room not in self.rooms:
                return
            for client_socket in self.rooms[room]:
                if client_socket != exclude:
                    self.send_to_client(client_socket, message)
    
    # =========================================================================
    # HISTORY
    # =========================================================================
    
    def add_to_history(self, room, message):
        """Add a message to room history.
        
        Args:
            room: Room name
            message: Formatted message to store
        """
        with self.lock:
            if room not in self.message_history:
                self.message_history[room] = []
            self.message_history[room].append(message)
            
            # Keep only last N messages
            if len(self.message_history[room]) > self.max_history:
                self.message_history[room] = self.message_history[room][-self.max_history:]
    
    def show_history(self, client_socket, room, count=10):
        """Show message history for a room.
        
        Args:
            client_socket: Client to send history to
            room: Room name
            count: Number of messages to show
        """
        with self.lock:
            if room not in self.message_history or not self.message_history[room]:
                self.send_to_client(client_socket, 
                    f"No message history for room '{room}'.")
                return
            
            history = self.message_history[room][-count:]
        
        header = f"\n📜 Last {len(history)} messages in {room}:"
        self.send_to_client(client_socket, header)
        for msg in history:
            self.send_to_client(client_socket, f"  {msg}")


def main():
    """Entry point for the chat server."""
    parser = argparse.ArgumentParser(
        description='Multi-client Chat Server',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python chat_server.py                    # Start on localhost:5555
  python chat_server.py --port 8080        # Start on localhost:8080
  python chat_server.py --host 0.0.0.0     # Accept connections from all interfaces
        """
    )
    parser.add_argument('--host', default='localhost', 
                       help='Host address to bind to (default: localhost)')
    parser.add_argument('--port', type=int, default=5555,
                       help='Port to listen on (default: 5555)')
    
    args = parser.parse_args()
    
    server = ChatServer(host=args.host, port=args.port)
    
    try:
        server.start()
    except KeyboardInterrupt:
        print("\n\nShutting down...")
        server.stop()


if __name__ == "__main__":
    main()
