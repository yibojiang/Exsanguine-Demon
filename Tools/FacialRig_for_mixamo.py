import bpy

def facial_rig():
    mesh_name = ["Body", "Beards", 'Eyelashes', 'Moustaches', 'default']

    for name in mesh_name:
        if name in bpy.data.objects:
            for block_key, block_val in bpy.data.objects[name].data.shape_keys.key_blocks.items():
                bpy.data.objects[name].data.shape_keys.key_blocks[block_key].value = 0
            # etc
            if 'Smile_Right' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["Smile_Right"].value = 0.3
            if 'Smile_Left' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["Smile_Left"].value = 0.3
            if 'UpperLipUp_Right' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["UpperLipUp_Right"].value = 0.4
            if 'UpperLipUp_Left' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["UpperLipUp_Left"].value = 0.4
            if 'LowerLipDown_Right' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["LowerLipDown_Right"].value = 0.8
            if 'LowerLipDown_Left' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["LowerLipDown_Left"].value = 0.8
            if 'MouthUp' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["MouthUp"].value = 0.1

            if (not 'etc' in bpy.data.objects[name].data.shape_keys.key_blocks):
                bpy.data.objects[name].shape_key_add(name='etc',from_mix=True)
            
            if 'Smile_Right' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["Smile_Right"].value = 0
            if 'Smile_Left' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["Smile_Left"].value = 0
            if 'UpperLipUp_Right' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["UpperLipUp_Right"].value = 0
            if 'UpperLipUp_Left' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["UpperLipUp_Left"].value = 0
            if 'LowerLipDown_Right' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["LowerLipDown_Right"].value = 0
            if 'LowerLipDown_Left' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["LowerLipDown_Left"].value = 0
            if 'MouthUp' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["MouthUp"].value = 0

            # U
            if 'LowerLipOut' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["LowerLipOut"].value = 1
            if 'UpperLipOut' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["UpperLipOut"].value = 1
            if 'MouthWhistle_NarrowAdjust_Right' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["MouthWhistle_NarrowAdjust_Right"].value = 1
            if 'MouthWhistle_NarrowAdjust_Left' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["MouthWhistle_NarrowAdjust_Left"].value = 1
            if 'Midmouth_Left' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["Midmouth_Left"].value = 0.4
            if 'Midmouth_Right' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["Midmouth_Right"].value = 0.4
            if 'MouthNarrow_Left' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["MouthNarrow_Left"].value = 0.6
            if 'MouthNarrow_Right' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["MouthNarrow_Right"].value = 0.6

            if (not 'U' in bpy.data.objects[name].data.shape_keys.key_blocks):
                bpy.data.objects[name].shape_key_add(name='U',from_mix=True)

            if 'LowerLipOut' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["LowerLipOut"].value = 0
            if 'UpperLipOut' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["UpperLipOut"].value = 0
            if 'MouthWhistle_NarrowAdjust_Right' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["MouthWhistle_NarrowAdjust_Right"].value = 0
            if 'MouthWhistle_NarrowAdjust_Left' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["MouthWhistle_NarrowAdjust_Left"].value = 0
            if 'Midmouth_Left' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["Midmouth_Left"].value = 0
            if 'Midmouth_Right' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["Midmouth_Right"].value = 0
            if 'MouthNarrow_Left' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["MouthNarrow_Left"].value = 0
            if 'MouthNarrow_Right' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["MouthNarrow_Right"].value = 0

            # MBP
            if 'Smile_Left' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["Smile_Left"].value = 0.4
            if 'Smile_Right' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["Smile_Right"].value = 0.4
            if 'Frown_Left' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["Frown_Left"].value = 0.5
            if 'Frown_Right' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["Frown_Right"].value = 0.5

            if (not 'MBP' in bpy.data.objects[name].data.shape_keys.key_blocks):
                bpy.data.objects[name].shape_key_add(name='MBP',from_mix=True)

            if 'Smile_Left' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["Smile_Left"].value = 0
            if 'Smile_Right' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["Smile_Right"].value = 0
            if 'Frown_Left' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["Frown_Left"].value = 0
            if 'Frown_Right' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["Frown_Right"].value = 0

            # O
            if 'LowerLipOut' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["LowerLipOut"].value = 0.4
            if 'UpperLipOut' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["UpperLipOut"].value = 0.4
            if 'MouthWhistle_NarrowAdjust_Right' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["MouthWhistle_NarrowAdjust_Right"].value = 0.5
            if 'MouthWhistle_NarrowAdjust_Left' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["MouthWhistle_NarrowAdjust_Left"].value = 0.4
            if 'MouthOpen' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["MouthOpen"].value = 0.4
            if 'Midmouth_Left' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["Midmouth_Left"].value = 0.5
            if 'Midmouth_Right' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["Midmouth_Right"].value = 0.5

            if (not 'O' in bpy.data.objects[name].data.shape_keys.key_blocks):
                bpy.data.objects[name].shape_key_add(name='O',from_mix=True)

            if 'LowerLipOut' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["LowerLipOut"].value = 0
            if 'UpperLipOut' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["UpperLipOut"].value = 0
            if 'MouthWhistle_NarrowAdjust_Right' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["MouthWhistle_NarrowAdjust_Right"].value = 0
            if 'MouthWhistle_NarrowAdjust_Left' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["MouthWhistle_NarrowAdjust_Left"].value = 0
            if 'MouthOpen' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["MouthOpen"].value = 0
            if 'Midmouth_Left' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["Midmouth_Left"].value = 0
            if 'Midmouth_Right' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["Midmouth_Right"].value = 0

            # AI
            if 'Smile_Left' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["Smile_Left"].value = 0.3
            if 'Smile_Right' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["Smile_Right"].value = 0.3
            if 'MouthOpen' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["MouthOpen"].value = 0.5
            if 'MouthUp' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["MouthUp"].value = 0.2

            if 'AI' in bpy.data.objects[name].data.shape_keys.key_blocks:
            	bpy.data.objects[name].shape_key_remove(bpy.data.objects[name].data.shape_keys.key_blocks['AI'])

            if (not 'AI' in bpy.data.objects[name].data.shape_keys.key_blocks):
                bpy.data.objects[name].shape_key_add(name='AI',from_mix=True)

            if 'Smile_Left' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["Smile_Left"].value = 0
            if 'Smile_Right' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["Smile_Right"].value = 0
            if 'MouthOpen' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["MouthOpen"].value = 0
            if 'MouthUp' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["MouthUp"].value = 0

            # E
            if 'Smile_Left' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["Smile_Left"].value = 0.1
            if 'Smile_Right' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["Smile_Right"].value = 0.1
            if 'UpperLipUp_Right' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["UpperLipUp_Right"].value = 0.3
            if 'UpperLipUp_Left' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["UpperLipUp_Left"].value = 0.3
            if 'LowerLipDown_Right' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["LowerLipDown_Right"].value = 1
            if 'LowerLipDown_Left' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["LowerLipDown_Left"].value = 1
            if 'MouthUp' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["MouthUp"].value = 0.2
            
            if (not 'E' in bpy.data.objects[name].data.shape_keys.key_blocks):
                bpy.data.objects[name].shape_key_add(name='E',from_mix=True)

            if 'Smile_Left' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["Smile_Left"].value = 0
            if 'Smile_Right' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["Smile_Right"].value = 0
            if 'UpperLipUp_Right' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["UpperLipUp_Right"].value = 0
            if 'UpperLipUp_Left' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["UpperLipUp_Left"].value = 0
            if 'LowerLipDown_Right' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["LowerLipDown_Right"].value = 0
            if 'LowerLipDown_Left' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["LowerLipDown_Left"].value = 0
            if 'MouthUp' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["MouthUp"].value = 0

            # WQ
            if 'MouthNarrow_Left' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["MouthNarrow_Left"].value = 1
            if 'MouthNarrow_Right' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["MouthNarrow_Right"].value = 1
            if 'LowerLipOut' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["LowerLipOut"].value = 1
            if 'UpperLipOut' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["UpperLipOut"].value = 1
            if 'MouthWhistle_NarrowAdjust_Right' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["MouthWhistle_NarrowAdjust_Right"].value = 1
            if 'MouthWhistle_NarrowAdjust_Left' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["MouthWhistle_NarrowAdjust_Left"].value = 1
            if 'Midmouth_Left' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["Midmouth_Left"].value = 0.1
            if 'Midmouth_Right' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["Midmouth_Right"].value = 0.1

            if 'WQ' in bpy.data.objects[name].data.shape_keys.key_blocks:
            	bpy.data.objects[name].shape_key_remove(bpy.data.objects[name].data.shape_keys.key_blocks['WQ'])

            if (not 'WQ' in bpy.data.objects[name].data.shape_keys.key_blocks):
                bpy.data.objects[name].shape_key_add(name='WQ',from_mix=True)

            if 'MouthNarrow_Left' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["MouthNarrow_Left"].value = 0
            if 'MouthNarrow_Right' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["MouthNarrow_Right"].value = 0
            if 'LowerLipOut' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["LowerLipOut"].value = 0
            if 'UpperLipOut' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["UpperLipOut"].value = 0
            if 'MouthWhistle_NarrowAdjust_Right' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["MouthWhistle_NarrowAdjust_Right"].value = 0
            if 'MouthWhistle_NarrowAdjust_Left' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["MouthWhistle_NarrowAdjust_Left"].value = 0
            if 'Midmouth_Left' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["Midmouth_Left"].value = 0
            if 'Midmouth_Right' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["Midmouth_Right"].value = 0

            # FV
            if 'Jaw_Up' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["Jaw_Up"].value = 1
            if 'LowerLipIn' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["LowerLipIn"].value = 1
            if 'MouthOpen' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["MouthOpen"].value = 0.3
            if 'JawBackward' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["JawBackward"].value = 0.2

            if 'FV' in bpy.data.objects[name].data.shape_keys.key_blocks:
            	bpy.data.objects[name].shape_key_remove(bpy.data.objects[name].data.shape_keys.key_blocks['FV'])

            if (not 'FV' in bpy.data.objects[name].data.shape_keys.key_blocks):
                bpy.data.objects[name].shape_key_add(name='FV',from_mix=True)

            if 'Jaw_Up' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["Jaw_Up"].value = 0
            if 'LowerLipIn' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["LowerLipIn"].value = 0
            if 'MouthOpen' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["MouthOpen"].value = 0
            if 'JawBackward' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["JawBackward"].value = 0

            # L
            if 'Smile_Left' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["Smile_Left"].value = 0.4
            if 'Smile_Right' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["Smile_Right"].value = 0.4
            if 'MouthNarrow_Left' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["MouthNarrow_Left"].value = 0.5
            if 'MouthNarrow_Right' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["MouthNarrow_Right"].value = 0.5
            if 'MouthOpen' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["MouthOpen"].value = 0.4
            if 'MouthUp' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["MouthUp"].value = 0.4
            if 'TongueUp' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["TongueUp"].value = 0.6
            if 'L' in bpy.data.objects[name].data.shape_keys.key_blocks:
            	bpy.data.objects[name].shape_key_remove(bpy.data.objects[name].data.shape_keys.key_blocks['L'])

            if (not 'L' in bpy.data.objects[name].data.shape_keys.key_blocks):
                bpy.data.objects[name].shape_key_add(name='L',from_mix=True)

            if 'Smile_Left' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["Smile_Left"].value = 0
            if 'Smile_Right' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["Smile_Right"].value = 0
            if 'MouthNarrow_Left' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["MouthNarrow_Left"].value = 0
            if 'MouthNarrow_Right' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["MouthNarrow_Right"].value = 0
            if 'MouthOpen' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["MouthOpen"].value = 0
            if 'MouthUp' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["MouthUp"].value = 0
            if 'TongueUp' in bpy.data.objects[name].data.shape_keys.key_blocks: 
                bpy.data.objects[name].data.shape_keys.key_blocks["TongueUp"].value = 0
            
            if (not 'rest' in bpy.data.objects[name].data.shape_keys.key_blocks):
                bpy.data.objects[name].shape_key_add(name='rest',from_mix=True)

facial_rig()