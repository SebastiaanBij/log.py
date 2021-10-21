#!/usr/bin/env python3

# ||Imports||
########################################################################################################################
from logpy.log import Format, Level, Levels
from datetime import datetime

# ||Class||
########################################################################################################################
class Logger:
    #region Constructor
    def __init__(self, l_format: Format = Format(), l_save: bool = False, l_filepath: str = "./logs",
                 l_file_extension: str = ".log"):
        self.format = l_format
        self.save = l_save
        self.filepath = l_filepath
        self.file_extension = l_file_extension
    #endregion

    #region Public Methods
    def log(self, l_message: str, l_level: Level = Levels.normal, l_date: datetime = datetime.now(),
            l_time: datetime = datetime.now()):
        if self.save:
            return
        else:
            print(self.format.generate_log(l_message, l_date, l_time, l_level))

    @staticmethod
    def slog(l_message: str, l_level: Level = Levels.normal, l_date: datetime = datetime.now(),
                   l_time: datetime = datetime.now(), l_format: Format = Format()):
        print(l_format.generate_log(l_message, l_date, l_time, l_level))
    #endregion
