from ursina import *
import object as obj
import cam as cam

app = Ursina(borderless= False, show_ursina_splash = True, size = (1000,500))


enabled_debug_mode = False
# création du sol des axes de debug et des entity de control camera
Ground = Entity(model='plane', color= rgb(1, 150, 1), scale_z= 100, scale_x= 100, collider='mesh')
Debug_axes = Entity(model= 'axes', texture='axes')
# Construction_point = Entity(model='../model/construction_point', texture= '../texture/construction_point')


def destroy_entity():
    destroy(Pneu, delay= 1)

Pneu = Entity(model='pneu', texture= 'pneu', collider= 'mesh', on_click= destroy_entity)


b = Button(text='Quit', color=color.azure, scale=.0625, position= (.85,.45))
b.on_click = application.quit # assign a function to the button.
b.tooltip = Tooltip('exit')

#* fonction pour passer du clavier azerty au clavier qwerty, rebind des touches
def aze_qwe_control():
    # permet de passer du clavier qwerty au clavier azerty
    if held_keys['k'] == 1 and held_keys['left control'] == 0:
        input_handler.rebind('z', 'w')
        input_handler.rebind('a', 'q')
        input_handler.rebind('q', 'a')
        input_handler.rebind('m', ',')
        input_handler.rebind(',', 'm')
        input_handler.rebind('w', 'z')

    if held_keys['k'] and held_keys['left control'] == 1:
        input_handler.rebind('w', 'w')
        input_handler.rebind('q', 'q')
        input_handler.rebind('a', 'a')
        input_handler.rebind(',', ',')
        input_handler.rebind('m', 'm')
        input_handler.rebind('z', 'z')

def debug_mod():
    global enabled_debug_mode
    if held_keys['i'] == 1 and held_keys['left control'] == 0:
        enabled_debug_mode = True
        
    if held_keys['i'] and held_keys['left control'] == 1:
        enabled_debug_mode = False
    Debug_axes.enabled = enabled_debug_mode
    cam.Cam_orbit.enabled = enabled_debug_mode
    cam.Cam_move.enabled = enabled_debug_mode


list_mat = []
for i in range(2):
    list_mat.append(obj.wood())
    
for el in list_mat:
    el.on_click = obj.collect

cam.set_cam()

def update():
    # activation du mode debug
    debug_mod()
    aze_qwe_control()

camera.update = cam.camera_control
app.run()
