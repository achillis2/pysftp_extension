pysftp Exension
================

This package extends pysftp by providing the disabled_algorithms option at connection. It solves the problem in this post https://stackoverflow.com/questions/70812056/pysftp-fails-with-authentication-failed-and-server-did-not-send-a-server-sig.

pysftp is a simple interface to SFTP.  The module offers high level abstractions and
task based routines to handle your SFTP needs.  Checkout the Cook Book, in the
docs, to see what pysftp can do for you.

Example
-------

    import pysftp_extension

    with pysftp_extension.Connection('hostname', username='me', password='secret', disabled_algorithms=dict(pubkeys=["rsa-sha2-512", "rsa-sha2-256"])) as sftp:
        with sftp.cd('public'):             # temporarily chdir to public
            sftp.put('/my/local/filename')  # upload file to public/ on remote
            sftp.get('remote_file')         # get a remote file


Supports
--------
Tested on Python 2.7, 3.2, 3.3, 3.4

.. image:: https://drone.io/bitbucket.org/dundeemt/pysftp/status.png
    :target: https://drone.io/bitbucket.org/dundeemt/pysftp/latest
    :alt: Build Status


* Project:  https://github.com/achillis2/pysftp_extension
* Download: https://github.com/achillis2/pysftp_extension
* Documentation: http://pysftp.rtfd.org/
