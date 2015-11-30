%{?scl:%scl_package python-mysql-python}
%{!?scl:%global pkg_name %{name}}

%global srcname MySQL-python

Summary: Python interface to MySQL
Name: %{?scl_prefix}python-mysql-python
Version: 1.2.5
Release: 0.1%{?dist}
Source0: https://pypi.python.org/packages/source/a/%{srcname}/%{srcname}-%{version}.zip
License: GPL
Group: Development/Libraries
Prefix: %{_prefix}
Vendor: MySQL-python SourceForge Project
Packager: Andy Dustman <adustman@users.sourceforge.net>
Requires: python
Url: https://github.com/farcepest/MySQLdb1
Distribution: Red Stains Linux
BuildRequires: python-devel mysql-devel zlib-devel openssl-devel
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
Requires: %{?scl_prefix}python(abi)

%description

=========================
Python interface to MySQL
=========================

MySQLdb is an interface to the popular MySQL_ database server for
Python.  The design goals are:

- Compliance with Python database API version 2.0 [PEP-0249]_
- Thread-safety
- Thread-friendliness (threads will not block each other)

MySQL-3.23 through 5.5 and Python-2.4 through 2.7 are currently
supported. Python-3.0 will be supported in a future release.
PyPy is supported.

MySQLdb is `Free Software`_.

.. _MySQL: http://www.mysql.com/
.. _`Free Software`: http://www.gnu.org/
.. [PEP-0249] http://www.python.org/peps/pep-0249.html

%prep
%setup -q -n %{srcname}-%{version}

%build
#env CFLAGS="$RPM_OPT_FLAGS" python setup.py build
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
%{python_sitearch}/*
#%{python_sitelib}/*
%doc GPL-2.0 HISTORY INSTALL README.md
%doc doc/*.rst

%changelog
* Mon Nov 30 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 1.2.5-0.1
- Build SRPM from setup.py
- Hand edit failed .spec file to use .tar.gz and better list of doc files
- Activate python2.7 build and dependenies
