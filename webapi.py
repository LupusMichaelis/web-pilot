
from bottle import request, response
from bottle import post, get, put, delete

import cruise_control

@get('/position')
def get_position():
    try:
        current_position = cruise_control.get_current_position()
        return {'current_position': current_position}
    except Exception as e:
        response.status = 500
        return {'error': ''}

@post('/forward')
def go_forward():
    try:
        cruise_control.forward()
        response.status = 200
    except Exception as e:
        # This might depend upon the kind of error that occur, you might want to return a
        # 404 if forward's not found, 403 if forbidden, etc
        response.status = 500
        return {'error': ''}

# I put direction and angle in the URI for the sake of demonstration, but it should be a
# payload provided in the body of the HTTP request
@post('/turn/<direction>/<angle:int>')
def make_turn(direction, angle):

    if direction not in ('left', 'right'):
        response.status = 400
        return { 'error': 'Wrong turn', 'description': 'Not left or right' }

    direction = cruise_control.LEFT if direction is 'left' else cruise_control.RIGHT

    if 0 > angle or angle > 180:
        response.status = 400
        return { 'error': 'Wrong turn', 'description': 'Improbable angle: Iä ! Iä ! Cthulhu fhtagn!' }

    try:
        cruise_control.turn(direction, angle)
        return cruise_control.get_direction()
    except Exception as e:
        response.status = 500
        return {'error': ''}
        
