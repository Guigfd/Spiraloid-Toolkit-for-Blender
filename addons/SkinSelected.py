bl_info = {
        'name': 'SkinSelected',
        'author': 'bay raitt',
        'version': (0, 1),
        'blender': (2, 7, 9),
        'category': 'View',
        'location': 'View > Smooth Vert Weights',
        'wiki_url': ''}

import bpy


def main(context):
    bpy.ops.object.mode_set(mode='OBJECT')
    selected = bpy.context.selected_objects
    bpy.ops.paint.weight_from_bones(type='AUTOMATIC')
    bpy.ops.wm.voxel_heat_diffuse()

class SkinSelected(bpy.types.Operator):
    """toggle to vertext mode and smooth weights"""
    bl_idname = "view3d.skin_selected"
    bl_label = "Skin Selected"

    def execute(self, context):
        main(context)
        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(SmoothVertWeights.bl_idname)



def register():
    bpy.utils.register_class(SkinSelected)
    bpy.types.VIEW3D_MT_view.prepend(menu_func)  

def unregister():
    bpy.utils.unregister_class(SkinSelected)
    bpy.types.VIEW3D_MT_view.remove(menu_func)  

    if __name__ != "__main__":
        bpy.types.VIEW3D_MT_view.remove(menu_func)

if __name__ == "__main__":
    register()
