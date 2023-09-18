from copy import deepcopy
import math

RED = (255, 0, 0)
WHITE = (255, 255, 255)


def minimax(position, depth, maxPlayer):
    if depth == 0:
        return position.evaluate(), position

    value = None
    newBoard = deepcopy(position)

    if maxPlayer == True:
        value = -math.inf
        for board in getAllMoves(position, WHITE):
            newValue = minimax(board, depth - 1, False)[0]
            if newValue >= value:
                value = newValue
                newBoard = deepcopy(board)

    elif maxPlayer == False:
        value = math.inf
        for board in getAllMoves(position, RED):
            newValue = minimax(board, depth - 1, True)[0]
            if newValue <= value:
                value = newValue
                newBoard = deepcopy(board)

    return value, newBoard


def simulateMove(piece, move, board, skip):
    board.remove(skip)
    board.move(piece, move[0], move[1])
    return board


def getAllMoves(board, color):
    boards = []
    for piece in board.getAllPieces(color):
        for move, skipped in board.getValidMoves(piece).items():
            newBoard = deepcopy(board)
            newBoard = simulateMove(newBoard.getPiece(piece.row, piece.col), move, newBoard, skipped)
            boards.append(newBoard)
    return boards