"""
Chat Client - TCP Chat Client
==============================

A command-line chat client for connecting to the chat server.
Supports all server commands and provides a clean interface.

Run: python chat_client.py [--host HOST] [--port PORT]
"""

import socket
import threading
import sys
import argparse
import select
from datetime import datetime


class ChatClient:
    """
    Chat client for connecting to the chat server.
    
    Features:
    - Connect to chat server
    - Send and receive messages
    - Command support
    - Clean CLI interface
    - Graceful disconnection
    
    Attributes:
        host (str): Server host address
        port (int): Server port number
        socket: Client socket connection
        running (bool): Client running state
        nickname (str): Current nickname
    """
    
    def __init__(self, host='localhost', port=5555):
        """Initialize the chat client.
        
        Args:
            host: Server host address (default: localhost)
            port: Server port number (default: 5555)
        """
        self.host = host
        self.port = port
        self.socket = None
        self.running = False
        self.nickname = None
        self.current_room = None
    
    # =========================================================================
    # CONNECTION
    # =========================================================================
    
    def connect(self):
        """Connect to the chat server."""
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.settimeout(5)  # Connection timeout
            
            print(f"Connecting to {self.host}:{self.port}...")
            self.socket.connect((self.host, self.port))
            
            self.socket.settimeout(None)  # Remove timeout for normal operation
            self.running = True
            
            # Start receiving thread
            receive_thread = threading.Thread(target=self.receive_messages, daemon=True)
            receive_thread.start()
            
            # Main input loop
            self.input_loop()
            
        except socket.timeout:
            print("❌ Connection timed out. Is the server running?")
        except ConnectionRefusedError:
            print("❌ Connection refused. Is the server running?")
        except socket.gaierror:
            print(f"❌ Invalid host address: {self.host}")
        except Exception as e:
            print(f"❌ Connection error: {e}")
        finally:
            self.disconnect()
    
    def disconnect(self):
        """Disconnect from the server."""
        if not self.running:
            return
        
        self.running = False
        
        if self.socket:
            try:
                self.socket.close()
            except:
                pass
        
        print("\nDisconnected from server.")
    
    # =========================================================================
    # MESSAGE HANDLING
    # =========================================================================
    
    def receive_messages(self):
        """Receive messages from the server (runs in separate thread)."""
        while self.running:
            try:
                message = self.socket.recv(4096)
                if not message:
                    # Server closed connection
                    print("\n❌ Server closed the connection.")
                    self.running = False
                    break
                
                message = message.decode('utf-8')
                
                # Update local state based on server messages
                self.update_state(message)
                
                # Display message
                self.display_message(message)
                
            except ConnectionResetError:
                print("\n❌ Connection lost.")
                self.running = False
                break
            except ConnectionAbortedError:
                # Normal disconnection
                break
            except OSError:
                # Socket closed
                break
            except Exception as e:
                if self.running:
                    print(f"\n❌ Error receiving message: {e}")
                break
    
    def update_state(self, message):
        """Update local state based on server messages.
        
        Args:
            message: Message from server
        """
        # Track nickname changes
        if "Your nickname:" in message:
            try:
                self.nickname = message.split("Your nickname: ")[1].split()[0]
            except:
                pass
        
        if "Nickname changed to" in message:
            try:
                self.nickname = message.split("'")[1]
            except:
                pass
        
        # Track room changes
        if "You joined room" in message:
            try:
                self.current_room = message.split("'")[1]
            except:
                pass
        
        if "returned to the lobby" in message:
            self.current_room = "lobby"
    
    def display_message(self, message):
        """Display a received message.
        
        Args:
            message: Message to display
        """
        # Clear current input line and reprint
        print(f"\r{message}")
        if self.running:
            print(f"{self.get_prompt()}", end='', flush=True)
    
    def get_prompt(self):
        """Get the input prompt string.
        
        Returns:
            str: Formatted prompt
        """
        if self.nickname and self.current_room:
            return f"[{self.nickname}@{self.current_room}]> "
        elif self.nickname:
            return f"[{self.nickname}]> "
        return "> "
    
    def send_message(self, message):
        """Send a message to the server.
        
        Args:
            message: Message to send
        """
        try:
            self.socket.send(message.encode('utf-8'))
        except Exception as e:
            print(f"\n❌ Error sending message: {e}")
            self.running = False
    
    # =========================================================================
    # INPUT HANDLING
    # =========================================================================
    
    def input_loop(self):
        """Main input loop for sending messages."""
        print("\n" + "=" * 50)
        print("Connected! Type /help for available commands.")
        print("=" * 50 + "\n")
        
        while self.running:
            try:
                # Get user input
                message = input(self.get_prompt())
                
                if not message.strip():
                    continue
                
                # Handle local commands
                if message.strip().lower() in ['/quit', '/exit']:
                    self.send_message('/quit')
                    self.running = False
                    break
                
                if message.strip().lower() in ['/clear', '/cls']:
                    self.clear_screen()
                    continue
                
                # Send to server
                self.send_message(message)
                
            except KeyboardInterrupt:
                print("\n\nDisconnecting...")
                self.send_message('/quit')
                self.running = False
                break
            except EOFError:
                # Handle Ctrl+D
                print("\n\nDisconnecting...")
                self.send_message('/quit')
                self.running = False
                break
            except Exception as e:
                if self.running:
                    print(f"\n❌ Error: {e}")
                break
    
    def clear_screen(self):
        """Clear the terminal screen."""
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n" + "=" * 50)
        print("Chat Client - Screen Cleared")
        print("=" * 50 + "\n")


