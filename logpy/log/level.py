#!/usr/bin/env python3

# ||Imports||
########################################################################################################################
from logpy.ansi import ForegroundColor, BackgroundColor

# ||Classes||
########################################################################################################################
class Level:
    def __init__(self, l_name: str, l_foreground_color: ForegroundColor = ForegroundColor.white,
                 l_background_color: BackgroundColor = None):
        self.name = l_name
        self.foreground_color = l_foreground_color
        self.background_color = l_background_color

class Levels:
    normal = Level("NORMAL", ForegroundColor.white)
    notification = Level("NOTIFICATION", ForegroundColor.blue)
    alert = Level("ALERT", ForegroundColor.yellow)
    warning = Level("WARNING", ForegroundColor.orange)
    error = Level("ERROR", ForegroundColor.red)
    success = Level("SUCCESS", ForegroundColor.green)
    unknown = Level("UNKNOWN", ForegroundColor.cyan)
