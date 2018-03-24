# Logs Analysis

Internal reporting tool for a newspaper site.

## Overview

This repository contains Python source code that implements an internal reporting tool for a newspaper site. It is a tool that analysis the logs contained in the database and answers the following questions based on the data from the server:

- What are the most popular three articles of all time?
- Who are the most popular article authors of all time?
- On which days did more than 1% of requests lead to errors?

## Repo Contents

- `analysis.py` contains the actual program that runs on the database.
- `database.py` contains the Database class that is used to connect and query the database.

## Requirements

- [Python interpreter](https://www.python.org/downloads/release/python-364/)
- [`psycopg2` package](http://initd.org/psycopg/docs/install.html#binary-install-from-pypi)
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
- [Vagrant](https://www.vagrantup.com/downloads.html)
- [Virtual machine configuration](https://github.com/udacity/fullstack-nanodegree-vm)
- [SQL database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

## Steps to get started

1. Install VirtualBox
2. Install Vagrant
3. Download the VM configuration and unzip it. You will get a directory called `FSND-Virtual-Machine`. Open up a terminal window and navigate to that folder like this:

    ```bash
    $ cd /path/to/unzipped/configuration/file/FSND-Virtual-Machine/
    $ ls
    README.md       vagrant
    $ cd /vagrant
    $ ls
    Vagrantfile     catalog     forum       pg_config.sh        tournament
    ```

    If you see the above output, then so far so good.

4. Now run the following:

    ```bash
    vagrant up
    ```

    This might take a long while, so hang tight!

5. Once the VM is done downloading and installing, run:

    ```bash
    vagrant ssh
    cd /vagrant
    ls
    ```

    You should see that the contents of this directory are the same as the `vagrant` subdirectory in `FSND-Virtual-Machine`.

6. At this point, check if `Python 3` is installed by running:

    ```bash
    python3 --version
    ```

    If it's not installed, then install it first before proceeding to the next step.

7. Now unzip the `newsdata.zip` file and place the `newsdata.sql` file in the shared `vagrant` directory. Now run the following:

    ```bash
    psql -d news -f newsdata.sql
    ```

    This connects psql to the `news` database and runs the SQL commands from `newsdata.sql` file within that database.

8. Inside the psql program, you can now run `\dt` to view the tables for the `news` database. There should be tables called `articles`, `authors` and `log`. If they're not there, then you may have to redo some of the above steps.
9. Now copy the contents of this repository into the `/vagrant` directory, navigate to it and run the program like this:
    ```bash
    cd /vagrant/logs-analysis
    python3 analysis.py
    ```

    You should see the output of the same form as that in the `log-output.txt` file of this repository.

### Contributors

The database and the VM configuration file was provided by [Udacity](https://github.com/udacity) and the rest of the development has been done by [Mohit Sakhuja](https://github.com/mohitsakhuja).
