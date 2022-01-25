from envparse import env
import sys
import os 
from AsunaRobot import LOGGER

DEFAULTS = {
    "LOAD_MODULES": True,
}


def get_str_key(name, required=False):
    default = DEFAULTS[name] if name in DEFAULTS else None
    if not (data := env.str(name, default=default)) and not required:
        LOGGER.warn("No str key: " + name)
        return None
    elif not data:
        LOGGER.critical("No str key: " + name)
        sys.exit(2)
    else:
        return data

def get_int_key(name, required=False):
    default = DEFAULTS[name] if name in DEFAULTS else None
    if not (data := env.int(name, default=default)) and not required:
        LOGGER.warn("No int key: " + name)
        return None
    elif not data:
        LOGGER.critical("No int key: " + name)
        sys.exit(2)
    else:
        return data
    
def get_bool_key(name, required=False):
    default = DEFAULTS[name] if name in DEFAULTS else None
    if not (data := env.bool(name, default=default)) and not required:
        log.warn("No bool key: " + name)
        return False
    elif not data:
        log.critical("No bool key: " + name)
        sys.exit(2)
    else:
        return data
