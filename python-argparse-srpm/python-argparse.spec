%{?scl:%scl_package python-argparse}
%{!?scl:%global pkg_name %{name}}

%global srcname  argparse

Summary:       Optparse inspired command line parser for Python
Name: %{?scl_prefix}python-argparse
Version:       1.2.1
Release:       0.1%{?dist}
License:       Python
Group:         Development/Languages
URL:           https://code.google.com/p/argparse/
Source0:       https://argparse.googlecode.com/files/argparse-%{version}.tar.gz
BuildRequires: python-setuptools
BuildRequires: dos2unix
BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
Requires: %{?scl_prefix}python(abi)
# Avoid python naming confusion
Provides: %{?scl_prefix}python-%{srcname} = %{version}-%{release}

%description

The argparse module is an optparse-inspired command line parser that
improves on optparse by:
 * handling both optional and positional arguments
 * supporting parsers that dispatch to sub-parsers
 * producing more informative usage messages
 * supporting actions that consume any number of command-line args
 * allowing types and actions to be specified with simple callables
    instead of hacking class attributes like STORE_ACTIONS or CHECK_METHODS

as well as including a number of other more minor improvements on the
optparse API.

%prep
%setup -q -n %{srcname}-%{version}
dos2unix -k README.txt NEWS.txt
%{__rm} -rf doc/source

%build
%{?scl:scl enable %{scl} "}
%{__python} setup.py build
%{?scl:"}

%install
%{__rm} -rf %{buildroot}
%{?scl:scl enable %{scl} "}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
%{?scl:"}

%check
pushd test
%{?scl:scl enable %{scl} "}
PYTHONPATH=../ %{__python} test_%{srcname}.py
%{?scl:"}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc README.txt LICENSE.txt NEWS.txt doc/*
%{python_sitelib}/*

%changelog
* Tue Dec 1 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 1.2.1-0.1
- Activate python2.7 build and dependenies

* Tue Sep 11 2012 Alan Pevec <apevec@redhat.com> 1.2.1-2.1
- Import to RHEL 6.4 (rhbz#851798)

* Wed Jun 29 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 1.2.1-2
- Include LICENSE.txt file

* Wed Jun 29 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 1.2.1-1
- New compatble upstream with some bugfixes and a GPL2 vompatible license
- Enable test suite

* Wed Feb 10 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 1.0.1-1.1
- First build for EL-5
- Small change to %%files section so lack of egg-info on EL-5 is okay.

* Sun Dec 06 2009 Terje Rosten <terje.rosten@ntnu.no> - 1.0.1-1
- 1.0.1
- Ship more docs
- Project has moved
- Disable test for now
- Change license to Apache 2.0

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 11 2009 Terje Rosten <terje.rosten@ntnu.no> - 0.8.0-2
- fixes from review, thanks Jussi!

* Sat Jan 17 2009 Terje Rosten <terje.rosten@ntnu.no> - 0.8.0-1
- initial build

