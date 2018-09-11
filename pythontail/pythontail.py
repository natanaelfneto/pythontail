#!/usr/bin/env python
from __future__ import print_function

# project name
__project__ = "pythontail"

# project version
__version__ = "0.6"

# prohect author
__author__ = "natanaelfneto"
__authoremail__ = "natanaelfneto@outlook.com"

# project source code
__source__ = "https://github.com/natanaelfneto/pythontail"

# project general description
__description__ = '''
This PythonTail module:

is a Unix tail implementation in python

# Author - Natanael F. Neto <natanaelfneto@outlook.com>
# Source - https://github.com/natanaelfneto/pythontail
'''

# project short description
short_description = "a unix tail implementation in python"

# third party imports
import argparse
import getpass
import logging
import mmap
import os
import sys
import time

# main class
class PythonTail(object):

    # pythontail init
    def __init__(self, logger):
        '''
            Initiate a PythonTail instance
        '''

        # get loggert on a self instance
        self.logger = logger

    # function to mmap file and get last line without buffering all data into memory
    def getlastline(self, file):
        '''
            Function to keep getting last line of a file as it updates

            Arguments:
                file: file to be tailed
        '''

        # open parsed file to be tailed
        with open(file, 'rb') as f:

            # trying to get end of file on memory
            try:
                # seek_end file
                f.seek(-2, os.SEEK_END)

                # walk on file data ultil it reaches a line breaker
                while f.read(1) != b'\n':

                    # seek_cur file
                    f.seek(-2, os.SEEK_CUR)

                # return obtained line decoded
                return f.readline().decode()

            # if an IOError occurr, just pass
            except IOError:
                pass    

    # function to tail follow all parsed paths
    def follow(self, lines, files):
        '''
            Function to get all parsed paths and call the getlasfile() function
            to each one at a time and merge in the standard output

            Arguments:
                paths: array of files to be tailed
        '''

        # check if validate paths remained
        if not len(files) > 0:
            self.logger.error('No paths were successfully parsed. Exiting...')
            sys.exit()

        # still no last line
        last_line = ''

        # start line counter
        lines_counter = 0

        # loop until user ends process
        while True:

            # break when line counter achieve lines value
            if lines_counter == lines and lines != 0:
                break

            # line vounter incremental
            lines_counter = lines_counter + 1

            # loop trhough parsed files paths
            for file in files:

                # do not update if the saved last line is identical to new retrieved line or if its None
                if last_line != self.getlastline(file) and self.getlastline(file) is not None:

                    # update last line variable
                    last_line = self.getlastline(file)

                    # output retrieve las line
                    print(last_line, end='\r')

# paths argument parser
class PathsValidity(object):

    # path validity init
    def __init__(self, logger):
        ''' 
            Initiate a PythonTail Path Validity instance.
        '''

        # get loggert on a self instance
        self.logger = logger
        
    # path validity checker function
    def checker(self, files):
        '''
            Function to check if each parsed path is a valid system file
            and if it can be accessed by the code.

            Arguments:
                paths: array of files to be checked
        '''

        # set basic variable for valid files
        valid_files = []

        # loop check through parsed path
        self.logger.debug('checking validity of parsed files')
        for file in files:

            # append path if it exists, is accessible and is a file
            if os.access(file, os.F_OK) and os.access(file, os.R_OK) and os.path.isfile(file) :
                self.logger.debug("Path %s is successfully parsed", file)
                valid_files.append(file)

            # if not, log the error
            else:
                self.logger.debug( \
                    "Path '%s' could not be found or does not have read permitions or it is not a file, \
                    therefore will be ignored", file
                    )
        
        # return all parsed valid files
        return valid_files

# logger configuration function
def logger_config(debug=False):

    # setup of log folder
    log_folder = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)),'../log/'))

    # set logging basic config variables
    log_level = 'INFO'
    log_date_format = '%Y-%m-%d %H:%M:%S'
    log_format = '%(asctime)s %(project)s-%(version)s --%(levelname)s-- user: %(user)s LOG: %(message)s'
    log_file = log_folder+'/'+__project__+'.log'

    # extra data into log formatter
    extra = {
        'project':  __project__,
        'version':  __version__,
        'user':     getpass.getuser()
    }

    # set formatter
    log_formatter = logging.Formatter(log_format)

    # set logger name
    logger_name = __project__+'-'+__version__

    # check debug flag
    if debug:
        log_level = 'DEBUG'
    else:
        log_level = 'ERROR'

    # check if log folder exists
    if not os.path.exists(log_folder):
        print("Log folder:",log_folder,"not found")
        try:
            os.makedirs(log_folder)
            print("Log folder:",log_folder,"created")
        except Exception  as e:
            print("Log folder:",Log_folder,"could not be created, error:", e)

     # setup of handlers
    handler = logging.FileHandler(log_file)        
    handler.setFormatter(log_formatter)

    # setup of loggers
    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)
    logger.addHandler(handler)

    # update logger to receive formatter within extra data
    logger = logging.LoggerAdapter(logger, extra)

    # parsinf logging basic config
    logging.basicConfig(
        level=getattr(logging,log_level),
        format=log_format,
        datefmt=log_date_format,
        filemode='w+'
    )

    # return configured logger instance
    return logger

# command line argument parser
def args(args):

    # argparser init
    parser = argparse.ArgumentParser(
        description=short_description
    )

    # prevent follow and lines flag to be setted at the same time
    group = parser.add_mutually_exclusive_group(required=False)

    # files with limited lines
    parser.add_argument(
        'files',
        nargs='+',
        help='dicom folders or files paths', 
        default=[]
    )

    # number of lines to limit tail
    group.add_argument(
        '-n','--lines',
        nargs='+',
        type=int,
        help='number of lines to follow in total array of files', 
        default=[10],
        required=False
    )

    # path argument parser
    group.add_argument(
        '-f','--follow',
        help='flag to not limit number of lines tailed', 
        default=False,
        required=False
    )

    # debug flag argument parser
    parser.add_argument(
        '-d','--debug',
        action='store_true', 
        help='process debug flag',
        default=False,
        required=False
    )

    # version output argument parser
    parser.add_argument(
        '-v','--version',
        action='version', 
        help='output software version',
        default=False,
        version=(__project__+"-"+__version__)
    )

    # passing filtered arguments as array
    args = parser.parse_args(args)
    
    # if any file being parsed
    if args.files:

        # set limit of lines to zero with follow flag
        if args.follow:
            lines = [0]
        
        # check and tail files
        files(args.debug, args.lines[0], args.files)

    # else no path was pass within the option
    else:
        logger.error('No option or argument was passed. Please try again\n')
        parser.print_help()

# function to check and tail files
def files(debug=False, lines=[10], files=[]):

    # call logger configuration function
    logger = logger_config(debug)

    # log variables
    logger.debug('DEBUG flags was setted as: %s', debug)
    logger.debug('LINES limit is: %s', lines)
    logger.debug('PATHS was parsed as an array: %s', files)

    # create instance of class
    paths = PathsValidity(logger)

    # check each parsed path of file
    files = paths.checker(files)
    
    # create instance of class
    pythontail = PythonTail(logger)

    # tail each parsed path of file
    pythontail.follow(lines, files)

# run function on command call
if __name__ == "__main__":
    args(sys.argv[1:])
# end of code