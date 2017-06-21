import urllib
import shutil

b3d_url = r"https://builder.blender.org/download/"
b3d_file = blender-2.80-0ef7ccb-win64.zip

with urllib.request.urlopen(b3d_url) as reponse, open(b3d_file, 'wb') as \
        out_file:
    data = reponse.read()
    out_file.write(data)