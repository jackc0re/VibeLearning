# 🎯 Project 5: Quiz Game

Build an interactive multiple-choice quiz game with categories, difficulty levels, scoring, and a leaderboard.

---

## 📋 Project Overview

This project helps you practice:
- Object-oriented programming (classes and objects)
- JSON file handling for data persistence
- Timer functionality and time tracking
- Data structures for organizing questions and scores
- User interface design

### Features to Build

1. ✅ Question Bank
   - Load questions from JSON file
   - Organize by categories (Science, History, Geography, etc.)
   - Support multiple difficulty levels (Easy, Medium, Hard)

2. ✅ Game Mechanics
   - Multiple choice questions (A, B, C, D)
   - Timer per question (configurable time limit)
   - Immediate feedback (correct/incorrect)
   - Score tracking with time bonuses

3. ✅ Leaderboard System
   - Track high scores
   - Save player names and scores
   - Display top scores by category/difficulty

4. ✅ User Interface
   - Welcome screen and menu
   - Category and difficulty selection
   - Progress tracking during quiz
   - Final results and statistics

---

## 💻 Requirements

### Prerequisites

Complete these modules before starting:
- [00_getting_started](../../00_getting_started/README.md)
- [01_foundations](../../01_foundations/README.md)
- [02_data_structures](../../02_data_structures/README.md)
- [04_oop_concepts](../../04_oop_concepts/README.md)
- [10_file_io](../../10_file_io/README.md)

### Skills You'll Use

- **Classes & Objects** — Create Question, Quiz, and Leaderboard classes
- **JSON** — Load questions and save high scores
- **Random Module** — Shuffle questions and options
- **Time Module** — Track time per question
- **Control Flow** — Handle game logic and user choices
- **String Formatting** — Display formatted output

---

## 🚀 Development Steps

### Step 1: Question Class (15 minutes)

Create a class to represent a single question:

```python
class Question:
    """Represents a single quiz question."""
    
    def __init__(self, question_text, options, correct_answer, 
                 category="General", difficulty="Medium", points=10):
        self.question_text = question_text
        self.options = options  # List of 4 options
        self.correct_answer = correct_answer  # Index 0-3 or option text
        self.category = category
        self.difficulty = difficulty
        self.points = points
    
    def is_correct(self, answer):
        """Check if the given answer is correct."""
        if isinstance(self.correct_answer, int):
            return answer == self.correct_answer
        return answer.upper() == self.correct_answer.upper()
    
    def display(self):
        """Display the question with options."""
        print(f"\n{self.question_text}")
        print("-" * 50)
        for i, option in enumerate(self.options, 1):
            print(f"  {chr(64 + i)}. {option}")
```

### Step 2: Load Questions from JSON (20 minutes)

Create a function to load questions from a JSON file:

```python
import json
import random

def load_questions(filename="questions.json"):
    """Load questions from JSON file."""
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        
        questions = []
        for q in data.get("questions", []):
            questions.append(Question(
                question_text=q["question"],
                options=q["options"],
                correct_answer=q["correct_answer"],
                category=q.get("category", "General"),
                difficulty=q.get("difficulty", "Medium"),
                points=q.get("points", 10)
            ))
        return questions
    except FileNotFoundError:
        print(f"Error: {filename} not found!")
        return []
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in {filename}!")
        return []

def filter_questions(questions, category=None, difficulty=None, count=10):
    """Filter questions by category and difficulty, then shuffle."""
    filtered = questions
    
    if category and category != "All":
        filtered = [q for q in filtered if q.category == category]
    
    if difficulty and difficulty != "All":
        filtered = [q for q in filtered if q.difficulty == difficulty]
    
    random.shuffle(filtered)
    return filtered[:count]
```

### Step 3: Quiz Game Class (30 minutes)

Create the main quiz game class:

