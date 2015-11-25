%{?scl:%scl_package python-cm-api}
%{!?scl:%global pkg_name %{name}}

%global srcname cm_api

Summary: Cloudera Manager API client
Name: %{?scl_prefix}python-cm-api
Version: 10.0.0
Release: 0.2%{?dist}
Source0: https://pypi.python.org/packages/source/c/%{srcname}/%{srcname}-%{version}.tar.gz
License: Apache License 2.0
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Cloudera, Inc. <scm-users@cloudera.org>
Url: http://cloudera.github.com/cm_api/
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
Requires: %{?scl_prefix}python(abi)

%description
UNKNOWN

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
# Not yet published in 0
#%doc LICENSE.txt README.md
#%doc build/*

%changelog
* Mon Nov 16 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 0.10.0-0.1
- Activate python2.7 build and dependenies
- Add python(abi) dependency
