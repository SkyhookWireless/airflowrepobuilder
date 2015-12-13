%{?scl:%scl_package python-vertica-python}
%{!?scl:%global pkg_name %{name}}

%global srcname vertica-python

Summary: A native Python client for the Vertica database.
Name: %{?scl_prefix}python-vertica-python
Version: 0.5.4
Release: 0.1%{?dist}
Source0: https://pypi.python.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Justin Berka, Alex Kim, Kenneth Tran <justin.berka@gmail.com, alex.kim@uber.com, tran@uber.com>
Url: https://github.com/uber/vertica-python/
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
Requires: %{?scl_prefix}python-psycopg2 >= 2.5.1
Requires: %{?scl_prefix}python-dateutil >= 1.5
Requires: %{?scl_prefix}pytz
Requires: %{?scl_prefix}python(abi)
# Avoid python naming confusion
Provides: %{?scl_prefix}python-%{srcname} = %{version}-%{release}

%description
vertica-python is a native Python adapter for the Vertica (http://www.vertica.com) database.

vertica-python is currently in beta stage; it has been tested for functionality and has a very basic test suite. Please use with caution, and feel free to submit issues and/or pull requests (after running the unit tests).

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
%doc LICENSE README.md
#%doc build/*

%changelog
* Tue Dec  1  2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 0.5.4-0.1
- Build SRPM from setup.py
- Activate python2.7 build and dependenies
