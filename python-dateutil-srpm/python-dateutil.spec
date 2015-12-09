%{?scl:%scl_package python-dateutil}
%{!?scl:%global pkg_name %{name}}

%global srcname python-dateutil

Summary: Extensions to the standard Python datetime module
Name: %{?scl_prefix}python-dateutil
Version: 2.4.2
Release: 0.3%{?dist}
Source0: https://pypi.python.org/packages/source/p/%{name}/%{srcname}-%{version}.tar.gz
License: Simplified BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Yaron de Leeuw <me@jarondl.net>
Url: https://dateutil.readthedocs.org
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
Requires: %{?scl_prefix}python(abi)
# Renamed package
Provides: %{?scl_prefix}python-python-dateutil = %{verwsion}-%{release}

%description
The dateutil module provides powerful extensions to the
datetime module available in the Python standard library.


%prep
%setup -q -n %{srcname}-%{version}
%{__sed} -i 's/\r//' LICENSE

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
%doc LICENSE NEWS README.rst
#%doc build/*

%changelog
* Wed Dec  9 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 2.4.2-0.3
- Rename to python-dateutil

* Mon Nov 16 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 2.4.2-0.2
- Provide full URL for source
- Add python(abi) dependency

* Mon Nov  9 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 2.4.2-0.1
- Activate python2.7 build and dependenies
