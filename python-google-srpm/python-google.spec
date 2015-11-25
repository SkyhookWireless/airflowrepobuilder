%{?scl:%scl_package python-google}
%{!?scl:%global pkg_name %{name}}

%global srcname google

Summary: Python bindings to the Google search engine.
Name: %{?scl_prefix}python-google
Version: 1.7
Release: 0.1%{?dist}
Source0: https://pypi.python.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Mario Vilas <mvilas@gmail.com>
Url: http://breakingcode.wordpress.com/
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
Requires: %{?scl_prefix}python(abi)
#Requires:  %{?scl_prefix}python-beautifulsoup4 >= 4.0

%description
google
======

Google search from Python.

https://breakingcode.wordpress.com/2010/06/29/google-search-python/

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
%attr(755,root,root) %{_bindir}/*
%{python_sitelib}/*
%doc README.md
#%doc build/*

%changelog
* Mon Nov 23 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 1.7-0.1
- Build RPM with setup.py
- Add python(abi) dependency

