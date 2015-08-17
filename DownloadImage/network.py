"""
Functions or classes associating with network come here.
"""
import urllib2
import os.path
import socket
import sys
import UI as ui
import httplib

__author__ = 'Qianhao Lu <luqsim@gmail.com>'
__date__ = '16/08/15'

#module constants
BLOCK_SIZE = 8192  # as urllib.urlretrieve does
socket.setdefaulttimeout(30)  # set global default timeout to be 30 sec


class Downloader(object):
    """
    A class to download the file and store it locally.
    Usage:
    >dl = Downloader('http://webserver/image.jpg', '~/')
    >if dl.is_ok==0:
    >    dl.save_file()
    >

    We do not use the urllib.urlretrieve, because we want to handle the
    sophiscated exceptions and timeouts. urllib2.open_url() also provides
    more information about the object by returning the HTTPRequest object.

    Check status with dl.is_ok:
    0 or >0: all fine
    -1: file exists already locally
    -2: HTTPError
    -3: URLError
    -4: HTTPException
    -5: User interuption
    -6: timeout
    -7: some unknown reason
    for more details see code or contact me.
    """
    def __init__(self, remote, local, timeout=None, force_replace=False):
        """
        initiate a Downloader object.

        :param remote: remote link
        :param local: local address
        :param timeout: time out, if None: global setting (30 sec)
        :param force_replace: if the local file exists already, what we do?
        :return: check attribute "is_ok"
        """
        # remote = r"http://some.big.file"
        # local = r"c:\downloads\bigfile.dat"
        self.remote = remote
        self.local = os.path.expanduser(local)

        if os.path.exists(self.local):
            if not force_replace:
                self.is_ok = -1
                return
            pass

        self.block_size = BLOCK_SIZE
        self.timeout = timeout

        self.is_ok = self.open_url()
        pass


    def open_url(self):
        """
        - open the file
        - handle exceptions
        - get information of the HTTPRequest object

        We do not use the urllib.urlretrieve, because we want to handle the
        sophiscated exceptions and timeouts. urllib2.open_url() also provides
        more information about the object by returning the HTTPRequest object.

        NOTE: already called in the constructor.

        :return: True for running through, False for exceptions
        """
        try:
            if self.timeout is None:
                self.url = urllib2.urlopen(self.remote)
            else:
                self.url = urllib2.urlopen(self.remote, None, self.timeout)
                pass

            # exceptions
            #TODO: a logger? If this will be a deamon, probabaly yes.
        except urllib2.HTTPError, e:
            print >> sys.stderr, 'HTTPError: ' + str(e.code)
            return -2
        except urllib2.URLError, e:
            print >> sys.stderr, 'URLError: ' + str(e.reason)
            return -3
        except httplib.HTTPException, e:
            print >> sys.stderr, 'HTTPException'
            return -4
        except KeyboardInterrupt, e:
            print >> sys.stderr, 'User interuption'
            return -5
        except socket.timeout:
            print >> sys.stderr, 'Connection timed out'
            return -6
        except Exception:
            # import traceback as tb
            print >> sys.stderr, 'generic exception: %s %s'% (sys.exc_info()[0], sys.exc_info()[1])
            return -7
            pass

        self.header = self.url.info()
        self.total_size = int(self.header["Content-Length"])
        return 0
        pass


    def save_file(self, silient=False):
        """
        save the file to the location set in the constructor.
        For more usage see class doc string.

        :param silient: True/False
        :return: True for all fine, False for faulty
        """
        if self.is_ok < 0:
            return False

        if not self.total_size:
            return False


        print '%s --> %s'%(self.remote, self.local)
        print "Downloading %s bytes..." % self.total_size,
        count = 0

        with open(self.local, 'wb') as fp:  # so it doesn't cause trouble when KeyboardInterupt etc.
            while True:
                chunk = self.url.read(self.block_size)

                if not chunk: break

                fp.write(chunk)

                count += 1

                if not silient:
                    if self.total_size > 0:
                        percent = int(count * self.block_size * 100 / self.total_size)

                        if percent > 100: percent = 100

                        ui.show_bars(percent)
                        pass

                    pass # silient

                pass # while
            ui.new_bar()
            pass # with


        return True
        pass # def save_file


    def get_error_msg(self):
        status = self.is_ok
        if status == -1:
            return 'file exists already locally'
        elif status == -2:
            return 'HTTPError'
        elif status == -3:
            return 'URLError'
        elif status == -4:
            return 'HTTPException'
        elif status == -5:
            return 'User interuption'
        elif status == -6:
            return 'timeout'
        elif status == -7:
            return 'some unknown reason'
        elif status >= 0:
            return ''

        pass

    pass  #class Downloader


