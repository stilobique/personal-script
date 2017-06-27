# -----------------------------
# Generate all data needs to know enviroment we want build, the stadium
# name, suffix name and -by deduction the path
# -----------------------------
lvl_root = '//ProVolley/UnrealProjects/ProVolley/Content/Scenes/'
lvl_path = "e:/WORKS/Perforce/ProVolley/UnrealProjects/ProVolley/Content" \
           "/Scenes/"

levels_dict = {
    # Gymnasium
    1: ('GYM01', 'SanJuanTheater', 'False'),
    2: ('GYM02', 'MittelbrunnZentrum', 'False'),
    # Stadium
    3: ('STA01', 'UmmDharbStadium', 'False'),
    4: ('STA02', 'ManzoVBArena', 'False'),
    # 5: ('STA03', 'BanKhaemSporthall', 'False'),
    # 6: ('STA04', 'HosojimiCenter', 'False'),
    # 7: ('STA05', 'CharlesFrabetStadium', 'False'),
    # 8: ('STA06', 'JalbarosCenterArena', 'False'),
    # 9: ('STA07', 'CuapixcoEsteColegio', 'False'),
    # 10: ('STA08', 'AbramCenterStadium', 'False'),
    # 11: ('STA09', 'PretovkaClubStadion', 'False'),
    # Training Courts
    # 12: ('TC01', 'RoyalStratfordGymnasium', 'False'),
    # 13: ('TC02', 'MartinSherpardHall', 'False'),
}

levels_rendering = []

revisions = []

path_ue4 = r"E:\WORKS\Perforce\EpicGames\UE4-QA\Engine\Binaries\Win64\UE4Editor.exe"
path_project = r"E:\WORKS\Perforce\ProVolley\UnrealProjects\ProVolley\ProVolley.uproject"