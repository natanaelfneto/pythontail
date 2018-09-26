from pythontail import tail
from pathlib import Path

import os


# get as many valid files paths you want to be tailed
log_file_1 = str(Path("{0}/log/fake_1.log".format(os.path.expanduser('~'))))
log_file_2 = str(Path("{0}/log/fake_2.log".format(os.path.expanduser('~'))))

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
