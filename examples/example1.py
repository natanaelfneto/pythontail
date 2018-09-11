from pythontail import tail
import os

# get as many filepaths you want to be tailed
log_file_1 = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)),'../log/fake_1.log'))
log_file_2 = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)),'../log/fake_2.log'))

# tail them
tail.files(
    debug=True,
    paths=[
        log_file_1, 
        log_file_2
    ]
)