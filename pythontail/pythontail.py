#!/usr/bin/env python

# project name
__project__ = "pythontail"

# project version
__version__ = "0.8"

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
import os
import sys
import time


# main class
class GetTail(object):

    # gettail init
    def __init__(self, lines=0):
        '''
            Initiate a GetTail instance
        '''

        # get loggert on a self instance
        self.logger = logger.adapter

        # set desired number of lines
        self.lines = lines

        # set output index string length
        self.line_pad = len(str(self.lines))
    
    # enter function for class basic rotine
    def __enter__(self):
        '''
            Function for entering class with python 3 standards of
            'with' parameter and a following __exit__ function for
            a cleanner use of the class instancies
        '''
        try:
            return self
        except StopIteration:
           raise RuntimeError("Instance could not be returned")

    # function to seek file and get last N lines without buffering all data into memory
    def getlines(self, file, lines):
        '''
            Function to keep getting last line of a file as it updates

            Arguments:
                file: file to be tailed
        '''

        # array of found lines 
        lineset = []

        # block counter will be multiplied by buffer to get the block size from the end
        block_counter = -1

        # buffer memory (if file too small it will trigger an expected I/O Error)
        buffer=4098

        # use file as variable with read bytes
        with open(file, "rb") as f:

            # keep loop until the array of founded lines match desired number of lines
            while len(lineset) < lines:

                # attempt to seek line block from file end
                try:
                    f.seek(block_counter * buffer, os.SEEK_END)

                # either file is too small, or too many lines requested
                except IOError: 

                    # error handler
                    f.seek(0)
                    lineset = f.readlines()
                    break

                # update lineset
                lineset = f.readlines()

                # update block counter
                block_counter = block_counter - 1

            # return lineset array
            return lineset[-lines:]

    # function to get seek live file and get last line without buffering all data into memory
    def getlastline(self, file):

        # use file as variable with read bytes
        with open(file, "rb") as f:

            # trying to get end of file on memory
            try:

                # seek_end file
                f.seek(-2, os.SEEK_END)

                # walk on file data ultil it reaches a line breaker
                while f.read(1) != b"\n":

                    # seek_cur file
                    f.seek(-2, os.SEEK_CUR)

                # return obtained line decoded
                return f.readline()

            # if an IOError occurr, just pass
            except IOError:
                pass    

    # function for tail lines from files
    def tail(self, sources):

        # get files from sources
        files = sources["files"]

        # add line break for file output lines
        print("\n", end="\r")

        # file loop
        for file in files:
            
            # set output message for file output header
            loud_output = f" from {os.path.basename(file)}" if not quiet_flag else ''
            output = f">>> tailing {self.lines} lines{loud_output} <<<"

            # print output
            print(output)

            # call function to retrieve lines from file
            retrieved_lines = self.getlines(file, self.lines)

            # output lines founded
            for index, line in enumerate(retrieved_lines):

                # set output message
                output = f"{(self.lines - index):0{self.line_pad}d}: {line.decode()}"

                # print output
                print(output, end="\r")
            
            # print line break at the end of file loop
            print("\n", end="\r")

    # function to tail follow files
    def follow(self, sources):

        # get files from sources
        files = sources["files"]

        last_line = {}
        # set las line variable
        for index, file in enumerate(files):
            last_line[index] = None

        # for an infinite tail of file
        while True:

            # loop files
            for index, file in enumerate(files):
                try:
                    # get last line
                    updated_last_line = self.getlastline(file).decode()

                    # do not update if the saved last line is identical to new retrieved line or if its None
                    if last_line[index] != updated_last_line and updated_last_line is not None:
                        print(updated_last_line, end="\r")
                        last_line[index] = updated_last_line

                        # sleep time between line retrieves
                        if sleep_time:
                            time.sleep(sleep_time)

                # get keyboard interruption for a gracefull system exit
                except KeyboardInterrupt:
                    self.logger.info("tail was interrupted by the user")
                    sys.exit()

    #  exit function for class basic routine
    def __exit__(self, exc_type, exc_value, traceback):
        pass

