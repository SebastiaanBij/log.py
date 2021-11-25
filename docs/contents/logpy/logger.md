# logger
## **Class:** Logger
A logger object which can be used in instantiated and/or non-instantiated use-cases.

---

### **Method: ** constructor
Instantiates the Logger object.
??? abstract "Source"
    ````python
    def __init__(self, l_format: Format = Format(), l_echo: bool = True, l_save: bool = False,
                 l_filepath: str = "./logs", l_file_extension: str = "log"):
        self.format = l_format
        self.echo = l_echo
        self.save = l_save
        self.filepath = l_filepath
        self.file_extension = l_file_extension
    ````

??? help "Parameters"
    #### l_format
    The format of the log message, date and time.<br>
    **- Type: `#!python Format`**<br>
    **- Default: `#!python Format()`**<br>
    ---
    #### l_echo
    Whether to echo the log to the terminal.<br>
    **- Type: `#!python bool`**<br>
    **- Default: `#!python True`**<br>
    ---
    #### l_save
    Whether to save the logs to a file.<br>
    **- Type: `#!python bool`**<br>
    **- Default: `#!python False`**<br>
    ---
    #### l_filepath
    The filepath to save the log files to if the <i>'l_save'</i> property is set to True.<br>
    **- Type: `#!python str`**<br>
    **- Default: `#!python "./logs"`**<br>
    ---
    #### l_file_extension
    The log file extension.<br>
    **- Type: `#!python str`**<br>
    **- Default: `#!python ".log"`**<br>

??? example
    ````python
    from logpy import Logger
    
    logger = Logger()
    ````
---
### **Method: ** log
Log an event and depending on your logger object properties save and/or echo the log.
??? abstract "Source"
    ````python
    def log(self, l_message: str, l_level: Level = Levels.normal, l_date: datetime = datetime.now(),
        l_time: datetime = datetime.now()):
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
    ````

??? help "Parameters"
    #### l_message
    The message of the log.<br>
    **- Type: `#!python str`**<br>
    ---
    #### l_level
    The level of the log.<br>
    **- Type: `#!python Level`**<br>
    **- Default: `#!python Levels.normal`**<br>
    ---
    #### l_date
    The date of the log.<br>
    **- Type: `#!python datetime.datetime`**<br>
    **- Default: `#!python datetime.datetime.now()`**<br>
    ---
    #### l_time
    The time of the log.<br>
    **- Type: `#!python datetime.datetime`**<br>
    **- Default: `#!python datetime.datetime.now()`**<br>

??? example
    ````python
    from logpy import Logger
    
    logger = Logger()
    logger.log("Hello World!")
    ````
---
### **Method: ** slog
Log an event and echo it to the terminal.

!!! warning
    This method does not allow saving to a file. For that you will need to instantiate the Logger object and use the log method.

??? abstract "Source"
    ````python
    @staticmethod
    def slog(l_message: str, l_level: Level = Levels.normal, l_date: datetime = datetime.now(),
             l_time: datetime = datetime.now(), l_format: Format = Format()):
            print(l_format.generate_log(l_message, l_date, l_time, l_level))
    ````

??? help "Parameters"
    #### l_message
    The message of the log.<br>
    **- Type: `#!python str`**<br>
    ---
    #### l_level
    The level of the log.<br>
    **- Type: `#!python Level`**<br>
    **- Default: `#!python Levels.normal`**<br>
    ---
    #### l_date
    The date of the log.<br>
    **- Type: `#!python datetime.datetime`**<br>
    **- Default: `#!python datetime.datetime.now()`**<br>
    ---
    #### l_time
    The time of the log.<br>
    **- Type: `#!python datetime.datetime`**<br>
    **- Default: `#!python datetime.datetime.now()`**<br>
    ---
    #### l_format
    The format of the log.
    **- Type: `#!python Format`**<br>
    **- Default: `#!python Format()`**<br>

??? example
    ````python
    from logpy import Logger
    
    Logger.slog("Hello World!")
    ````
