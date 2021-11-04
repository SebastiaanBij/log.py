#!/usr/bin/env python3

# ||Imports||
########################################################################################################################
from logpy.log import Format, Level, Levels
from datetime import datetime
import os

# ||Class||
########################################################################################################################
class Logger:
    #region Constructor
    def __init__(self, l_format: Format = Format(), l_echo: bool = True, l_save: bool = False,
                 l_filepath: str = "./logs", l_file_extension: str = "log"):
        """
        A logger object which can be used in instantiated and/or non-instantiated use-cases.

        Parameters
        ----------
        l_format : Format
            The format of the log message, date and time.
        l_echo : bool
            Whether to echo the log to the terminal.
        l_save : bool
            Whether to save the logs to a file.
        l_filepath : str
            The filepath to save the log files to if the <i>'l_save'</i> property is set to True.
        l_file_extension : str
            The log file extension.
        """
        self.format = l_format
        self.echo = l_echo
        self.save = l_save
        self.filepath = l_filepath
        self.file_extension = l_file_extension
    #endregion

    # region Magic Methods
    def __repr__(self) -> str:
        return "logpy.logger.Logger"
    # endregion

    #region Public Methods
    def log(self, l_message: str, l_level: Level = Levels.normal, l_date: datetime = datetime.now(),
            l_time: datetime = datetime.now()):
        """
        Log an event and depending on your logger object properties save and/or echo the log.

        Parameters
        ----------
        l_message : str
            The message of the log.
        l_level : Level
            The level of the log.
        l_date : datetime
            The date of the log.
        l_time : datetime
            The time of the log

        Examples
        --------
        Basic logging:
        >>> from logpy import Logger
        >>>
        >>> logger = Logger()
        >>> logger.log("Example log message.")

        Logging with a custom format:
        >>> from logpy import Logger
        >>> from logpy.log import Format
        >>>
        >>> custom_format = Format(
        >>>    "$date - $time | ($level) $message",
        >>>    "%Y-%m-%d",
        >>>    "%H;%M;%S"
        >>> )
        >>>
        >>> logger = Logger(custom_format)
        >>> logger.log("Example log message.")

        Logging with a custom level:
        >>> from logpy import Logger
        >>> from logpy.log import Level
        >>> from logpy.ansi import ForegroundColor, BackgroundColor, Effect
        >>>
        >>> custom_level = Level(
        >>>        "LEVEL NAME",
        >>>        ForegroundColor.red,
        >>>        BackgroundColor.white,
        >>>        Effect.reverse
        >>> )
        >>>
        >>> logger = Logger()
        >>> logger.log("Example log message.", custom_level)
        """
        log = self.format.generate_log(l_message, l_date, l_time, l_level)

        if self.save:
            file = f"{self.filepath}/{datetime.now().strftime(self.format.date)}.{self.file_extension}"

            if os.path.exists(file):
                with open(file, "a") as log_file:
                    log_file.write(f"{log}\n")
            else:
                if self.filepath == "./logs" and not os.path.exists(self.filepath):
                    os.makedirs("./logs")

                with open(file, "w") as log_file:
                    log_file.write(f"{log}\n")

        if self.echo:
            print(log)

    @staticmethod
    def slog(l_message: str, l_level: Level = Levels.normal, l_date: datetime = datetime.now(),
             l_time: datetime = datetime.now(), l_format: Format = Format()):
        """
        Log an event and echo it to the terminal. (This method does not allow saving to a file.)

        Parameters
        ----------
        l_message : str
            The message of the log.
        l_level : Level
            The level of the log.
        l_date : datetime
            The date of the log.
        l_time : datetime
            The time of the log.
        l_format : Format
            The format of the log.

        Warnings
        --------
        This method does not allow saving to a file. For that you will need to instantiate the logger object and use the log method.

        Examples
        --------
        Basic logging:
        >>> from logpy import Logger
        >>>
        >>> Logger.slog("Example log message.")

        Logging with a custom format:
        >>> from logpy import Logger
        >>> from logpy.log import Format
        >>>
        >>> custom_format = Format(
        >>>    "$date - $time | ($level) $message",
        >>>    "%Y-%m-%d",
        >>>    "%H;%M;%S"
        >>> )
        >>>
        >>> Logger.slog("Example log message.", l_format = custom_format)

        Logging with a custom level:
        >>> from logpy import Logger
        >>> from logpy.log import Level
        >>> from logpy.ansi import ForegroundColor, BackgroundColor, Effect
        >>>
        >>> custom_level = Level(
        >>>        "LEVEL NAME",
        >>>        ForegroundColor.red,
        >>>        BackgroundColor.white,
        >>>        Effect.reverse
        >>> )
        >>>
        >>> Logger.slog("Example log message.", custom_level)
        """
        print(l_format.generate_log(l_message, l_date, l_time, l_level))
    #endregion
