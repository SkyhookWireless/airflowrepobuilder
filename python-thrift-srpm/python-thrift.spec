%{?scl:%scl_package python-thrift}
%{!?scl:%global pkg_name %{name}}

%global srcname thrift

%define version 0.9.3
%define release 1

Summary: Python bindings for the Apache Thrift RPC system
Name: %{?scl_prefix}python-thrift
Version: 0.9.3
Release: 0.1%{?dist}
Source0: https://pypi.python.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
License: Apache License 2.0
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Thrift Developers <dev@thrift.apache.org>
Url: http://thrift.apache.org
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools

%description
The Apache Thrift software framework, for scalable cross-language
services development, combines a software stack with a code generation
engine to build services that work efficiently and seamlessly between
C++, Java, Python, PHP, Ruby, Erlang, Perl, Haskell, C, Cocoa,
JavaScript, Node.js, Smalltalk, OCaml and Delphi and other languages.

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
#%attr(755,root,root) %{_bindir}/*
%{python_sitearch}/*
#%{python_sitelib}/*
# No documentation found!
#%doc LICENSE
#%doc build/*

%changelog
* Mon Nov 16 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 0.9.3-0.1
- Activate python2.7 build and dependenies
- Add description manually from website
