# Examples
??? example "Custom format"
    ````python
    from logpy import Logger
    from logpy.log import Format
    
    custom_format = Format(
        "$date - $time | ($level) $message",
        "%Y-%m-%d",
        "%H;%M;%S"
    )
    logger = Logger(custom_format)
    
    logger.log("Custom log format.")
    ````

??? example "Custom level"
    ````python
    from logpy import Logger
    from logpy.log import Level
    from logpy.ansi import ForegroundColor, BackgroundColor, Effect
    
    logger = Logger()
    level = Level(
        "LEVEL NAME",
        ForegroundColor.red,
        BackgroundColor.white,
        Effect.reverse
    )
    
    logger.log("Custom log level.", level)
    ````
