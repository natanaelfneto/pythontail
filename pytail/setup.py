from setuptools import setup

'''
      This package was released using the The Hitchhiker’s Guide to Packaging
      at https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/index.html
'''

setup(name='pytail',
      version='0.1',
      description='Unix tail implementation in python',
      long_description=open('README.md').read(),
      url='http://github.com/natanaelfneto/pytail',
      author='natanaelfneto,
      author_email='natanaelfneto@outlook.com',
      license='MIT',
      packages=['pytail'],
      zip_safe=False)