# paths argument parser
class PathsValidity(object):

    # path validity init
    def __init__(self):
        ''' 
            Initiate a PythonTail Path Validity instance.
        '''

        # get loggert on a self instance
        self.logger = logger.adapter
        
    # path validity checker function
    def validate(self, files):
        '''
            Function to check if each parsed path is a valid system file
            and if it can be accessed by the code.

            Arguments:
                paths: array of files to be checked
        '''

        # set basic variable for valid files
        valid_files = []

        # loop check through parsed path
        self.logger.debug("Checking validity of inputed sources")

        for file in files:            
            file = file.replace('~', os.path.expanduser("~")) if "~" in file else file
            
            # file output if not quiet_flag
            loud_file = f" {file}" if not quiet_flag else ''
            
            # append path if it exists, is accessible and is a file
            if os.access(file, os.F_OK) and os.access(file, os.R_OK) and os.path.isfile(file):
                
                output = f"Source path{loud_file} was successfully parsed"

                # append valid file to array
                valid_files.append(file)

            # if not, log the error
            else:
                output = f"Source path{loud_file} could not be accessed as a file"

            # log output
            self.logger.debug(output)
        
        # return all parsed valid files
        return valid_files

# class for logger instancies and configurations
class Logger(object):

    # path validity init
    def __init__(self, folder=None, format=None, extra=None, debug_flag=False, quiet_flag=False, verbose_flag=False):
        ''' 
            Initiate a DICOM Populate Logger instance.
            Argument:
                logger: a logging instance for output and log
        '''

        # 
        log = {
            # setup of log folder
            "folder": folder,
            # set logging basic config variables
            "level": "INFO",
            # 
            "date_format": "%Y-%m-%d %H:%M:%S",
            # 
            "filepath": f"{folder}/{__project__}.log",
            #
            "format": format,
            # extra data into log formatter
            "extra": extra
        }

        # set log name
        logger = logging.getLogger(f"{__project__}-{__version__}")

        # set formatter
        formatter = logging.Formatter(log["format"])

        # check debug flag
        if debug_flag:
            logger.setLevel("DEBUG")
        else:
            logger.setLevel("INFO")

        # check if log folder exists
        if not os.path.exists(log["folder"]):
            folder_variable = f": {log['folder']}" if not quiet_flag else ''
            print(f"Log folder{folder_variable} not found")
            try:
                os.makedirs(log["folder"])
                print(f"Log folder{folder_variable} created")
  
            except Exception  as e:
                print(f"Log folder{folder_variable} could not be created, error: {e}")
                sys.exit()

        # setup of file handler
        file_handler = logging.FileHandler(log["filepath"])     
        file_handler.setFormatter(formatter)

        # setup of stream handler
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        # add handler to the logger
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

        # update logger to receive formatter within extra data
        logger = logging.LoggerAdapter(logger, log["extra"])

        self.adapter = logger

def __exit__(output):
    '''
        Argument Parser custom error handler
    '''
    # set output message
    output = "" +\
        "usage: pythontail.py [-h] [-f | -n LINES] [-q] [-s SLEEP] [-d] [-v] sources [sources ...]\n" +\
        output

    # print output message
    print(output, end="")

    # exit on error
    sys.exit()

