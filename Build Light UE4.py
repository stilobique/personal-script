import os
import subprocess
import perforce
import tkinter

# -----------------------------
# Generate all data needs to know enviroment we want build, the stadium
# name, suffix name and -by deduction the path
# -----------------------------
lvl_root = '//ProVolley/UnrealProjects/ProVolley/Content/Scenes/'
lvl_path = "e:/WORKS/Perforce/ProVolley/UnrealProjects/ProVolley/Content" \
           "/Scenes/"

lvl_suffix = [
    # Gymnasium
    'GYM01',
    'GYM02',
    # Stadium
    # 'STA01',
    # 'STA02',
    # 'STA03',
    # 'STA04',
    # 'STA05',
    # 'STA06',
    # 'STA07',
    # 'STA08',
    # 'STA09',
    # # Training Courts
    # 'TC01',
    # 'TC02'
]
lvl_folder = [
    # Gymnasium
    'SanJuanTheater',
    'MittelbrunnZentrum',
    # Stadium
    # 'UmmDharbStadium',
    # 'ManzoVBArena',
    # 'BanKhaemSporthall',
    # 'HosojimiCenter',
    # 'CharlesFrabetStadium',
    # 'JalbarosCenterArena',
    # 'CuapixcoEsteColegio',
    # 'AbramCenterStadium',
    # 'PretovkaClubStadion',
    # Training Courts
    # 'RoyalStratfordGymnasium',
    # 'MartinSherpardHall'
]

revisions = []

path_ue4 = r"E:\WORKS\Perforce\EpicGames\UE4-QA\Engine\Binaries\Win64\UE4Editor.exe"
path_project = r"E:\WORKS\Perforce\ProVolley\UnrealProjects\ProVolley\ProVolley.uproject"


# -----------------------------
# Connect to perfoce to check all map (and lvl ussat)
# -----------------------------
p4 = perforce.connect()


for i in range(len(lvl_suffix)):
    lvl_name = lvl_suffix[i]
    lvl_end = lvl_folder[i]
    map = lvl_path + lvl_name + '_' + lvl_end + '/'
    depot = lvl_root + lvl_name + '_' + lvl_end + '/'

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
# UI Tkinter
# -----------------------------
# fenetre = tkinter.Tk()
#
# for lvl_name in levels:
#     suffix = lvl_name
#     name = 'button_' + lvl_name
#     name = tkinter.Checkbutton(fenetre, text=lvl_name)
#     name.pack()
#
#
# fenetre.mainloop()

# -----------------------------
# Build level
# -----------------------------
for i in range(len(lvl_suffix)):
    print('Build Level > ', lvl_suffix[i])
    level = '-map=' + lvl_suffix[i] + '.umap'
    subprocess.run([path_ue4,
                    path_project,
                    '-run=resavepackages',
                    '-buildlighting',
                    '-allowcommandletrendering',
                    level,
                    # '-mapstorebuildlightmaps=GYM01.umap',
                    # '-AutomatedMapBuild',
                    ])
