"read a file and create a board"
import sys
import random
import pygame
from pygame.locals import *

def ReadFile(filename):
    board = [[]]
    with open(filename) as f:
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].strip()
            for j in range(len(lines[i])):
                board[i].append(lines[i][j])
            if i != len(lines)-1:
                board.append([])
    return board

def FindStart(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'S':
                return (i, j)
            
def FindFinish(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'F':
                return (i, j)
            
def FindNeighbors(board, pos):
    neighbors = []
    if pos[0] > 0 and board[pos[0]-1][pos[1]] != '*':
        neighbors.append((pos[0]-1, pos[1]))
    if pos[0] < len(board)-1 and board[pos[0]+1][pos[1]] != '*':
        neighbors.append((pos[0]+1, pos[1]))
    if pos[1] > 0 and board[pos[0]][pos[1]-1] != '*':
        neighbors.append((pos[0], pos[1]-1))
    if pos[1] < len(board[0])-1 and board[pos[0]][pos[1]+1] != '*':
        neighbors.append((pos[0], pos[1]+1))
    return neighbors

def FindPath(board):
    start = FindStart(board)
    finish = FindFinish(board)
    stack = [start]
    path = []
    while len(stack) > 0:
        pos = stack.pop()
        if pos == finish:
            path.append(pos)
            break
        if pos not in path:
            path.append(pos)
            neighbors = FindNeighbors(board, pos)
            for neighbor in neighbors:
                stack.append(neighbor)
    return path

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 360))
    pygame.display.set_caption("Maze")
    board = ReadFile("maze.txt")
    path = FindPath(board)
    while (len(path) > 0):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((0, 0, 0))
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '*':
                    pygame.draw.rect(screen, (255, 255, 255), Rect(j*40, i*40, 40, 40))
                elif board[i][j] == 'S':
                    pygame.draw.rect(screen, (0, 255, 0), Rect(j*40, i*40, 40, 40))
                elif board[i][j] == 'F':
                    pygame.draw.rect(screen, (255, 0, 0), Rect(j*40, i*40, 40, 40))
        pos = path.pop(0)
        pygame.draw.rect(screen, (0, 0, 255), Rect(pos[1]*40, pos[0]*40, 40, 40))
        pygame.display.update()
        pygame.time.delay(100)
    pygame.time.delay(1000)
    pygame.quit()

main()