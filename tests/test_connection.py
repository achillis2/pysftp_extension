'''test pysftp.Connection - uses py.test'''
import pytest

from common import VFS, conn, SKIP_IF_CI, SFTP_LOCAL
import pysftp


def test_connection_with(sftpserver):
    '''connect to a public sftp server'''
    with sftpserver.serve_content(VFS):
        with pysftp.Connection(**conn(sftpserver)) as sftp:
            assert sftp.listdir() == ['pub', 'read.me']


def test_connection_bad_host():
    '''attempt connection to a non-existing server'''
    with pytest.raises(pysftp.ConnectionException):
        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None
        sftp = pysftp.Connection(host='',
                                 username='demo',
                                 password='password',
                                 cnopts=cnopts)
        sftp.close()


@SKIP_IF_CI
def test_connection_bad_credentials():
    '''attempt connection to a non-existing server'''
    copts = SFTP_LOCAL.copy()
    copts['password'] = 'badword'
    with pytest.raises(pysftp.SSHException):
        with pysftp.Connection(**copts) as sftp:
            sftp.listdir()


def test_connection_good(sftpserver):
    '''connect to a public sftp server'''
    with sftpserver.serve_content(VFS):
        sftp = pysftp.Connection(**conn(sftpserver))
        sftp.close()
