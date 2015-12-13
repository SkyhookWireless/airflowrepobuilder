%{?scl:%scl_package python-airflow16}
%{!?scl:%global pkg_name %{name}}

%global srcname airflow

Summary: Programmatically author, schedule and monitor data pipelines
Name: %{?scl_prefix}python-airflow16
Version: 1.6.1
Release: 0.9%{?dist}
Source0: https://pypi.python.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
Patch1: airflow-1.6.1-oracle.patch
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
# Avoid python naming confusion
Provides: %{?scl_prefix}python-%{srcname} = %{version}-%{release}

# Manually added from setup.py
Requires:  %{?scl_prefix}python-alembic >= 0.8.3
Requires:  %{?scl_prefix}python-alembic < 0.9
# python27-python has strange argparse Provides, set local argparse
#Requires:  %{?scl_prefix}python-argparse
Requires:  %{?scl_prefix}python-argparse == 1.2.1
# Update from 2.36.0, roll back if needed
#Requires:  %{?scl_prefix}python-boto = 2.36.0
Requires:  %{?scl_prefix}python-boto >= 2.36.0
Requires:  %{?scl_prefix}python-celery >= 3.1.17
Requires:  %{?scl_prefix}python-chartkick >= 0.4.2
Requires:  %{?scl_prefix}python-chartkick < 0.5
Requires:  %{?scl_prefix}python-croniter >= 0.3.8
Requires:  %{?scl_prefix}python-croniter < 0.4
Requires:  %{?scl_prefix}python-coverage
Requires:  %{?scl_prefix}python-coveralls
Requires:  %{?scl_prefix}python-cryptography
# Disabled and patched out of devel submodule
# cx_Oracle requires local Oracle to build
#Requires:  %{?scl_prefix}python-cx_oracle >= 5.1.2
Requires:  %{?scl_prefix}python-dateutil >= 2.3
Requires:  %{?scl_prefix}python-dateutil < 3
Requires:  %{?scl_prefix}python-dill >= 0.2.2
Requires:  %{?scl_prefix}python-dill < 0.3
Requires:  %{?scl_prefix}python-eventlet > 0.9.7
Requires:  %{?scl_prefix}python-filechunkio >= 1.6
Requires:  %{?scl_prefix}python-flake8
Requires:  %{?scl_prefix}python-flask >= 0.10.1
Requires:  %{?scl_prefix}python-flask < 0.11
Requires:  %{?scl_prefix}python-flask-admin >= 1.2.0
Requires:  %{?scl_prefix}python-flask-cache < 014
Requires:  %{?scl_prefix}python-flask-cache >= 0.13.1
# Ensure specific RPM version
#Requires:  %{?scl_prefix}python-flask-login >= 0.2.11
#Requires:  %{?scl_prefix}python-flask-login < 0.2.12
Requires:  %{?scl_prefix}python-flask-login == 0.2.11
Requires:  %{?scl_prefix}python-flower >= 0.7.3
Requires:  %{?scl_prefix}python-future < 0.16
Requires:  %{?scl_prefix}python-future >= 0.15.0
Requires:  %{?scl_prefix}python-gevent >= 0.13
Requires:  %{?scl_prefix}python-gunicorn < 20.0
Requires:  %{?scl_prefix}python-gunicorn >= 19.3.0
Requires:  %{?scl_prefix}python-hive-thrift-py >= 0.0.1
# Hiddependency not in requires.txt
Requires:  %{?scl_prefix}python-itsdangerous
Requires:  %{?scl_prefix}python-jaydebeapi >= 0.2.0
Requires:  %{?scl_prefix}python-jinja2 < 3.0
Requires:  %{?scl_prefix}python-jinja2 >= 2.7.3
Requires:  %{?scl_prefix}python-ldap3 >= 0.9.9.1
Requires:  %{?scl_prefix}python-librabbitmq >= 1.6.1
# Hidden dependency not in requies.txt
Requires:  %{?scl_prefix}python-mako
Requires:  %{?scl_prefix}python-markdown < 3.0
Requires:  %{?scl_prefix}python-markdown >= 2.5.2
Requires:  %{?scl_prefix}python-mysqlclient >= 1.3.6
Requires:  %{?scl_prefix}python-nose
Requires:  %{?scl_prefix}python-pandas < 1.0.0
Requires:  %{?scl_prefix}python-pandas >= 0.15.2
Requires:  %{?scl_prefix}python-psycopg2 >= 2.6
Requires:  %{?scl_prefix}python-pydruid >= 0.2.1
Requires:  %{?scl_prefix}python-pygments < 3.0
Requires:  %{?scl_prefix}python-pygments >= 2.0.1
Requires:  %{?scl_prefix}python-pyhive >= 0.1.3
Requires:  %{?scl_prefix}python-pyhs2 >= 0.6.0
Requires:  %{?scl_prefix}python-pykerberos >= 1.1.0
Requires:  %{?scl_prefix}python-pymssql >= 2.1.1
Requires:  %{?scl_prefix}python-pysmbclient >= 0.1.3
Requires:  %{?scl_prefix}python-requests >= 2.5.1
Requires:  %{?scl_prefix}python-requests < 3
# Included in base python package
#Requires:  %{?scl_prefix}python-setproctitle >= 1.1.8
#Requires:  %{?scl_prefix}python-setproctitle < 2
Requires:  %{?scl_prefix}python-flask-wtf
Requires:  %{?scl_prefix}python-ldap3
Requires:  %{?scl_prefix}python-mysqlclient
Requires:  %{?scl_prefix}python-slackclient >= 0.14
Requires:  %{?scl_prefix}python-snakebite >= 2.4.13
Requires:  %{?scl_prefix}python-sphinx >= 1.2.3
Requires:  %{?scl_prefix}python-sphinx-argparse >= 0.1.13
Requires:  %{?scl_prefix}python-sphinx-pypi-upload
Requires:  %{?scl_prefix}python-sphinx_rtd_theme >= 0.1.6
Requires:  %{?scl_prefix}python-sqlalchemy >= 0.9.0
Requires:  %{?scl_prefix}python-statsd < 4.0
Requires:  %{?scl_prefix}python-statsd >= 3.0.1
Requires:  %{?scl_prefix}python-thrift < 0.10
Requires:  %{?scl_prefix}python-thrift >= 0.9.2
Requires:  %{?scl_prefix}python-unicodecsv >= 0.13.0
Requires:  %{?scl_prefix}python-vertica-python >= 0.5.1

