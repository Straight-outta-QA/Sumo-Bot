# Reflected light intensity of the edge of the sumo board
EDGE_REFLECTION = 30

def is_on_edge(reflected_light):
    if (reflected_light < 0):
        raise ValueError('The light sensor cannot read a value that is less than 0.')
    if (reflected_light > 100):
        raise ValueError('The light sensor cannot read a value that is greater than 100.')


    if (reflected_light <= EDGE_REFLECTION):
        return True
    else: 
        return False
