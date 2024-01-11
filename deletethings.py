import os

def prune(path, pattern):
    if os.path.isfile(path) and path.endswith(pattern):
        print("- Removed :", path)
        os.remove(path)
    if os.path.isdir(path):
        for item in os.listdir(path):
            prune(os.path.join(path, item), pattern)
        
prune('./', ".Identifier")