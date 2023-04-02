from ursina import *

app = Ursina(borderless= False, show_ursina_splash = True, size = (1000,500))

CAM_spd = 80
enabled_debug_mode = False
# création du sol des axes de debug et des entity de control camera
Ground = Entity(model='plane', color= rgb(1, 150, 1), scale_z= 10, scale_x= 10, collider='mesh')
Debug_axes = Entity(model= 'axes', texture='axes')
# Construction_point = Entity(model='../model/construction_point', texture= '../texture/construction_point')


def destroy_entity():
    destroy(Pneu, delay= 1)

Pneu = Entity(model='pneu', texture= 'pneu', collider= 'mesh', on_click= destroy_entity)


b = Button(text='Quit', color=color.azure, scale=.0625, text_origin=(-.5,0), position= (.85,.45))
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
    Cam_orbit.enabled = enabled_debug_mode
    Cam_move.enabled = enabled_debug_mode

# entity pour le controile de la camera
Cam_orbit = Entity(model='sphere', color= rgb(255, 255, 255, 100))
Cam_move = Entity(model='sphere', color= rgb(255, 255, 255, 100), position= (5, 0, 0)) 

# set camera
camera.y = 7
camera.z = -10
camera.rotation_x = 34
camera.rotation_y = 0
Cam_orbit.rotation_y = 0
camera.parent = Cam_orbit
Cam_move.parent = Cam_orbit

def camera_control():
    cam_dir_forward= (Cam_orbit.world_x - camera.world_x, Cam_orbit.world_z - camera.world_z)
    cam_dir_right= (Cam_orbit.world_x - Cam_move.world_x, Cam_orbit.world_z - Cam_move.world_z)

    # deplacement en avant en arriere
    Cam_orbit.x += held_keys['z'] *  cam_dir_forward[0] * time.dt
    Cam_orbit.z += held_keys['z'] *  cam_dir_forward[1] * time.dt
    Cam_orbit.x -= held_keys['s'] *  cam_dir_forward[0] * time.dt
    Cam_orbit.z -= held_keys['s'] *  cam_dir_forward[1] * time.dt
    
    # controle pour déplacement de gauche a droite
    Cam_orbit.x += held_keys['q'] *  cam_dir_right[0] * time.dt
    Cam_orbit.z += held_keys['q'] *  cam_dir_right[1] * time.dt
    Cam_orbit.x -= held_keys['d'] *  cam_dir_right[0] * time.dt
    Cam_orbit.z -= held_keys['d'] *  cam_dir_right[1] * time.dt
    
    # rotation orbitale de la camera
    Cam_orbit.rotation_y += held_keys['a'] * CAM_spd * time.dt
    Cam_orbit.rotation_y -= held_keys['e'] * CAM_spd * time.dt
    if Cam_orbit.rotation_x > -20:
        Cam_orbit.rotation_x -= held_keys['left shift'] * CAM_spd * time.dt
    if Cam_orbit.rotation_x < 30:
        Cam_orbit.rotation_x += held_keys['space'] * CAM_spd * time.dt
        
    # TODO: limiter la camera a l'air de jeux
   
def update():
    camera_control()
    debug_mod()
    aze_qwe_control()
    # activation du mode debug
    
app.run()
