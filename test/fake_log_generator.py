#!/usr/bin/env python
from __future__ import print_function
# third party imports
import logging
import getpass
import time
import os
import sys

# get project log folder
fake_log_folder = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)),'../log/'))

# setup function
def setup(i):

    # setup of loggin config values
    fake_log_level = 'INFO'
    fake_log_file = fake_log_folder+'/fake_'+str(i)+'.log'
    fake_log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    fake_log_date_format = '%Y-%m-%d %H:%M:%S'

    # check if log folder exists
    if not os.path.exists(fake_log_folder):
        print("Fake log folder:",fake_log_folder,"not found")
        try:
            os.makedirs(fake_log_folder)
            print("Fake log folder:",fake_log_folder,"created")
        except Exception  as e:
            print("Fake log folder:",fake_log_folder,"could not be created, error:", e)

    # setup of handlers
    handler = logging.FileHandler(fake_log_file)        
    handler.setFormatter(fake_log_formatter)

    # setup of loggers
    logger = logging.getLogger('logger '+str(i))
    logger.setLevel(fake_log_level)
    logger.addHandler(handler)

    # first log message inside log file
    logger.info("Fake log %s configuration is done", str(i))

    # check if log file exists
    if os.path.exists(fake_log_file):
        logger.info("Fake log file: %s already exist.",fake_log_file)
    else:
        logger.info("Fake log file will be created at: %s",fake_log_file)
    
    return logger

# writing loop function
def loop(logger):

    # setting up the output message
    output_message = str(getpass.getuser())+' Fake log file output!'

    # get a while loop to populate the fake log file
    while True:
        # write log for each file instance
        for i in logger:
            # log output message in especific logger
            logger[i].info(output_message+' instance %s',str(i))
            # wait before writing a new line
            time.sleep(2)

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
        raise ValueError('You must pass a valid number of log instances or leave ir blank for single instance')

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
        
    logger = {}
    # loop for many log instances
    for i in range(log_instances):
        # call setup function
        logger[i+1] = setup(i+1)
    # call logger function
    loop(logger)
# end of code