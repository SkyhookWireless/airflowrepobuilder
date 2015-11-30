%{?scl:%scl_package python-pyhive}
%{!?scl:%global pkg_name %{name}}

%define srcname PyHive

Summary: Python interface to Hive
Name: %{?scl_prefix}python-pyhive
Version: 0.1.6
Release: 0.1%{?dist}
Source0: https://pypi.python.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
License: Apache License, Version 2.0
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Jing Wang <jing@dropbox.com>
Url: https://github.com/dropbox/PyHive
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
Requires: %{?scl_prefix}python(abi)

%description
======
PyHive
======

PyHive is a collection of Python `DB-API <http://www.python.org/dev/peps/pep-0249/>`_ and
`SQLAlchemy <http://www.sqlalchemy.org/>`_ interfaces for `Presto <http://prestodb.io/>`_ and
`Hive <http://hive.apache.org/>`_.

Usage
=====

DB-API
------
.. code-block:: python

    from pyhive import presto
    cursor = presto.connect('localhost').cursor()
    cursor.execute('SELECT * FROM my_awesome_data LIMIT 10')
    print cursor.fetchone()
    print cursor.fetchall()

SQLAlchemy
----------
First install this package to register it with SQLAlchemy (see ``setup.py``).

.. code-block:: python

    from sqlalchemy import *
    from sqlalchemy.engine import create_engine
    from sqlalchemy.schema import *
    engine = create_engine('presto://localhost:8080/hive/default')
    logs = Table('my_awesome_data', MetaData(bind=engine), autoload=True)
    print select([func.count('*')], from_obj=logs).scalar()

Note: query generation functionality is not exhaustive or fully tested, but there should be no
problem with raw SQL.

Requirements
============

Install using ``pip install pyhive[hive,presto]``.

- Python 2.7
- For Presto: Presto install
- For Hive: `HiveServer2 <https://cwiki.apache.org/confluence/display/Hive/Setting+up+HiveServer2>`_ daemon

There's also a `third party Conda package <https://binstar.org/blaze/pyhive>`_.

Testing
=======
.. image:: https://travis-ci.org/dropbox/PyHive.svg
    :target: https://travis-ci.org/dropbox/PyHive
.. image:: http://codecov.io/github/dropbox/PyHive/coverage.svg?branch=master
    :target: http://codecov.io/github/dropbox/PyHive?branch=master

Run the following in an environment with Hive/Presto::

    ./scripts/make_test_tables.sh
    virtualenv --no-site-packages env
    source env/bin/activate
    pip install -e .
    pip install -r dev_requirements.txt
    py.test

WARNING: This drops/creates tables named ``one_row``, ``one_row_complex``, and ``many_rows``, plus a
database called ``pyhive_test_database``.


%prep
%setup -n %{srcname}-%{version}

%build
%{?scl:scl enable %{scl} "}
%{__python} setup.py build
%{?scl:"}

%install
%{__rm} -rf %{buildroot}
%{?scl:scl enable %{scl} "}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
%{?scl:"}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
#%attr(755,root,root) %{_bindir}/*
%{python_sitelib}/*
%doc README.rst
#%doc build/*

%changelog
* Mon Nov 30 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 0.1.6-0.1
- Build SRPM from setup.py
- Activate python2.7 build and dependenies
