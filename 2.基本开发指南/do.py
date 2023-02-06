import os, sys


old_names = os.listdir(r'./')
for old_name in old_names:
    if old_name != sys.argv[0]:
        os.rename(old_name, old_name[2:])
