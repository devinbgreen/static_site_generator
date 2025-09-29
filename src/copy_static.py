import os
import shutil

def stage_static(source_dir, dest_dir):
    print(f"Copying contents from {source_dir} to {dest_dir}")
    # Assuming dest_dir is "public"
    full_dest_path = os.path.join(dest_dir)
                                
    if os.path.exists(full_dest_path):
        shutil.rmtree(full_dest_path)
    os.mkdir(full_dest_path)

    full_source_path = os.path.join(source_dir)
    _copy_recursive_helper(full_source_path, full_dest_path)
            

def _copy_recursive_helper(full_source_path, full_dest_path):
    print(f"Entering directory: {full_source_path}") # Good for debugging!

    contents = os.listdir(full_source_path)
    for item in contents:
        full_path_to_item = os.path.join(full_source_path, item)
        full_path_to_item_dest = os.path.join(full_dest_path, item)

        if os.path.isfile(full_path_to_item):
            print(f"copying {item} to {full_dest_path}")
            shutil.copy(full_path_to_item, full_path_to_item_dest)
        elif os.path.isdir(full_path_to_item):
            os.mkdir(full_path_to_item_dest)
            _copy_recursive_helper(full_path_to_item, full_path_to_item_dest)
        else:
            raise Exception("item is not file or directory???")
