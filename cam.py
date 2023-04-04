from ursina import *

# entity pour le controle de la camera
Cam_orbit = Entity(model='sphere', color= rgb(255, 255, 255, 100))
Cam_move = Entity(model='sphere', color= rgb(255, 255, 255, 100), position= (5, 0, 0)) 

def set_cam():
    global Cam_move, Cam_orbit, camera
    camera.y = 7
    camera.z = -10
    camera.rotation_x = 34
    camera.rotation_y = 0
    Cam_orbit.rotation_y = 0
    camera.parent = Cam_orbit
    Cam_move.parent = Cam_orbit

def camera_control():
    CAM_spd = 80
    cam_dir_forward= (Cam_orbit.world_x - camera.world_x, Cam_orbit.world_z - camera.world_z)
    cam_dir_right= (Cam_orbit.world_x - Cam_move.world_x, Cam_orbit.world_z - Cam_move.world_z)

    # deplacement en avant en arriere
    if -10.1 < Cam_orbit.x < 10.1:
        Cam_orbit.x += held_keys['z'] *  cam_dir_forward[0] * time.dt
        Cam_orbit.x -= held_keys['s'] *  cam_dir_forward[0] * time.dt
    else:
        Cam_orbit.x = 10 if Cam_orbit.x > 10 else -10
    if -10.1 < Cam_orbit.z < 10.1:
        Cam_orbit.z += held_keys['z'] *  cam_dir_forward[1] * time.dt
        Cam_orbit.z -= held_keys['s'] *  cam_dir_forward[1] * time.dt
    else:
        Cam_orbit.z = 10 if Cam_orbit.z > 10 else -10

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