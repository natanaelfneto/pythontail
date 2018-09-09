#!/usr/bin/env python
from __future__ import print_function
# Authorship
__description__ = '''
This PyTail module:
# Author - Natanael F. Neto <natanaelfneto@outlook.com>
# Source - https://github.com/natanaelfneto/pytail

is based on the python-tail module from
# Author - Kasun Herath <kasunh01 at gmail.com>
# Source - https://github.com/kasun/python-tail

but simplified for pratical use
'''

# Installation
'''
pip install pytail
'''

# Usage example
'''

''' 
# third party imports
import argparse
import logging
import mmap
import os
import sys
import time

# module name
__project__ = 'pytail'
# module version
__version__ = "0.1"

# main class
class PyTail(object):
    # represents a tail command
    def __init__(self):
        ''' 
            Initiate a PyTail instance.
            
            Arguments:
         '''

    # function to mmap file and get last line without buffering all data into memory
    def getlastline(self, file):
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
    # check if validate paths remained
        if not len(paths) > 0:
            logger.error('No paths were successfully parsed. Exiting...')
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
    def __init__(self):
        ''' 
            Initiate a PyTail Path Validity instance.
        '''

    # path validity checker function
    def checker(self, paths):
        # set basic variables
        valid_paths = []    # array for AEs
        logger.debug('checking validity of parsed files')
        for path in paths:
            if os.access(path, os.F_OK) and os.access(path, os.R_OK) and os.path.isfile(path) :
                logger.debug("Path %s is successfully parsed", path)
                valid_paths.append(path)
            else:
                logger.debug( \
                    "Path '%s' could not be found or does not have read permitions or it is not a file, \
                    therefore will be ignored", path
                    )
        return valid_paths

if __name__ == "__main__":
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
    args = parser.parse_args() 

    # output software version info
    if args.version:
        print(__project__+' version '+__version__+'\n'+__description__)
        os.system('python '+os.path.dirname(os.path.realpath(__file__))+'/'+__project__+'.py -h')
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
        paths = PathsValidity()
        paths = paths.checker(args.follow)

        # tail follow paths parsed
        pytail = PyTail()
        pytail.follow(paths)

