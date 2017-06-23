import os
import perforce
import tkinter

# -----------------------------
# Generate all data needs to know enviroment we want build, the stadium
# name, suffix name and -by deduction the path
# -----------------------------
lvl_root = '//ProVolley/UnrealProjects/ProVolley/Content/Scenes/'
lvl_suffix = [
    # Gymnasium
    'GYM01',
    'GYM02',
    # Stadium
    'STA01',
    'STA02',
    'STA03',
    'STA04',
    'STA05',
    'STA06',
    'STA07',
    'STA08',
    'STA09',
    # # Training Courts
    # 'TC01',
    # 'TC02'
]
lvl_folder = [
    # Gymnasium
    'SanJuanTheater',
    'MittelbrunnZentrum',
    # Stadium
    'UmmDharbStadium',
    'ManzoVBArena',
    'BanKhaemSporthall',
    'HosojimiCenter',
    'CharlesFrabetStadium',
    'JalbarosCenterArena',
    'CuapixcoEsteColegio',
    'AbramCenterStadium',
    'PretovkaClubStadion',
    # Training Courts
    # 'RoyalStratfordGymnasium',
    # 'MartinSherpardHall'
]


# -----------------------------
# Connect to perfoce to check all map (and lvl ussat), check if i can't move
#  or move to next
# -----------------------------
p4 = perforce.connect()
for i in range(len(lvl_suffix)):
    lvl_name = lvl_suffix[i]
    lvl_end = lvl_folder[i]
    map = lvl_root + lvl_name + '_' + lvl_end + '/' + lvl_name + '.umap'

    i = +1
    # revision = p4.ls(map)
    print(map)

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


# path_ue4 = r"E:\WORKS\Perforce\EpicGames\UE4-QA\Engine\Binaries\Win64\UE4Editor.exe"
# path_project = r"E:\WORKS\Perforce\ProVolley\UnrealProjects\ProVolley\ProVolley.uproject"
#
# path_ue4 path_project -run=resavepackages -buildlighting \
#                            -AllowCommandletRendering -AutoCheckOutPackages \
#                            -FILE=STA02.umap



# "f:\Jenkins\EpicGames\UE4-QA\Engine\Binaries\Win64\UE4Editor.exe"
# "f:\Jenkins\ProVolley\UnrealProjects\ProVolley\ProVolley.uproject"
# -run=resavepackages -buildtexturestreaming -buildlighting
# -AllowCommandletRendering -AutoCheckOutPackages -AutoCheckIn
# -FILE="f:\Jenkins\ProVolley\UnrealProjects\ProVolley\RebuildLigthMaps.txt"