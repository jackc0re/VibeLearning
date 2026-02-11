# 🏆 Chat Server Challenges

Extend your chat server with these challenging features. Each challenge builds on the core implementation and teaches advanced concepts.

---

## Challenge 1: Message History Persistence ⭐⭐

**Goal:** Save chat history to disk and restore it on server restart.

### Requirements

1. Save all messages to a JSON file with timestamps
2. Load history when server starts
3. Each room has its own history file
4. Limit history to last 1000 messages per room

### Implementation Hints

```python
import json
from datetime import datetime

class MessageHistory:
    """Persistent message history manager."""
    
    def __init__(self, history_dir="chat_history"):
        self.history_dir = history_dir
        os.makedirs(history_dir, exist_ok=True)
    
    def save_message(self, room, message, timestamp=None):
        """Save a message to room history."""
        if timestamp is None:
            timestamp = datetime.now().isoformat()
        
        filename = f"{self.history_dir}/{room}.json"
        
        # Load existing history
        history = self.load_history(room)
        
        # Add new message
        history.append({
            "timestamp": timestamp,
            "message": message
        })
        
        # Keep only last 1000 messages
        history = history[-1000:]
        
        # Save back to file
        with open(filename, 'w') as f:
            json.dump(history, f, indent=2)
    
    def load_history(self, room, limit=50):
        """Load recent messages for a room."""
        filename = f"{self.history_dir}/{room}.json"
        try:
            with open(filename, 'r') as f:
                history = json.load(f)
                return history[-limit:]
        except FileNotFoundError:
            return []
```

### Testing

1. Send messages in different rooms
2. Restart the server
3. Verify messages are restored
4. Check that history limit works

---

## Challenge 2: File Transfer ⭐⭐⭐

**Goal:** Allow users to send files to each other.

### Requirements

1. `/sendfile <user> <filepath>` - Send file to user
2. `/acceptfile` - Accept incoming file transfer
3. Files are transferred directly between clients
4. Maximum file size limit (e.g., 10MB)
5. Progress indicator during transfer

### Implementation Hints

```python
# Protocol for file transfer
# 1. Sender requests: /sendfile bob photo.jpg
# 2. Server sends to bob: [FILE REQUEST] alice wants to send photo.jpg (2.3 MB)
# 3. Bob accepts: /acceptfile
# 4. Server coordinates direct transfer or proxies the file

FILE_HEADER = "!FILE!"
FILE_ACCEPT = "!ACCEPT!"
FILE_REJECT = "!REJECT!"
FILE_DATA = "!DATA!"

def handle_file_request(self, sender_socket, recipient, filename):
    """Handle file transfer request."""
    # Get file size
    file_size = os.path.getsize(filename)
    
    if file_size > 10 * 1024 * 1024:  # 10MB limit
        self.send_to_client(sender_socket, "File too large (max 10MB)")
        return
    
    # Store pending transfer
    self.pending_files[recipient] = {
        'sender': sender_socket,
        'filename': filename,
        'size': file_size
    }
    
    # Notify recipient
    sender_nick = self.clients[sender_socket]['nickname']
    self.send_to_client(recipient_socket,
        f"[FILE REQUEST] {sender_nick} wants to send {filename} ({file_size} bytes)")
```

### Testing

1. Send a small text file between users
2. Try sending a file that's too large
3. Reject a file transfer
4. Test with binary files (images)

---

## Challenge 3: Moderation System ⭐⭐⭐

**Goal:** Add room moderators with kick/ban powers.

### Requirements

1. First user to join a room becomes moderator
2. `/kick <user>` - Remove user from room
3. `/ban <user>` - Ban user from room
4. `/unban <user>` - Remove ban
5. `/mods` - List moderators in room
6. Moderators can assign other moderators

### Implementation Hints

```python
class Room:
    """Represents a chat room with moderation."""
    
    def __init__(self, name):
        self.name = name
        self.members = set()  # socket objects
        self.moderators = set()  # nicknames
        self.banned = set()  # nicknames
        self.creator = None
    
    def add_member(self, socket, nickname):
        """Add a member to the room."""
        if nickname in self.banned:
            return False, "You are banned from this room"
        
        self.members.add(socket)
        
        # First member becomes creator/moderator
        if not self.creator:
            self.creator = nickname
            self.moderators.add(nickname)
        
        return True, None
    
    def is_moderator(self, nickname):
        """Check if user is a moderator."""
        return nickname in self.moderators
    
    def kick(self, moderator, target_nick):
        """Kick a user from the room."""
        if not self.is_moderator(moderator):
            return False, "You are not a moderator"
        
        # Find and remove target
        # ...
```

