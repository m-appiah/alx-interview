#!/usr/bin/python3


def canUnlockAll(boxes):
    """
    Function to determine if all boxes can be opened.

    Parameters:
    boxes (list of lists): Each list represents a box and
    contains keys to other boxes.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """

    # Initialize a set with the first box, which is already opened
    opened = set([0])

    # Get the keys from the first box
    keys = [key for key in boxes[0]]

    # While there are keys in the queue
    while keys:
        # Take a key from the queue
        key = keys.pop()

        # If the key corresponds to a box that hasn't been opened yet
        if key < len(boxes) and key not in opened:
            # Add the box to the set of opened boxes
            opened.add(key)

            # Add all its keys to the queue
            keys.extend(boxes[key])

    # Check if the number of opened boxes is equal to the total number of boxes
    return len(opened) == len(boxes)
    opened = set([0])
    keys = [key for key in boxes[0]]

    while keys:
        key = keys.pop()
        if key < len(boxes) and key not in opened:
            opened.add(key)
            keys.extend(boxes[key])

    return len(opened) == len(boxes)
