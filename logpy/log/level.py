#!/usr/bin/env python3

# ||Imports||
########################################################################################################################
from logpy.ansi import ForegroundColor, BackgroundColor, Effect

# ||Classes||
########################################################################################################################
class Level:
    def __init__(self, l_name: str, l_foreground_color: ForegroundColor | str = ForegroundColor.white,
                 l_background_color: BackgroundColor | str = "", l_effect: Effect | str = ""):
        """
        The level of a log.\n
        :param l_name: The name of the log level. This is shown in the log string.
        :param l_foreground_color: The foreground color of the log level. This will be the log string foreground color.
        :param l_background_color: The background color of the log level. This will be the log string background color.
        :param l_effect: The effect of the log level. This will be the effect applied to the log string.
        """
        self.name = l_name
        self.foreground_color = l_foreground_color
        self.background_color = l_background_color
        self.effect = l_effect

class Levels:
    """
    A collection of default (and the most used) log levels.\n
    """
    normal = Level("NORMAL", ForegroundColor.white)
    notification = Level("NOTIFICATION", ForegroundColor.blue)
    alert = Level("ALERT", ForegroundColor.yellow)
    warning = Level("WARNING", ForegroundColor.orange)
    error = Level("ERROR", ForegroundColor.red)
    success = Level("SUCCESS", ForegroundColor.green)
    unknown = Level("UNKNOWN", ForegroundColor.cyan)
