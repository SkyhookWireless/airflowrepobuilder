#
# spec file for package python-ipaddress
#
# Copyright (c) 2015 Nico Kadel-Garcia.
#

%{?scl:%scl_package python-ipaddress}
%{!?scl:%global pkg_name %{name}}

%global srcname ipaddress

Name: %{?scl_prefix}python-ipaddress
Version:        1.0.15
Release:        0.1%{?dist}
Url:            https://github.com/phihag/ipaddress
Summary:        IPv4/IPv6 manipulation library
License:        Python-2.0
Group:          Development/Languages/Python
Source:         https://pypi.python.org/packages/source/i/%{srcname}/%{srcname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
BuildRequires:  %{?scl_prefix}python(abi)
Requires: %{?scl_prefix}python(abi)
# Avoid python naming confusion
Provides: %{?scl_prefix}python-%{srcname} = %{version}-%{release}

%description
Port of the 3.3+ ipaddress module to 2.6, 2.7, 3.2

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
%doc README.md README
%{python_sitelib}/*

%changelog
* Sat Dec  5 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 1.0.15-0.2
- Use srcname consistently for python-ipaddress

* Mon Nov 16 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 1.0.15-0.1
- Build SRPM with py2pack
- Activate python2.7 build and dependenies
