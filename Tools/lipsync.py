# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# TODO:
# * Relative path to lipsync file
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "LipSync Importer & Blinker",
    "author": "Yousef Harfoush - bat3a ;) / Konstantin Dmitriev / fixed for 2.76x by Looch", 
    "version": (0, 5, 3),
    "blender": (2, 70, 0),
    "location": "3D window > Tool Shelf",
    "description": "Plot Moho (Papagayo, Jlipsync, Yolo) file to frames and adds automatic blinking. Modified by Konstantin Dmitriev for Morevna Project to support Pose Libraries and CG Cookie Flex Rig",
    "warning": "",
    "wiki_url": "http://wiki.blender.org/index.php?title=Extensions:2.6/Py/"
        "Scripts/Import-Export/Lipsync Importer",
    "tracker_url": "https://developer.blender.org/T24080",
    "category": "Import-Export"}

import sys
import os
import bpy, re
from random import random
from bpy.props import *
from bpy.props import IntProperty, FloatProperty, StringProperty
# from bpy.types import EnumProperty
global lastPhoneme
lastPhoneme="nothing"

global blinker
global blinkerFlexRig
global lipsyncerFlexRig
global addFlexRigKey
global lipsyncerBone
global resetBoneScale
global addBoneKey
global createBoneKeys
global lipsyncer
global createShapekey
global lipsync_batch

global fpath
global scn_offset
global scn_easeIn
global scn_easeOut
global scn_holdGap
global skscale
global enumFileTypes
global enumModeTypes
global enumBlinkTypes
# add blinking
def blinker(obj):

    # scn = bpy.context.scene
    # obj = bpy.context.object

    if enumBlinkTypes == '0':
        modifier = 0
    elif enumBlinkTypes == '1':
        modifier = scn.blinkMod

    #creating keys with blinkNm count
    for y in range(scn.blinkNm):
        frame = y * scn.blinkSp + int(random()*modifier)
        createShapekey('blink', frame)
        
# ----------- cg cookie flexrig support-------------------

lastPhonemeIdx = -100

def blinkerFlexRig(obj):
    
    scn = bpy.context.scene
    # obj = bpy.context.object
    
    # saving current scene state
    state_record = scn.tool_settings.use_keyframe_insert_auto
    state_frame = scn.frame_current
    state_poselib = obj.pose_library

    if enumBlinkTypes == '0':
        modifier = 0
    elif enumBlinkTypes == '1':
        modifier = scn.blinkMod
    
    
    # activate pose library
    obj.pose_library = bpy.data.actions[scn.eyesLib]
    scn.tool_settings.use_keyframe_insert_auto = True
    
    # find which bones should be affected by pose library
    bones_list=[]
    for bone in bpy.data.actions[scn.eyesLib].groups.keys():
        if len(bpy.data.actions[scn.eyesLib].groups[bone].channels)!=0:
            bones_list.append(bone)
    
    # select bones
    if len(bpy.context.selected_pose_bones) != 0:
        bpy.ops.pose.select_all()
    for bone_name in obj.data.bones.keys():
        if bone_name in bones_list:
            obj.data.bones[bone_name].select=True
        else:
            obj.data.bones[bone_name].select=False
    
    offst = scn_offset     # offset value
    frmIn = scn_easeIn     # ease in value
    frmOut = scn_easeOut   # ease out value
    hldIn = scn_holdGap    # holding time value
    
    
    
    #creating keys with blinkNm count
    for y in range(scn.blinkNm):
        frame = y * scn.blinkSp + int(random()*modifier)
        #createShapekey('blink', frame)
        
        # inserting the In key only when phonem change or when blinking
        #if lastPhoneme!=phoneme or eval(enumModeTypes) == 1:
        #    addFlexRigKey(offst+frame-frmIn, phoneme)
        
        addFlexRigKey(offst+frame-frmIn, 'rest')
        addFlexRigKey(offst+frame, 'blink')
        addFlexRigKey(offst+frame+hldIn, 'blink')
        addFlexRigKey(offst+frame+hldIn+frmOut, 'rest')

    
    # restoring current scene state
    scn.tool_settings.use_keyframe_insert_auto = state_record
    scn.frame_current = state_frame
    obj.pose_library = state_poselib
        
