%{?scl:%scl_package python-airflow}
%{!?scl:%global pkg_name %{name}}

%global srcname airflow

Summary: Programmatically author, schedule and monitor data pipelines
Name: %{?scl_prefix}python-airflow
Version: 1.5.1
Release: 0.10%{?dist}
Source0: https://pypi.python.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
License: Apache
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{srcname}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Maxime Beauchemin <maximebeauchemin@gmail.com>
Url: https://github.com/airbnb/airflow
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
Requires: %{?scl_prefix}python(abi)

# Manually added from setup.py
Requires:  %{?scl_prefix}python-alembic >= 0.8.0
Requires:  %{?scl_prefix}python-alembic < 0.9
# python27-python has strange argparse Provides, set local argparse
#Requires:  %{?scl_prefix}python-argparse
Requires:  %{?scl_prefix}python-argparse == 1.2.1
Requires:  %{?scl_prefix}python-boto
Requires:  %{?scl_prefix}python-celery >= 3.1.17
Requires:  %{?scl_prefix}python-chartkick >= 0.4.2
Requires:  %{?scl_prefix}python-chartkick < 0.5
Requires:  %{?scl_prefix}python-dateutil >= 2.3
Requires:  %{?scl_prefix}python-dateutil < 3
Requires:  %{?scl_prefix}python-dill >= 0.2.2
Requires:  %{?scl_prefix}python-dill < 0.3
Requires:  %{?scl_prefix}python-flask >= 0.10.1
Requires:  %{?scl_prefix}python-flask < 0.11
Requires:  %{?scl_prefix}python-flask-admin == 1.2.0
Requires:  %{?scl_prefix}python-flask-cache >= 0.13.1
Requires:  %{?scl_prefix}python-flask-cache < 0.14
# Ensure specific RPM version
#Requires:  %{?scl_prefix}python-flask-login >= 0.2.11
#Requires:  %{?scl_prefix}python-flask-login < 0.2.12
Requires:  %{?scl_prefix}python-flask-login == 0.2.11
Requires:  %{?scl_prefix}python-flower >= 0.7.3
Requires:  %{?scl_prefix}python-future >= 0.15.0
Requires:  %{?scl_prefix}python-future < 0.16
Requires:  %{?scl_prefix}python-gunicorn >= 19.3.0
Requires:  %{?scl_prefix}python-gunicorn < 20.0
Requires:  %{?scl_prefix}python-jinja2 >= 2.7.3
Requires:  %{?scl_prefix}python-jinja2 < 3.0
Requires:  %{?scl_prefix}python-markdown >= 2.5.2
Requires:  %{?scl_prefix}python-markdown < 3.0
Requires:  %{?scl_prefix}python-pandas >= 0.15.2
Requires:  %{?scl_prefix}python-pandas < 1.0.0
Requires:  %{?scl_prefix}python-pygments >= 2.0.1
Requires:  %{?scl_prefix}python-pygments < 3.0
Requires:  %{?scl_prefix}python-requests >= 2.5.1
Requires:  %{?scl_prefix}python-requests < 3
# Included in base python package
#Requires:  %{?scl_prefix}python-setproctitle >= 1.1.8
#Requires:  %{?scl_prefix}python-setproctitle < 2
Requires:  %{?scl_prefix}python-sqlalchemy >= 0.9.8
Requires:  %{?scl_prefix}python-statsd >= 3.0.1
Requires:  %{?scl_prefix}python-thrift >= 0.9.2
Requires:  %{?scl_prefix}python-thrift < 0.10
# From [all] stanza
Requires:  %{?scl_prefix}python-boto >= 2.36.0
Requires:  %{?scl_prefix}python-cryptography >= 0.9.3
Requires:  %{?scl_prefix}python-hive-thrift-py >= 0.0.1
Requires:  %{?scl_prefix}python-librabbitmq >= 1.6.1
Requires:  %{?scl_prefix}python-nose
Requires:  %{?scl_prefix}python-psycopg2 >= 2.6
Requires:  %{?scl_prefix}python-pyhive >= 0.1.2
Requires:  %{?scl_prefix}python-pyhs2 >= 0.6.0
Requires:  %{?scl_prefix}python-pymssql >= 2.1.1
Requires:  %{?scl_prefix}python-pysmbclient >= 0.1.3
Requires:  %{?scl_prefix}python-slackclient >= 0.15
Requires:  %{?scl_prefix}python-sphinx >= 1.2.3
Requires:  %{?scl_prefix}python-sphinx-argparse >= 0.1.13
Requires:  %{?scl_prefix}python-sphinx-pypi-upload >= 0.2.1
Requires:  %{?scl_prefix}python-sphinx_rtd_theme >= 0.1.6
Requires:  %{?scl_prefix}python-unicodecsv >= 0.13.0
# Added from requirements.txt for [alldbs]
Requires:  %{?scl_prefix}python-psycopg2 >= 2.6
Requires:  %{?scl_prefix}python-mysql-python >= 1.2.5
Requires:  %{?scl_prefix}python-hive-thrift-py >= 0.0.1
Requires:  %{?scl_prefix}python-pyhive >= 0.1.3
Requires:  %{?scl_prefix}python-pyhs2 >= 0.6.0
Requires:  %{?scl_prefix}python-pymssql >= 2.1.1
Requires:  %{?scl_prefix}python-unicodecsv >= 0.13.0
Requires:  %{?scl_prefix}python-snakebite >= 2.4.13
# Added from requirements.txt for [crypto]
Requires:  %{?scl_prefix}python-cryptography >= 0.9.3
# Added from requirements.txt for [development]
Requires:  %{?scl_prefix}python-sphinx-pypi-upload >= 0.2.1
Requires:  %{?scl_prefix}python-boto >= 2.36.0
Requires:  %{?scl_prefix}python-cryptography >= 0.9.3
Requires:  %{?scl_prefix}python-hive-thrift-py >= 0.0.1
Requires:  %{?scl_prefix}python-mysql-python >= 1.2.5
Requires:  %{?scl_prefix}python-nose
Requires:  %{?scl_prefix}python-psycopg2 >= 2.6
Requires:  %{?scl_prefix}python-pyhive >= 0.1.3
Requires:  %{?scl_prefix}python-pyhs2 >= 0.6.0
Requires:  %{?scl_prefix}python-pymssql >= 2.1.1
Requires:  %{?scl_prefix}python-pysmbclient >= 0.1.3
Requires:  %{?scl_prefix}python-slackclient >= 0.15
Requires:  %{?scl_prefix}python-snakebite >= 2.4.13
Requires:  %{?scl_prefix}python-sphinx-argparse >= 0.1.13
Requires:  %{?scl_prefix}python-sphinx_rtd_theme >= 0.1.6
Requires:  %{?scl_prefix}python-sphinx >= 1.2.3
Requires:  %{?scl_prefix}python-unicodecsv >= 0.13.0
# Added from requirements.txt for [doc]
Requires:  %{?scl_prefix}python-sphinx >= 1.2.3
Requires:  %{?scl_prefix}python-sphinx-argparse >= 0.1.13
Requires:  %{?scl_prefix}python-sphinx_rtd_theme >= 0.1.6
Requires:  %{?scl_prefix}python-sphinx-pypi-upload >= 0.2.1

