@echo off
REM Script to make the bpy build a python module.  Prior to running this, go in the blender folder and
REM enter "make bpy"
REM See https://wiki.blender.org/index.php/User:Ideasman42/BlenderAsPyModule

copy Release\bpy.pyd C:\Python35\Lib\site-packages
copy Release\*.dll C:\Python35\Lib\site-packages\
del C:\Python35\Lib\site-packages\python35.dll
xcopy /E/I Release\2.79 C:\Python35\2.79

pause