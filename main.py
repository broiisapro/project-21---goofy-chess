class ChessPiece:
    def __init__(self, color, name, symbol):
        self.color = color
        self.name = name
        self.symbol = symbol
        self.has_moved = False

    def __repr__(self):
        return self.symbol


class King(ChessPiece):
    def __init__(self, color):
        symbol = "♔" if color == "white" else "♚"
        super().__init__(color, "king", symbol)


class Rook(ChessPiece):
    def __init__(self, color):
        symbol = "♖" if color == "white" else "♜"
        super().__init__(color, "rook", symbol)


class Knight(ChessPiece):
    def __init__(self, color):
        symbol = "♘" if color == "white" else "♞"
        super().__init__(color, "knight", symbol)


class Bishop(ChessPiece):
    def __init__(self, color):
        symbol = "♗" if color == "white" else "♝"
        super().__init__(color, "bishop", symbol)


class Queen(ChessPiece):
    def __init__(self, color):
        symbol = "♕" if color == "white" else "♛"
        super().__init__(color, "queen", symbol)


class Pawn(ChessPiece):
    def __init__(self, color):
        symbol = "♙" if color == "white" else "♟"
        super().__init__(color, "pawn", symbol)

    def can_move(self, start, end, board):
        start_row, start_col = start
        end_row, end_col = end

        # Pawns can move one square forward by default
        if self.color == "white":
            # Move one square forward if the square is empty
            if end_col == start_col and end_row == start_row - 1 and not isinstance(board[end_row][end_col], ChessPiece):
                return True
            # On first move, pawns can move two squares forward if both squares are empty
            if not self.has_moved and end_col == start_col and end_row == start_row - 2 and not isinstance(board[end_row][end_col], ChessPiece) and not isinstance(board[start_row - 1][start_col], ChessPiece):
                return True
        elif self.color == "black":
            # Move one square forward if the square is empty
            if end_col == start_col and end_row == start_row + 1 and not isinstance(board[end_row][end_col], ChessPiece):
                return True
            # On first move, pawns can move two squares forward if both squares are empty
            if not self.has_moved and end_col == start_col and end_row == start_row + 2 and not isinstance(board[end_row][end_col], ChessPiece) and not isinstance(board[start_row + 1][start_col], ChessPiece):
                return True
        return False



class ChessBoard:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.white_king_position = (7, 4)  # Starting position of white king
        self.black_king_position = (0, 4)  # Starting position of black king
        self.castling_rights = {
            "white": {"kingside": True, "queenside": True},
            "black": {"kingside": True, "queenside": True},
        }
        self.en_passant_target = None
        self.setup_board()

    def setup_board(self):
        # Place major pieces for both sides
        self.board[0] = [
            Rook("black"), Knight("black"), Bishop("black"), Queen("black"),
            King("black"), Bishop("black"), Knight("black"), Rook("black")
        ]
        self.board[7] = [
            Rook("white"), Knight("white"), Bishop("white"), Queen("white"),
            King("white"), Bishop("white"), Knight("white"), Rook("white")
        ]
        
        # Place pawns for both sides
        self.board[1] = [Pawn("black") for _ in range(8)]
        self.board[6] = [Pawn("white") for _ in range(8)]

    def display(self):
        print("   a    b    c    d    e    f    g    h  ")
        print(" +--------------------------------------+")
        row_num = 8
        for row in self.board:
            print(f"{row_num}|", end="")
            for square in row:
                if square:
                    print(f"  {square}  ", end="")
                else:
                    print("  .  ", end="")
            print(f"| {row_num}")
            row_num -= 1
        print(" +--------------------------------------+")

    def is_valid_move(self, start, end, color):
        start_row, start_col = start
        end_row, end_col = end
        piece = self.board[start_row][start_col]

        if piece and piece.color == color:
            return piece.can_move(start, end, self.board)
        return False

    def move_piece(self, start, end, color):
        start_row, start_col = start
        end_row, end_col = end
        piece = self.board[start_row][start_col]

        if isinstance(piece, Pawn):
            if piece.can_move(start, end, self.board):
                self.board[end_row][end_col] = piece
                self.board[start_row][start_col] = None
                piece.has_moved = True
                return True
        elif isinstance(piece, King):
            # Implement king's movement logic here if necessary
            pass

        # Add more movement logic for other pieces
        return False

    def is_castling_move(self, start, end, color):
        # Castling can only occur if the king and rook haven't moved
        pass

    def castle(self, start, end, color):
        pass



class ChessGame:
    def __init__(self):
        self.board = ChessBoard()
        self.current_turn = "white"

    def play(self):
        while True:
            self.board.display()
            print(f"{self.current_turn.capitalize()}'s turn")
            start = input("Enter the start position (e.g. 'a2'): ")
            end = input("Enter the end position (e.g. 'a3'): ")

            start = self.position_to_coords(start)
            end = self.position_to_coords(end)

            if start and end:
                piece = self.board.board[start[0]][start[1]]
                if piece and piece.color == self.current_turn:
                    if self.board.move_piece(start, end, self.current_turn):
                        self.toggle_turn()
                    else:
                        print("Invalid move! Try again.")
                else:
                    print("Invalid piece selection. Try again.")
            else:
                print("Invalid input format. Please use chess notation.")

    def toggle_turn(self):
        # Switch turns between white and black
        self.current_turn = "black" if self.current_turn == "white" else "white"

    def position_to_coords(self, position):
        try:
            col, row = position[0], position[1]
            col = ord(col.lower()) - ord('a')
            row = 8 - int(row)
            if 0 <= col < 8 and 0 <= row < 8:
                return row, col
            else:
                return None
        except (ValueError, IndexError):
            return None


if __name__ == "__main__":
    game = ChessGame()
    game.play()
