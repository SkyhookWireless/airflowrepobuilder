%{?scl:%scl_package python-hive-thrift-py}
%{!?scl:%global pkg_name %{name}}

%global srcname hive-thrift-py

Summary: Hive Python Thrift Libs
Name: %{?scl_prefix}python-hive-thrift-py
Version: 0.0.1
Release: 0.1%{?dist}
Source0: https://pypi.python.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
License: Apache License
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Youngwoo Kim <warwithin@gmail.com>
Url: http://hive.apache.org
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
Requires: %{?scl_prefix}python(abi)

%description
Hive Python Thrift Libs

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
# New module lacks documentation!
#%doc README.rst
#%doc build/*

%changelog
* Mon Nov 30 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 0.0.1-0.1
- Build SRPM from setup.py
- Activate python2.7 build and dependenies