# Added from requirements.txt for [druid]
Requires:  %{?scl_prefix}python-pydruid >= 0.2.1

# Added from requirements.txt for [hdfs]
Requires:  %{?scl_prefix}python-snakebite >= 2.4.13

# Added from requirements.txt for [hive]
Requires:  %{?scl_prefix}python-hive-thrift-py >= 0.0.1
Requires:  %{?scl_prefix}python-pyhive >= 0.1.3
Requires:  %{?scl_prefix}python-pyhs2 >= 0.6.0

# Added from requirements.txt for [jdbc]
Requires:  %{?scl_prefix}python-jaydebeapi >= 0.2.0

# Added from requirements.txt for [mssql]
Requires:  %{?scl_prefix}python-pymssql >= 2.1.1
Requires:  %{?scl_prefix}python-unicodecsv >= 0.13.0

# Added from requirements.txt for [mysql-python]
Requires:  %{?scl_prefix}python-mysql-python >= 1.2.5

# Added from requirements.txt for [postgres]
Requires:  %{?scl_prefix}python-psycopg2 >= 2.6

# Added from requirements.txt for [s3]
Requires:  %{?scl_prefix}python-boto >= 2.36.0

# Added from requirements.txt for [samba]
Requires:  %{?scl_prefix}python-pysmbclient >= 0.1.3

# Added from requirements.txt for [slack]
Requires:  %{?scl_prefix}python-slackclient >= 0.15

# Added because pip installation generates the module
Requires:  %{?scl_prefix}python-python-editor

# Added for authentication modules
Requires: cyrus-sasl-gssapi
Requires: cyrus-sasl-plain
# Manually added to ease installation
Provides: airflow
%description
Airflow is a platform to programmatically author, schedule and monitor workflows.

When workflows are defined as code, they become more maintainable,
versionable, testable, and collaborative.

Use airflow to author workflows as directed acyclic graphs (DAGs) of
tasks. The airflow scheduler executes your tasks on an array of
workers while following the specified dependencies. Rich command line
utilities make performing complex surgeries on DAGs a snap. The rich
user interface makes it easy to visualize pipelines running in
production, monitor progress, and troubleshoot issues when needed.

%prep
%setup -q -n %{srcname}-%{version}

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
%attr(755,root,root) %{_bindir}/*
%{python_sitelib}/*
# Currently no documentaiton
#%doc CHANGES LICENSE README.rst README.unittests.rst
#%doc build/*

%changelog
* Tue Dec  8 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 1.5.1-0.9
- Make python-sphinx-argparse, python-python-editor, python-argparse, and
  python-flask-login more specific
- Change python-python-dateutil back to python-dateutil

* Sun Dec  6 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 1.5.1-0.8
- Add more specific python-flask-login dependency

* Mon Nov 30 2015 Nico Kadel-Garcia <nkadel@skyhookwireless.com> - 1.5.1-0.6
- Activate dependencies for many more submodules

* Mon Nov 23 2015 Nico Kadel-Garcia <nkadel@skyhookwireless.com> - 1.5.1-0.6
- Activate python-thrift dependency
- Add cyrus-sasl-gssapi and cyrus-sasl-plain dependencies
- Add python(abi) dependency

* Fri Nov 20 2015 Nico Kadel-Garcia <nkadel@skyhookwireless.com> - 1.5.1-0.4
- Introduce python-pyhs2 dependency

* Mon Nov 16 2015 Nico Kadel-Garcia <nkadel@skyhookwireless.com> - 1.5.1-0.3
- Roll back to 1.5.1 for compatibility reasons

* Fri Nov 13 2015 Nico Kadel-Garcia <nkadel@skyhookwireless.com> - 1.5.2-0.2
- Reset dependencies for python-thrift, which is on

* Mon Nov  9 2015 Nico Kadel-Garcia <nkadel@skyhookwireless.com> - 1.5.2-0.1
- Activate python2.7 build and dependenies