def lipsyncerFlexRig(obj):
    # reading imported file & creating keys
    # obj = bpy.context.object
    scene = bpy.context.scene
    bone = bpy.context.active_pose_bone
    
    # saving current scene state
    state_record = scene.tool_settings.use_keyframe_insert_auto
    state_frame = scene.frame_current
    state_poselib = obj.pose_library
    
    
    offst = scene.offset     # offset value
    skVlu = scene.skscale    # shape key value
    
    #in case of Papagayo format
    if enumFileTypes == '0' :
        frmIn = scene.easeIn     # ease in value
        frmOut = scene.easeOut   # ease out value
        hldIn = scene.holdGap    # holding time value
        
    #in case of Jlipsync format or Yolo
    elif enumFileTypes == '1' :
        frmIn = 1
        frmOut = 1
        hldIn = 0
        
    # activate pose library
    obj.pose_library = bpy.data.actions[scene.phonemesLib]
    scene.tool_settings.use_keyframe_insert_auto = True
        
    # find which bones should be affected by pose library
    bones_list=[]
    for bone in bpy.data.actions[scene.phonemesLib].groups.keys():
        if len(bpy.data.actions[scene.phonemesLib].groups[bone].channels)!=0:
            bones_list.append(bone)
    
    # select bones
    if len(bpy.context.selected_pose_bones) != 0:
        bpy.ops.pose.select_all()
    for bone_name in obj.data.bones.keys():
        if bone_name in bones_list:
            obj.data.bones[bone_name].select=True
        else:
            obj.data.bones[bone_name].select=False
    
    
    f=open(bpy.path.abspath(scene.fpath)) # importing file
    f.readline() # reading the 1st line that we don"t need
    
    global lastPhonemeIdx
    global lastPhoneme
    lastPhoneme = []
    #lastPhoneme.append("rest")
    global prevFrame
    prevFrame = -100
    
    for line in f:
        # removing new lines
        lsta = re.split("\n+", line)

        # building a list of frames & shapes indexes
        lst = re.split(":? ", lsta[0])# making a list of a frame & number 
        frame = int(lst[0])
        phoneme = lst[1]
        
        print("%s --> %s" % (frame,lst[1]))
        
        pl = obj.pose_library
        
        # inserting the In key only when phonem change or when blinking
        #if lastPhoneme[-1]!=phoneme or eval(enumModeTypes) == 1:
        #    addFlexRigKey(offst+frame-frmIn, phoneme)
        
        # add rest position right before the first phoneme
        #if  len(lastPhoneme) == 0:
        #    addFlexRigKey(offst+frame-frmIn, "rest")
        
        if ( len(lastPhoneme)==0 or lastPhoneme[-1] == "rest" ) and frame-prevFrame > hldIn:
            if phoneme != "rest":
                addFlexRigKey(offst+frame-frmIn, "rest")
                print("adding extra keyframe for REST position")
        
        if frame-prevFrame>=frmOut or frame-prevFrame==0:
            
            if len(lastPhoneme)>=2 and frame-prevFrame==0 and lastPhoneme[-2]==phoneme:
                # avoid duplicating phonemes
                pass
            elif len(lastPhoneme)!=0 and lastPhoneme[-1] == "rest" and phoneme == "rest":
                # don't insert double rest phonemes
                pass
            else:
                addFlexRigKey(offst+frame, phoneme)
                addFlexRigKey(offst+frame+hldIn, phoneme)
                #addFlexRigKey(offst+frame+hldIn+frmOut, phoneme)
                
                lastPhoneme.append(phoneme)
                prevFrame=frame
        else:
            addFlexRigKey(offst+frame+1, phoneme)
            addFlexRigKey(offst+frame+1+hldIn, phoneme)
            lastPhoneme.append(phoneme)
            prevFrame=frame+1
                
            
    
    # restoring current scene state
    scene.tool_settings.use_keyframe_insert_auto = state_record
    scene.frame_current = state_frame
    obj.pose_library = state_poselib

                
def addFlexRigKey(frame=0, pose=""):
    
    global lastPhonemeIdx
    
    bpy.context.scene.frame_current=frame
    
    obj = bpy.context.object
    pl = obj.pose_library
    
    idx = pl.pose_markers.find(pose)
    rest_idx = pl.pose_markers.find("rest")
    
    
    
    if idx == -1:
        idx = pl.pose_markers.find("etc")
    
    if idx != -1:
        if (idx != lastPhonemeIdx) or (idx == rest_idx):
            print("Apply pose %s" % idx)
            bpy.ops.poselib.apply_pose(pose_index=idx)
            lastPhonemeIdx=idx
        
        else:
            print("skipping phoneme: pose already set")
    
    


# -----------code contributed by dalai felinto adds armature support modified by me-------------------

bone_keys = {
"AI":   ('location', 0),
"E":    ('location', 1),
"FV":   ('location', 2),
"L":    ('rotation_euler', 0),
"MBP":  ('rotation_euler', 1),
"O":    ('rotation_euler', 2),
"U":    ('scale', 0),
"WQ":   ('scale', 1),
"etc":  ('scale', 2),
"rest": ('ik_stretch', -1)
}

