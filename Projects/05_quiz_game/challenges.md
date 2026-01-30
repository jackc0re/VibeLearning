# 🎯 Quiz Game Challenges

Extend your quiz game with these additional features. Each challenge builds on your existing knowledge and introduces new concepts.

---

## Challenge 1: Question Editor

Add the ability to create, edit, and delete questions directly from the application.

### Features to Add

1. **Add New Question** — Create a new question through the CLI
2. **Edit Question** — Modify existing questions
3. **Delete Question** — Remove questions from the bank
4. **View All Questions** — List all questions with filters

### Implementation

```python
def add_question_menu(self):
    """Add a new question to the question bank."""
    print("\n" + "=" * 50)
    print("           ADD NEW QUESTION")
    print("=" * 50)
    
    # Get question text
    question_text = input("Enter question text: ").strip()
    if not question_text:
        print("Question text cannot be empty!")
        return
    
    # Get options
    options = []
    for i in range(4):
        option = input(f"Enter option {chr(65 + i)}: ").strip()
        options.append(option)
    
    # Get correct answer
    while True:
        correct = input("Correct answer (A/B/C/D): ").strip().upper()
        if correct in ['A', 'B', 'C', 'D']:
            correct_index = ord(correct) - ord('A')
            break
        print("Invalid input. Please enter A, B, C, or D.")
    
    # Get category
    category = input("Category (default: General): ").strip() or "General"
    
    # Get difficulty
    print("\nDifficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    diff_choice = input("Select (1-3): ").strip()
    difficulties = {"1": "Easy", "2": "Medium", "3": "Hard"}
    difficulty = difficulties.get(diff_choice, "Medium")
    
    # Get points
    points = input("Points (default: 10): ").strip()
    points = int(points) if points.isdigit() else 10
    
    # Create and add question
    new_question = Question(
        question_text=question_text,
        options=options,
        correct_answer=correct_index,
        category=category,
        difficulty=difficulty,
        points=points
    )
    
    self.questions.append(new_question)
    self.save_questions()
    print("\nQuestion added successfully!")

def save_questions(self):
    """Save all questions to JSON file."""
    data = {
        "questions": [
            {
                "question": q.question_text,
                "options": q.options,
                "correct_answer": q.correct_answer,
                "category": q.category,
                "difficulty": q.difficulty,
                "points": q.points
            }
            for q in self.questions
        ]
    }
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, "questions.json")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
```

### New Menu Option

Add to the main menu:
- 6. Question Editor

---

## Challenge 2: Lifelines

Add "Who Wants to Be a Millionaire" style lifelines to help players.

### Features to Add

1. **50/50** — Remove two wrong answers
2. **Ask the Audience** — Show simulated audience votes
3. **Phone a Friend** — Get a hint with a probability of being correct

### Implementation

