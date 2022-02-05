'''common setup code for tests'''

import os

import pytest

from pysftp import CnOpts

# pytest-sftpserver plugin information
SFTP_INTERNAL = {'host': 'localhost', 'username': 'user', 'password': 'pw'}
# used if ptest-sftpserver plugin does not support what we are testing
SFTP_LOCAL = {'host': 'localhost', 'username': 'test', 'password': 'test1357'}

# can only reach public, read-only server from CI platform, only test locally
# if environment variable CI is set  to something to disable local tests
# the CI env var is set to true by both drone-io and travis
SKIP_IF_CI = pytest.mark.skipif(os.getenv('CI', '') > '', reason='Not Local')
# try:
#     stars8192 = bytes('*'*8192)
# except TypeError:
STARS8192 = '*'*8192


def conn(sftpsrv):
    """return a dictionary holding argument info for the pysftp client"""
    cnopts = CnOpts()
    cnopts.hostkeys.load('sftpserver.pub')
    return {'host': sftpsrv.host, 'port': sftpsrv.port, 'username': 'user',
            'password': 'pw', 'default_path': '/home/test', 'cnopts': cnopts}

# filesystem served by pytest-sftpserver plugin
VFS = {
    'home': {
        'test': {
            'pub': {
                'make.txt': "content of make.txt",
                'foo1': {
                    'foo1.txt': 'content of foo1.txt',
                    'image01.jpg': 'data for image01.jpg'
                },
                'foo2': {
                    'foo2.txt': 'content of foo2.txt',
                    'bar1': {
                        'bar1.txt': 'contents bar1.txt'
                    }
                }
            },
            'read.me': 'contents of read.me',
        }
    }
}
