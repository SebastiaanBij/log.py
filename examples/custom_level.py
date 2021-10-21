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
