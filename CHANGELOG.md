# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Released]

### 0.6 - 2018-09-11
#### Added
- added example folder with basic use of pythontail for multiple files
- added a fake log generator for tests inside a test folder

#### Changed
- moved variables of the project configuration to the main file: pythontail.py and imported in setup.py file
- fixed log level for console output errors and debug flag outputs

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