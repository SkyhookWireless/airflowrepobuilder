#
# spec file for package python-mysqlclient
#
# Copyright (c) 2015 Nico Kadel-Garcia.
#

%{?scl:%scl_package python-mysqlclient}
%{!?scl:%global pkg_name %{name}}

%global srcname mysqlclient

Name: %{?scl_prefix}python-mysqlclient
Version:        1.3.7
Release:        0.2%{?dist}
Url:            https://github.com/PyMySQL/mysqlclient-python
Summary:        Python interface to MySQL
License:        GPLv2
Group:          Development/Languages/Python
Source:         https://pypi.python.org/packages/source/m/mysqlclient/mysqlclient-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# Provides mysql_config
BuildRequires:  mysql
# Provides mysql libraries
BuildRequires:  mysql-devel
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
Requires: %{?scl_prefix}python(abi)
# Similar but incompatible package
Conflicts: %{?scl_prefix}python-mysql-python

%description
=========================
Python interface to MySQL
=========================

mysqlclient is a fork of MySQL-python. It adds Python 3.3~ support
and merges some pull requests.

MySQLdb is an interface to the popular MySQL_ database server for
Python. The design goals are:

- Compliance with Python database API version 2.0 [PEP-0249]_
- Thread-safety
- Thread-friendliness (threads will not block each other)

MySQL-4.1 through 5.5 and Python-2.7, 3.3-3.5 are currently
supported. PyPy is supported.

MySQLdb is `Free Software`_.

.. _MySQL: http://www.mysql.com/
.. _`Free Software`: http://www.gnu.org/
.. [PEP-0249] https://www.python.org/dev/peps/pep-0249/

%prep
%setup -q -n %{srcname}-%{version}

%build
export CFLAGS="%{optflags}"
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
%doc GPL-2.0 HISTORY INSTALL README.md
%{python_sitearch}/*
#%{python_sitelib}/*

%changelog
* Mon Nov 30 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 1.3.7-0.1
- Build from py2pack
- Activate python2.7 build and dependenies
- Add Conflicts for python-mysql-python
