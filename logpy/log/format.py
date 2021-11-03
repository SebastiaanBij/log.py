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
        The level of a log.

        Parameters
        ----------
        f_string : str
            The format string. This uses custom variables, which are identifiable by the <i>'$'</i> symbol.
            These are the current variables:
                - <b>$date</b> = the date of the log.
                - <b>$time</b> = the time of the log.
                - <b>$level</b> = the level of the log.
                - <b>$message</b> = the message of the log.
        f_date : str
            The format of the date. This uses the datetime variables.
        f_time : str
            The format of the time. This uses the datetime variables.
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
        Generate the log string, which in turn can be used to show in the terminal and/or be saved to a file.

        Parameters
        ----------
        f_message : str
            The message of the log.
        f_date : datetime
            The date of the log.
        f_time : datetime
            The time of the log.
        f_level : Level
            The level of the log.

        Returns
        -------
        str
            The log string.
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
