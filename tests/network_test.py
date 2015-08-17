"""
Created on Aug 16, 2014
@author: Qianhao Lu

The minimal set of nose test for package UI.
"""

from nose.tools import *
import DownloadImage.network as nt
import os

__author__ = 'Qianhao Lu <luqsim@gmail.com>'
__date__ = '16/08/15'

class test_downloader():

    def setup(self):
        self.remote_link = 'http://www.google.com/images/logos/google_logo_41.png' # this probably works always
        self.local = 'tests/test_file.png'
        self.dl = nt.Downloader(self.remote_link, self.local)  # test download function
        pass


    def test_downloader(self):
        #TODO: we should use a static file for this test!
        file_size = 2357 # may change

        print os.getcwd()
        if self.dl.is_ok < 0:
            assert_true(False)  #this should fail!
        else:
            self.dl.save_file()
            assert_equal(os.path.getsize(self.local), 2357)

            # now test when file exists
            self.dl = nt.Downloader(self.remote_link, self.local)  # test download function
            self.dl.save_file()
            assert_equal(self.dl.is_ok, -1)

            # remove template file
            try:
                os.remove(self.local)
            except:
                pass

            pass

        pass

    def test_downloader_err_msg(self):
        assert_equal(self.dl.get_error_msg(), '')
        pass

    pass # class test_downloader

