#! /usr/bin/env python
"""
Created on Aug 16, 2014
@author: Qianhao Lu

Take plaintext file as input, download the images listed in the file.
The links must be separated by '\n'.

Usage example:
>bin/download_from_file.py -d data -s _sufix -p prefix_ data/test_links.txt

TODO: maybe multiple parallel processes?
"""
import argparse
import os.path
import sys
import re
import DownloadImage.network as nt

__author__ = 'Qianhao Lu <luqsim@gmail.com>'
__date__ = '16/08/15'

def main(filename, out_dir, filter, prefix, suffix, bln_print_sum):
    if not os.path.exists(filename):
        print >> sys.stderr, 'File not exists.'
        sys.exit(-1)
        pass

    if not os.path.exists(out_dir):
        print >> sys.stderr, 'Output directory dose not exist.'
        sys.exit(-2)
        pass

    if filter is not None:
        pc = re.compile(filter)
    else:
        pc = None
        pass

    lst_summary = []  # not using dictionary for duplicates
    with open(filename, 'rU') as f:
        for line in f:
            remote = line.strip().strip('\n')
            if len(remote) == 0:
                continue
                pass

            if pc is not None:
                if pc.search(line) is None:
                    continue
                    pass
                pass

            fn_output_base = remote.split('/')[-1]
            fn_output_base_main, fn_output_base_ext = os.path.splitext(fn_output_base)

            fn_out = os.path.join(out_dir, '%s%s%s%s'%(prefix, fn_output_base_main, suffix, fn_output_base_ext))

            dl = nt.Downloader(remote, fn_out)
            print dl.get_error_msg()
            if dl.is_ok<0:

                lst_summary.append((remote, 'not OK', dl.get_error_msg()))
            else:
                dl.save_file()
                lst_summary.append((remote, 'OK', '__succeed__'))  #'__' for sorting to the first place
                pass

            pass #for line
        pass # with

    # print summary
    if bln_print_sum:
        lst_summary.sort(key=lambda x: x[1])
        print
        print 'Summary:'
        print '=' * 30
        for i in lst_summary:
            print '-' * 30
            print '%s:\n%s\n%s'%(i)
            pass
        pass

    pass # def main

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('links_file', help='file with links')
    parser.add_argument('--dir', '-d', type=str, default='.', help='output directory')
    parser.add_argument('--filter', '-f', type=str, help='regex filter')
    parser.add_argument('--suffix', '-s', type=str, default='', help='suffix to the local file name')
    parser.add_argument('--prefix', '-p', type=str, default='', help='prefix to the local file name')
    parser.add_argument('--no_summary', '-n', action='store_false', default=True, help='set to suppress printing summary')

    args = parser.parse_args()

    fn = args.links_file
    out_dir = args.dir
    filter = args.filter
    prefix = args.prefix
    suffix = args.suffix
    bln_print_sum = args.no_summary

    main(fn, out_dir, filter, prefix, suffix, bln_print_sum)

    pass