#!/usr/bin/env python
from __future__ import print_function

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
    userdir = os.path.expanduser('~')

    # add a log subfolder folder
    temp_folder = "{0}/log/".format(userdir)

    # parse it as a valid path
    temp_folder = Path(temp_folder)

    # stringfy path instance
    fake_log_folder = str(temp_folder)

# if any exception found, exit
except Exception as e:
    print("Fake log folder: {0} could not be created".format(fake_log_folder))
    sys.exit()

# setup function
def setup(i):

    # setup of loggin config values
    fake_log_level = 'INFO'
    fake_log_file = fake_log_folder+'/fake_'+str(i)+'.log'
    fake_log_date_format = '%Y-%m-%d %H:%M:%S'
    fake_log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

    # check if log folder exists
    if not os.path.exists(fake_log_folder):
        print("Fake log folder: {0} not found".format(fake_log_folder))
        try:
            os.makedirs(fake_log_folder)
            print("Fake log folder: {0} created".format(fake_log_folder))
        except Exception  as e:
            print("Fake log folder: {0} could not be created, error: {1}".format(fake_log_folder, e))

    # setup of handlers
    handler = logging.FileHandler(fake_log_file)        
    handler.setFormatter(fake_log_formatter)

    # setup of loggers
    logger = logging.getLogger('logger '+str(i))
    logger.setLevel(fake_log_level)
    logger.addHandler(handler)

    # first log message inside log file
    logger.info("Fake log {0} configuration is done".format(str(i)))

    # check if log file exists
    if os.path.exists(fake_log_file):
        logger.info("Fake log file: {0} already exist.".format(fake_log_file))
    else:
        logger.info("Fake log file will be created at: {0}".format(fake_log_file))
    
    return logger

# writing loop function
def loop(logger):

    # setting up the output message
    output_message = "{0} Fake log file output!".format(str(getpass.getuser()))

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
                logger[i].info("{0}, instance {1}, iteration {2}".format(output_message, str(i), str(iteration)))

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
        print('You must pass a valid number of log instances or leave ir blank for single instance')
        sys.exit()

    # set loggin config values
    fake_log_level = 'INFO'
    fake_log_format = '%(asctime)s %(levelname)s %(message)s'
    fake_log_date_format = '%Y-%m-%d %H:%M:%S'

    # parsinf logging basic config
    logging.basicConfig(
        level=getattr(logging,fake_log_level),
        format=fake_log_format,
        datefmt=fake_log_date_format,
        filemode='w+'
        )
        
    # create logger variable
    logger = {}

    # loop for many log instances
    for i in range(log_instances):
        # call setup function
        logger[i+1] = setup(i+1)

    # call logger function
    loop(logger)

# end of code