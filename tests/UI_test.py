"""
Created on Aug 16, 2014
@author: Qianhao Lu

The minimal set of nose test for package UI.
"""

from nose.tools import *
import DownloadImage.UI as ui

__author__ = 'Qianhao Lu <luqsim@gmail.com>'
__date__ = '16/08/15'

def test_progress_bar():

    # test 0%
    ui_out = ui.show_bars(0,20)
    assert_equal(ui_out, '[                    ] 0%')

    # test 100%
    ui_out = ui.show_bars(100,20)
    assert_equal(ui_out, '[====================] 100%')


    pass


@raises(ValueError)
def test_progress_bar_exception():
    import DownloadImage.UI as ui

    # test exception
    # assert_raises(ValueError, ui.show_bars, 'abc')
    str_out = ui.show_bars('abc')

    pass