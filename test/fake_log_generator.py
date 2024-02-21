#!/usr/bin/env python

# third party imports
import logging
import getpass
import time
import os
import sys

from pathlib import Path


# get project log folder
fake_log_folder = None

# trying to parse local user folder as a valid output log folder
try:

    # get logged user path
    userdir = os.path.expanduser("~")

    # add a log subfolder folder
    temp_folder = f"{userdir}/log/"

    # parse it as a valid path
    temp_folder = Path(temp_folder)

    # stringfy path instance
    fake_log_folder = str(temp_folder)

# if any exception found, exit
except Exception as e:
    print(f"Fake log folder: {fake_log_folder} could not be created")
    sys.exit()

# setup function
def setup(i):

    # setup of loggin config values
    fake_log_level = "INFO"
    fake_log_file = fake_log_folder+f"/fake_'{str(i)}.log"
    fake_log_date_format = "%Y-%m-%d %H:%M:%S"
    fake_log_formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")

    # check if log folder exists
    if not os.path.exists(fake_log_folder):
        print(f"Fake log folder: {fake_log_folder} not found")
        try:
            os.makedirs(fake_log_folder)
            print(f"Fake log folder: {fake_log_folder} created")
        except Exception  as e:
            print(f"Fake log folder: {fake_log_folder} could not be created, error: {e}")

    # setup of handlers
    handler = logging.FileHandler(fake_log_file)        
    handler.setFormatter(fake_log_formatter)

    # setup of loggers
    logger = logging.getLogger(f"logger {str(i)}")
    logger.setLevel(fake_log_level)
    logger.addHandler(handler)

    # first log message inside log file
    logger.info(f"Fake log {str(i)} configuration is done")

    # check if log file exists
    if os.path.exists(fake_log_file):
        logger.info(f"Fake log file: {fake_log_file} already exist.")
    else:
        logger.info(f"Fake log file will be created at: {fake_log_file}")
    
    return logger

# writing loop function
def loop(logger):

    # setting up the output message
    output_message = f"{str(getpass.getuser())} Fake log file output!"

    # iteration variable start value
    iteration = 0

    # get a while loop to populate the fake log file
    while True:

        try:
            # iteration incrementer
            iteration = iteration + 1

            # write log for each file instance
            for i in logger:

                # log output message in especific logger
                logger[i].info(f"{output_message}, instance {str(i)}, iteration {str(iteration)}")

                # wait before writing a new line
                time.sleep(2)
        except KeyboardInterrupt:
            logger[i].error("All processes were interrupted by the user")
            sys.exit()

if __name__ == "__main__":

    # get all args
    args = sys.argv[1:]

    try:
        # parse args for integers or emprty
        if not args or int(args[0]) == 0:
            log_instances = 1
        else:
            log_instances = int(args[0])
    except Exception as e:
        print("You must pass a valid number of log instances or leave ir blank for single instance")
        sys.exit()

    # set loggin config values
    fake_log_level = "INFO"
    fake_log_format = "%(asctime)s %(levelname)s %(message)s"
    fake_log_date_format = "%Y-%m-%d %H:%M:%S"

    # parsinf logging basic config
    logging.basicConfig(
        level=getattr(logging,fake_log_level),
        format=fake_log_format,
        datefmt=fake_log_date_format,
        filemode='w+'
        )
        
    # create logger variable
    logger = {}
    
    print(f"The created fake_n log files can be found at {fake_log_folder}")

    # loop for many log instances
    for i in range(log_instances):
        # call setup function
        logger[i+1] = setup(i+1)

    # call logger function
    loop(logger)

# end of code