### Testing

1. Create a room and verify first user is mod
2. Kick a user from a room
3. Ban a user and verify they can't rejoin
4. Try to kick without moderator status

---

## Challenge 4: Emoji Support ⭐⭐

**Goal:** Support emoji shortcodes in messages.

### Requirements

1. Convert `:smile:` to 😄
2. Support at least 20 common emojis
3. `/emojis` command to list available emojis
4. Case-insensitive matching

### Implementation Hints

```python
EMOJI_MAP = {
    ':smile:': '😄',
    ':sad:': '😢',
    ':laugh:': '😂',
    ':heart:': '❤️',
    ':thumbsup:': '👍',
    ':thumbsdown:': '👎',
    ':fire:': '🔥',
    ':star:': '⭐',
    ':check:': '✅',
    ':x:': '❌',
    ':thinking:': '🤔',
    ':cool:': '😎',
    ':party:': '🎉',
    ':rocket:': '🚀',
    ':coffee:': '☕',
    ':pizza:': '🍕',
    ':game:': '🎮',
    ':music:': '🎵',
    ':book:': '📚',
    ':code:': '💻',
}

def convert_emojis(message):
    """Convert emoji shortcodes to unicode."""
    for shortcode, emoji in EMOJI_MAP.items():
        message = message.replace(shortcode.lower(), emoji)
        message = message.replace(shortcode, emoji)
    return message
```

### Testing

1. Send message with `:smile:` and verify conversion
2. Test mixed case `:SMILE:`, `:Smile:`
3. Test multiple emojis in one message
4. List all available emojis

---

## Challenge 5: Server Logging ⭐⭐

**Goal:** Log all server activity to a file.

### Requirements

1. Log all messages with timestamps
2. Log connections/disconnections
3. Log nickname changes
4. Log room joins/leaves
5. Log file for each day
6. Include IP addresses for security

### Implementation Hints

```python
import logging
from datetime import datetime

class ChatLogger:
    """Logger for chat server activity."""
    
    def __init__(self, log_dir="logs"):
        self.log_dir = log_dir
        os.makedirs(log_dir, exist_ok=True)
        self.setup_logger()
    
    def setup_logger(self):
        """Set up daily rotating log files."""
        today = datetime.now().strftime('%Y-%m-%d')
        log_file = f"{self.log_dir}/chat_{today}.log"
        
        self.logger = logging.getLogger('chat_server')
        self.logger.setLevel(logging.INFO)
        
        handler = logging.FileHandler(log_file)
        handler.setFormatter(logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s'
        ))
        self.logger.addHandler(handler)
    
    def log_message(self, room, sender, message):
        """Log a chat message."""
        self.logger.info(f"[{room}] {sender}: {message}")
    
    def log_connection(self, nickname, address):
        """Log a user connection."""
        self.logger.info(f"CONNECT: {nickname} from {address}")
    
    def log_disconnection(self, nickname, reason=""):
        """Log a user disconnection."""
        self.logger.info(f"DISCONNECT: {nickname} {reason}")
    
    def log_command(self, nickname, command):
        """Log a command execution."""
        self.logger.info(f"COMMAND: {nickname} executed {command}")
```

### Testing

1. Connect and disconnect several users
2. Send messages in different rooms
3. Execute various commands
4. Verify log file format and content

---

## Challenge 6: Authentication System ⭐⭐⭐

**Goal:** Add password-protected nicknames.

### Requirements

1. `/register <password>` - Register current nickname with password
2. `/login <nickname> <password>` - Login to registered nickname
3. Store hashed passwords (use hashlib)
4. Persist user database to JSON
5. Prevent unauthorized nickname changes

### Implementation Hints

```python
import hashlib
import json

class AuthManager:
    """Manages user authentication."""
    
    def __init__(self, db_file="users.json"):
        self.db_file = db_file
        self.users = {}  # nickname -> {password_hash, created_at}
        self.load_users()
    
    def hash_password(self, password):
        """Hash a password using SHA-256."""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def register(self, nickname, password):
        """Register a new user."""
        if nickname in self.users:
            return False, "Nickname already registered"
        
        self.users[nickname] = {
            'password_hash': self.hash_password(password),
            'created_at': datetime.now().isoformat()
        }
        self.save_users()
        return True, "Registration successful"
    
    def login(self, nickname, password):
        """Verify login credentials."""
        if nickname not in self.users:
            return False, "Nickname not registered"
        
        stored_hash = self.users[nickname]['password_hash']
        if self.hash_password(password) == stored_hash:
            return True, "Login successful"
        return False, "Invalid password"
    
    def is_registered(self, nickname):
        """Check if nickname is registered."""
        return nickname in self.users
    
    def save_users(self):
        """Save user database to file."""
        with open(self.db_file, 'w') as f:
            json.dump(self.users, f, indent=2)
    
    def load_users(self):
        """Load user database from file."""
        try:
            with open(self.db_file, 'r') as f:
                self.users = json.load(f)
        except FileNotFoundError:
            self.users = {}
```

