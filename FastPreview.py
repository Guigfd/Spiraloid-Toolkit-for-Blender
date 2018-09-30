

import bpy
from mathutils import Vector

bl_info = {
    'name': 'Playback Preview',
        'author': 'Bay Raitt',
        'version': (0, 1),
        'blender': (2, 7, 9),
        'category': 'Animation',
        'location': 'Timeline  > Preview Toggle',
        'wiki_url': ''}

playing = "False"
brCurframe = 0
brStartRange = 1              
brEndRange = 72

class fastPreview(bpy.types.Operator):
    """play range and return to current frame on stop"""
    bl_idname   = "view3d.fast_preview"
    bl_label   = "Preview"
    bl_description = "start playback from the first frame"

    def execute(self, context):
        global playing
        if playing == "False":
            global brCurframe
                     
            brCurframe = bpy.context.scene.frame_current
            
            context = bpy.context
            c = context.copy()
            for i, area in enumerate(context.screen.areas):
                if area.type != 'GRAPH_EDITOR':
                    continue
                region = area.regions[-1]
                print("SCREEN:", context.screen.name , "[", i, "]")
                c["space_data"] = area.spaces.active
                c["area"] = area
                c["region"] = region            
                h = region.height # screen
                w = region.width  # 
                bl = region.view2d.region_to_view(0, 0)
                tr = region.view2d.region_to_view(w, h)

                bpy.context.scene.use_preview_range = True

                bpy.context.scene.frame_preview_start =  int(bl[0])
                bpy.context.scene.frame_preview_end =  int(tr[0])
                
                bpy.context.scene.frame_current = int(bl[0])
            
            
            #bpy.context.scene.frame_current = bpy.context.scene.frame_start            
            bpy.ops.screen.animation_play()
            playing = "True"   
        elif playing == "True":
            global brCurframe

            bpy.context.scene.frame_preview_start =  bpy.context.scene.frame_start
            bpy.context.scene.frame_preview_end =  bpy.context.scene.frame_end

            bpy.context.scene.use_preview_range = False

            
            bpy.ops.screen.animation_cancel(restore_frame=False)
            bpy.context.scene.frame_current = brCurframe
                                    
            playing = "False"  
            print ("woo")   
          
        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(fastPreview.bl_idname)

def register():
    bpy.utils.register_class(fastPreview)
    bpy.types.TIME_HT_header.prepend(menu_func)

def unregister():
    bpy.utils.unregister_class(fastPreview)
    bpy.types.TIME_HT_header.remove(menu_func)

    if __name__ != "__main__":
        bpy.types.TIME_HT_header.remove(menu_func)
                
if __name__ == "__main__":
    register()


            
