from lib.controller import *
from datetime import datetime
import logging

logger = logging.getLogger("logfile")

#
# Main - starting point
#
def main():
    print("start", datetime.now())
    logger.info(f"start Creatives Rebuild New York app")
    # create controller obj
    controller = CreativesRebuildController()
    # check for dup UIDs
    # try:
    controller.checkForDupUID()
    # except:
        # logger.info(f"**** error: dump data struct {config.uid_data_struct}")
    print("finished", datetime.now())


if __name__ == "__main__":
    main()
