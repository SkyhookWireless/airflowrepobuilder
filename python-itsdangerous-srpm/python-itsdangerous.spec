%{?scl:%scl_package python-itsdangerous}
%{!?scl:%global pkg_name %{name}}

%global srcname itsdangerous

Name:           %{?scl_prefix}python-%{srcname}
Version:        0.24
Release:        0.1%{?dist}
Summary:        Python library for passing trusted data to untrusted environments
License:        BSD
URL:            http://pythonhosted.org/itsdangerous/
Source0:        https://pypi.python.org/packages/source/i/%{srcname}/%{srcname}-%{version}.tar.gz
# Tarballs on PyPi lack LICENSE, CHANGES, and tests.
# https://github.com/mitsuhiko/itsdangerous/pull/22
BuildArch:      noarch
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools

%description
Itsdangerous is a Python library for passing data through untrusted 
environments (for example, HTTP cookies) while ensuring the data is not 
tampered with.

Internally itsdangerous uses HMAC and SHA1 for signing by default and bases the 
implementation on the Django signing module. It also however supports JSON Web 
Signatures (JWS).

%prep
%setup -q -n %{srcname}-%{version}
rm -r *.egg-info

%build
%{?scl:scl enable %{scl} "}
%{__python} setup.py build
%{?scl:"}

%install
%{__rm} -rf %{buildroot}
%{?scl:scl enable %{scl} "}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
%{?scl:"}

#n%check
#%{?scl:scl enable %{scl} "}
#%{__python} PYTHONPATH=%{buildroot}%{python_sitelib} %{__python} tests.py
#%{?scl:"}

%files
%doc LICENSE CHANGES README
%{python_sitelib}/%{srcname}.py*
%{python_sitelib}/%{srcname}*.egg-info

%changelog
* Wed Nov 11 2015 Nico Kadel-Garcia <nkadel@skyhookwireless.com> - 0.24-0.1
- update to 0.24
- Activate python2.7 build and dependenies
- Use tarball versions of LICENSE, CHANGES, and test.py

* Tue Jul 09 2013 Dan Callaghan <dcallagh@redhat.com> - 0.22-1
- new upstream release 0.22

* Tue Jun 18 2013 Dan Callaghan <dcallagh@redhat.com> - 0.21-3
- disable Python 3 subpackage on Fedora 17

* Mon Jun 17 2013 Dan Callaghan <dcallagh@redhat.com> - 0.21-2
- $RPM_BUILD_ROOT -> %%{buildroot}

* Fri Jun 14 2013 Dan Callaghan <dcallagh@redhat.com> - 0.21-1
- updated to upstream release 0.21
- added Python 3 subpackage

* Wed Nov 16 2011 Dan Callaghan <dcallagh@redhat.com> - 0.11-1
- initial version
