#!/usr/bin/env bash

# BLENDER_PATH="/private/var/ninja/Applications/blender-2.79-macOS-10.6/blender.app/Contents/MacOS/blender"

SRC_PATH=$1

DIR=$(dirname "$SRC_PATH")

FILE_NAME=`basename "$SRC_PATH"`
EXTENSION="${FILE_NAME##*.}"

if [ -e "$SRC_PATH" ]; then
	echo "$SRC_PATH modified or added" 
	if [ $EXTENSION = "fbx" ] ; then
		
		EXPORT_PATH="$DIR/RootMotion/${FILE_NAME%.*}_root.fbx"
		SUFFIX="_root"

		SCAN_FOLDER="/Animations/"
		
		if [ ! "${SRC_PATH/$SCAN_FOLDER}" = "$SRC_PATH" ] ; then
			echo "Animations asset."
			if [ "${FILE_NAME/$SUFFIX}" = "$FILE_NAME" ] ; then
				mkdir -p "$DIR/RootMotion"
				$BLENDER_PATH --background --python "Tools/rootmotion_fix.py" "$SRC_PATH" "$EXPORT_PATH"
			fi
		fi

		SCAN_FOLDER="/Model/"
		
		if [ ! "${SRC_PATH/$SCAN_FOLDER}" = "$SRC_PATH" ] ; then
			echo "Model asset."
			if [ "${FILE_NAME/$SUFFIX}" = "$FILE_NAME" ] ; then
				mkdir -p "$DIR/RootMotion"
				$BLENDER_PATH --background --python "Tools/rootmotion_fix.py" "$SRC_PATH" "$EXPORT_PATH"
			fi
		fi

	fi

	if [ $EXTENSION = "dat" ] ; then
		SCAN_FOLDER="/Sounds/Characters/"
		ADAM_FOLDER="/Adam/"

		if [ ! "${SRC_PATH/$SCAN_FOLDER}" = "$SRC_PATH" ] ; then
			echo "Lipsync asset."

			if [ ! "${SRC_PATH/$ADAM_FOLDER}" = "$SRC_PATH" ] ; then
				echo "Adam folder"
				# BLENDER_SCENE="`pwd`/Arts/Model/adam.blend"
				MODEL_PATH=`pwd`/Arts/Model/RootMotion/adam_nofoot_root.fbx
			fi

			Doctor_FOLDER="/Doctor/"
			if [ ! "${SRC_PATH/$Doctor_FOLDER}" = "$SRC_PATH" ] ; then
				# BLENDER_SCENE="`pwd`/Arts/Model/doctor.blend"
				MODEL_PATH=`pwd`/Arts/Model/RootMotion/doctor_root.fbx
				echo "Doctor folder"
			fi

			EXPORT_PATH="${SRC_PATH%.*}.fbx"
			$BLENDER_PATH --background --python "Tools/lipsync.py" "$SRC_PATH" "$EXPORT_PATH" "$MODEL_PATH"
		fi
	fi
else
	echo "$SRC_PATH removed" 
fi
# EXPORT_PATH="${SRC_PATH%.*}.fbx"
