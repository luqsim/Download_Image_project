"""
Created on Aug 16, 2014
@author: Qianhao Lu

The minimal set of nose test.
"""

from nose.tools import *
import DownloadImage

__author__ = 'Qianhao Lu <luqsim@gmail.com>'
__date__ = '16/08/15'


def setup():
    print "SETUP!"


def teardown():
    print "TEAR DOWN!"


def test_basic():
    """
    test the project skeleton.
    """
    print "GO!"


