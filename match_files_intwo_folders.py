import os
from pathlib import Path

# specify paths
root_folder = Path('sample')
src_folder = root_folder / 'images'
dest_folder = root_folder / 'labels'

# specify extensions to consider
src_extensions = ['jpg', 'jpeg', 'png']
dest_extensions = ['txt']


src_extensions = "|".join(src_extensions)
dest_extensions = "|".join(dest_extensions)
src_files = list(src_folder.rglob( "*[{}]".format(src_extensions)))


dest_files = list(dest_folder.rglob("*[{}]".format(dest_extensions)))
dest_dict = {i.name.split('.')[0]: i for i in dest_files}
src_dict = {i.name.split('.')[0]: i for i in src_files}
print(src_dict, dest_dict)

delete_arr = []
for file in dest_files:
    dest_fname = file.name.split('.')[0]
    if dest_fname not in src_dict.keys():
        delete_arr.append(dest_dict[dest_fname])

if len(delete_arr) >=1 : 
    print(f'Do you really want to delete the following files from {dest_folder}:')
    print([str(i) for i in delete_arr])

    ch = input('y/n to delete: \n')
    if ch == 'y' or ch == 'Y':
        for i in delete_arr:
            os.remove(i)
    print('files deleted')

else:
    print('nothing to delete')
        
    

    

