#!/usr/bin/python3
""" Lockboxes """


def canUnlockAll(boxes):
    """ Method that determines if all the boxes can be opened. """
    no_of_boxes = len(boxes)  # Number of boxes
    unlocked_boxes = [False] * no_of_boxes  # List of unlocked boxes
    unlocked_boxes[0] = True  # First box is unlocked by default
    keys = boxes[0]  # First box keys

    for key in keys:
        if key < no_of_boxes and not unlocked_boxes[key]:
            unlocked_boxes[key] = True
            keys.extend(boxes[key])

    return all(unlocked_boxes)
