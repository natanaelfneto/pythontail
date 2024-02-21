# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Released]

### 0.8 - 2024-02-21
### Changed
- moved all the base code from Python 2 to Python 3 standards including f-string and print functions

### 0.7 - 2018-09-22
### Added
- logging handler configurations class and global variable
- faker log generator inside tests now print instance and line
- quiet input option [-q, --quiet, --silent] flag parameter to remove source heads from tailing process
- sleep interval time input [-s, --sleep, --sleep-interval] that accespts integer values for sleep in seconds between output updates of --follow flag

### Changed
- class PythonTail is now GetTail
- from unique function to separated functions for tail N lines from files and for follow live file
- logging basic config to handlers for file and stream outputs
- main function name from files to run for future standards in use with PID and remote sources tailing
- rename files/paths to sources for future standards in use with PID and remote sources tailing

### 0.6 - 2018-09-11
#### Added
- added example folder with basic use of pythontail for multiple files
- added a fake log generator for tests inside a test folder
- added commands '-n' for limit lines 
- added standard value of 10 lines for tailed files with no parameters
- added mutual block usage for '-f' and -n commands
- added '-n 0' behavior to match the '-f'

#### Changed
- moved variables of the project configuration to the main file: pythontail.py and imported in setup.py file
- fixed log level for console output errors and debug flag outputs
- removed obligatory use of '-f' for filepaths and correct to the regular unix usage of follow files

### 0.5 - 2018-09-09
#### Changed
- changed main function from main() to args() for better code writing as imported module tail.args(['-h'])

### 0.4 - 2018-09-09
#### Changed
- fixed setup.py file according to pypi guide

### 0.3 - 2018-09-09
#### Changed
- added logger to a self variable to be used inside instancies of classes outside of main() function

### 0.2 - 2018-09-09
#### Changed
- changed name from pytail to pythontail due to conflicts with pre-existing pypi package
- change routines to a main() function while trying to solve import issues

### 0.1 - 2018-09-09
#### Added
- option to tail many files at same time
- added argsparse and logging

## [Unreleased]

### 0.0 - 2018-09-09
#### Added
- project created