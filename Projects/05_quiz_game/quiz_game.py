"""
Quiz Game Project
=================
An interactive multiple-choice quiz game with categories, 
difficulty levels, scoring, and a leaderboard.
"""

import json
import random
import time
import os


# =============================================================================
# QUESTION CLASS
# =============================================================================

class Question:
    """Represents a single quiz question."""
    
    def __init__(self, question_text, options, correct_answer, 
                 category="General", difficulty="Medium", points=10):
        self.question_text = question_text
        self.options = options
        self.correct_answer = correct_answer
        self.category = category
        self.difficulty = difficulty
        self.points = points
    
    def is_correct(self, answer):
        """Check if the given answer is correct.
        
        Args:
            answer: Can be an index (0-3) or a letter ('A'-'D')
        
        Returns:
            bool: True if answer is correct
        """
        if isinstance(answer, int):
            return answer == self.correct_answer
        elif isinstance(answer, str) and len(answer) == 1:
            answer_index = ord(answer.upper()) - ord('A')
            return answer_index == self.correct_answer
        return False
    
    def display(self):
        """Display the question with options."""
        print(f"\n{self.question_text}")
        print("-" * 50)
        for i, option in enumerate(self.options, 1):
            print(f"  {chr(64 + i)}. {option}")


# =============================================================================
# QUESTION LOADING FUNCTIONS
# =============================================================================

def load_questions(filename="questions.json"):
    """Load questions from JSON file.
    
    Args:
        filename: Path to the JSON file containing questions
    
    Returns:
        list: List of Question objects
    """
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, filename)
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
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
    """Filter questions by category and difficulty, then shuffle.
    
    Args:
        questions: List of Question objects
        category: Category to filter by (or "All")
        difficulty: Difficulty to filter by (or "All")
        count: Maximum number of questions to return
    
    Returns:
        list: Filtered and shuffled questions
    """
    filtered = questions[:]
    
    if category and category != "All":
        filtered = [q for q in filtered if q.category == category]
    
    if difficulty and difficulty != "All":
        filtered = [q for q in filtered if q.difficulty == difficulty]
    
    random.shuffle(filtered)
    return filtered[:count]


# =============================================================================
# LEADERBOARD CLASS
# =============================================================================

