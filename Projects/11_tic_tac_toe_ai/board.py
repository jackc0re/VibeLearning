"""
Tic-Tac-Toe AI - Board Module
=============================
Represents the game board and handles all board-related operations.

This module provides a clean interface for:
- Board state management
- Move validation and execution
- Win detection
- Board display
"""


class Board:
    """
    Represents a Tic-Tac-Toe game board.
    
    The board is a 3x3 grid where each cell can be:
    - ' ' (empty)
    - 'X' (player X)
    - 'O' (player O)
    """
    
    def __init__(self):
        """Initialize an empty 3x3 board."""
        self.size = 3
        self.cells = [[' ' for _ in range(self.size)] for _ in range(self.size)]
    
    def reset(self):
        """Reset the board to empty state."""
        self.cells = [[' ' for _ in range(self.size)] for _ in range(self.size)]
    
    def display(self):
        """Display the current board state."""
        print("\n    0   1   2")
        print("  +---+---+---+")
        
        for i, row in enumerate(self.cells):
            print(f"{i} | {row[0]} | {row[1]} | {row[2]} |")
            print("  +---+---+---+")
    
    def is_empty(self, row, col):
        """
        Check if a cell is empty.
        
        Args:
            row: Row index (0-2)
            col: Column index (0-2)
        
        Returns:
            bool: True if cell is empty
        """
        return self.cells[row][col] == ' '
    
    def make_move(self, row, col, symbol):
        """
        Place a symbol on the board.
        
        Args:
            row: Row index (0-2)
            col: Column index (0-2)
            symbol: 'X' or 'O'
        
        Returns:
            bool: True if move was successful
        """
        if self.is_valid_position(row, col) and self.is_empty(row, col):
            self.cells[row][col] = symbol
            return True
        return False
    
    def undo_move(self, row, col):
        """
        Remove a symbol from the board (used by AI for simulation).
        
        Args:
            row: Row index (0-2)
            col: Column index (0-2)
        """
        if self.is_valid_position(row, col):
            self.cells[row][col] = ' '
    
    def is_valid_position(self, row, col):
        """
        Check if position is within board bounds.
        
        Args:
            row: Row index
            col: Column index
        
        Returns:
            bool: True if position is valid
        """
        return 0 <= row < self.size and 0 <= col < self.size
    
    def get_available_moves(self):
        """
        Get list of all empty cells.
        
        Returns:
            list: List of (row, col) tuples
        """
        moves = []
        for row in range(self.size):
            for col in range(self.size):
                if self.is_empty(row, col):
                    moves.append((row, col))
        return moves
    
    def is_full(self):
        """
        Check if board has no empty cells.
        
        Returns:
            bool: True if board is full
        """
        return len(self.get_available_moves()) == 0
    
    def check_winner(self):
        """
        Check if there's a winner.
        
        Returns:
            str: 'X' or 'O' if there's a winner, None otherwise
        """
        # Check rows
        for row in range(self.size):
            if self.cells[row][0] == self.cells[row][1] == self.cells[row][2] != ' ':
                return self.cells[row][0]
        
        # Check columns
        for col in range(self.size):
            if self.cells[0][col] == self.cells[1][col] == self.cells[2][col] != ' ':
                return self.cells[0][col]
        
        # Check diagonals
        if self.cells[0][0] == self.cells[1][1] == self.cells[2][2] != ' ':
            return self.cells[0][0]
        
        if self.cells[0][2] == self.cells[1][1] == self.cells[2][0] != ' ':
            return self.cells[0][2]
        
        return None
    
    def is_game_over(self):
        """
        Check if game has ended (win or draw).
        
        Returns:
            bool: True if game is over
        """
        return self.check_winner() is not None or self.is_full()
    
    def get_board_state(self):
        """
        Get a copy of the current board state.
        
        Returns:
            list: 3x3 list representing the board
        """
        return [row[:] for row in self.cells]
    
    def copy(self):
        """
        Create a deep copy of the board.
        
        Returns:
            Board: New board with same state
        """
        new_board = Board()
        new_board.cells = self.get_board_state()
        return new_board
    
    def __str__(self):
        """String representation of the board."""
        lines = []
        lines.append("  0 1 2")
        for i, row in enumerate(self.cells):
            lines.append(f"{i} {'|'.join(row)}")
        return '\n'.join(lines)


# =============================================================================
# DEMONSTRATION
# =============================================================================

if __name__ == "__main__":
    print("=" * 50)
    print("BOARD MODULE - Demonstration")
    print("=" * 50)
    
    # Create a new board
    board = Board()
    
    print("\n1. Empty Board:")
    board.display()
    
    print("\n2. Making some moves...")
    board.make_move(0, 0, "X")
    board.make_move(1, 1, "O")
    board.make_move(0, 2, "X")
    board.display()
    
    print("\n3. Available moves:", board.get_available_moves())
    
    print("\n4. Checking for winner...")
    winner = board.check_winner()
    if winner:
        print(f"Winner: {winner}")
    else:
        print("No winner yet")
    
    print("\n5. Complete a winning row...")
    board.make_move(0, 1, "X")
    board.display()
    
    winner = board.check_winner()
    print(f"Winner: {winner}")
    
    print("\n6. Reset board...")
    board.reset()
    board.display()
    
    print("\n" + "=" * 50)
    print("Demo complete!")
    print("=" * 50)
