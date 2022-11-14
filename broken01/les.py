#!/usr/bin/env python3


list1 = ["apple", 24, {1: "nba", 2: "nfl"}, 1.2 ]


for item in list1:
    try:
        plus1 = item + 1
        print(plus1)
    except TypeError as err:
        print(err, "error")



print(list1)

