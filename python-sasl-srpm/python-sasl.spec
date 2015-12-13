%{?scl:%scl_package python-sasl}
%{!?scl:%global pkg_name %{name}}

%global srcname sasl

Summary: Cyrus-SASL bindings for Python
Name: %{?scl_prefix}python-sasl
Version: 0.1.3
Release: 0.2%{?dist}
Source0: https://pypi.python.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
Requires: %{?scl_prefix}python(abi)
# Avoid python naming confusion
Provides: %{?scl_prefix}python-%{srcname} = %{version}-%{release}

License: Apache
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Todd Lipcon <todd@cloudera.com>
Url: https://github.com/toddlipcon/python-sasl/tree/master
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Added manually for full SASL capability
BuildRequires: cyrus-sasl-devel
Requires: cyrus-sasl-lib
Requires: cyrus-sasl-plain
Requires: cyrus-sasl-gssapi

%description
===========
sasl
===========

Required for python-pyhs2

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
%{python_sitearch}/*
#%{python_sitelib}/*
# Currently has no documentation!
#%doc LICENSE.txt

%changelog
* Fri Nov 20 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 0.1.3-0.4
- Build initial RPM from setup.py
- Activate python2.7 build and dependenies
- Add suite of cyrus-sasl libraries for full capability
- Add python(abi) dependency