# Added because pip installation generates the module
Requires:  %{?scl_prefix}python-python-editor

# Manually added to ease installation
Provides: airflow

# Added for authentication modules
Requires: cyrus-sasl-gssapi
Requires: cyrus-sasl-plain

# Avoid conflicting with airflow15
Conflicts: %{?scl_prefix}python-airflow
Conflicts: %{?scl_prefix}python-airflow15

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
%patch1 -p1 -b .oracle

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
* Tue Dec  8 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 1.6.1-0.8
- Make python-sphinx-argparse, python-python-editor, python-argparse, and
  python-flask-login more specific
- Change python-python-dateutil back to python-dateutil

* Sun Dec  6 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 1.6.1-0.7
- Add hidden dependencies on python-mako,  pythion-itsdangerous,
  and more python-flask-login = 0.2.11

* Mon Nov 30 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 1.6.1-0.5
- Update to 1.6.1
- List all dependencies from requires.txt
- Disable cx_Oracle dependency, too difficult to use

* Sat Nov 28 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 1.6.1-0.1
- Update to 1.1.6
- List all dependencies from requires.txt

* Mon Nov 23 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 1.5.1-0.4
- Activate python-thrift dependency
- Add python(abi) dependency

* Fri Nov 20 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 1.5.1-0.4
- Introduce python-pyhs2 dependency

* Mon Nov 16 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 1.5.1-0.3
- Roll back to 1.5.1 for compatibility reasons

* Fri Nov 13 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 1.5.2-0.2
- Reset dependencies for python-thrift, which is on

* Mon Nov  9 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 1.5.2-0.1
- Activate python2.7 build and dependenies
