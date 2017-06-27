import os
import subprocess
import perforce
from BatchLightUE4.Models.DB import levels_dict

# -----------------------------
# Generate all data needs to know enviroment we want build, the stadium
# name, suffix name and -by deduction the path
# -----------------------------
lvl_root = '//ProVolley/UnrealProjects/ProVolley/Content/Scenes/'
lvl_path = "e:/WORKS/Perforce/ProVolley/UnrealProjects/ProVolley/Content" \
           "/Scenes/"

revisions = []

path_ue4 = r"E:\WORKS\Perforce\EpicGames\UE4-QA\Engine\Binaries\Win64\UE4Editor.exe"
path_project = r"E:\WORKS\Perforce\ProVolley\UnrealProjects\ProVolley\ProVolley.uproject"


# -----------------------------
# Connect to perfoce to check all map (and lvl ussat)
# -----------------------------
def perforcecheckout():
    p4 = perforce.connect()

    for cle, value in levels_dict.items():
        lvl_name = value[0]
        lvl_end = value[1]
        map = lvl_path + lvl_name + '_' + lvl_end + '/'
        depot = lvl_root + lvl_name + '_' + lvl_end + '/'
        print('Checkout Level > ', map)

        for filename in os.listdir(os.path.normpath(map)):
            filename = depot + filename
            revisions.append(filename)

        description = """
        [ProVolley][GFX][LightmapAuto] Automatic Build Lightmap generate for the level
        """
        description = description + lvl_name
        cl = p4.findChangelist(description)
        for i in range(len(revisions)):
            file = revisions[i]
            p4.ls(file)
            cl.append(revisions[i])

        revisions.clear()

# -----------------------------
# Build level
# -----------------------------
def buildmap(levels_used):
    for i in levels_used:
        levels_dict.get(i)
        level = levels_dict[i]
        lvl_name = level[0]
        level = '-map=' + lvl_name + '.umap'
        print(level)
        subprocess.run([path_ue4,
                        path_project,
                        '-run=resavepackages',
                        '-buildlighting',
                        '-allowcommandletrendering',
                        level,
                        # '-mapstorebuildlightmaps=GYM01.umap',
                        # '-AutomatedMapBuild',
                        ])