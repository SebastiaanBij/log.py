#!/usr/bin/env python3

# ||Imports||
########################################################################################################################
from logpy.ansi import ForegroundColor, BackgroundColor, Effect

# ||Classes||
########################################################################################################################
class Level:
    #region Constructor
    def __init__(self, l_name: str, l_foreground_color: ForegroundColor | str = ForegroundColor.white,
                 l_background_color: BackgroundColor | str = "", l_effect: Effect | str = ""):
        """
        The level of the log.

        Parameters
        ----------
        l_name : str
            The name of the log level. This is shown in the log string.
        l_foreground_color : ForegroundColor | str
            The foreground color of the log level. This will be the log string foreground color.
        l_background_color : BackgroundColor | str
            The background color of the log level. This will be the log string background color.
        l_effect: Effect | str
            The effect of the log level. This will be the effect applied to the log string.
        """
        self.name = l_name
        self.foreground_color = l_foreground_color
        self.background_color = l_background_color
        self.effect = l_effect
    #endregion

    # region Magic Methods
    def __repr__(self) -> str:
        return "logpy.log.level.Level"
    # endregion

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
