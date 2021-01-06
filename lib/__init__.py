import os

def relative_path(current_file, relative_path):
    return os.path.join(os.path.dirname(os.path.realpath(current_file)), relative_path)

def collision_detected(l1, r1, l2, r2):
    if (l1.x > r2.x or l2.x > r1.x):
        return False

    if (l1.y > r2.y or l2.y > r1.y):
        return False

    return True
