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
        A logger object which can be used in instantiated and/or non-instantiated use-cases.\n
        :param l_format: The format of the log message, date and time.
        :param l_echo: Whether to echo the log to the terminal.
        :param l_save: Whether to save the logs to a file.
        :param l_filepath: The filepath to save the log files to if the <i>'l_save'</i> property is set to True.
        :param l_file_extension: The log file extension.
        """
        self.format = l_format
        self.echo = l_echo
        self.save = l_save
        self.filepath = l_filepath
        self.file_extension = l_file_extension
    #endregion

    #region Public Methods
    def log(self, l_message: str, l_level: Level = Levels.normal, l_date: datetime = datetime.now(),
            l_time: datetime = datetime.now()):
        """
        Log an event and depending on your logger object properties save and/or echo the log.\n
        :param l_message: The message of the log.
        :param l_level: The level of the log.
        :param l_date: The date of the log.
        :param l_time: The time of the log.
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
        Log an event and echo it to the terminal. (This method does not allow saving to a file.)\n
        :param l_message: The message of the log.
        :param l_level: The level of the log.
        :param l_date: The date of the log.
        :param l_time: The time of the log.
        :param l_format: The format of the log.
        """
        print(l_format.generate_log(l_message, l_date, l_time, l_level))
    #endregion
