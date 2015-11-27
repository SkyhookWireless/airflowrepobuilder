%{?scl:%scl_package python-wtforms}
%{!?scl:%global pkg_name %{name}}

%global srcname WTForms

Summary: A flexible forms validation and rendering library for python web development.
Name: %{?scl_prefix}python-wtforms
Version: 2.0.2
Release: 0.1%{?dist}
# Not available as .tar.gz
Source0: https://pypi.python.org/packages/source/W/%{srcname}/%{srcname}-%{version}.zip
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Thomas Johansson, James Crasta <wtforms@simplecodes.com>
Url: http://wtforms.simplecodes.com/
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Specifically requires python 2.6
Requires: %{?scl_prefix}python(abi)
Requires: %{?scl_prefix}python-ordereddict >= 1.1
Requires: %{?scl_prefix}python-babel
# Testing requirements
#Requires: %{?scl_prefix}python-coverage
#Requires: %{?scl_prefix}python-babel >= 1.3
#Requires: %{?scl_prefix}python-sqlalchemy
#Requires: %{?scl_prefix}python-pep
#Requires: %{?scl_prefix}python-dateutil


%description
A flexible forms validation and rendering library for python web development

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
%doc AUTHORS.txt CHANGES.rst LICENSE.txt README.md
#%doc build/*

%changelog
* Fri Nov 27 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 2.0.2-0.1
- Build RPM with setup.py
- Activate python2.7 build and dependenies
