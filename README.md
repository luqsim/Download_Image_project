# DownloadImage

Convenient downloader of files from internet.

# Intro

Given a plaintext file with listed links, the script will download the files under the links after filtering. Filter can be specified as regular expression. 

# Installation

run:
	python setup.py install at the root of the project.

Using VirtualEnv or VirtualEnvWrapper is recommended. Find them here: https://virtualenv.pypa.io/en/latest/ or https://virtualenvwrapper.readthedocs.org


# test

The setup.py installs nosetest automatically. To test the code use:

	nosetests

# Usage:

A test file with links has been prepared as data/test_links.txt
After installation, just call:

	download_from_file.py -d data -p prefix_ -s _suffix data/test_links.txt

Without installation, type the following under project root:

	python bin/download_from_file.py -d data -p prefix_ -s _suffix data/test_links.txt

More options can be found with command:

	download_from_file.py -h

# License:
GPL license, for more details see LICENSE.



