#!/usr/bin/python3
def canUnlockAll(boxes):
    n = len(boxes)

    opened = set([0])

    stack = [0]

    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if key < n and key not in opened:
                opened.add(key)
                stack.append(key)

    return len(opened) == n
