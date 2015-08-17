"""
Functions or classes associating with UI come here.
"""
import sys

__author__ = 'Qianhao Lu <luqsim@gmail.com>'
__date__ = '16/08/15'

def show_bars(progress_percent, bar_len=100):
    """
    Given progress in percent, show it linux-like.

    TODO: get the width of the terminal window automatically, so no need for bar_len any more.

    :param progress_percent: progress in percent
    :param bar_len: the number of the bars ('=') when 100% reachs
    :return: the output string. Result should be printed to stdout already

    :type bar_len: int
    :type progress_percent: float
    :rtype: str
    """
    pp = float(progress_percent)  # if progress_percent is not a number, the exception should go!

    if pp>100: # which can happen when download, we handle it here
        pp=100.
        pass

    if pp<0:
        pp=0.
        pass

    pg_value = bar_len*pp/100.
    pg_int_value = int(pg_value)

    sys.stdout.write('\r')  # remove everything before
    str_out_tpl = "[%%-%ds] %%d%%%%"%bar_len
    str_out = str_out_tpl % ('='*pg_int_value, pg_int_value/bar_len*100)
    sys.stdout.write(str_out)
    sys.stdout.flush()

    return str_out
    pass


def new_bar():
    """
    start a new bar.
    """
    print >> sys.stdout, '\n'
    pass