class Leaderboard:
    """Manages high scores and leaderboard."""
    
    def __init__(self, filename="leaderboard.json"):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.filename = os.path.join(script_dir, filename)
        self.scores = self.load_scores()
    
    def load_scores(self):
        """Load scores from file."""
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []
    
    def save_scores(self):
        """Save scores to file."""
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(self.scores, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving scores: {e}")
            return False
    
    def add_score(self, name, score, category, difficulty, accuracy):
        """Add a new score to the leaderboard."""
        entry = {
            "name": name[:15],  # Limit name length
            "score": score,
            "category": category,
            "difficulty": difficulty,
            "accuracy": round(accuracy, 1),
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
        print("                        LEADERBOARD")
        print("=" * 70)
        
        if not self.scores:
            print("No scores yet! Be the first to play!")
            return
        
        print(f"{'Rank':<6} {'Name':<15} {'Score':<8} {'Category':<12} {'Diff':<8} {'Date':<16}")
        print("-" * 70)
        
        for i, entry in enumerate(self.scores[:limit], 1):
            medal = ""
            if i == 1:
                medal = "🥇 "
            elif i == 2:
                medal = "🥈 "
            elif i == 3:
                medal = "🥉 "
            
            print(f"{medal}{i:<4} {entry['name']:<15} {entry['score']:<8} "
                  f"{entry['category']:<12} {entry['difficulty']:<8} {entry['date']:<16}")
        
        print("=" * 70)


# =============================================================================
# QUIZ GAME CLASS
# =============================================================================

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
        self.category = "All"
        self.difficulty = "All"
    
    def start_quiz(self, category="All", difficulty="All", question_count=10):
        """Start a new quiz session.
        
        Args:
            category: Category filter
            difficulty: Difficulty filter
            question_count: Number of questions
        
        Returns:
            bool: True if quiz started successfully
        """
        self.reset_game()
        self.category = category
        self.difficulty = difficulty
        self.current_questions = filter_questions(
            self.all_questions, category, difficulty, question_count
        )
        
        if not self.current_questions:
            print("No questions available for selected criteria!")
            return False
        
        print("\n" + "=" * 50)
        print(f"Starting quiz with {len(self.current_questions)} questions...")
        print(f"Category: {category} | Difficulty: {difficulty}")
        print(f"Time per question: {self.time_per_question} seconds")
        print("=" * 50)
        
        input("\nPress Enter to start...")
        return True
    
    def ask_question(self, question):
        """Ask a single question and return if correct.
        
        Args:
            question: Question object to ask
        
        Returns:
            tuple: (is_correct, points_earned)
        """
        print("\n" + "=" * 50)
        print(f"Question {self.current_question_index + 1} of {len(self.current_questions)}")
        print(f"Category: {question.category} | Points: {question.points}")
        print("=" * 50)
        
        question.display()
        
        # Start timer
        start_time = time.time()
        
        # Get answer
        answer = input("\nYour answer (A/B/C/D): ").strip().upper()
        
        elapsed_time = time.time() - start_time
        
        # Validate input
        if answer not in ['A', 'B', 'C', 'D']:
            print("\nInvalid input! Please enter A, B, C, or D.")
            return False, 0
        
        # Convert letter to index (A=0, B=1, etc.)
        answer_index = ord(answer) - ord('A')
        
        # Check if time exceeded
        if elapsed_time > self.time_per_question:
            print(f"\nTime's up! You took {elapsed_time:.1f} seconds.")
            correct_letter = chr(65 + question.correct_answer)
            correct_text = question.options[question.correct_answer]
            print(f"The correct answer was {correct_letter}: {correct_text}")
            return False, 0
        
        # Check answer
        if question.is_correct(answer_index):
            # Calculate time bonus (1 point per 5 seconds under limit, max 5 bonus)
            time_bonus = min(5, max(0, int((self.time_per_question - elapsed_time) / 5)))
            total_points = question.points + time_bonus
            print(f"\nCorrect! +{question.points} points", end="")
            if time_bonus > 0:
                print(f" (Time bonus: +{time_bonus})", end="")
            print()
            return True, total_points
        else:
            correct_letter = chr(65 + question.correct_answer)
            correct_text = question.options[question.correct_answer]
            print(f"\nWrong! The correct answer was {correct_letter}: {correct_text}")
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
        print(f"Correct: {self.correct_answers}")
        print(f"Wrong: {self.wrong_answers}")
        print(f"Accuracy: {accuracy:.1f}%")
        print(f"\nFINAL SCORE: {self.score}")
        
        # Performance rating
        if accuracy >= 90:
            print("\nExcellent work! You're a trivia master!")
        elif accuracy >= 70:
            print("\nGreat job! You did really well!")
        elif accuracy >= 50:
            print("\nGood effort! Keep practicing!")
        else:
            print("\nKeep learning! You'll do better next time!")
        
        print("=" * 50)
        
        return self.score, accuracy


# =============================================================================
# QUIZ APP CLASS
# =============================================================================

class QuizApp:
    """Main application class that handles the menu and game flow."""
    
    def __init__(self):
        self.questions = load_questions()
        self.leaderboard = Leaderboard()
        self.game = QuizGame(self.questions)
    
    def display_welcome(self):
        """Display welcome screen."""
        print("\n" + "=" * 60)
        print("     WELCOME TO THE PYTHON QUIZ GAME!")
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
        """Display available categories with question counts."""
        categories = {}
        difficulties = {}
        
        for q in self.questions:
            categories[q.category] = categories.get(q.category, 0) + 1
            difficulties[q.difficulty] = difficulties.get(q.difficulty, 0) + 1
        
        print("\n" + "=" * 40)
        print("           CATEGORIES")
        print("=" * 40)
        for cat, count in sorted(categories.items()):
            print(f"  {cat}: {count} questions")
        print("-" * 40)
        print("           DIFFICULTY LEVELS")
        print("=" * 40)
        for diff in ["Easy", "Medium", "Hard"]:
            if diff in difficulties:
                print(f"  {diff}: {difficulties[diff]} questions")
        print("=" * 40)
        print(f"Total: {len(self.questions)} questions available")
    
    def run(self):
        """Main application loop."""
        self.display_welcome()
        
        # Check if questions loaded
        if not self.questions:
            print("\nError: No questions loaded. Please check questions.json file.")
            return
        
        while True:
            self.display_menu()
            choice = self.get_choice(1, 5)
            
            if choice == 1:
                # Start quiz
                category = self.select_category()
                difficulty = self.select_difficulty()
                count = self.select_question_count()
                
                if self.game.start_quiz(category, difficulty, count):
                    score, accuracy = self.game.run_quiz()
                    
                    # Save to leaderboard
                    if score > 0:
                        name = input("\nEnter your name for the leaderboard: ").strip()
                        if name:
                            self.leaderboard.add_score(
                                name, score, category, difficulty, accuracy
                            )
                            print(f"\nScore saved! Great job, {name}!")
            
            elif choice == 2:
                self.leaderboard.display()
            
            elif choice == 3:
                self.show_categories()
            
            elif choice == 4:
                self.show_instructions()
            
            elif choice == 5:
                print("\nThanks for playing! Goodbye!")
                break


# =============================================================================
# MAIN ENTRY POINT
# =============================================================================

def main():
    """Entry point for the quiz game."""
    try:
        app = QuizApp()
        app.run()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing!")


if __name__ == "__main__":
    main()
