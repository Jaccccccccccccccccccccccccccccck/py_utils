import os
import shutil

def move_file_from_to(base_url,orig_file_path,new_file_path):
    orig_full_path = base_url + orig_file_path
    new_full_path = base_url + new_file_path

    new_file_location = os.path.dirname(os.path.realpath(new_full_path))
    if not os.path.exists(new_file_location):
        os.mkdir(new_file_location)
    try:
        shutil.move(orig_full_path, new_full_path)
    except Exception as e:
        raise e


def copy_path_from_to(origin_path, new_path):
    print('moving file from : ' + origin_path + ' to ' + new_path)
    if os.path.exists(origin_path):
        # if not os.path.exists(new_path):
        #     os.makedirs(new_path)
        try:
            shutil.copytree(origin_path, new_path)
        except Exception as e:
            print(e)
    else:
        print('path copy failed, file: ' + origin_path + ' is not exsit')
    pass

copy_path_from_to('/moveFrom','/moveTo')
