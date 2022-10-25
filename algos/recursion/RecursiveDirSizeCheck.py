'''
Logic:

if current directory has no child dir : return size and stop
else for all the directories size = size of files + all the directories in it

'''

import os


def finding_dir_size():
    parent_dir_path = '/Users/sg0220142/codebase/office/retail-iq'
    final_size = compute_size_recursively(parent_dir_path)
    print(f'....{final_size}')


def compute_size_recursively(folder_path):
    if not os.path.isdir(folder_path):
        path_size = os.path.getsize(folder_path)

    if os.path.isdir(folder_path):
        for file in os.listdir(folder_path):
            child_file_path = os.path.join(folder_path, file)
            path_size += compute_size_recursively(child_file_path)
    print(f'{folder_path}-{path_size}')
    return path_size


if __name__ == "__main__":
    finding_dir_size()
