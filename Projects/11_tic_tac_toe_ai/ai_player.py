"""
Tic-Tac-Toe AI - AI Player Module
=================================
Implements the AI player using the minimax algorithm with alpha-beta pruning.

The minimax algorithm explores all possible game states to find the optimal move.
Alpha-beta pruning optimizes minimax by eliminating branches that cannot affect
the final decision.
"""

import random
from board import Board


class AIPlayer:
    """
    AI player using minimax algorithm with alpha-beta pruning.
    
    The AI evaluates game states and chooses moves that maximize its chances
    of winning while minimizing the opponent's chances.
    """
    
    def __init__(self):
        self.nodes_evaluated = 0  # For performance tracking
    
    def get_move(self, board, ai_symbol, human_symbol, difficulty="hard"):
        """
        Get the AI's next move based on difficulty level.
        
        Args:
            board: Current game board
            ai_symbol: Symbol used by AI ("X" or "O")
            human_symbol: Symbol used by human ("X" or "O")
            difficulty: "easy", "medium", or "hard"
        
        Returns:
            tuple: (row, col) of the chosen move
        """
        self.nodes_evaluated = 0
        
        if difficulty == "easy":
            return self._get_random_move(board)
        elif difficulty == "medium":
            # 50% chance of smart move, 50% random
            if random.random() < 0.5:
                return self._get_random_move(board)
            else:
                return self._get_minimax_move(board, ai_symbol, human_symbol)
        else:  # hard
            return self._get_minimax_move(board, ai_symbol, human_symbol)
    
    def _get_random_move(self, board):
        """Get a random valid move."""
        available = board.get_available_moves()
        return random.choice(available)
    
    def _get_minimax_move(self, board, ai_symbol, human_symbol):
        """
        Get the best move using minimax with alpha-beta pruning.
        
        This is the entry point for the minimax algorithm.
        """
        best_score = float('-inf')
        best_move = None
        
        available_moves = board.get_available_moves()
        
        for row, col in available_moves:
            # Try this move
            board.make_move(row, col, ai_symbol)
            
            # Evaluate this move using minimax
            score = self._minimax(
                board, 
                0, 
                False,  # Next turn is human (minimizing)
                ai_symbol,
                human_symbol,
                float('-inf'),
                float('inf')
            )
            
            # Undo the move
            board.undo_move(row, col)
            
            # Update best move if this one is better
            if score > best_score:
                best_score = score
                best_move = (row, col)
        
        return best_move
    
    def _minimax(self, board, depth, is_maximizing, ai_symbol, human_symbol, alpha, beta):
        """
        Minimax algorithm with alpha-beta pruning.
        
        This recursive function evaluates all possible game states to find
        the optimal move. It alternates between maximizing (AI) and minimizing
        (human) players.
        
        Args:
            board: Current game board state
            depth: Current depth in the game tree
            is_maximizing: True if it's the maximizing player's turn (AI)
            ai_symbol: AI's symbol
            human_symbol: Human's symbol
            alpha: Best value maximizer can guarantee
            beta: Best value minimizer can guarantee
        
        Returns:
            int: Score of the board state
        """
        self.nodes_evaluated += 1
        
        # Check terminal states
        winner = board.check_winner()
        
        if winner == ai_symbol:
            # AI wins - positive score, prefer quicker wins
            return 10 - depth
        elif winner == human_symbol:
            # Human wins - negative score, prefer longer games when losing
            return depth - 10
        elif board.is_full():
            # Draw
            return 0
        
        if is_maximizing:
            # AI's turn - maximize the score
            max_eval = float('-inf')
            
            for row, col in board.get_available_moves():
                board.make_move(row, col, ai_symbol)
                eval_score = self._minimax(
                    board, 
                    depth + 1, 
                    False, 
                    ai_symbol, 
                    human_symbol,
                    alpha,
                    beta
                )
                board.undo_move(row, col)
                
                max_eval = max(max_eval, eval_score)
                alpha = max(alpha, eval_score)
                
                # Alpha-beta pruning
                if beta <= alpha:
                    break  # Prune this branch
            
            return max_eval
        
        else:
            # Human's turn - minimize the score
            min_eval = float('inf')
            
            for row, col in board.get_available_moves():
                board.make_move(row, col, human_symbol)
                eval_score = self._minimax(
                    board, 
                    depth + 1, 
                    True, 
                    ai_symbol, 
                    human_symbol,
                    alpha,
                    beta
                )
                board.undo_move(row, col)
                
                min_eval = min(min_eval, eval_score)
                beta = min(beta, eval_score)
                
                # Alpha-beta pruning
                if beta <= alpha:
                    break  # Prune this branch
            
            return min_eval
    
    def get_stats(self):
        """Return statistics about the last move calculation."""
        return {
            'nodes_evaluated': self.nodes_evaluated
        }


# =============================================================================
# DEMONSTRATION
# =============================================================================

if __name__ == "__main__":
    print("=" * 50)
    print("AI PLAYER - Minimax Algorithm Demo")
    print("=" * 50)
    
    # Create a sample board
    board = Board()
    ai = AIPlayer()
    
    # Set up a board state
    board.make_move(0, 0, "X")
    board.make_move(1, 1, "O")
    board.make_move(0, 2, "X")
    
    print("\nSample Board State:")
    board.display()
    
    print("\nAI is thinking...")
    move = ai.get_move(board, "O", "X", "hard")
    stats = ai.get_stats()
    
    print(f"AI chooses: {move}")
    print(f"Nodes evaluated: {stats['nodes_evaluated']}")
    
    print("\n" + "=" * 50)
    print("Demo complete!")
    print("=" * 50)
