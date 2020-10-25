import get_time as lecture
import logging as logger
from datetime import datetime
from sys import version, maxsize, platform, argv, executable
from subprocess import check_call

if argv[1] == "install":
    check_call([
        executable, 
        "-m", 
        "pip", 
        "install", 
        "-r", 
        "requirements.txt"
    ])

elif argv[1] == "run":
    filenames = "Lecture_" + str(datetime.now().isoformat()).replace(".", "_").replace(":","-")
    logger.basicConfig(
        level=logger.DEBUG, 
        handlers=[logger.FileHandler("debug.log"), 
        logger.StreamHandler()], 
        format='%(asctime)s  | %(name)s | %(levelname)s | %(message)s'
    )
    logger.debug(
        "Python {0:s} {1:d}bit on {2:s}\n".format(" ".join(item.strip() for item in version.split("\n")), 
        64 if maxsize > 0x100000000 else 32, platform)
        )
    lecture.WebLauncher(logger, filenames).main()

else:
    logger.error("\nTo run you must enter the following: \n>> python main.py install (followed by)\n>> python main.py run")