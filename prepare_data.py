import os
import shutil

source_folder = 'ori_data'
target_folder = 'mydata'
file_names = os.listdir(source_folder)

cnt = 1
for file in file_names:
    pre_file = file[ : -3]
    if file[-1] == 'g':
        if cnt <= 1500:
            target_path_image = os.path.join(target_folder, 'images', 'train')
            target_path_label = os.path.join(target_folder, 'labels', 'train')
        else:
            target_path_image = os.path.join(target_folder, 'images', 'val')
            target_path_label = os.path.join(target_folder, 'labels', 'val')
        cnt += 1

        source_path_image = os.path.join(source_folder, pre_file) + 'jpg'
        source_path_label = os.path.join(source_folder, pre_file) + 'txt'

        shutil.copy(source_path_image, target_path_image)
        shutil.copy(source_path_label, target_path_label)
    else:
        continue