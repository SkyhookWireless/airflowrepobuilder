%{?scl:%scl_package python-futures}
%{!?scl:%global pkg_name %{name}}

%global srcname futures

Summary: Backport of the concurrent.futures package from Python 3.2
Name: %{?scl_prefix}python-futures
Version: 3.0.3
Release: 0.2%{?dist}
Source0: https://pypi.python.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Alex Gronholm <alex.gronholm+pypi@nextday.fi>
Url: https://github.com/agronholm/pythonfutures
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
Requires: %{?scl_prefix}python(abi)
# Avoid python naming confusion
Provides: %{?scl_prefix}python-%{srcname} = %{version}-%{release}

%description
UNKNOWN

%prep
%setup -q -n %{srcname}-%{version}
%{?scl:scl enable %{scl} "}
%{__python} setup.py build
%{?scl:"}

%build

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
%doc CHANGES LICENSE
#%doc build/*

%changelog
* Mon Nov 23 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 3.8.3-0.1
- Build RPM with setup.py
- Add python(abi) dependency
