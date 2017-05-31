import os

path_ue4 = r"E:\WORKS\Perforce\EpicGames\UE4-QA\Engine\Binaries\Win64\UE4Editor.exe"
path_project = r"E:\WORKS\Perforce\ProVolley\UnrealProjects\ProVolley\ProVolley.uproject"

path_ue4 path_project -run=resavepackages -buildlighting \
                           -AllowCommandletRendering -AutoCheckOutPackages \
                           -FILE=STA02.umap



# "f:\Jenkins\EpicGames\UE4-QA\Engine\Binaries\Win64\UE4Editor.exe"
# "f:\Jenkins\ProVolley\UnrealProjects\ProVolley\ProVolley.uproject"
# -run=resavepackages -buildtexturestreaming -buildlighting
# -AllowCommandletRendering -AutoCheckOutPackages -AutoCheckIn
# -FILE="f:\Jenkins\ProVolley\UnrealProjects\ProVolley\RebuildLigthMaps.txt"