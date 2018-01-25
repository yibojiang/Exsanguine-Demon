#!/usr/bin/env bash

BLENDER_PATH="/private/var/ninja/Applications/blender-2.79-macOS-10.6/blender.app/Contents/MacOS/blender"
# BLENDER_SCENE="`pwd`/Arts/Model/adam.blend"
# EXPORT_PATH=$1
# SRC_PATH="/private/var/ninja/Documents/Projects/Psycho/Sounds/Adam/Story/Adam_DoctorRoom_1.dat"


SRC_PATH=$1

# echo $SRC_PATH

ADAM_FOLDER="/Adam/"
if [ ! "${SRC_PATH/$ADAM_FOLDER}" = "$SRC_PATH" ] ; then
echo "Adam folder"
BLENDER_SCENE="`pwd`/Arts/Model/adam.blend"
fi

Doctor_FOLDER="/Doctor/"
if [ ! "${SRC_PATH/$Doctor_FOLDER}" = "$SRC_PATH" ] ; then
BLENDER_SCENE="`pwd`/Arts/Model/doctor.blend"
echo "Doctor folder"
fi

EXPORT_PATH="${SRC_PATH%.*}.fbx"
echo $SRC_PATH
if [ -e "$SRC_PATH" ]
	then
	$BLENDER_PATH $BLENDER_SCENE --background --python "Tools/lipsync.py" $SRC_PATH $EXPORT_PATH
fi