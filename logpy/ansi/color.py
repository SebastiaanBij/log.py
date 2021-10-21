#!/usr/bin/env python3

# ||Classes||
########################################################################################################################
class ForegroundColor:
    """
    A collection of ANSI foreground colors in the Python format.\n
    """
    #region Variables
    black = "\033[30m"
    red = "\033[31m"
    green = "\033[32m"
    orange = "\033[33m"
    blue = "\033[34m"
    purple = "\033[35m"
    cyan = "\033[36m"
    pink = "\033[95m"
    yellow = "\033[93m"
    white = "\033[37m"
    grey = "\033[90m"
    light_red = "\033[91m"
    light_green = "\033[92m"
    light_blue = "\033[94m"
    light_cyan = "\033[96m"
    #endregion

class BackgroundColor:
    """
    A collection of ANSI background colors in the Python format.\n
    """
    #region Variables
    black = "\033[40m"
    red = "\033[41m"
    green = "\033[42m"
    orange = "\033[43m"
    blue = "\033[44m"
    purple = "\033[45m"
    cyan = "\033[46m"
    white = "\033[47m"
    #endregion
