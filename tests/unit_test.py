from context import react_to_opponent, sense_edge
import pytest

# Testing parameters; found through paritioning the input space of the light sensor
FULL_SPEED = 200
HALF_SPEED = FULL_SPEED/2

INVALID_DIST = 0
INVALID_DIST_2 = 2551
MIN_DIST = 1 # The robot is right next to the other robot
CLOSE_DIST = 60 # The robot should slow its speed when the opponent is <=25mm away
FAR_DIST = 61 # The robot should travel at full speed if the opponent is >25mm away
MAX_DIST = 2550

INVALID_REFLECTED_LIGHT = -1
INVALID_REFLECTED_LIGHT_2 = 101
SIGNAL_TURN = 30 # The robot turns if it senses a reflected light intensity <=30
NO_TURN_SIGNAL = 31
MIN_REFLECTED_LIGHT = 0
MAX_REFLECTED_LIGHT = 100

# Test react_to_opponent.py
def test_react_to_opponent_invalid_dist():
    with pytest.raises(ValueError) as error_info:
        react_to_opponent.set_speed(INVALID_DIST)

def test_react_to_opponent_invalid_dist_2():
    with pytest.raises(ValueError) as error_info:
        react_to_opponent.set_speed(INVALID_DIST_2)

def test_react_to_opponent_close():
    assert(react_to_opponent.set_speed(CLOSE_DIST) == HALF_SPEED)

def test_react_to_opponent_min():
    assert(react_to_opponent.set_speed(MIN_DIST) == HALF_SPEED)

def test_react_to_opponent_far():
    assert(react_to_opponent.set_speed(FAR_DIST) == FULL_SPEED)

def test_react_to_opponent_max():
    assert(react_to_opponent.set_speed(MAX_DIST) == FULL_SPEED)

# Test sense_edge.py
def test_sense_edge_invalid_reading():
    with pytest.raises(ValueError) as error_info:
        sense_edge.is_on_edge(INVALID_REFLECTED_LIGHT)

def test_sense_edge_invalid_reading_2():
    with pytest.raises(ValueError) as error_info:
        sense_edge.is_on_edge(INVALID_REFLECTED_LIGHT_2)

def test_sense_edge_signal_turn():
    assert(sense_edge.is_on_edge(SIGNAL_TURN))

def test_sense_edge_no_turn_signal():
    print(not(sense_edge.is_on_edge(NO_TURN_SIGNAL)))
    assert(not(sense_edge.is_on_edge(NO_TURN_SIGNAL)))

def test_sense_edge_min_light():
    assert(sense_edge.is_on_edge(MIN_REFLECTED_LIGHT))

def test_sense_edge_max_light():
    assert(not(sense_edge.is_on_edge(MAX_REFLECTED_LIGHT)))