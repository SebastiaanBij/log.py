#!/usr/bin/env python3

# ||Imports||
########################################################################################################################
from datetime import datetime
from logpy.log.level import Level, Levels
from logpy.ansi import Effect

# ||Class||
########################################################################################################################
class Format:
    #region Constructor
    def __init__(self, f_string: str = "<$date | $time> [$level] $message", f_date: str = "%d-%m-%Y",
                 f_time: str = "%H:%M:%S"):
        self.string = f_string
        self.date = f_date
        self.time = f_time
    #endregion

    #region Public Methods
    def generate_log(self, f_message: str, f_date: datetime = datetime.now(),
                     f_time: datetime = datetime.now(), f_level: Level = Levels.normal) -> str:
        result = f"{f_level.foreground_color}{f_level.background_color}{f_level.effect}{self.string}{Effect.reset}"
        dictionary = {
            "$date": f_date.strftime(self.date),
            "$time": f_time.strftime(self.time),
            "$level": f_level.name,
            "$message": f_message
        }

        for variable in dictionary:
            if variable in result:
                result = result.replace(variable, dictionary[variable])
        return result
    #endregion
