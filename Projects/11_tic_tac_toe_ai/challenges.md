# Project 11: Tic-Tac-Toe AI - Challenges & Extensions

Once you've completed the basic Tic-Tac-Toe AI, try these challenges to deepen your understanding and add cool features!

---

## 🎯 Beginner Challenges

### 1. Better User Interface
**Difficulty:** ⭐  
**Skills:** String formatting, User experience

Improve the visual presentation:
- Add color to the board display (use ANSI escape codes)
- Show row/column headers more clearly
- Add a border around the game area
- Display the current player turn prominently

**Example:**
```
╔═══════════════════════╗
║     TIC-TAC-TOE       ║
╠═══════════════════════╣
║   0   1   2           ║
║ 0 X │ O │ X           ║
║  ───┼───┼───          ║
║ 1   │ X │ O           ║
║  ───┼───┼───          ║
║ 2 O │   │ X           ║
╚═══════════════════════╝
```

---

### 2. Input Validation
**Difficulty:** ⭐  
**Skills:** Error handling, Input validation

Make the game more robust:
- Handle non-numeric input gracefully
- Allow input like "a1" or "1a" (chess notation)
- Add an "undo" command for the last move
- Add a "quit" command to exit mid-game

---

### 3. Game History
**Difficulty:** ⭐  
**Skills:** Lists, Data structures

Track and display game history:
- Show the sequence of moves made
- Allow replaying a game move by move
- Save game history to a file
- Load and replay saved games

---

## 🚀 Intermediate Challenges

### 4. Connect Four
**Difficulty:** ⭐⭐  
**Skills:** 2D arrays, Game logic adaptation

Adapt your AI to play Connect Four:
- Change board size to 6 rows x 7 columns
- Pieces fall to the lowest empty space in a column
- Win requires 4 in a row (horizontal, vertical, or diagonal)
- The AI should still use minimax but with a deeper search

**Note:** Connect Four has a much larger state space, so you'll need to limit the minimax depth!

---

### 5. Variable Board Sizes
**Difficulty:** ⭐⭐  
**Skills:** Dynamic arrays, Generalization

Make the game configurable:
- Allow 4x4 or 5x5 boards
- Adjust win condition (3-in-a-row, 4-in-a-row, etc.)
- The AI should work with any board size
- Add a "custom game" menu option

**Challenge:** Larger boards make minimax very slow. How can you optimize it?

---

### 6. Transposition Table
**Difficulty:** ⭐⭐  
**Skills:** Hashing, Memoization, Optimization

Optimize the AI with a transposition table:
- Store evaluated board positions in a dictionary
- Before evaluating a position, check if it's already been computed
- This can dramatically speed up the AI
- Track how many positions are saved vs. computed

```python
class TranspositionTable:
    def __init__(self):
        self.table = {}
    
    def get(self, board_state):
        return self.table.get(board_state)
    
    def store(self, board_state, score):
        self.table[board_state] = score
```

---

## 🔥 Advanced Challenges

### 7. Monte Carlo Tree Search (MCTS)
**Difficulty:** ⭐⭐⭐  
**Skills:** Probability, Tree search, Statistics

Implement an alternative AI using MCTS:
- Instead of exploring all possibilities, simulate random games
- Build a tree of moves based on win rates from simulations
- Great for games where minimax is too slow
- Compare MCTS vs. minimax performance

**Resources:**
- MCTS is used in AlphaGo and many modern game AIs
- Good introduction to probabilistic AI algorithms

---

### 8. Ultimate Tic-Tac-Toe
**Difficulty:** ⭐⭐⭐  
**Skills:** Nested data structures, Complex game logic

Implement Ultimate Tic-Tac-Toe (also called Super Tic-Tac-Toe):
- A 3x3 grid of Tic-Tac-Toe boards
- Your move determines which sub-board the opponent plays in
- Win sub-boards to claim spots on the meta-board
- First to win the meta-board wins the game

**Rules:**
- Play in any cell of any sub-board
- Your opponent must play in the sub-board corresponding to your cell
- If sent to a won/full board, opponent can play anywhere

This is a much more strategic game and very hard to solve!

---

### 9. Network Multiplayer
**Difficulty:** ⭐⭐⭐  
**Skills:** Sockets, Networking, Threading

Add online multiplayer:
- Create a server that hosts games
- Allow two clients to connect and play
- Handle network latency and disconnections
- Support spectators who can watch games

**Files to create:**
- `server.py` - Game server
- `client.py` - Player client
- `network_game.py` - Networked game logic

---

### 10. Machine Learning Opponent
**Difficulty:** ⭐⭐⭐⭐  
**Skills:** Machine learning basics, Data collection

