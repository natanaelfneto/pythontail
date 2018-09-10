#!/usr/bin/env python
from __future__ import print_function
# Authorship
__author__ = '@natanaelfneto'
__description__ = '''
This PythonTail module:

Unix tail implementation in python

# Author - Natanael F. Neto <natanaelfneto@outlook.com>
# Source - https://github.com/natanaelfneto/pythontail
'''
# Installation
'''
pip install pythontail
'''
# Usage example
'''
from pythontail import tail
tail.main(['-h'])
''' 
# third party imports
import argparse
import logging
import mmap
import os
import sys
import time
# module name
__project__ = 'pythontail'
# module version
__version__ = "0.5"
# main class
class PythonTail(object):
    # represents a tail command
    def __init__(self, logger):
        '''
            Initiate a PythonTail instance
        '''
        self.logger = logger
    # function to mmap file and get last line without buffering all data into memory
    def getlastline(self, file):
        '''
            Function to keep getting last line of a file as it updates

            Arguments:
                file: file to be tailed
        '''
        with open(file, 'rb') as f:
            try:
                f.seek(-2, os.SEEK_END)
                while f.read(1) != b'\n':
                    f.seek(-2, os.SEEK_CUR)
                return f.readline().decode()
            except IOError:
                pass    
    # function to tail follow all parsed paths
    def follow(self, paths):
        '''
            Function to get all parsed paths and call the getlasfile() function
            to each one at a time and merge in the standard output

            Arguments:
                paths: array of files to be tailed
        '''
    # check if validate paths remained
        if not len(paths) > 0:
            self.logger.error('No paths were successfully parsed. Exiting...')
            sys.exit()
        last_line = ''
        while True:
            for path in paths:
                if last_line != self.getlastline(path) and self.getlastline(path) is not None:
                    last_line = self.getlastline(path)
                    print(last_line, end='\r')
# paths argument parser
class PathsValidity(object):
    # path validity init
    def __init__(self, logger):
        ''' 
            Initiate a PythonTail Path Validity instance.
        '''
        self.logger = logger
    # path validity checker function
    def checker(self, paths):
        '''
            Function to check if each parsed path is a valid system file
            and if it can be accessed by the code.

            Arguments:
                paths: array of files to be checked
        '''
        # set basic variables
        valid_paths = []    # array for AEs
        self.logger.debug('checking validity of parsed files')
        for path in paths:
            if os.access(path, os.F_OK) and os.access(path, os.R_OK) and os.path.isfile(path) :
                self.logger.debug("Path %s is successfully parsed", path)
                valid_paths.append(path)
            else:
                self.logger.debug( \
                    "Path '%s' could not be found or does not have read permitions or it is not a file, \
                    therefore will be ignored", path
                    )
        return valid_paths
def args(args):
    # argparser init
    parser = argparse.ArgumentParser(
        description='Unix tail implementation in python'
    )
    # path argument parser
    parser.add_argument(
        '-f','--follow',
        nargs='+',
        help='dicom folders or files paths', 
        default="check_string_for_empty",
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
        '-V','--version',
        action='store_true', 
        help='output software version',
        default=False,
        required=False
    )
    # passing filtered arguments as array
    args = parser.parse_args(args) 
    # output software version info
    if args.version:
        print(__project__+' version '+__version__+'\n'+__description__+'\n'+'Author: '+__author__)
        # os.system('python '+os.path.dirname(os.path.realpath(__file__))+'/'+__project__+'.py -h')
        sys.exit()
    # setting logging basic config avriables
    log_folder = 'log'
    if args.debug:
        log_level = 'DEBUG'
        log_file = log_folder+'/'+__project__+'_debug.log'
        log_format = '%(asctime)s %(name)s %(levelname)s %(message)s'
        log_date_format = '%Y-%m-%d %H:%M:%S'
    else:
        log_level = 'INFO'
        log_file = log_folder+'/'+__project__+'_info.log'
        log_format = '%(asctime)s %(levelname)s %(message)s'
        log_date_format = '%Y-%m-%d %H:%M:%S'
    # check if log folder exists
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)
    # setting logging basic config
    logging.basicConfig(
        level=getattr(logging,log_level),
        format=log_format,
        datefmt=log_date_format,
        filename=log_file,
        filemode='a+'
        )
    logger = logging.getLogger(__name__)
    # tail follow paths
    if args.follow:
        # check validity of the paths parsed
        paths = PathsValidity(logger)
        paths = paths.checker(args.follow)
        # tail follow paths parsed
        pythontail = PythonTail(logger)
        pythontail.follow(paths)
# run main function
if __name__ == "__main__":
    args(sys.argv[1:])
# end of code