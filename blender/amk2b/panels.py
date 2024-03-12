import bpy

class AMK2BPANEL_PT_INIT(bpy.types.Panel):
    bl_label = "AMK2B"
    bl_space_type = 'VIEW_3D'
    bl_category = 'AMK2B'
    bl_region_type = 'UI'

    def draw(self, context):
        print("ADS")
        layout = self.layout

        row = layout.row()
        row.label(text="Receive Kinect Data")
        row = layout.row()
        if not bpy.amk2b.kinect_data_receiving_started:
            row.operator("amk2b.kinect_data_receiving_operator", text="Start")
        else:
            row.operator("amk2b.kinect_data_receiving_operator", text="Stop")

        row = layout.row()
        row.label(text="Apply Kinect Data")
        row = layout.row()
        if not bpy.amk2b.kinect_data_applying_started:
            row.operator("amk2b.kinect_data_applying_operator", text="Start")
        else:
            row.operator("amk2b.kinect_data_applying_operator", text="Stop")

        row = layout.row()
        row.label(text="Recording")
        row = layout.row()
        if not bpy.amk2b.recording_pre_started:
            row.operator("amk2b.recording_operator", text="Start")
        else:
            if not bpy.amk2b.recording_started:
                row.operator(
                    "amk2b.recording_operator",
                    text="waiting..." + str(bpy.amk2b.recording_wait_time)
                )
            else:
                row.operator("amk2b.recording_operator", text="Stop")
