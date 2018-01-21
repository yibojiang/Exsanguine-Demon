#!/usr/bin/env bash


BLENDER_PATH="/private/var/ninja/Applications/blender-2.79-macOS-10.6/blender.app/Contents/MacOS/blender"
BLENDER_SCENE="../Arts/Model/adam.blend"
# EXPORT_PATH=$1
# SRC_PATH="/private/var/ninja/Documents/Projects/Psycho/Sounds/Adam/Story/Adam_DoctorRoom_1.dat"
SRC_PATH=$1
# EXPORT_PATH="/private/var/ninja/Documents/Projects/Psycho/Arts/Lipsync/fff.fbx"
EXPORT_PATH="${SRC_PATH%.*}.fbx"
echo $SRC_PATH
if [ -e "$SRC_PATH" ]
	then
	$BLENDER_PATH $BLENDER_SCENE --background --python lipsync.py $SRC_PATH $EXPORT_PATH
fi