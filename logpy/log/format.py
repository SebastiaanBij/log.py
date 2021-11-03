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
        """
        The format of a log.\n
        :param f_string: The format string. This uses custom variables, which are identifiable by the <i>'$'</i> symbol.<br>
        These are the current variables:<br>
        - $date = the date of the log.<br>
        - $time = the time of the log.<br>
        - $level = the level of the log.<br>
        - $message = the message of the log.
        :param f_date: The format of the date. This uses the datetime variables.
        :param f_time: The format of the time. This uses the datetime variables.
        """
        self.string = f_string
        self.date = f_date
        self.time = f_time
    #endregion

    #region Magic Methods
    def __repr__(self) -> str:
        return "logpy.log.format.Format"
    #endregion

    #region Public Methods
    def generate_log(self, f_message: str, f_date: datetime = datetime.now(),
                     f_time: datetime = datetime.now(), f_level: Level = Levels.normal) -> str:
        """
        Generate the log string, which in turn can be used to show in the terminal and/or be saved to a file.\n
        :param f_message: The message of the log.
        :param f_date: The date of the log.
        :param f_time: The time of the log.
        :param f_level: The level of the log.
        :return: The log string.
        """
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