class ChatClientNonBlocking:
    """
    Alternative chat client using select for non-blocking I/O.
    
    This version uses select to check for input without blocking,
    providing a more responsive interface.
    """
    
    def __init__(self, host='localhost', port=5555):
        """Initialize the chat client.
        
        Args:
            host: Server host address
            port: Server port number
        """
        self.host = host
        self.port = port
        self.socket = None
        self.running = False
        self.nickname = None
        self.current_room = None
    
    def connect(self):
        """Connect to the chat server."""
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.settimeout(5)
            
            print(f"Connecting to {self.host}:{self.port}...")
            self.socket.connect((self.host, self.port))
            self.socket.settimeout(None)
            self.socket.setblocking(False)
            
            self.running = True
            
            print("\n" + "=" * 50)
            print("Connected! Type /help for available commands.")
            print("Press Ctrl+C to disconnect.")
            print("=" * 50 + "\n")
            
            self.main_loop()
            
        except socket.timeout:
            print("❌ Connection timed out.")
        except ConnectionRefusedError:
            print("❌ Connection refused.")
        except Exception as e:
            print(f"❌ Connection error: {e}")
        finally:
            self.disconnect()
    
    def main_loop(self):
        """Main loop using select for non-blocking I/O."""
        import sys
        
        while self.running:
            try:
                # Wait for input from socket or stdin
                readable, _, _ = select.select([self.socket], [], [], 0.1)
                
                # Check for socket data
                for sock in readable:
                    if sock == self.socket:
                        try:
                            message = self.socket.recv(4096)
                            if not message:
                                print("\n❌ Server closed connection.")
                                self.running = False
                                return
                            
                            message = message.decode('utf-8')
                            print(f"\n{message}")
                            print(f"{self.get_prompt()}", end='', flush=True)
                            
                        except BlockingIOError:
                            pass
                        except Exception as e:
                            print(f"\n❌ Error: {e}")
                            self.running = False
                            return
                
                # Check for user input (non-blocking)
                if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                    message = sys.stdin.readline().strip()
                    if message:
                        if message.lower() in ['/quit', '/exit']:
                            self.socket.send('/quit'.encode('utf-8'))
                            self.running = False
                            break
                        self.socket.send(message.encode('utf-8'))
                        print(self.get_prompt(), end='', flush=True)
                        
            except KeyboardInterrupt:
                print("\n\nDisconnecting...")
                try:
                    self.socket.send('/quit'.encode('utf-8'))
                except:
                    pass
                self.running = False
                break
            except Exception as e:
                if self.running:
                    print(f"\n❌ Error: {e}")
                break
    
    def get_prompt(self):
        """Get the input prompt string."""
        if self.nickname and self.current_room:
            return f"[{self.nickname}@{self.current_room}]> "
        elif self.nickname:
            return f"[{self.nickname}]> "
        return "> "
    
    def disconnect(self):
        """Disconnect from the server."""
        self.running = False
        if self.socket:
            try:
                self.socket.close()
            except:
                pass
        print("Disconnected.")


def main():
    """Entry point for the chat client."""
    parser = argparse.ArgumentParser(
        description='Chat Client',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python chat_client.py                        # Connect to localhost:5555
  python chat_client.py --port 8080            # Connect to localhost:8080
  python chat_client.py --host 192.168.1.100   # Connect to remote server

Commands (once connected):
  /nick <name>      Change your nickname
  /join <room>      Join a chat room
  /leave            Leave current room
  /rooms            List all rooms
  /users            List users in current room
  /whisper <u> <m>  Send private message
  /help             Show all commands
  /quit             Disconnect
        """
    )
    parser.add_argument('--host', default='localhost',
                       help='Server host address (default: localhost)')
    parser.add_argument('--port', type=int, default=5555,
                       help='Server port (default: 5555)')
    parser.add_argument('--non-blocking', action='store_true',
                       help='Use non-blocking I/O mode')
    
    args = parser.parse_args()
    
    # Choose client implementation
    if args.non_blocking:
        client = ChatClientNonBlocking(host=args.host, port=args.port)
    else:
        client = ChatClient(host=args.host, port=args.port)
    
    client.connect()


if __name__ == "__main__":
    main()
