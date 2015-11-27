%{?scl:%scl_package python-tox}
%{!?scl:%global pkg_name %{name}}

%global srcname tox

# Tests requiring Internet connections are disabled by default
# pass --with internet to run them (e.g. when doing a local rebuild
# for sanity checks before committing)
%bcond_with internet

%global srcname tox
Name: %{?scl_prefix}python-tox
Version:        2.2.1
Release:        0.1%{?dist}
Summary:        Virtualenv-based automation of test activities

# file toxbootstrap.py is licensed under MIT License
License:        GPLv2+ and MIT
URL:            http://codespeak.net/tox
Source0:        https://pypi.python.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
Requires: %{?scl_prefix}python(abi)
Requires: %{?scl_prefix}python-py >= 1.4.17
Requires: %{?scl_prefix}python-virtualenv >= 1.11.2
Requires: %{?scl_prefix}python-pluggy >= 0.3.0
Requires: %{?scl_prefix}python-pluggy <= 0.4.0

%if 0%{?rhel}==6
Requires: %{?scl_prefix}python-argparse
%endif

## required for check
#%if 0%{?fedora}
#BuildRequires: %{?scl_prefix}python-py
#BuildRequires: %{?scl_prefix}pytest
#BuildRequires: %{?scl_prefix}python-virtualenv
#%endif

%description
Tox as is a generic virtualenv management and test command line tool you 
can use for:

 - checking your package installs correctly with different Python versions 
   and interpreters
 - running your tests in each of the environments, configuring your test tool 
   of choice
 - acting as a frontend to Continuous Integration servers, greatly reducing 
   boilerplate and merging CI and shell-based testing.

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

# if internet connection available, run tests
%if %{with internet}
%check
# python 2.7: fedora 17, fedora 18
# python 3.2: fedora 17
# python 3.3: fedora 18

# el6: buildrequirements missing
#%if 0%{?rhel}==6
#TOXENV=py26 %{__python} setup.py test
#%endif

%endif
 
%clean
%{__rm} -rf %{buildroot}

%files
%doc CHANGELOG CONTRIBUTORS ISSUES.txt LICENSE README.rst
%doc doc
%{_bindir}/%{srcname}*
%{python_sitelib}/%{srcname}
%{python_sitelib}/%{srcname}-%{version}-py2.?.egg-info


%changelog
* Thu Nov 26 2015 Nico Kadel-Garcia <nkadel@skyhookwireless.com> 2.2.1-0.1
- Update to 2.2.1
- Migrate to python27 for RHEL 6

* Mon Feb 17 2014 Matthias Runge <mrunge@redhat.com> - 1.4.2-8
- python 2.6 requires argparse (rhbz#1065824)

* Wed Nov 14 2012 Matthias Runge <mrunge@redhat.com> - 1.4.2-7
- add requires python-py, python-virtualenv (rhbz#876246)

* Thu Oct 18 2012 Matthias Runge <mrunge@redhat.com> - 1.4.2-6
- change license to GPLv2+ and MIT

* Tue Oct 16 2012 Matthias Runge <mrunge@redhat.com> - 1.4.2-5
- totally disable python3 support for now

* Fri Oct 12 2012 Matthias Runge <mrunge@redhat.com> - 1.4.2-4
- conditionalize checks, as internet connection required, not available on koji

* Thu Oct 11 2012 Matthias Runge <mrunge@redhat.com> - 1.4.2-3
- buildrequirement: virtualenv
- disable python3-tests because of missing build-requirement python3-virtualenv

* Wed Oct 10 2012 Matthias Runge <mrunge@redhat.com> - 1.4.2-2
- include tests

* Tue Oct 09 2012 Matthias Runge <mrunge@redhat.com> - 1.4.2-1
- initial packaging
