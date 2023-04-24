def canUnlockAll(boxes):
    num_boxes = len(boxes)
    keys = set(boxes[0])
    unlocked = {0}
    while len(keys) > 0:
        box_num = keys.pop()
        if box_num not in unlocked:
            unlocked.add(box_num)
            keys.update(boxes[box_num])
    return len(unlocked) == num_boxes

