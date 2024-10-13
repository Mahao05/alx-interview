#!/usr/bin/python3
def canUnlockAll(boxes):
    unlocked = [False] * len(boxes)
    unlocked[0] = True  # The first box is unlocked
    stack = [0]  # Start with the first box

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key < len(boxes) and not unlocked[key]:
                unlocked[key] = True
                stack.append(key)

    return all(unlocked)
