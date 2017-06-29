import os
import json
# -----------------------------
# Generate all data needs to know enviroment we want build, the stadium
# name, suffix name and -by deduction the path
# -----------------------------
lvl_root = '//ProVolley/UnrealProjects/ProVolley/Content/Scenes/'
lvl_path = "e:/WORKS/Perforce/ProVolley/UnrealProjects/ProVolley/Content" \
           "/Scenes/"

levels_dict = {
    # Gymnasium
    1: ('GYM01', 'SanJuanTheater'),
    2: ('GYM02', 'MittelbrunnZentrum'),
    # Stadium
    3: ('STA01', 'UmmDharbStadium'),
    4: ('STA02', 'ManzoVBArena'),
    5: ('STA03', 'BanKhaemSporthall'),
    6: ('STA04', 'HosojimiCenter'),
    7: ('STA05', 'CharlesFrabetStadium'),
    8: ('STA06', 'JalbarosCenterArena'),
    9: ('STA07', 'CuapixcoEsteColegio'),
    10: ('STA08', 'AbramCenterStadium'),
    11: ('STA09', 'PretovkaClubStadion'),
    # Training Courts
    12: ('TC01', 'RoyalStratfordGymnasium'),
    13: ('TC02', 'MartinSherpardHall'),
}

levels_rendering = []

revisions = []

if os.path.isfile("Models/setup.json"):
    with open('Models/setup.json') as f:
        paths_dict = json.load(f)

else:
    paths_dict = {
        "UE4 Editor": "UE4Editor.exe",
        "UE4 Project": "Project.uproject",
    }
path_ue4 = r"E:\WORKS\Perforce\EpicGames\UE4-QA\Engine\Binaries\Win64\UE4Editor.exe"
path_project = r"E:\WORKS\Perforce\ProVolley\UnrealProjects\ProVolley\ProVolley.uproject"