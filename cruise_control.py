LEFT = 1
RIGHT = 2

def forward():
    """
    Instructions to have the contraction going forward.
    """

    print('Run Forrest! Run!')

def get_current_position():
    """
    Here I'm giving a simple example where the contraption device position is in a
    cartesian reference. But it's obvious that it could be corrdinates provided bythe
    embeded gyroscope and accelerometer if any.
    """
    return {'x': 10, 'y': 20, 'z': 0}