```python
class QuizGame:
    def __init__(self, questions, time_per_question=30):
        # ... existing code ...
        self.lifelines = {
            "50_50": True,
            "audience": True,
            "phone": True
        }
    
    def use_50_50(self, question):
        """Remove two wrong answers."""
        if not self.lifelines["50_50"]:
            print("You've already used this lifeline!")
            return None
        
        # Keep correct answer and one random wrong answer
        wrong_indices = [i for i in range(4) if i != question.correct_answer]
        keep_wrong = random.choice(wrong_indices)
        
        removed = [i for i in wrong_indices if i != keep_wrong]
        self.lifelines["50_50"] = False
        
        print("\n50/50 used! Two wrong answers removed.")
        return removed  # Indices of removed options
    
    def ask_audience(self, question):
        """Simulate audience votes."""
        if not self.lifelines["audience"]:
            print("You've already used this lifeline!")
            return None
        
        self.lifelines["audience"] = False
        
        # Generate audience votes (correct answer gets more votes)
        votes = [0, 0, 0, 0]
        total_votes = 100
        
        # Correct answer gets 40-70% of votes
        correct_votes = random.randint(40, 70)
        votes[question.correct_answer] = correct_votes
        remaining = total_votes - correct_votes
        
        # Distribute remaining votes among wrong answers
        wrong_indices = [i for i in range(4) if i != question.correct_answer]
        for i, idx in enumerate(wrong_indices[:-1]):
            if i == len(wrong_indices) - 2:
                votes[idx] = remaining
            else:
                v = random.randint(0, remaining)
                votes[idx] = v
                remaining -= v
        
        print("\n📊 Audience Votes:")
        for i, vote in enumerate(votes):
            bar = "█" * (vote // 5)
            print(f"  {chr(65 + i)}: {bar} {vote}%")
        
        return votes
    
    def phone_friend(self, question):
        """Get a suggestion from a 'friend'."""
        if not self.lifelines["phone"]:
            print("You've already used this lifeline!")
            return None
        
        self.lifelines["phone"] = False
        
        # Friend is 70% likely to give correct answer
        if random.random() < 0.7:
            suggestion = question.correct_answer
        else:
            wrong_indices = [i for i in range(4) if i != question.correct_answer]
            suggestion = random.choice(wrong_indices)
        
        friend_names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
        friend = random.choice(friend_names)
        
        confidence = random.choice([
            "I'm pretty sure it's",
            "I think it's",
            "If I had to guess, I'd say",
            "Definitely"
        ])
        
        print(f"\n📞 {friend} says: \"{confidence} option {chr(65 + suggestion)}.\"")
        return suggestion
    
    def reset_lifelines(self):
        """Reset lifelines for a new game."""
        self.lifelines = {
            "50_50": True,
            "audience": True,
            "phone": True
        }
```

### Update Question Display

```python
def display_lifelines(self):
    """Display available lifelines."""
    print("\nLifelines available:")
    if self.lifelines["50_50"]:
        print("  [1] 50/50 - Remove two wrong answers")
    if self.lifelines["audience"]:
        print("  [2] Ask the Audience - See audience votes")
    if self.lifelines["phone"]:
        print("  [3] Phone a Friend - Get a suggestion")
    print("  [Enter] Skip lifeline")
```

---

## Challenge 3: Streak Multiplier

Add bonus points for consecutive correct answers.

### Features to Add

1. **Streak Counter** — Track consecutive correct answers
2. **Multiplier Bonus** — Increase points for streaks
3. **Streak Display** — Show current streak during game

### Implementation

```python
class QuizGame:
    def __init__(self, questions, time_per_question=30):
        # ... existing code ...
        self.streak = 0
        self.max_streak = 0
    
    def reset_game(self):
        # ... existing code ...
        self.streak = 0
        self.max_streak = 0
    
    def calculate_streak_bonus(self, base_points):
        """Calculate bonus based on current streak."""
        # Bonus multiplier: 1x, 1.2x, 1.5x, 2x, 2.5x
        multipliers = [1, 1, 1.2, 1.5, 2, 2.5]
        multiplier = multipliers[min(self.streak, len(multipliers) - 1)]
        return int(base_points * multiplier)
    
    def ask_question(self, question):
        # ... existing question display code ...
        
        # Show streak if > 0
        if self.streak > 1:
            print(f"🔥 Streak: {self.streak}x!", end="")
            if self.streak >= 3:
                print(" (Bonus active!)")
            else:
                print()
        
        # ... get answer ...
        
        if question.is_correct(answer_index):
            self.streak += 1
            if self.streak > self.max_streak:
                self.max_streak = self.streak
            
            # Calculate points with streak bonus
            base_points = question.points
            total_points = self.calculate_streak_bonus(base_points)
            bonus = total_points - base_points
            
            print(f"\nCorrect! +{base_points} points", end="")
            if bonus > 0:
                print(f" (Streak bonus: +{bonus})", end="")
            print()
            return True, total_points
        else:
            # Reset streak on wrong answer
            if self.streak > 0:
                print(f"\nStreak broken! (Max streak: {self.streak})")
            self.streak = 0
            # ... show correct answer ...
            return False, 0
```

---

## Challenge 4: Timed Mode

Add a total timer mode where players race against the clock for the entire quiz.

### Features to Add

1. **Total Timer Mode** — Set a total time for the entire quiz
2. **Time Pressure Scoring** — Bonus points for finishing early
3. **Survival Mode** — Keep going until time runs out

