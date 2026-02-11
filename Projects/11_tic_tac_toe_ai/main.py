"""
Tic-Tac-Toe AI - Main Game Module
=================================
Entry point for the Tic-Tac-Toe game with AI opponent.

Run: python main.py
"""

from board import Board
from ai_player import AIPlayer
import random


class GameStatistics:
    """Track game statistics across sessions."""
    
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.games_played = 0
    
    def record_win(self):
        self.wins += 1
        self.games_played += 1
    
    def record_loss(self):
        self.losses += 1
        self.games_played += 1
    
    def record_draw(self):
        self.draws += 1
        self.games_played += 1
    
    def display(self):
        print("\n" + "=" * 40)
        print("         GAME STATISTICS")
        print("=" * 40)
        print(f"  Games Played: {self.games_played}")
        print(f"  Wins:         {self.wins}")
        print(f"  Losses:       {self.losses}")
        print(f"  Draws:        {self.draws}")
        if self.games_played > 0:
            win_rate = (self.wins / self.games_played) * 100
            print(f"  Win Rate:     {win_rate:.1f}%")
        print("=" * 40)


class TicTacToeGame:
    """Main game controller class."""
    
    def __init__(self):
        self.board = Board()
        self.ai = AIPlayer()
        self.stats = GameStatistics()
        self.difficulty = "hard"  # easy, medium, hard
        self.human_symbol = "X"
        self.ai_symbol = "O"
    
    def display_menu(self):
        print("\n" + "=" * 40)
        print("       TIC-TAC-TOE AI")
        print("=" * 40)
        print("  1. Play vs AI (You go first)")
        print("  2. Play vs AI (AI goes first)")
        print("  3. AI vs AI (Watch)")
        print("  4. View Statistics")
        print("  5. Change Difficulty")
        print("  6. Quit")
        print("=" * 40)
    
    def get_menu_choice(self):
        while True:
            choice = input("Choose an option (1-6): ").strip()
            if choice in ["1", "2", "3", "4", "5", "6"]:
                return choice
            print("Invalid choice. Please enter 1-6.")
    
    def change_difficulty(self):
        print("\n--- Difficulty Level ---")
        print("  1. Easy (Random moves)")
        print("  2. Medium (Sometimes smart)")
        print("  3. Hard (Unbeatable)")
        
        while True:
            choice = input("Select difficulty (1-3): ").strip()
            if choice == "1":
                self.difficulty = "easy"
                print("Difficulty set to EASY")
                break
            elif choice == "2":
                self.difficulty = "medium"
                print("Difficulty set to MEDIUM")
                break
            elif choice == "3":
                self.difficulty = "hard"
                print("Difficulty set to HARD")
                break
            else:
                print("Invalid choice. Please enter 1-3.")
    
    def get_human_move(self):
        """Get and validate human player move."""
        while True:
            try:
                move_input = input("Your move (row col, e.g., '1 1'): ").strip()
                parts = move_input.split()
                
                if len(parts) != 2:
                    print("Please enter two numbers separated by space.")
                    continue
                
                row, col = int(parts[0]), int(parts[1])
                
                if not (0 <= row <= 2 and 0 <= col <= 2):
                    print("Row and column must be between 0 and 2.")
                    continue
                
                if not self.board.is_empty(row, col):
                    print("That cell is already occupied!")
                    continue
                
                return row, col
            
            except ValueError:
                print("Invalid input. Please enter numbers only.")
    
    def play_human_vs_ai(self, human_first=True):
        """Play a game of human vs AI."""
        self.board.reset()
        
        if human_first:
            current_player = "human"
            self.human_symbol = "X"
            self.ai_symbol = "O"
        else:
            current_player = "ai"
            self.human_symbol = "O"
            self.ai_symbol = "X"
        
        print(f"\n--- Human vs AI ({self.difficulty.upper()}) ---")
        print(f"You are '{self.human_symbol}', AI is '{self.ai_symbol}'")
        
        while True:
            self.board.display()
            
            if self.board.is_full():
                print("\n*** It's a DRAW! ***")
                self.stats.record_draw()
                break
            
            if current_player == "human":
                row, col = self.get_human_move()
                self.board.make_move(row, col, self.human_symbol)
                
                if self.board.check_winner() == self.human_symbol:
                    self.board.display()
                    print("\n*** YOU WIN! ***")
                    self.stats.record_win()
                    break
                
                current_player = "ai"
            
            else:  # AI's turn
                print("\nAI is thinking...")
                row, col = self.ai.get_move(
                    self.board, 
                    self.ai_symbol, 
                    self.human_symbol,
                    self.difficulty
                )
                self.board.make_move(row, col, self.ai_symbol)
                print(f"AI plays: {row} {col}")
                
                if self.board.check_winner() == self.ai_symbol:
                    self.board.display()
                    print("\n*** AI WINS! ***")
                    self.stats.record_loss()
                    break
                
                current_player = "human"
    
    def play_ai_vs_ai(self):
        """Watch AI play against itself."""
        self.board.reset()
        
        ai1_symbol = "X"
        ai2_symbol = "O"
        current_symbol = ai1_symbol
        
        print("\n--- AI vs AI ---")
        print("Watching two AIs battle it out...")
        input("Press Enter to start...")
        
        move_count = 0
        max_moves = 9
        
        while move_count < max_moves:
            self.board.display()
            
            if self.board.is_full():
                print("\n*** It's a DRAW! ***")
                break
            
            print(f"\nAI ({current_symbol}) is thinking...")
            
            # Both AIs use hard difficulty for competitive play
            opponent = ai2_symbol if current_symbol == ai1_symbol else ai1_symbol
            row, col = self.ai.get_move(
                self.board,
                current_symbol,
                opponent,
                "hard"
            )
            
            self.board.make_move(row, col, current_symbol)
            print(f"AI ({current_symbol}) plays: {row} {col}")
            move_count += 1
            
            if self.board.check_winner() == current_symbol:
                self.board.display()
                print(f"\n*** AI ({current_symbol}) WINS! ***")
                break
            
            current_symbol = ai2_symbol if current_symbol == ai1_symbol else ai1_symbol
            
            # Pause briefly between moves for visibility
            import time
            time.sleep(1)
    
    def run(self):
        """Main game loop."""
        print("\nWelcome to Tic-Tac-Toe AI!")
        print("Can you beat the unbeatable AI?")
        
        while True:
            self.display_menu()
            choice = self.get_menu_choice()
            
            if choice == "1":
                self.play_human_vs_ai(human_first=True)
            elif choice == "2":
                self.play_human_vs_ai(human_first=False)
            elif choice == "3":
                self.play_ai_vs_ai()
            elif choice == "4":
                self.stats.display()
            elif choice == "5":
                self.change_difficulty()
            elif choice == "6":
                print("\nThanks for playing!")
                print("Final Statistics:")
                self.stats.display()
                break


def main():
    """Entry point for the game."""
    game = TicTacToeGame()
    game.run()


if __name__ == "__main__":
    main()
