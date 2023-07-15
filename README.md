# Sumo Bot 🤖

[![CircleCI](https://circleci.com/gh/NdagiStanley/python_app.svg?style=svg)](https://circleci.com/gh/Straight-outta-QA/Sumo-Bot)

This repo contains the [MicroPython](https://micropython.org/) code needed to control an EV3 sumo bot. The robot is programed to navigate a 4 foot-diameter ring, and push out any robots that are also in the ring. For a full list of the compeition rules, please refer to the [official ORC rulebook](http://www.orc.ieeeottawa.ca/wp-content/uploads/ORC2023-SumoEN.pdf). 

The sumo bot is equiped with a [color sensor](https://pybricks.com/ev3-micropython/ev3devices.html?highlight=color%20sensor#color-sensor) to sense the edge of the ring, and an [ultrasonic sensor](https://pybricks.com/ev3-micropython/ev3devices.html?highlight=color%20sensor#ultrasonic-sensor) to sense its opponent.

Two [medium motors](https://pybricks.com/ev3-micropython/ev3devices.html?highlight=color%20sensor#motors) are used to move the robot forward.

## Testing

The goal of this project is to thouroughly test the code base to ensure the robot does not critically fail during a match. To accomplish this goal, advanced testing methodologies were used. The following techniques will be used to ensure the code's quality:
* Control Flow Graph Coverage
* Logic Coverage
* Input Space Paritioning
* Mutation Testing
* Integration Testing