Train an AI using machine learning:
- Generate thousands of random games
- Record board states and outcomes
- Train a simple neural network or decision tree
- Compare ML AI vs. minimax AI

**Approach:**
1. Generate training data by having AIs play each other
2. Use a simple library like `sklearn` (if allowed) or implement a basic neural network
3. Input: board state (9 values: -1, 0, 1)
4. Output: best move (9 probabilities)

---

## 🎨 Creative Challenges

### 11. Themed Boards
**Difficulty:** ⭐  
**Skills:** Unicode, Creativity

Create different visual themes:
- Classic: X and O
- Emoji: 🐱 vs 🐶, 🔥 vs 💧
- Holiday themes: 🎄 vs 🎁, 🎃 vs 👻
- Custom: Allow players to choose their symbols

---

### 12. Sound Effects
**Difficulty:** ⭐⭐  
**Skills:** Audio, Cross-platform compatibility

Add sound to the game:
- Play a sound when a move is made
- Different sounds for win/loss/draw
- Background music (optional)
- Use simple beeps if external files aren't available

**Cross-platform tip:** Use `winsound` on Windows, `os.system('say')` on Mac, `print('\a')` as fallback.

---

### 13. Tournament Mode
**Difficulty:** ⭐⭐  
**Skills:** Loops, Statistics, File I/O

Run a tournament between multiple AIs:
- Create different AI strategies (random, defensive, aggressive, minimax)
- Have them play round-robin against each other
- Track win/loss/draw statistics
- Rank AIs by performance
- Save tournament results to a file

---

## 🧪 Testing Challenges

### 14. Unit Tests
**Difficulty:** ⭐⭐  
**Skills:** Testing, unittest module

Write comprehensive tests:
- Test all board operations
- Test win detection for all patterns
- Test AI makes optimal moves in known positions
- Test edge cases (full board, first move, etc.)

**Example test cases:**
```python
def test_horizontal_win():
    board = Board()
    board.make_move(0, 0, "X")
    board.make_move(0, 1, "X")
    board.make_move(0, 2, "X")
    assert board.check_winner() == "X"

def test_ai_blocks_win():
    # Set up board where human can win next move
    # Verify AI blocks it
    pass
```

---

### 15. Performance Benchmarking
**Difficulty:** ⭐⭐  
**Skills:** Performance analysis, Time complexity

Measure and optimize performance:
- Time how long minimax takes for each board state
- Count how many nodes are evaluated
- Compare with and without alpha-beta pruning
- Create a performance report

**Metrics to track:**
- Average decision time per move
- Nodes evaluated per decision
- Win rate vs. random player
- Win rate vs. minimax with different depths

---

## 📊 Project Extensions

### 16. Web Version
**Difficulty:** ⭐⭐⭐  
**Skills:** Web development, APIs

Create a web-based version:
- Use Flask or http.server to serve a web interface
- Create an HTML/CSS board
- Use JavaScript for user interaction
- Python backend handles AI moves via API

---

### 17. GUI Version
**Difficulty:** ⭐⭐⭐  
**Skills:** GUI programming, Event handling

Create a graphical version:
- Use tkinter (built-in) for a desktop GUI
- Draw the board with canvas or buttons
- Animate piece placement
- Add click-to-play interface

---

## 🏆 Expert Challenge

### 18. Perfect Play Database
**Difficulty:** ⭐⭐⭐⭐⭐  
**Skills:** Database, Optimization, Algorithm design

Pre-compute all Tic-Tac-Toe positions:
- There are only 5,478 unique game states
- Pre-calculate the optimal move for each
- Store in a dictionary or file
- AI becomes O(1) lookup instead of search!

**Approach:**
1. Write a script to enumerate all possible board states
2. Use retrograde analysis to determine optimal moves
3. Store as {board_hash: best_move}
4. AI just looks up the answer

This makes the AI instant and uses zero CPU during play!

---

## 📝 Challenge Checklist

- [ ] **Beginner (1-3):** UI improvements, validation, history
- [ ] **Intermediate (4-6):** Connect Four, variable boards, transposition table
- [ ] **Advanced (7-10):** MCTS, Ultimate TTT, networking, ML
- [ ] **Creative (11-13):** Themes, sounds, tournaments
- [ ] **Testing (14-15):** Unit tests, benchmarking
- [ ] **Extensions (16-17):** Web, GUI versions
- [ ] **Expert (18):** Perfect play database

---

## 💡 Tips for Success

1. **Start small:** Complete one challenge before moving to the next
2. **Test frequently:** Run your code often to catch bugs early
3. **Read the code:** Understand how minimax works before modifying it
4. **Use git:** Commit after each working feature
5. **Have fun:** These challenges are meant to be educational and enjoyable!

---

**Pick a challenge and start coding! Which one interests you most?** 🚀
