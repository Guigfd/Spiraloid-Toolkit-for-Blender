bl_info = {
        'name': 'SmoothVertWeights',
        'author': 'bay raitt',
        'version': (0, 1),
        'blender': (2, 7, 9),
        'category': 'View',
        'location': 'View > Smooth Vert Weights',
        'wiki_url': ''}

import bpy


def main(context):
    selected = bpy.context.selected_objects
    bpy.ops.object.vertex_group_smooth()
    bpy.data.meshes.selected.use_paint_mask_vertex               
                
class SmoothVertWeights(bpy.types.Operator):
    """toggle to vertext mode and smooth weights"""
    bl_idname = "view3d.smooth_vertex_weights"
    bl_label = "Smooth vertex weights"

    def execute(self, context):
        main(context)
        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(SmoothVertWeights.bl_idname)



def register():
    bpy.utils.register_class(SmoothVertWeights)
    bpy.types.weights_MT_vertex_group.prepend(menu_func)  

def unregister():
    bpy.utils.unregister_class(SmoothVertWeights)
    bpy.types.VIEW3D_MT_vertex_group.remove(menu_func)  

    if __name__ != "__main__":
        bpy.types.VIEW3D_MT_vertex_group.remove(menu_func)

if __name__ == "__main__":
    register()