### Testing

1. Register a nickname with password
2. Disconnect and reconnect with same nickname
3. Try to use registered nickname without password
4. Test wrong password rejection

---

## Challenge 7: Admin Commands ⭐⭐⭐

**Goal:** Add server administrator commands.

### Requirements

1. Admin password set via command line or config
2. `/admin <password>` - Gain admin privileges
3. `/shutdown` - Gracefully shut down server
4. `/broadcast <message>` - Send message to all rooms
5. `/listall` - List all connected users with IPs
6. `/forcerename <old> <new>` - Force rename a user

### Implementation Hints

```python
class AdminManager:
    """Manages admin authentication and commands."""
    
    def __init__(self, admin_password):
        self.admin_password = admin_password
        self.admin_sockets = set()  # Sockets with admin privileges
    
    def authenticate(self, socket, password):
        """Attempt to authenticate as admin."""
        if password == self.admin_password:
            self.admin_sockets.add(socket)
            return True
        return False
    
    def is_admin(self, socket):
        """Check if socket has admin privileges."""
        return socket in self.admin_sockets
    
    def revoke(self, socket):
        """Revoke admin privileges."""
        self.admin_sockets.discard(socket)


# In ChatServer class:
def cmd_admin(self, client_socket, password):
    """Admin authentication command."""
    if self.admin_manager.authenticate(client_socket, password):
        self.send_to_client(client_socket, "✅ Admin privileges granted.")
    else:
        self.send_to_client(client_socket, "❌ Invalid admin password.")

def cmd_shutdown(self, client_socket, args):
    """Shutdown server command (admin only)."""
    if not self.admin_manager.is_admin(client_socket):
        self.send_to_client(client_socket, "❌ Admin privileges required.")
        return
    
    self.broadcast_message("⚠️ Server is shutting down...")
    self.running = False
```

### Testing

1. Try admin commands without authentication
2. Authenticate with correct password
3. Execute admin commands
4. Verify shutdown works gracefully

---

## Challenge 8: Rate Limiting ⭐⭐

**Goal:** Prevent spam by limiting message rate.

### Requirements

1. Maximum 5 messages per second per user
2. Maximum 100 characters per message
3. Warning on first violation
4. Mute repeat offenders for 30 seconds
5. `/mutelist` command for admins

### Implementation Hints

```python
import time
from collections import deque

class RateLimiter:
    """Rate limiter for messages."""
    
    def __init__(self, max_messages=5, window_seconds=1):
        self.max_messages = max_messages
        self.window = window_seconds
        self.user_messages = {}  # socket -> deque of timestamps
        self.muted = {}  # socket -> mute_end_time
    
    def is_allowed(self, socket):
        """Check if user can send a message."""
        # Check if muted
        if socket in self.muted:
            if time.time() < self.muted[socket]:
                return False, "You are muted"
            else:
                del self.muted[socket]
        
        # Get message history
        if socket not in self.user_messages:
            self.user_messages[socket] = deque()
        
        now = time.time()
        messages = self.user_messages[socket]
        
        # Remove old timestamps
        while messages and messages[0] < now - self.window:
            messages.popleft()
        
        # Check rate
        if len(messages) >= self.max_messages:
            return False, "Rate limit exceeded"
        
        # Record this message
        messages.append(now)
        return True, None
    
    def mute(self, socket, duration=30):
        """Mute a user for a duration."""
        self.muted[socket] = time.time() + duration
    
    def cleanup(self, socket):
        """Clean up data for disconnected user."""
        self.user_messages.pop(socket, None)
        self.muted.pop(socket, None)
```

### Testing

1. Send messages rapidly to trigger limit
2. Verify mute works
3. Wait for mute to expire
4. Test with multiple users

---

## Challenge 9: Chat Bot API ⭐⭐⭐⭐

**Goal:** Create a bot that can join and respond to messages.

### Requirements

1. Create a `ChatBot` base class
2. Bot can respond to specific patterns
3. Built-in trivia bot example
4. Built-in reminder bot example
5. `/bots` command to list active bots

### Implementation Hints

