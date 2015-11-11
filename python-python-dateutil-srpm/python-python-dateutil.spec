%{?scl:%scl_package python-python-dateutil}
%{!?scl:%global pkg_name %{name}}

%global srcname python-dateutil

Summary: Extensions to the standard Python datetime module
Name: %{?scl_prefix}python-python-dateutil
Version: 2.4.2
Release: 0.1%{?dist}
Source0: %{srcname}-%{version}.tar.gz
License: Simplified BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Yaron de Leeuw <me@jarondl.net>
Url: https://dateutil.readthedocs.org
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools

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
* Mon Nov  9 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 2.4.2-0.1
- Activate python2.7 build and dependenies

