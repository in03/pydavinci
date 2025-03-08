import sys
from typing import Any
from rich.console import Console
from rich.logging import RichHandler
import logging

# Configure rich console
console = Console()

# Configure logging with rich
logging.basicConfig(
    level="INFO",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)]
)

# Get logger
logger = logging.getLogger("pydavinci")

def info(message: str, depth: int = 2) -> None:
    logger.info(message)

def warn(message: str, depth: int = 2) -> None:
    logger.warning(message)

def debug(message: str, depth: int = 2) -> None:
    logger.debug(message)

def error(message: str, depth: int = 2) -> None:
    logger.error(message)

def raise_exception(exception: Any, message: str, depth: int = 2) -> None:
    try:
        raise exception
    except exception:
        logger.exception(message)
