import tkinter as tk
import chess
import chess.svg

# Create a main window
root = tk.Tk()
root.title("Chess Game")

# Initialize the chess board and game
board = chess.Board()

# Set up the tkinter canvas
canvas = tk.Canvas(root, width=480, height=480)
canvas.pack()

# Mapping from chess notation to pixel positions on the board
square_size = 60  # size of each square on the board
piece_images = {}

# Initialize the images for the chess pieces
def load_images():
    global piece_images
    piece_images = {
        'P': tk.PhotoImage(file="images/wp.png"),
        'p': tk.PhotoImage(file="images/bp.png"),
        'R': tk.PhotoImage(file="images/wr.png"),
        'r': tk.PhotoImage(file="images/br.png"),
        'N': tk.PhotoImage(file="images/wn.png"),
        'n': tk.PhotoImage(file="images/bn.png"),
        'B': tk.PhotoImage(file="images/wb.png"),
        'b': tk.PhotoImage(file="images/bb.png"),
        'Q': tk.PhotoImage(file="images/wq.png"),
        'q': tk.PhotoImage(file="images/bq.png"),
        'K': tk.PhotoImage(file="images/wk.png"),
        'k': tk.PhotoImage(file="images/bk.png")
    }

# Draw the chessboard and pieces
def draw_board():
    canvas.delete("all")  # Clear any previous board
    for row in range(8):
        for col in range(8):
            # Draw the squares (alternating colors)
            color = "#A9D08E" if (row + col) % 2 == 0 else "#D3D3D3"  # light green, light gray
            x1 = col * square_size
            y1 = row * square_size
            x2 = (col + 1) * square_size
            y2 = (row + 1) * square_size
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")
            
            # Highlight the selected square
            if selected_square and selected_square == chess.square(col, 7 - row):
                canvas.create_rectangle(x1, y1, x2, y2, outline="red", width=4)

            # Draw the pieces
            piece = board.piece_at(chess.square(col, 7 - row))  # board is reversed vertically
            if piece:
                piece_image = piece_images.get(piece.symbol())
                if piece_image:
                    canvas.create_image(x1 + square_size // 2, y1 + square_size // 2, image=piece_image)

# Handle the click to make a move
selected_square = None

def on_square_click(event):
    global selected_square
    row = event.y // square_size
    col = event.x // square_size
    clicked_square = chess.square(col, 7 - row)

    if selected_square is None:
        # Select a piece
        if board.piece_at(clicked_square):
            selected_square = clicked_square
    else:
        # Make a move
        move = chess.Move(selected_square, clicked_square)
        if move in board.legal_moves:
            board.push(move)
        selected_square = None

    draw_board()  # Redraw the board with updated pieces

# Bind mouse click event to the board
canvas.bind("<Button-1>", on_square_click)

# Load piece images and draw the initial board
load_images()
draw_board()

# Start the Tkinter event loop
root.mainloop()
