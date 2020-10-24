import get_handle as handle
import record_call as record
import get_time as lecture
import logging as logger
import sys

logger.basicConfig(level=logger.DEBUG, handlers=[logger.FileHandler("debug.log"), logger.StreamHandler()], format='%(asctime)s  | %(name)s | %(levelname)s | %(message)s')
logger.debug("Python {0:s} {1:d}bit on {2:s}\n".format(" ".join(item.strip() for item in sys.version.split("\n")), 64 if sys.maxsize > 0x100000000 else 32, sys.platform))

lecture.WebLauncher(logger).main()