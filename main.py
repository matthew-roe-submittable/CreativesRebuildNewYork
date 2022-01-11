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
    # load the database with submittable form information
    # validate unique identifier


    print("finished", datetime.now())



if __name__ == "__main__":
    main()