```python
import re
from abc import ABC, abstractmethod

class ChatBot(ABC):
    """Base class for chat bots."""
    
    def __init__(self, nickname):
        self.nickname = nickname
    
    @abstractmethod
    def on_message(self, room, sender, message):
        """Called when a message is received.
        
        Returns:
            str or None: Response message or None to stay silent
        """
        pass
    
    @abstractmethod
    def on_join(self, room):
        """Called when bot joins a room."""
        pass


class TriviaBot(ChatBot):
    """A bot that runs trivia games."""
    
    def __init__(self):
        super().__init__("TriviaBot")
        self.questions = [
            {"q": "What is 2+2?", "a": "4"},
            {"q": "Capital of France?", "a": "paris"},
        ]
        self.current_question = None
        self.scores = {}
    
    def on_message(self, room, sender, message):
        # Check for trivia commands
        if message.lower() == "!trivia":
            return self.ask_question()
        elif message.lower() == "!scores":
            return self.show_scores()
        elif self.current_question:
            if message.lower() == self.current_question["a"]:
                self.current_question = None
                return f"🎉 {sender} got it right!"
        return None
    
    def ask_question(self):
        import random
        self.current_question = random.choice(self.questions)
        return f"❓ Trivia: {self.current_question['q']}"


class ReminderBot(ChatBot):
    """A bot that sets reminders."""
    
    def __init__(self):
        super().__init__("ReminderBot")
        self.reminders = []  # [(time, user, message), ...]
    
    def on_message(self, room, sender, message):
        # Parse !remind command
        match = re.match(r'!remind (\d+)([mh]) (.+)', message.lower())
        if match:
            amount = int(match.group(1))
            unit = match.group(2)
            text = match.group(3)
            
            # Calculate reminder time
            # Store reminder
            return f"⏰ I'll remind you in {amount}{unit}: {text}"
        return None
```

### Testing

1. Create a trivia bot and test questions
2. Create a reminder bot and test reminders
3. Test bot commands in different rooms
4. Verify bot doesn't respond to itself

---

## Challenge 10: Encrypted Messaging ⭐⭐⭐⭐

**Goal:** Add end-to-end encryption for private messages.

### Requirements

1. Generate RSA key pair for each user
2. Exchange public keys on first whisper
3. Encrypt private messages with recipient's public key
4. Decrypt with private key
5. Use `cryptography` library (external dependency)

### Implementation Hints

```python
# Note: This requires the 'cryptography' package
# pip install cryptography

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization

class EncryptionManager:
    """Manages encryption for private messages."""
    
    def __init__(self):
        self.private_keys = {}  # nickname -> private_key
        self.public_keys = {}   # nickname -> public_key
    
    def generate_keys(self, nickname):
        """Generate a new key pair for a user."""
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        public_key = private_key.public_key()
        
        self.private_keys[nickname] = private_key
        self.public_keys[nickname] = public_key
        
        return public_key
    
    def encrypt(self, message, public_key):
        """Encrypt a message with a public key."""
        return public_key.encrypt(
            message.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
    
    def decrypt(self, encrypted, nickname):
        """Decrypt a message with user's private key."""
        private_key = self.private_keys[nickname]
        return private_key.decrypt(
            encrypted,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        ).decode()
```

### Testing

1. Generate keys for two users
2. Send encrypted whisper
3. Verify only recipient can decrypt
4. Test with multiple users

---

## 🎯 Challenge Completion Tracker

Track your progress:

| Challenge | Difficulty | Completed |
|-----------|------------|-----------|
| 1. Message History Persistence | ⭐⭐ | [ ] |
| 2. File Transfer | ⭐⭐⭐ | [ ] |
| 3. Moderation System | ⭐⭐⭐ | [ ] |
| 4. Emoji Support | ⭐⭐ | [ ] |
| 5. Server Logging | ⭐⭐ | [ ] |
| 6. Authentication System | ⭐⭐⭐ | [ ] |
| 7. Admin Commands | ⭐⭐⭐ | [ ] |
| 8. Rate Limiting | ⭐⭐ | [ ] |
| 9. Chat Bot API | ⭐⭐⭐⭐ | [ ] |
| 10. Encrypted Messaging | ⭐⭐⭐⭐ | [ ] |

---

## 💡 Tips for Success

1. **Start Simple** - Implement one challenge at a time
2. **Test Often** - Test each feature before moving on
3. **Read Errors** - Error messages tell you what's wrong
4. **Use Logging** - Add print statements to debug
5. **Ask for Help** - Search online for similar problems

Good luck! 🚀
