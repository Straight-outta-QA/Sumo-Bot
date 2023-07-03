# This file's purpose is to give the individual tests import context
# Following the project structure outlined in "The Hitchhiker’s Guide to Python"

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../sumo_bot')))

import react_to_opponent
import sense_edge