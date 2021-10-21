from logpy import Logger
from logpy.log import Levels

logger = Logger()

logger.log("Hello World!")  # The default level is normal, so this is the equivalent of Levels.normal
logger.log("Be notified.", Levels.notification)
logger.log("Be alerted.", Levels.alert)
logger.log("Be warned.", Levels.warning)
logger.log("Oh no, something went wrong!", Levels.error)
logger.log("Yes, we did it!", Levels.success)
logger.log("I have no clue what's going on.", Levels.unknown)
