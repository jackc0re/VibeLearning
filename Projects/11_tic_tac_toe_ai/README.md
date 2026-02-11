# Project 11: Tic-Tac-Toe AI

> **Difficulty:** ⭐⭐⭐ (Intermediate)  
> **Estimated Time:** 6-8 hours  
> **Skills:** OOP, Minimax Algorithm, Recursion, Game Theory

---

## 🎯 Overview

Build an unbeatable Tic-Tac-Toe game with an AI opponent using the minimax algorithm. This project demonstrates game theory concepts, recursive algorithms, and object-oriented design.

---

## ✨ Features

### Core Features
- **Human vs AI Mode**: Play against an unbeatable computer opponent
- **AI vs AI Mode**: Watch two AIs battle it out
- **Minimax Algorithm**: Perfect play with alpha-beta pruning optimization
- **Difficulty Levels**: Easy, Medium, Hard (Impossible)
- **Score Tracking**: Wins, losses, and draws

### Advanced Features
- **Alpha-Beta Pruning**: Optimized minimax for faster decision-making
- **Board Analysis**: Detect winning positions and blocks
- **Game History**: Review past moves
- **Clean Interface**: Text-based UI with visual board

---

## 🏗️ Project Structure

```
11_tic_tac_toe_ai/
├── README.md          # This file
├── main.py            # Entry point and game loop
├── board.py           # Game board logic
├── ai_player.py       # AI with minimax algorithm
└── challenges.md      # Extension ideas
```

---

## 🚀 Quick Start

### Run the Game
```bash
cd Projects/11_tic_tac_toe_ai
python main.py
```

### Game Menu
```
=== TIC-TAC-TOE AI ===

1. Play vs AI (Human First)
2. Play vs AI (AI First)
3. AI vs AI (Watch)
4. View Statistics
5. Change Difficulty
6. Quit

Choose an option: 1
```

---

## 🧠 How It Works

### The Minimax Algorithm

Minimax is a recursive algorithm used for decision-making in two-player games:

1. **Maximizing Player (AI)**: Tries to maximize the score
2. **Minimizing Player (Human)**: Tries to minimize the AI's score
3. **Game Tree**: Explores all possible moves to find the optimal one
4. **Evaluation**: Assigns scores to terminal states (+10 for win, -10 for loss, 0 for draw)

```
        [Current Board]
           /       \
    [Move 1]     [Move 2]     [Move 3] ...
      /   \
[Response 1] [Response 2] ...
```

### Alpha-Beta Pruning

An optimization that eliminates branches that cannot affect the final decision:
- **Alpha**: Best value the maximizer can guarantee
- **Beta**: Best value the minimizer can guarantee
- **Pruning**: Skip branches when alpha >= beta

---

## 🎮 Gameplay

### Making Moves
Enter moves as row and column numbers (0-2):
```
  0 1 2
0 X . O
1 . X .
2 O . X

Your move (row col): 1 1
```

### Difficulty Levels
- **Easy**: AI makes random moves
- **Medium**: AI uses minimax with 50% chance of random move
- **Hard**: AI uses full minimax (unbeatable)

---

## 📚 Learning Objectives

By completing this project, you will learn:

1. **Game Theory Basics**
   - Zero-sum games
   - Optimal strategies
   - Game trees

2. **Recursion**
   - Recursive function design
   - Base cases and recursive cases
   - Call stack management

3. **OOP Design**
   - Class separation of concerns
   - Encapsulation
   - Composition over inheritance

4. **Algorithm Optimization**
   - Alpha-beta pruning
   - Time complexity analysis
   - Space vs time tradeoffs

---

## 🧪 Testing Strategy

### Manual Testing
1. Play multiple games against the AI
2. Try to beat the Hard difficulty (impossible!)
3. Test all difficulty levels
4. Verify score tracking

### Edge Cases
- Full board (draw)
- Immediate win detection
- Invalid move handling
- Game restart

---

## 🔧 Implementation Tips

### Step 1: Board Class
Start with a simple board representation:
```python
class Board:
    def __init__(self):
        self.cells = [[' ' for _ in range(3)] for _ in range(3)]
```

### Step 2: Win Detection
Implement methods to check for wins:
```python
def check_winner(self):
    # Check rows, columns, and diagonals
```

### Step 3: Minimax Algorithm
Build the recursive minimax function:
```python
def minimax(self, depth, is_maximizing):
    # Base case: game over
    # Recursive case: explore all moves
```

### Step 4: Game Loop
Create the main game interface:
```python
def play_game():
    # Initialize board and players
    # Main game loop
    # Handle user input
```

---

## 📊 Performance

| Difficulty | Average Moves Evaluated | Response Time |
|------------|------------------------|---------------|
| Easy | 1 | <1ms |
| Medium | ~100 | <10ms |
| Hard | ~50,000 (with pruning) | <100ms |

Without alpha-beta pruning, Hard mode would evaluate ~250,000 positions!

---

## 🎓 Further Reading

- **Game Theory**: "Theory of Games and Economic Behavior" by von Neumann
- **Minimax**: Wikipedia - Minimax algorithm
- **Alpha-Beta Pruning**: Wikipedia - Alpha-beta pruning
- **Python OOP**: Real Python - Object-Oriented Programming in Python

---

## ✅ Success Criteria

- [ ] Human can play against AI
- [ ] AI vs AI mode works
- [ ] Minimax algorithm implemented correctly
- [ ] Alpha-beta pruning optimization added
- [ ] All difficulty levels functional
- [ ] Score tracking works
- [ ] Clean, readable code with comments

---

**Ready to build an unbeatable AI? Let's code! 🚀**
