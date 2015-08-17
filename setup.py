"""
Created on Aug 16, 2014
@author: Qianhao Lu

The minimal set of setup.py.

Please add more content as the project progresses!
"""

__author__ = 'Qianhao Lu <luqsim@gmail.com>'
__date__ = '16/08/15'

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Download images from a predefined plaintext file.',
    'author': 'Qianhao Lu',
    'url': 'N.A.',
    'download_url': 'N.A.',
    'author_email': 'luqsim@gmail.com',
    'version': '0.1',
    'install_requires': ['nose', 'argparse'],
    'packages': ['DownloadImage'],
    'scripts': ['bin/download_from_file.py'],  # this needs to grow
    'name': 'Download_Images_project'
}

setup(**config)