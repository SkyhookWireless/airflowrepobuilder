#
# spec file for package python-protobuf
#
# Copyright (c) 2015 Nico Kadel-Garcia.
#

%{?scl:%scl_package python-alembic}
%{!?scl:%global pkg_name %{name}}

%global srcname alembic

Name: %{?scl_prefix}python-alembic
Version:        3.0.0a3
Release:        0
Url:            https://developers.google.com/protocol-buffers/
Summary:        Protocol Buffers
License:        BSD-3-Clause
Group:          Development/Languages/Python
Source:         https://pypi.python.org/packages/source/p/protobuf/protobuf-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
BuildRequires:  %{?scl_prefix}python(abi)
Requires: %{?scl_prefix}python-setuptools
Requires: %{?scl_prefix}python(abi)

%description
Protocol Buffers are Google's data interchange format

%prep
%setup -q -n protobuf-%{version}

%build
#export CFLAGS="%{optflags}"
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
%{python_sitelib}/*

%changelog
* Mon Nov 16 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 3.0.0a3-0.1
- Build SRPM with py2pack
- Activate python2.7 build and dependenies