```python
import time

class QuizGame:
    """Main quiz game class that manages the game flow."""
    
    def __init__(self, questions, time_per_question=30):
        self.all_questions = questions
        self.time_per_question = time_per_question
        self.reset_game()
    
    def reset_game(self):
        """Reset game state for a new quiz."""
        self.current_questions = []
        self.score = 0
        self.correct_answers = 0
        self.wrong_answers = 0
        self.current_question_index = 0
        self.player_name = ""
    
    def start_quiz(self, category="All", difficulty="All", question_count=10):
        """Start a new quiz session."""
        self.reset_game()
        self.current_questions = filter_questions(
            self.all_questions, category, difficulty, question_count
        )
        
        if not self.current_questions:
            print("No questions available for selected criteria!")
            return False
        
        print(f"\nStarting quiz with {len(self.current_questions)} questions...")
        print(f"Category: {category} | Difficulty: {difficulty}")
        print(f"Time per question: {self.time_per_question} seconds")
        print("-" * 50)
        
        input("\nPress Enter to start...")
        return True
    
    def ask_question(self, question):
        """Ask a single question and return if correct."""
        print(f"\n{'=' * 50}")
        print(f"Question {self.current_question_index + 1} of {len(self.current_questions)}")
        print(f"Category: {question.category} | Points: {question.points}")
        print("=" * 50)
        
        question.display()
        
        # Start timer
        start_time = time.time()
        
        # Get answer with timeout (simplified version)
        answer = input("\nYour answer (A/B/C/D): ").strip().upper()
        
        elapsed_time = time.time() - start_time
        
        # Convert letter to index (A=0, B=1, etc.)
        answer_index = ord(answer) - ord('A') if answer in 'ABCD' else -1
        
        # Check if time exceeded
        if elapsed_time > self.time_per_question:
            print(f"\n⏰ Time's up! You took {elapsed_time:.1f} seconds.")
            return False, 0
        
        # Check answer
        if question.is_correct(answer_index):
            # Calculate time bonus
            time_bonus = max(0, int((self.time_per_question - elapsed_time) / 5))
            total_points = question.points + time_bonus
            print(f"\n✅ Correct! +{question.points} points")
            if time_bonus > 0:
                print(f"⚡ Time bonus: +{time_bonus} points")
            return True, total_points
        else:
            correct_letter = chr(65 + question.correct_answer)
            correct_text = question.options[question.correct_answer]
            print(f"\n❌ Wrong! The correct answer was {correct_letter}: {correct_text}")
            return False, 0
    
    def run_quiz(self):
        """Run the complete quiz and return final score."""
        for i, question in enumerate(self.current_questions):
            self.current_question_index = i
            is_correct, points = self.ask_question(question)
            
            if is_correct:
                self.correct_answers += 1
                self.score += points
            else:
                self.wrong_answers += 1
            
            print(f"\nCurrent Score: {self.score}")
            
            if i < len(self.current_questions) - 1:
                input("\nPress Enter for next question...")
        
        return self.show_results()
    
    def show_results(self):
        """Display quiz results."""
        total_questions = len(self.current_questions)
        accuracy = (self.correct_answers / total_questions * 100) if total_questions > 0 else 0
        
        print("\n" + "=" * 50)
        print("                QUIZ COMPLETE!")
        print("=" * 50)
        print(f"Questions: {total_questions}")
        print(f"Correct: {self.correct_answers} ✅")
        print(f"Wrong: {self.wrong_answers} ❌")
        print(f"Accuracy: {accuracy:.1f}%")
        print(f"\n🏆 FINAL SCORE: {self.score}")
        print("=" * 50)
        
        return self.score
```

### Step 4: Leaderboard System (20 minutes)

Add a leaderboard to track high scores:

```python
class Leaderboard:
    """Manages high scores and leaderboard."""
    
    def __init__(self, filename="leaderboard.json"):
        self.filename = filename
        self.scores = self.load_scores()
    
    def load_scores(self):
        """Load scores from file."""
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []
    
    def save_scores(self):
        """Save scores to file."""
        try:
            with open(self.filename, 'w') as f:
                json.dump(self.scores, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving scores: {e}")
            return False
    
    def add_score(self, name, score, category, difficulty, accuracy):
        """Add a new score to the leaderboard."""
        entry = {
            "name": name,
            "score": score,
            "category": category,
            "difficulty": difficulty,
            "accuracy": accuracy,
            "date": time.strftime("%Y-%m-%d %H:%M")
        }
        self.scores.append(entry)
        # Sort by score descending
        self.scores.sort(key=lambda x: x["score"], reverse=True)
        # Keep only top 20
        self.scores = self.scores[:20]
        self.save_scores()
    
    def display(self, limit=10):
        """Display the leaderboard."""
        print("\n" + "=" * 70)
        print("                        🏆 LEADERBOARD 🏆")
        print("=" * 70)
        
        if not self.scores:
            print("No scores yet! Be the first to play!")
            return
        
        print(f"{'Rank':<6} {'Name':<15} {'Score':<8} {'Category':<12} {'Diff':<8} {'Date':<16}")
        print("-" * 70)
        
        for i, entry in enumerate(self.scores[:limit], 1):
            print(f"{i:<6} {entry['name']:<15} {entry['score']:<8} "
                  f"{entry['category']:<12} {entry['difficulty']:<8} {entry['date']:<16}")
        
        print("=" * 70)
```

### Step 5: Menu and User Interface (25 minutes)

Create the main menu and game loop:

```python
class QuizApp:
    """Main application class that handles the menu and game flow."""
    
    def __init__(self):
        self.questions = load_questions()
        self.leaderboard = Leaderboard()
        self.game = QuizGame(self.questions)
    
    def display_welcome(self):
        """Display welcome screen."""
        print("\n" + "=" * 60)
        print("     🎯 WELCOME TO THE PYTHON QUIZ GAME! 🎯")
        print("=" * 60)
        print("\nTest your knowledge across various categories!")
        print("Answer multiple choice questions against the clock.")
        print("Earn time bonuses for quick answers!")
        print("\n" + "=" * 60)
    
    def display_menu(self):
        """Display main menu."""
        print("\n" + "=" * 40)
        print("           MAIN MENU")
        print("=" * 40)
        print("1. Start Quiz")
        print("2. View Leaderboard")
        print("3. View Categories")
        print("4. How to Play")
        print("5. Exit")
        print("=" * 40)
    
    def select_category(self):
        """Let user select a category."""
        categories = list(set(q.category for q in self.questions))
        categories.sort()
        categories.insert(0, "All")
        
        print("\n--- Select Category ---")
        for i, cat in enumerate(categories, 1):
            print(f"{i}. {cat}")
        
        choice = self.get_choice(1, len(categories))
        return categories[choice - 1]
    
    def select_difficulty(self):
        """Let user select difficulty."""
        difficulties = ["All", "Easy", "Medium", "Hard"]
        
        print("\n--- Select Difficulty ---")
        for i, diff in enumerate(difficulties, 1):
            print(f"{i}. {diff}")
        
        choice = self.get_choice(1, len(difficulties))
        return difficulties[choice - 1]
    
    def select_question_count(self):
        """Let user select number of questions."""
        print("\n--- Number of Questions ---")
        print("1. 5 questions (Quick)")
        print("2. 10 questions (Standard)")
        print("3. 20 questions (Marathon)")
        
        choice = self.get_choice(1, 3)
        return {1: 5, 2: 10, 3: 20}[choice]
    
    def get_choice(self, min_val, max_val):
        """Get valid menu choice."""
        while True:
            try:
                choice = int(input(f"\nEnter choice ({min_val}-{max_val}): "))
                if min_val <= choice <= max_val:
                    return choice
                print(f"Please enter a number between {min_val} and {max_val}.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    def show_instructions(self):
        """Display how to play."""
        print("\n" + "=" * 50)
        print("              HOW TO PLAY")
        print("=" * 50)
        print("1. Select a category and difficulty level")
        print("2. Answer multiple choice questions (A, B, C, or D)")
        print("3. Each question has a time limit (default: 30 seconds)")
        print("4. Correct answers earn base points + time bonus")
        print("5. Wrong answers or timeouts get 0 points")
        print("6. Try to get the highest score and make the leaderboard!")
        print("=" * 50)
    
    def show_categories(self):
        """Display available categories."""
        categories = {}
        for q in self.questions:
            categories[q.category] = categories.get(q.category, 0) + 1
        
        print("\n" + "=" * 40)
        print("           CATEGORIES")
        print("=" * 40)
        for cat, count in sorted(categories.items()):
            print(f"  {cat}: {count} questions")
        print("=" * 40)
    
    def run(self):
        """Main application loop."""
        self.display_welcome()
        
        while True:
            self.display_menu()
            choice = self.get_choice(1, 5)
            
            if choice == 1:
                # Start quiz
                category = self.select_category()
                difficulty = self.select_difficulty()
                count = self.select_question_count()
                
                if self.game.start_quiz(category, difficulty, count):
                    score = self.game.run_quiz()
                    
                    # Save to leaderboard
                    if score > 0:
                        name = input("\nEnter your name for the leaderboard: ").strip()
                        if name:
                            total = len(self.game.current_questions)
                            accuracy = (self.game.correct_answers / total * 100)
                            self.leaderboard.add_score(
                                name, score, category, difficulty, accuracy
                            )
                            print(f"\n✅ Score saved! Great job, {name}!")
            
            elif choice == 2:
                self.leaderboard.display()
            
            elif choice == 3:
                self.show_categories()
            
            elif choice == 4:
                self.show_instructions()
            
            elif choice == 5:
                print("\nThanks for playing! Goodbye! 👋")
                break


def main():
    """Entry point for the quiz game."""
    app = QuizApp()
    app.run()


if __name__ == "__main__":
    main()
```

