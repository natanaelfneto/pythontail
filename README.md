<p align="left">
  <a href="#">
    <img 
      alt="pythontail-logo" 
      src="https://raw.githubusercontent.com/natanaelfneto/pythontail/master/assets/pythontail-logo.png" 
      width="240"/>
  </a>
</p>

**PythonTail** a Unix tail implementation in python.
Version: **0.5**
***
# Table of Contents
* [Getting Started](#getting-started)
    * [Installation process](#installation-process)
    * [Usage](#usage)
* [License](#license)
***
## Getting Started
### Via Bash
#### Installation Process
_install as a module:_
```Shell
pip install pythontail
```
_and use it as:_
```Python
from pythontail import tail
tail.args(['-h'])
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
usage: pythontail.py [-h] [-f FOLLOW [FOLLOW ...]] [-d] [-V]

Unix tail implementation in python 

optional arguments:
-h, --help                                            show this help message and exit
-f FOLLOW [FOLLOW ...], --follow FOLLOW [FOLLOW ...]  check if filepaths are valid
-d, --debug                                           process debug flag
-V, --version                                         output software version
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