import os

def relative_path(current_file, relative_path):
    return os.path.join(os.path.dirname(os.path.realpath(current_file)), relative_path)