### Implementation

```python
class QuizGame:
    def __init__(self, questions, time_per_question=30):
        # ... existing code ...
        self.total_time_limit = None
        self.quiz_start_time = None
    
    def start_timed_mode(self, category="All", difficulty="All", 
                         total_minutes=5):
        """Start a timed quiz mode."""
        self.reset_game()
        self.total_time_limit = total_minutes * 60
        self.category = category
        self.difficulty = difficulty
        
        # Load all available questions (no limit)
        self.current_questions = filter_questions(
            self.all_questions, category, difficulty, count=999
        )
        
        print(f"\nTIMED MODE: {total_minutes} minutes")
        print(f"Answer as many questions as you can!")
        print(f"Category: {category} | Difficulty: {difficulty}")
        
        input("\nPress Enter to start...")
        self.quiz_start_time = time.time()
        return True
    
    def check_time_remaining(self):
        """Check how much time is remaining."""
        if self.total_time_limit is None:
            return float('inf')
        
        elapsed = time.time() - self.quiz_start_time
        remaining = self.total_time_limit - elapsed
        return remaining
    
    def run_timed_quiz(self):
        """Run timed quiz mode."""
        questions_answered = 0
        
        for question in self.current_questions:
            # Check time
            remaining = self.check_time_remaining()
            if remaining <= 0:
                print("\n⏰ Time's up!")
                break
            
            # Show remaining time
            print(f"\n[Time remaining: {int(remaining // 60)}:{int(remaining % 60):02d}]")
            
            is_correct, points = self.ask_question(question)
            questions_answered += 1
            
            if is_correct:
                self.correct_answers += 1
                self.score += points
            else:
                self.wrong_answers += 1
        
        # Time bonus for finishing early
        remaining = self.check_time_remaining()
        if remaining > 0:
            time_bonus = int(remaining / 10)  # 1 point per 10 seconds remaining
            self.score += time_bonus
            print(f"\nTime bonus: +{time_bonus} points!")
        
        return self.show_results()
```

---

## Challenge 5: Multiplayer Mode

Add support for 2 or more players to compete.

### Features to Add

1. **Hot Seat Mode** — Players take turns on the same device
2. **Round-Based** — Each player answers the same questions
3. **Winner Display** — Show final standings

### Implementation

```python
class MultiplayerGame:
    """Handles multiplayer quiz games."""
    
    def __init__(self, questions):
        self.questions = questions
        self.players = []
        self.scores = {}
    
    def setup_players(self):
        """Get player names."""
        print("\n" + "=" * 50)
        print("           MULTIPLAYER SETUP")
        print("=" * 50)
        
        while True:
            name = input(f"Enter player {len(self.players) + 1} name (or Enter to start): ").strip()
            if not name:
                if len(self.players) >= 2:
                    break
                print("Need at least 2 players!")
            elif name in self.players:
                print("Name already taken!")
            else:
                self.players.append(name)
                self.scores[name] = 0
    
    def play_round(self, question, round_num):
        """Play a round where all players answer."""
        print(f"\n{'=' * 50}")
        print(f"           ROUND {round_num}")
        print(f"{'=' * 50}")
        print(f"\nQuestion: {question.question_text}")
        
        for i, option in enumerate(question.options, 1):
            print(f"  {chr(64 + i)}. {option}")
        
        # Each player answers
        answers = {}
        for player in self.players:
            print(f"\n{player}'s turn:")
            answer = input("Your answer (A/B/C/D): ").strip().upper()
            answers[player] = answer
        
        # Reveal and score
        correct_letter = chr(65 + question.correct_answer)
        print(f"\nCorrect answer: {correct_letter}")
        
        for player, answer in answers.items():
            if answer == correct_letter:
                print(f"  {player}: Correct! +10 points")
                self.scores[player] += 10
            else:
                print(f"  {player}: Wrong (answered {answer})")
    
    def display_standings(self):
        """Display current standings."""
        print("\n" + "=" * 40)
        print("           STANDINGS")
        print("=" * 40)
        
        sorted_scores = sorted(self.scores.items(), key=lambda x: x[1], reverse=True)
        for i, (player, score) in enumerate(sorted_scores, 1):
            print(f"{i}. {player}: {score} points")
        print("=" * 40)
    
    def play_game(self, question_count=10):
        """Run a complete multiplayer game."""
        self.setup_players()
        
        # Select questions
        selected = filter_questions(self.questions, count=question_count)
        
        for i, question in enumerate(selected, 1):
            self.play_round(question, i)
            self.display_standings()
            
            if i < len(selected):
                input("\nPress Enter for next round...")
        
        # Final results
        print("\n" + "=" * 50)
        print("           FINAL RESULTS")
        print("=" * 50)
        self.display_standings()
        
        winner = max(self.scores.items(), key=lambda x: x[1])
        print(f"\n🏆 Winner: {winner[0]} with {winner[1]} points!")
```