### Step 6: Create Question Bank JSON (10 minutes)

Create a sample `questions.json` file:

```json
{
  "questions": [
    {
      "question": "What is the capital of France?",
      "options": ["London", "Berlin", "Paris", "Madrid"],
      "correct_answer": 2,
      "category": "Geography",
      "difficulty": "Easy",
      "points": 10
    },
    {
      "question": "Which planet is known as the Red Planet?",
      "options": ["Venus", "Mars", "Jupiter", "Saturn"],
      "correct_answer": 1,
      "category": "Science",
      "difficulty": "Easy",
      "points": 10
    }
  ]
}
```

---

## 🧪 Testing

Test your quiz game with these scenarios:

1. **Basic Quiz Flow**
   - Start a quiz with default settings
   - Answer all questions
   - Verify scoring works correctly

2. **Category Filtering**
   - Try different categories
   - Verify only relevant questions appear

3. **Difficulty Levels**
   - Test each difficulty level
   - Verify appropriate questions are selected

4. **Time Limits**
   - Test timeout behavior
   - Verify time bonuses are calculated

5. **Leaderboard**
   - Add multiple scores
   - Verify sorting and display

---

## 🎯 Learning Checkpoints

After completing this project, you should understand:

- ✅ How to design classes for a game application
- ✅ How to load and parse JSON data
- ✅ How to use the random module for shuffling
- ✅ How to implement timing with the time module
- ✅ How to create a menu-driven CLI application
- ✅ How to persist high scores to a file

---

## 🏆 Challenges

Complete these challenges to enhance your quiz game:

1. **Question Editor** — Add ability to create/edit questions
2. **Lifelines** — Add "50/50" and "Ask the Audience" lifelines
3. **Streak Multiplier** — Bonus points for consecutive correct answers
4. **Timed Mode** — Race against a total timer, not per question
5. **Multiplayer** — Support for 2+ players taking turns
6. **Question Images** — Support for image-based questions
7. **Export Results** — Save quiz results to a text file

See [challenges.md](challenges.md) for detailed instructions.

---

## 📁 File Structure

```
05_quiz_game/
├── README.md          # This file
├── quiz_game.py       # Your main implementation
├── questions.json     # Question bank
└── challenges.md      # Additional challenge tasks
```

---

**Ready to start?** Create `quiz_game.py` and `questions.json`, then begin building! 🚀
