%{?scl:%scl_package python-pymssql}
%{!?scl:%global pkg_name %{name}}

%global srcname pymssql

Summary: DB-API interface to Microsoft SQL Server for Python. (new Cython-based version)
Name: %{?scl_prefix}python-pymssql
Version: 2.1.1
Release: 0.1%{?dist}
Source0: https://pypi.python.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
License: LGPL
Group: Development/Libraries
Prefix: %{_prefix}
Vendor: pymssql Google Group <pymssql@googlegroups.com>
Url: http://pymssql.org
BuildRequires:  freetds-devel
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
Requires: %{?scl_prefix}python(abi)
# Avoid python naming confusion
Provides: %{?scl_prefix}python-%{srcname} = %{version}-%{release}

%description

pymssql - DB-API interface to Microsoft SQL Server
==================================================

A simple database interface for `Python`_ that builds on top of `FreeTDS`_ to
provide a Python DB-API (`PEP-249`_) interface to `Microsoft SQL Server`_.

.. _Microsoft SQL Server: http://www.microsoft.com/sqlserver/
.. _Python: http://www.python.org/
.. _PEP-249: http://www.python.org/dev/peps/pep-0249/
.. _FreeTDS: http://www.freetds.org/

Version 2.1.0 - 2014-02-25 - `Marc Abramowitz <http://marc-abramowitz.com/>`_
=============================================================================

Features
--------

- Sphinx-based documentation (GH-149)

  Read it online at http://pymssql.org/

  Thanks, Ramiro Morales!

  See:

%prep
%setup -n %{srcname}-%{version}

%build
export CFLAGS="$RPM_OPT_FLAGS"
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
%doc ChangeLog ChangeLog_highlights.rst LICENSE README_building_and_developing.rst README.rst
#%doc build/*

%changelog
* Mon Nov 24 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 2.1.1-0.1
- Build SRPM from setup.py
- Activate python2.7 build and dependenies
