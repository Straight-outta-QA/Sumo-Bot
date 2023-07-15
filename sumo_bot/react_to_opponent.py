# Preset speed of robot
FAST = 200
SLOW = 100

# The distance (mm) where the robot changes speed
DIST = 60

def set_speed(ultrasonicReading):
    if (ultrasonicReading <= 0):
        raise ValueError('The ultrasonic sensor cannot read a value that is less than 0.') # pragma: no mutate

    if (ultrasonicReading > 2550):
        raise ValueError('The ultrasonic sensor is limited to a range of 2550mm. "' # pragma: no mutate
        + str(ultrasonicReading) + '" is an invalid reading') # pragma: no mutate

    if (ultrasonicReading <= DIST):
        return SLOW
    else:
        return FAST

