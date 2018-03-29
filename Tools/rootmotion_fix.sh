#!/usr/bin/env bash

BLENDER_PATH="/private/var/ninja/Applications/blender-2.79-macOS-10.6/blender.app/Contents/MacOS/blender"
# BLENDER_SCENE="`pwd`/Arts/Model/adam.blend"
# EXPORT_PATH=$1
# SRC_PATH="/private/var/ninja/Documents/Projects/Psycho/Sounds/Adam/Story/Adam_DoctorRoom_1.dat"


SRC_PATH=$1
# SRC_PATH="/private/var/ninja/Documents/Projects/Psycho/Arts/Animations/Amy/Disarmed.fbx"
DIR=$(dirname "$SRC_PATH")
# echo $SRC_PATH

FILE_NAME=`basename $SRC_PATH`
EXTENSION="${FILE_NAME##*.}"

echo $EXTENSION
if [ $EXTENSION = "fbx" ] ; then
	mkdir -p $DIR/RootMotion
	EXPORT_PATH=$HOME/Desktop/root/${FILE_NAME%.*}_root.fbx
	EXPORT_PATH="$DIR/RootMotion/${FILE_NAME%.*}_root.fbx"
	SUFFIX="_root"

	if [ -e "$SRC_PATH" ]; then
		if [ "${FILE_NAME/$SUFFIX}" = "$FILE_NAME" ] ; then
			$BLENDER_PATH --background --python "Tools/rootmotion_fix.py" $SRC_PATH $EXPORT_PATH
		fi
	fi
fi

# if [ $EXTENSION = "dat" ] ; then
# 	ADAM_FOLDER="/Adam/"

# 	if [ ! "${SRC_PATH/$ADAM_FOLDER}" = "$SRC_PATH" ] ; then
# 		echo "Adam folder"
# 		BLENDER_SCENE="`pwd`/Arts/Model/adam.blend"
# 	fi

# 	Doctor_FOLDER="/Doctor/"
# 	if [ ! "${SRC_PATH/$Doctor_FOLDER}" = "$SRC_PATH" ] ; then
# 		BLENDER_SCENE="`pwd`/Arts/Model/doctor.blend"
# 		echo "Doctor folder"
# 	fi

# 	EXPORT_PATH="${SRC_PATH%.*}.fbx"
# 	echo $SRC_PATH
# 	if [ -e "$SRC_PATH" ]
# 		then
# 		$BLENDER_PATH $BLENDER_SCENE --background --python "Tools/lipsync.py" $SRC_PATH $EXPORT_PATH
# 	fi
# fi
# EXPORT_PATH="${SRC_PATH%.*}.fbx"
