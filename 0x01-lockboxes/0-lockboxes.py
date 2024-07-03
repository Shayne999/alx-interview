#!/usr/bin/python3
""" A module for working with lockboxes. """


def canUnlockAll(boxes):
    """Checks if all the boxes in a list of boxes can be unlocked."""
    n = len(boxes)
    if n == 0:
        return True
    
    # this set keeps track of visited boxes starting with the first box
    visited = set()
    visited.add(0)
    
    #  Queue for Breadth First Search(BFS algorithim) starting with the keys from the first box
    queue = [0]
    
    while queue:
        current_box = queue.pop(0)
        
        for key in boxes[current_box]:
            if key not in visited:
                visited.add(key)
                queue.append(key)
    
    return len(visited) == n
