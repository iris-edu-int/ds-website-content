import os

for dirpath, dirnames, filenames in os.walk('.'):
    for f in filenames:
        if f.endswith('.textile') and not f.startswith('index'):
            updatedpath = os.path.join(dirpath, os.path.splitext(f)[0])
            os.makedirs(updatedpath, exist_ok=True)
            os.rename(
                os.path.join(dirpath, f),
                os.path.join(updatedpath, 'index.textile')
            )
