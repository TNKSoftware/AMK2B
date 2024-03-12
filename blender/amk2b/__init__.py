from .common import ComObject
from .operators import KinectDataApplyingOperator
from .operators import KinectDataReceivingOperator
from .operators import RecordingOperator
from . import panels

import bpy

bl_info = {
    "name": "AMK2B - Kinect Data Receiver",
    "description": "for KinectDataSender.",
    "author": "asahiufo@AM902",
    'category': 'Animation',
    "location": "View 3D > Tool Shelf > AMK2B",
    "version": (1, 0, 0, 0),
    "blender": (2, 80, 0),
}

first_startup = "bpy" not in locals()

def register():
    print("REG")
    if first_startup:
        pass


    bpy.amk2b = ComObject()
    bpy.amk2b.kinect_data_receiving_started = False
    bpy.amk2b.kinect_data_applying_started = False
    bpy.amk2b.recording_pre_started = False
    bpy.amk2b.recording_started = False

    bpy.utils.register_class(panels.AMK2BPANEL_PT_INIT)
    bpy.utils.register_class(KinectDataReceivingOperator)
    bpy.utils.register_class(KinectDataApplyingOperator)
    bpy.utils.register_class(RecordingOperator)


def unregister():
    bpy.utils.unregister_class(RecordingOperator)
    bpy.utils.unregister_class(KinectDataApplyingOperator)
    bpy.utils.unregister_class(KinectDataReceivingOperator)
    bpy.utils.unregister_class(panels.AMK2BPANEL_PT_INIT)
    del bpy.amk2b


if __name__ == '__main__':
    register()