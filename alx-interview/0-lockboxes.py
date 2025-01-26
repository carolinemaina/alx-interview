#!/usr/bin/python3
'''A module for working with lockboxes.
'''

def canUnlockAll(boxes):
    unlocked = {0}
    keys = [0]
    
    while keys:
        box = keys.pop()
        for key in boxes[box]:
            if key not in unlocked:
                unlocked.add(key)
                keys.append(key)

    return len(unlocked) == len(boxes)
