%{?scl:%scl_package python-pyhs2}
%{!?scl:%global pkg_name %{name}}

%global srcname pyhs2

Summary: Python Hive Server 2 Client Driver
Name: %{?scl_prefix}python-pyhs2
Version: 0.6.0
Release: 0.2%?{dist}
Source0: https://pypi.python.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
License: Apache
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Brad Ruderman <bradruderman@gmail.com>
Url: https://github.com/BradRuderman/pyhs2
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
Requires: %{?scl_prefix}python(abi)
Requires: %{?scl_prefix}python-sasl

%description
===========
pyhs2
===========

pyHS2 is a python client driver for connecting to hive server 2.

See example.py for an example of how to use it.

Please log all issues/new feature requests under the issues tab and I will respond ASAP.

Contact @bradruderman or bradruderman@gmail.com with questions.

Enjoy

![alt tag](https://rs.gwallet.com/r1/pixel/x11399)


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
#%attr(755,root,root) %{_bindir}/*
%{python_sitelib}/*
%doc README.md

%changelog
* Fri Nov 20 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 1.6.0-0.4
- Build initial RPM from setup.py
- Activate python2.7 build and dependenies
- Add python(abi) dependency
