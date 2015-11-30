%{?scl:%scl_package python-jaydebeapi}
%{!?scl:%global pkg_name %{name}}

%global srcname JayDeBeApi

Summary: Use JDBC database drivers from Python 2/3 or Jython with a DB-API.
Name: %{?scl_prefix}python-jaydebeapi
Version: 0.2.0
Release: 0.1%{?dist}
Source0: https://pypi.python.org/packages/source/j/%{srcname}/%{srcname}-%{version}.tar.gz
License: GNU LGPL
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Bastian Bowe <bastian.dev@gmail.com>
Url: https://github.com/baztian/jaydebeapi
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
Requires: %{?scl_prefix}python(abi)

%description
=================================================================
 JayDeBeApi - bridge from JDBC database drivers to Python DB-API
=================================================================

The JayDeBeApi module allows you to connect from Python code to
databases using Java `JDBC
<http://java.sun.com/products/jdbc/overview.html>`_. It provides a
Python DB-API_ v2.0 to that database.

It works on ordinary Python (cPython) using the JPype_ Java
integration or on `Jython <http://www.jython.org/>`_ to make use of
the Java JDBC driver.

In contrast to zxJDBC from the Jython project JayDeBeApi let's you
access a database with Jython AND Python with only minor code
modifications. JayDeBeApi's future goal is to provide a unique and
fast interface to different types of JDBC-Drivers through a flexible
plug-in mechanism.

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
%doc COPYING COPYING.LESSER README_development.rst README.rst
#%doc build/*

%changelog
* Mon Nov 30 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 0.2.0-0.1
- Provide full URL for source
- Activate python2.7 build and dependenies
