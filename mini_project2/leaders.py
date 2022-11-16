#!/usr/bin/python3

import json

with open('leaderboard.json', 'r') as board:
    sortedlist = []
    j_board = json.load(board)


print(j_board)
