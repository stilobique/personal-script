import os
import subprocess
import git

path = os.path.dirname(__file__)
folders = []

print(path)

for ob in os.listdir(path):
    if os.path.isdir(ob):
        folders.append(ob)

# Process for all folder
i = 1

for i in range(len(folders)):
    print("Loop 1 : ", folders[i])
    # subprocess.Popen(['Git', 'Pull'], stdout=subprocess.PIPE)

    g = git.cmd.Git(folders[i])
    g.pull()
