import os


def rename(names):
    for n in names:
        old_name = n
        new_name = names[n]
        try:
            os.rename(old_name, new_name)
            print('renamed from ' + old_name + ' to ' + new_name)
        except FileNotFoundError:
            print("file is not found " + old_name)