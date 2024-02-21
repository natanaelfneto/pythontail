<p align="left">
  <a href="#">
    <img 
      alt="pythontail-logo" 
      src="https://raw.githubusercontent.com/natanaelfneto/pythontail/master/assets/pythontail-logo.png" 
      width="240"/>
  </a>
</p>

**PythonTail**: a Unix tail implementation in python.
Version: **0.8**
***
# Table of Contents
* [Getting Started](#getting-started)
    * [Unix version comparison](#unix-version-comparison)
    * [Installation process](#installation-process)
    * [Usage](#usage)
    * [Examples](#examples)
* [License](#license)
***
## Getting Started
### Unix version comparison
#### Unix tail implementation list (adapted)
-   item:           `default output line = 10`\
    descrtption:    default output with 10 lines for each tailed file\
    status:         [**OK**]
-   item:           `-c, --bytes=[+]NUM`\
    description:    output the last NUM bytes; or use -c +NUM to output starting\
                    with byte NUM of each file\
    status:         [**PENDING**]
-   item:           `-f, --follow`\
    description:    output appended data as the file grows;\
    status:         [**OK**]
-   item:           `-n, --lines=NUM`\
    description:    output the last NUM lines, instead of the last 10; or use -n\
                    <!-- +NUM to output starting with line NUM\ -->
    status:         [**OK**]
-   item:           `--max-unchanged-stats=N`\
    description:    with --follow=name, reopen a FILE which has not\
                    changed size after N (default 5) iterations to see if it has\
                    been unlinked or renamed (this is the usual case of rotated\
                    log files); with inotify, this option is rarely useful\
    status:         [**PENDING**]
-   item:           `--pid=PID`\
    description:    with -f, terminate after process ID, PID dies\
    status:         [**PENDING**]
-   item:           `-q, --quiet, --silent`\
    description:    never output headers giving file names\
    status:         [**OK**]
-   item:           `--retry`\
    description:    keep trying to open a file if it is inaccessible\
    status:         [**PENDING**]
-   item:           `-s, --sleep-interval=N`\
    description:    with -f, sleep for approximately N seconds (default 0)\
                    between iterations; at least once every N seconds\
    status:         [**OK**]
-   item:           `-v, --verbose`\
    description:    always output headers giving file names\
    status:         [**PENDING**]
-   item:           `-z, --zero-terminated`\
    description:    line delimiter is NUL, not newline\
    status:         [**PENDING**]
-   item:           `--help`\
    description:    display this help and exit\
    status:         [**OK**]
-   item:           `--version`\
    description:    output version information and exit\
    status:         [**OK**]
-   item:           `multiple files support`\
    description:    tail as many files as wanted with all available parameters working as well\
    status:         [**OK**]
#### Unique tail implementations
-   item:           `usage as both terminal command and as python module`\
    description:    the use of all parameters within terminal command line\
                    and by importing as a module inside a python script\
    status:         [**OK**]
-   item:           `-d, --debug`\
    description:    create a log file and register all ocurrencies of regular\
                    behavior information, debug and errors as the timestamp and logged user\
    status:         [**OK**]
-   item:           `?`\
    description:    tail files over tcp/ip\
    status:         [**PENDING**]
### Via Bash
#### Installation Process
_install as a module:_
```Shell
pip install pythontail
```
_and use it as:_
```Python
from pythontail import tail
tail.run(["dir/log/file.log"])
```
_use as terminal command:_
```Shell
git clone https://github.com/natanaelfneto/pythontail.git
python pythontail.py -h
```
_enjoy_
***
## Usage
_this messagem can also be found with_ **python pythontail.py -h** _command_
```ShellSession
usage: pythontail.py [-h] [-f | -n LINES] [-q] [-s SLEEP] [-d] [-v] sources [sources ...]

Unix tail implementation in python 

optional arguments:
-h, --help                  show this help message and exit
-f, --follow                flag to not limit number of lines tailed
-n LINES, --lines LINES     number of lines to follow in total array of sources

-q, --quiet, --silent       never output headers giving file names

-s SLEEP, --sleep SLEEP, --sleep-interval SLEEP
                            with --follow, sleep for approximately N seconds
                            (default 0) between iterations; least once every N seconds

-d, --debug                 process debug flag
-v, --version               output software version
```
## Examples
### First we need a fake log file
Generate many live fake logs files by running:
```Shell
python pythontail/test/fake_log_generator.py <integer> &
```
_for the example1.py, generate the minimum of 2 fake log files_\
This will create two **fake_n.log** files in _~/log/fake_n.log_ that can be tailed
### Using it as console command for tail files
```
python pythontail/pythontail.py -f ~/log/fake_1.log ~/log/fake_2.log
```
### Using it as python module for tail files
Create a virtual env and activate it (can be pyenv or virtualenv or any other)
```Shell
mkvirtualenv pythontail
workon pythontail
```
Install pythontail module
```Shell
pip install pythontail
```
Create your code as the available in _pythontail/examples/example1.py_\
```Python
from pythontail import tail
from pathlib import Path

import os


# get as many valid files paths you want to be tailed
log_file_1 = str(Path(f"{os.path.expanduser("~")}/log/fake_1.log"))
log_file_2 = str(Path(f"{os.path.expanduser("~")}/log/fake_2.log"))

# tail them
tail.run(
    # debug=False,
    # quiet=False,
    # lines=10,
    # sleep=0,
    sources=[
        log_file_1, 
        log_file_2
    ]
)

# for a --follow atribute, set the maximum number of lines to zero [lines=0]
# optional --sleep atribute only works with --follow flag, done by making [lines=0]
```
Check the output of example1 by running the script file:
```Shell
python pythontail/examples/example1.py
```
## License
MIT License

Copyright (c) 2017 Natanael F. Neto (natanaelfneto)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.