---

## Challenge 6: Export Results

Add the ability to export quiz results to various formats.

### Features to Add

1. **Text Export** — Save results to a text file
2. **CSV Export** — Export for spreadsheet analysis
3. **Detailed Report** — Include all answered questions

### Implementation

```python
def export_results_text(self, filename="quiz_results.txt"):
    """Export quiz results to a text file."""
    total_questions = len(self.current_questions)
    accuracy = (self.correct_answers / total_questions * 100) if total_questions > 0 else 0
    
    with open(filename, 'w') as f:
        f.write("=" * 50 + "\n")
        f.write("           QUIZ RESULTS\n")
        f.write("=" * 50 + "\n\n")
        f.write(f"Date: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Category: {self.category}\n")
        f.write(f"Difficulty: {self.difficulty}\n\n")
        f.write(f"Questions: {total_questions}\n")
        f.write(f"Correct: {self.correct_answers}\n")
        f.write(f"Wrong: {self.wrong_answers}\n")
        f.write(f"Accuracy: {accuracy:.1f}%\n")
        f.write(f"Final Score: {self.score}\n")
        f.write("\n" + "=" * 50 + "\n")
    
    print(f"Results exported to {filename}")

def export_leaderboard_csv(self, filename="leaderboard.csv"):
    """Export leaderboard to CSV."""
    import csv
    
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Rank', 'Name', 'Score', 'Category', 'Difficulty', 'Accuracy', 'Date'])
        
        for i, entry in enumerate(self.leaderboard.scores, 1):
            writer.writerow([
                i, entry['name'], entry['score'], 
                entry['category'], entry['difficulty'],
                entry['accuracy'], entry['date']
            ])
    
    print(f"Leaderboard exported to {filename}")
```

---

## Challenge 7: Question Images

Add support for image-based questions (ASCII art or file paths).

### Features to Add

1. **ASCII Art Questions** — Display ASCII art as questions
2. **File Path Support** — Reference external image files
3. **Visual Hints** — Show visual clues

### Implementation

```python
# Sample ASCII art questions in JSON
{
  "question": "What is this shape?",
  "image": "
     /\\
    /  \\
   /____\\
  /      \\
 /        \\
",
  "options": ["Square", "Triangle", "Circle", "Rectangle"],
  "correct_answer": 1,
  "category": "Visual",
  "difficulty": "Easy"
}

# Modified Question class
def display(self):
    """Display the question with optional image."""
    if hasattr(self, 'image') and self.image:
        print(self.image)
    
    print(f"\n{self.question_text}")
    print("-" * 50)
    for i, option in enumerate(self.options, 1):
        print(f"  {chr(64 + i)}. {option}")
```

---

## 🏆 Challenge Completion

Track your progress:

- [ ] Challenge 1: Question Editor
- [ ] Challenge 2: Lifelines
- [ ] Challenge 3: Streak Multiplier
- [ ] Challenge 4: Timed Mode
- [ ] Challenge 5: Multiplayer Mode
- [ ] Challenge 6: Export Results
- [ ] Challenge 7: Question Images

---

**Tip:** Complete challenges in any order. Start with the ones that interest you most!

**Bonus Idea:** Combine multiple challenges! For example, add lifelines to multiplayer mode, or create a timed survival mode with streak multipliers.