def lipsyncerBone(obj):
    # reading imported file & creating keys
    # object = bpy.context.object
    scene = bpy.context.scene
    bone = bpy.context.active_pose_bone

    resetBoneScale(bone)

    f=open(bpy.path.abspath(scene.fpath)) # importing file
    f.readline() # reading the 1st line that we don"t need

    for line in f:
        # removing new lines
        lsta = re.split("\n+", line)

        # building a list of frames & shapes indexes
        lst = re.split(":? ", lsta[0])# making a list of a frame & number
        frame = int(lst[0])

        for key,attribute in bone_keys.items():
            if lst[1] == key:
                createBoneKeys(key, bone, attribute, frame)

def resetBoneScale(bone):
    # set the attributes used by papagayo to 0.0
    for attribute,index in bone_keys.values():
        if index != -1:
            #bone.location[0] = 0.0
            exec("bone.%s[%d] = %f" % (attribute, index, 0.0))
        else:
            exec("bone.%s = %f" % (attribute, 0.0))

def addBoneKey(bone, data_path, index=-1, value=None, frame=0, group=""):
    # set a value and keyframe for the bone
    # it assumes the 'bone' variable was defined before
    # and it's the current selected bone
    frame=bpy.context.scene.frame_current
    if value != None:
        if index != -1:
            # bone.location[0] = 0.0
            exec("bone.%s[%d] = %f" % (data_path, index, value))
        else:
            exec("bone.%s = %f" % (data_path, value))

    # bone.keyframe_insert("location", 0, 10.0, "Lipsync")
    exec('bone.keyframe_insert("%s", %d, %f, "%s")' % (data_path, index, frame, group))

# creating keys with offset and eases for a phonem @ the Skframe
def createBoneKeys(phoneme, bone, attribute, frame):
    global lastPhoneme

    scene = bpy.context.scene
    object = bpy.context.object

    offst = scn_offset     # offset value
    skVlu = skscale    # shape key value

    #in case of Papagayo format
    if enumFileTypes == '0' :
        frmIn = scene.easeIn     # ease in value
        frmOut = scene.easeOut   # ease out value
        hldIn = scene.holdGap    # holding time value

    #in case of Jlipsync format or Yolo
    elif enumFileTypes == '1' :
        frmIn = 1
        frmOut = 1
        hldIn = 0

    # inserting the In key only when phonem change or when blinking
    if lastPhoneme!=phoneme or eval(enumModeTypes) == 1:
        addBoneKey(bone, attribute[0], attribute[1], 0.0, offst+frame-frmIn, "Lipsync")

    addBoneKey(bone, attribute[0], attribute[1], skVlu, offst+frame, "Lipsync")
    addBoneKey(bone, attribute[0], attribute[1], skVlu, offst+frame+hldIn, "Lipsync")
    addBoneKey(bone, attribute[0], attribute[1], 0.0, offst+frame+hldIn+frmOut, "Lipsync")

    lastPhoneme=phoneme

# -------------------------------------------------------------------------------

# reading imported file & creating keys
def lipsyncer(obj):
    print(obj.name)
    # obj = bpy.context.object
    scn = bpy.context.scene

    f=open(bpy.path.abspath(fpath)) # importing file
    f.readline() # reading the 1st line that we don"t need

    min_frame = 9999
    max_frame = -1

    for line in f:
        # removing new lines
        lsta = re.split("\n+", line)

        # building a list of frames & shapes indexes
        lst = re.split(":? ", lsta[0])# making a list of a frame & number
        frame = int(lst[0])
        if (frame < min_frame):
            min_frame = frame

        if (frame > max_frame):
            max_frame = frame
    
    global scn_offset
    scn_offset = -min_frame + scn_easeIn + 1;
    scn.frame_end = (max_frame - min_frame) + scn_easeIn + scn_easeOut
    bpy.context.scene.render.fps = 24
    print("min_frame: ", min_frame)
    print("max_frame: ", max_frame)
    print("offset: ", scn_offset)
    print("frame_end: ", scn.frame_end)

    f=open(bpy.path.abspath(fpath)) # importing file
    f.readline() # reading the 1st line that we don"t need
    for line in f:

        # removing new lines
        lsta = re.split("\n+", line)

        # building a list of frames & shapes indexes
        lst = re.split(":? ", lsta[0])# making a list of a frame & number
        frame = int(lst[0])

        for key in obj.data.shape_keys.key_blocks:
            if lst[1] == key.name:
                createShapekey(obj, key.name, frame)

