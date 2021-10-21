from logpy import Logger
from logpy.log import Format

custom_format = Format(
    "$date - $time | ($level) $message",
    "%Y-%m-%d",
    "%H;%M;%S"
)
logger = Logger(custom_format)

logger.log("Custom log format.")
