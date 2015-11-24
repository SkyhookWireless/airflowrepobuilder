%{?scl:%scl_package python-snowballstemmer}
%{!?scl:%global pkg_name %{name}}

%global srcname snowballstemmer

Summary: This package provides 16 stemmer algorithms (15 + Poerter English stemmer) generated from Snowball algorithms.
Name: %{?scl_prefix}python-snowballstemmer
Version: 1.2.0
Release: 0.1%{?dist}
Source0: https://pypi.python.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Yoshiki Shibukawa <yoshiki at shibu.jp>
Url: https://github.com/shibukawa/snowball_py
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools

%description

It includes following language algorithms:

* Danish
* Dutch
* English (Standard, Porter)
* Finnish
* French
* German
* Hungarian
* Italian
* Norwegian
* Portuguese
* Romanian
* Russian
* Spanish
* Swedish
* Turkish

This is a pure Python stemming library. If `PyStemmer <http://pypi.python.org/pypi/PyStemmer>`_ is available, this module uses
it to accelerate.

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

echo __python_sitelib: %{__pythonsitelib}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
#%attr(755,root,root) %{_bindir}/*
%{python_sitelib}/*
%doc LICENSE.rst README.rst
#%doc build/*

%changelog
* Tue Nov 24 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 1.5.1-0.4
- Activate python-thrift dependency
