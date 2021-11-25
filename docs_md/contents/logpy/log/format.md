# format
## **Class:** Format
The format of a log.

---

### **Method: ** constructor
Instantiates the Format object.
??? abstract "Source"
    ````python
    def __init__(self, f_string: str = "<$date | $time> [$level] $message", f_date: str = "%d-%m-%Y",
                 f_time: str = "%H:%M:%S"):
        self.string = f_string
        self.date = f_date
        self.time = f_time
    ````

??? help "Parameters"
    #### f_string
    The format string. This uses custom variables, which are identifiable by the <i>'$'</i> symbol.<br>
    These are the current variables:<br>
    &emsp;- **$date** = the date of the log.<br>
    &emsp;- **$time** = the time of the log.<br>
    &emsp;- **$level** = the level of the log.<br>
    &emsp;- **$message** = the message of the log.<br>
    **- Type: `#!python str`**<br>
    **- Default: `#!python "<$date | $time> [$level] $message"`**<br>
    ---
    #### f_date
    The format of the date. This uses the datetime variables.<br>
    **- Type: `#!python str`**<br>
    **- Default: `#!python "%d-%m-%Y"`**<br>
    ---
    #### f_time
    The format of the time. This uses the datetime variables.<br>
    **- Type: `#!python str`**<br>
    **- Default: `#!python "%H:%M:%S"`**<br>

??? example
    ````python
    from logpy.log import Format
    
    custom_format = Format(
        "$date - $time | ($level) $message",
        "%Y-%m-%d",
        "%H;%M;%S"
    )
    ````
---
### **Method: ** generate_log
Generate the log string, which in turn can be used to show in the terminal and/or be saved to a file.
??? abstract "Source"
    ````python
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
    ````

??? help "Parameters"
    #### f_message
    The message of the log.<br>
    **- Type: `#!python str`**<br>
    ---
    #### f_date
    The date of the log.<br>
    **- Type: `#!python datetime.datetime`**<br>
    **- Default: `#!python datetime.datetime.now()`**<br>
    ---
    #### f_time
    The time of the log.<br>
    **- Type: `#!python datetime.datetime`**<br>
    **- Default: `#!python datetime.datetime.now()`**<br>
    ---
    #### f_level
    The level of the log.<br>
    **- Type: `#!python Level`**<br>
    **- Default: `#!python Levels.normal`**<br>

??? example
    ````python
    from logpy.log import Format
    
    custom_format = Format(
        "$date - $time | ($level) $message",
        "%Y-%m-%d",
        "%H;%M;%S"
    )
    custom_format.generate_log("Hello World!")
    ````
---