# creating keys with offset and eases for a phonem @ the frame
def createShapekey(obj, phoneme, frame):

    global lastPhoneme

    scn = bpy.context.scene
    # obj = bpy.context.object
    objSK = obj.data.shape_keys

    offst = scn_offset     # offset value
    # print('offset: ', offst)
    # print('fps:', bpy.context.scene.render.fps)
    # skVlu = scn.skscale    # shape key value
    skVlu = skscale

    #in case of Papagayo format
    if enumFileTypes == '0' :
        frmIn = scn_easeIn     # ease in value
        frmOut = scn_easeOut   # ease out value
        hldIn = scn_holdGap    # holding time value

    #in case of Jlipsync format or Yolo
    elif enumFileTypes == '1' :
        frmIn = 1
        frmOut = 1
        hldIn = 0

    # inserting the In key only when phonem change or when blinking
    if lastPhoneme!=phoneme or eval(enumModeTypes) == 1:
        objSK.key_blocks[phoneme].value=0.0
        objSK.key_blocks[phoneme].keyframe_insert("value",
            -1, offst+frame-frmIn, "Lipsync")

    objSK.key_blocks[phoneme].value=skVlu
    objSK.key_blocks[phoneme].keyframe_insert("value",
        -1, offst+frame, "Lipsync")

    objSK.key_blocks[phoneme].value=skVlu
    objSK.key_blocks[phoneme].keyframe_insert("value",
        -1, offst+frame+hldIn, "Lipsync")

    objSK.key_blocks[phoneme].value=0.0
    objSK.key_blocks[phoneme].keyframe_insert("value",
    -1, offst+frame+hldIn+frmOut, "Lipsync")

    lastPhoneme = phoneme


def lipsync_batch():
    scn = bpy.context.scene
    # scn_offset = 20

    # fpath = "/var/ninja/Documents/Projects/Psycho/Sounds/Chapter1_data/Adam1.dat"
    # fpath = sys.argv[-2::][0]
    print("dat file: ", fpath)
    bpy.context.scene.unit_settings.system = 'METRIC'
    bpy.context.scene.unit_settings.scale_length = 1
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=True)
    bpy.ops.import_scene.fbx(filepath=sys.argv[-3::][2], axis_forward='-Z',
                              axis_up='Y', directory="",
                              filter_glob="*.fbx", ui_tab='MAIN',
                              use_manual_orientation=False, global_scale=1.0,
                              bake_space_transform=False,
                              use_custom_normals=True,
                              use_image_search=True,
                              use_alpha_decals=False, decal_offset=0.0,
                              use_anim=False, anim_offset=1.0,
                              use_custom_props=True,
                              use_custom_props_enum_as_string=True,
                              ignore_leaf_bones=False,
                              force_connect_children=False,
                              automatic_bone_orientation=True,
                              primary_bone_axis='Y',
                              secondary_bone_axis='X',
                              use_prepost_rot=True),
    for obj in scn.objects:
        if obj.type=="MESH":
            scn.objects.active = obj
            # print(bpy.context.active_object)
            # bpy.context.active_object.animation_data_clear()
            if obj.type=="MESH":
                if obj.data.shape_keys!=None:
                    if fpath!='': lipsyncer(obj)
                    else: print ("select a Moho file")
                else: print("No shape keys")

            elif obj.type=="ARMATURE":
                if enumBoneMethodTypes == '0':
                    if fpath!='': lipsyncerFlexRig(obj)
                    else: print ("select a Moho file")
                else:
                    if 1:#XXX add prop test
                        if fpath!='': lipsyncerBone(obj)
                        else: print ("select a Moho file")
                    else: print("Create Pose properties")
                    
            else: print ("Object is not a mesh ot bone")

    # output_file = "/var/ninja/Desktop/lipsync/test.fbx"
    # print(output_file)
    output_file = sys.argv[-3::][1]
    print("output file: ", output_file)

    bpy.ops.export_scene.fbx(filepath=output_file,
                             version='BIN7400',
                             use_selection=False,
                             apply_unit_scale=False,
                             add_leaf_bones=False,
                             axis_forward='-Z',
                             axis_up='Y',
                             mesh_smooth_type='FACE',
                             use_mesh_modifiers=False,
                             use_anim=True,
                             use_anim_action_all=True,
                             bake_anim=True,
                             bake_anim_use_all_bones=False,
                             bake_anim_use_nla_strips=False,
                             bake_anim_use_all_actions=False,
                             bake_anim_force_startend_keying=False
                             )
    return {'FINISHED'}


scn_easeIn = 2
scn_easeOut = 2
scn_holdGap = 0
scn_offset = 10
skscale = 0.8
enumBlinkTypes = '0'
enumModeTypes = '0'
enumFileTypes = '0'
scn = bpy.context.scene
fpath = sys.argv[-3::][0]
lipsync_batch()