# command line argument parser
def args(args):
    '''
        Main function for terminal call of library
        Arguments:
          args: receive all passed arguments and filter them using
          the argparser library
    '''

    # argparser init
    parser = argparse.ArgumentParser(description=short_description)

    # prevent follow and lines flag to be setted at the same time
    group = parser.add_mutually_exclusive_group(required=False)

    # files with limited lines
    parser.add_argument(
        "sources",
        nargs="+",
        help="sources to be tailed", 
        default=[]
    )

    # path argument parser
    group.add_argument(
        "-f","--follow",
        action="store_true",
        help="flag to not limit number of lines tailed", 
        default=False,
        required=False
    )

    # number of lines to limit tail
    group.add_argument(
        "-n","--lines",
        type=int,
        help="number of lines to follow in total array of sources", 
        default=None,
        required=False
    )

    # quiet flag argument parser
    parser.add_argument(
        "-q","--quiet", "--silent",
        action="store_true", 
        help="never output headers giving file names",
        default=False,
        required=False
    )

    # sleep interval input
    parser.add_argument(
        "-s","--sleep", "--sleep-interval",
        type=int, 
        help="with --follow, sleep for approximately N seconds (default 0) between iterations; least once every N seconds",
        default=None,
        required=False
    )

    # debug flag argument parser
    parser.add_argument(
        "-d","--debug",
        action="store_true", 
        help="process debug flag",
        default=False,
        required=False
    )

    # version output argument parser
    parser.add_argument(
        "-v","--version",
        action="version",
        help="output software version",
        default=False,
        version=(f"{__project__}-{__version__}")
    )

    # passing filtered arguments as array
    args = parser.parse_args(args)

    # check follow flag
    if args.follow == True:

        # check lines value
        if args.lines is not None:
            output = "pythontail.py: error: argument -f/--follow: not allowed with argument -n/--lines"
            __exit__(output)

        # check sleep value
        if args.sleep is None:
            args.sleep = 0
        
        # set lines to zero on follow flag
        args.lines = 0

    # check for incompatible arguments
    elif args.follow == False and args.lines != 0 and args.sleep is not None:
        output = "pythontail.py: error: argument -n/--lines: not allowed with argument -s/--sleep/--sleep-interval"
        __exit__(output)
    
    # call tail sources function
    run(
        debug=args.debug,
        quiet=args.quiet,
        lines=args.lines,
        sleep=args.sleep,
        sources=args.sources,
    )

# function to check and tail files
def run(debug=False, quiet=False, lines=10, sleep=0, sources=[]):

    # normalizing debug variable
    global debug_flag
    debug_flag = debug

    # normalizing quiet variable
    global quiet_flag
    quiet_flag = quiet

    # normalizing sleep variable
    global sleep_time
    sleep_time = sleep

    # standard log folder
    log_folder = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)),"../log/"))

    # standard log format
    log_format = "%(asctime)-8s %(levelname)-5s [%(project)s-%(version)s] user: %(user)s LOG: %(message)s"

    # creates a logger instance from class Logger within:
    # an adapter (the logging library Logger Adapter) and the verbose flag
    global logger
    logger = Logger(
        folder = log_folder,
        format = log_format,
        debug_flag = debug_flag,
        extra = {
            "project":  __project__,
            "version":  __version__,
            "user":     getpass.getuser()
        },
        # verbose_flag = verbose_flag
    )

    # debug flag variable
    logger.adapter.debug(f"DEBUG flags was setted as: {debug}")

    # lines limit number
    logger.adapter.debug(f"LINES limit number is: {lines}")

    # sleep time value
    if lines == 0:
        logger.adapter.debug(f"SLEEP time is: {sleep_time} seconds")

    # check for quiet flag
    if not quiet_flag:

        # log folder location
        logger.adapter.debug(f"Log file is being stored at directory: {log_folder}")

        # paths to be followed
        if len(sources) > 1:

            # create a fake array for output
            fake_array = ""
            for source in sources:
                fake_array = f"{fake_array}\n\t'{source}'"
            fake_array +="\n]"

            output = f"More than one SOURCE was inputed: \nSOURCES = [{fake_array}"
        else:
            output = f"Only one SOURCE was inputed: {sources}"
        
        # log output value
        logger.adapter.debug(output)

    # create instance of class and validate files
    valid_files = PathsValidity().validate(sources)

    # check if validate paths remained
    if not len(valid_files) > 0:
        logger.adapter.error("No paths were successfully parsed. Exiting...")
        sys.exit()

    # combine valid files and vallid process
    valid_sources = {
        "files": valid_files,
    }

    if lines != 0:
        with GetTail(lines=lines) as get:
            get.tail(sources=valid_sources)
    else:
        GetTail().follow(sources=valid_sources)

# run function on command call
if __name__ == "__main__":
    args(sys.argv[1:])
# end of code