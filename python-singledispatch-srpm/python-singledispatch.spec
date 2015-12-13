#
# spec file for package python-singledispatch
#
# Copyright (c) 2015 Nico Kadel-Garcia.
#

%{?scl:%scl_package python-singledispatch}
%{!?scl:%global pkg_name %{name}}

%global srcname singledispatch

Name: %{?scl_prefix}python-singledispatch
Version:        3.4.0.3
Release:        0.1%{?dist}
Url:            http://docs.python.org/3/library/functools.html#functools.singledispatch
Summary:        This library brings functools.singledispatch from Python 3.4 to Python 2.6-3.3.
License:        MIT
Group:          Development/Languages/Python
Source:         https://pypi.python.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
BuildRequires:  %{?scl_prefix}python-six
BuildRequires:  %{?scl_prefix}python(abi)
Requires: %{?scl_prefix}python-six
Requires: %{?scl_prefix}python(abi)
# Avoid python naming confusion
Provides: %{?scl_prefix}python-%{srcname} = %{version}-%{release}

%description
==============
singledispatch
==============

`PEP 443 <http://www.python.org/dev/peps/pep-0443/>`_ proposed to expose
a mechanism in the ``functools`` standard library module in Python 3.4
that provides a simple form of generic programming known as
single-dispatch generic functions.

This library is a backport of this functionality to Python 2.6 - 3.3.

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
%doc README.rst
%{python_sitelib}/*

%changelog
* Mon Nov 16 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 3.4.0.3-0.1
- Build SRPM with py2pack
- Activate python2.7 build and dependenies
