# level
## **Class:** Level
The level of the log.

---

### **Method: ** constructor
Instantiates the Level object.
??? abstract "Source"
    ````python
    def __init__(self, l_name: str, l_foreground_color: ForegroundColor | str = ForegroundColor.white,
                 l_background_color: BackgroundColor | str = "", l_effect: Effect | str = ""):
        self.name = l_name
        self.foreground_color = l_foreground_color
        self.background_color = l_background_color
        self.effect = l_effect
    ````

??? help "Parameters"
    #### l_name
    The name of the log level. This is shown in the log string.<br>
    **- Type: `#!python str`**<br>
    ---
    #### l_foreground_color
    The foreground color of the log level. This will be the log string foreground color.<br>
    **- Type: `#!python ForegroundColor | str`**<br>
    **- Default: `#!python ForegroundColor.white`**<br>
    ---
    #### l_background_color
    The background color of the log level. This will be the log string background color.<br>
    **- Type: `#!python BackgroundColor | str`**<br>
    **- Default: `#!python """`**<br>
    #### l_effect
    The effect of the log level. This will be the effect applied to the log string.<br>
    **- Type: `#!python Effect | str`**<br>
    **- Default: `#!python """`**<br>

??? example
    ````python
    from logpy.log import Level
    
    custom_level = Level(
        "LEVEL NAME",
        ForegroundColor.red,
        BackgroundColor.white,
        Effect.reverse
    )
    ````

---

## **Class:** Levels
A collection of default (and the most used) log levels.

---

### **Attribute: ** normal
Normal log level.
??? abstract "Source"
    ````python
    normal = Level("NORMAL", ForegroundColor.white)
    ````

??? example
    ````python
    from logpy.log import Levels

    Levels.normal
    ````
---
### **Attribute: ** notification
Notification log level.
??? abstract "Source"
    ````python
    notification = Level("NOTIFICATION", ForegroundColor.blue)
    ````

??? example
    ````python
    from logpy.log import Levels

    Levels.notification
    ````
---
### **Attribute: ** alert
Alert log level.
??? abstract "Source"
    ````python
    alert = Level("ALERT", ForegroundColor.yellow)
    ````

??? example
    ````python
    from logpy.log import Levels

    Levels.alert
    ````
---
### **Attribute: ** warning
Warning log level.
??? abstract "Source"
    ````python
    warning = Level("WARNING", ForegroundColor.orange)
    ````

??? example
    ````python
    from logpy.log import Levels

    Levels.warning
    ````
---
### **Attribute: ** error
Error log level.
??? abstract "Source"
    ````python
    error = Level("ERROR", ForegroundColor.red)
    ````

??? example
    ````python
    from logpy.log import Levels

    Levels.error
    ````
---
### **Attribute: ** success
Success log level.
??? abstract "Source"
    ````python
    success = Level("SUCCESS", ForegroundColor.green)
    ````

??? example
    ````python
    from logpy.log import Levels

    Levels.success
    ````
---
### **Attribute: ** unknown
Unknown log level.
??? abstract "Source"
    ````python
    unknown = Level("UNKNOWN", ForegroundColor.cyan)
    ````

??? example
    ````python
    from logpy.log import Levels

    Levels.unknown
    ````
---
