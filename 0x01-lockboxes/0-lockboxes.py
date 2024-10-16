#!/usr/bin/python3
"""
A method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Parameters:
    boxes (list of lists): Each inner list contains keys to other boxes.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    unlocked = [False] * len(boxes)
    unlocked[0] = True
    keys = set(boxes[0])

    while keys:
        new_keys = set()
        for key in keys:
            if key < len(boxes) and not unlocked[key]:
                unlocked[key] = True
                new_keys.update(boxes[key])
        keys = new_keys

    return all(unlocked)
