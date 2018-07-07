pgbackup
========

CLI for backing up remote PostgreSQL databases locally or to AWS s3.

Preparing for Development
-------------------------

1. ensure ``pip`` amnd ``pipenv`` are installed
2. clone repository ``git clone: git@github.com/pgbakup``
3. Fetch developement dependencies:  ``make install``

Usage
----

Pass in a full database URL, the storage driver, and detination

S3 Example w/ bucket name

::

    $ pgbackup postgres://bob@example.com:5432/db_one --driver s3 backups

local  Example w/ local path

::

    $ pgbackup postgres://bob@example.com:5432/db_one --driver local /var/lib/.....

Running Tests
-------------

Run tests locally using ``make`` if virtenv is active:

::

    $ make

If virtenv is not active then use:

::

    $ pipenv run make 
