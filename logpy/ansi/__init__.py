#!/usr/bin/env python3

# ||Documentation||
########################################################################################################################
"""
The ANSI module containing:
- ForegroundColor
- BackgroundColor
- Effect

These are used to edit your logs appearance. You can use them in the logpy.log.level.Level object.
"""

# ||Imports||
########################################################################################################################
from .color import ForegroundColor, BackgroundColor
from .effect import Effect
