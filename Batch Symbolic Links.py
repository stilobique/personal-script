import os

path_script = r"E:\WIP Git\Blender Addons"
path_blender_script = r"C:\Users\Aurélien\AppData\Roaming\Blender Foundation\Blender"
addons = r"\scripts\addons"
blender_version = []
all_script = []

for folder in os.listdir(path_script):
    # print(folder)
    all_script.append(folder)

for blender in os.listdir(path_blender_script):
    # print(blender)
    blender_version.append(blender)

for all_b3d_version in enumerate(blender_version):  
    i = +1
    folder_script = path_blender_script + "\\" + all_b3d_version[i] + addons

    for script in all_script:
        final_path = folder_script + "\\" + script + "\\"
        # print(final_path)

        if os.path.isdir(final_path):
            print("Path Deja Present >>", script)

        else:
            source = path_script + "\\" + script + "\\"
            target = folder_script + "\\" + script
            print("source >>", source)
            print("Target >>", target)
            os.symlink(source, target, 1)

