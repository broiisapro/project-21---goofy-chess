# Chess Game

This is a simple chess game built using Python with the Tkinter library for the graphical user interface and the `python-chess` library to manage the chessboard logic.

## Features:
- **Chessboard GUI**: A visually appealing chessboard with alternating square colors (dark green for black squares and light grey for white squares).
- **Piece Movement**: Players can select pieces by clicking on them and move them to valid squares on the board.
- **Piece Highlighting**: The selected piece is highlighted with a red border to indicate the player's selection.


### Images
The game uses images for the chess pieces. You will need to download or create the following image files and place them in an `images/` directory:

- **wp.png**: White pawn
- **bp.png**: Black pawn
- **wr.png**: White rook
- **br.png**: Black rook
- **wn.png**: White knight
- **bn.png**: Black knight
- **wb.png**: White bishop
- **bb.png**: Black bishop
- **wq.png**: White queen
- **bq.png**: Black queen
- **wk.png**: White king
- **bk.png**: Black king

## How to Play:
- Click on a piece to select it. The selected piece will be highlighted with a red border.
- After selecting a piece, click on a valid square to move it.
- The game will automatically update the board after each move.

## Code Overview:
- **Tkinter GUI**: The graphical interface is created using Tkinter. It includes the chessboard layout and allows interaction by clicking the squares.
- **python-chess**: The game logic, such as legal move generation and board state updates, is managed using the `python-chess` library.
- **Highlighting**: When a piece is selected, the square is highlighted with a red border to indicate the selected piece.
