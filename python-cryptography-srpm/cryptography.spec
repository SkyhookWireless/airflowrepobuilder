%{?scl:%scl_package python-cryptography}
%{!?scl:%global pkg_name %{name}}

%global srcname cryptography

Summary: cryptography is a package which provides cryptographic recipes and primitives to Python developers.
Name: %{?scl_prefix}python-cryptography
Version: 1.1.1
Release: 0.1%{?dist}
Source0: https://pypi.python.org/packages/source/c/%{srcname}/%{srcname}-%{version}.tar.gz
License: BSD or Apache License, Version 2.0
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: The cryptography developers <cryptography-dev@python.org>
Url: https://github.com/pyca/cryptography
BuildRequires:  libffi-devel
BuildRequires:  openssl-devel
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
Requires: %{?scl_prefix}python(abi)
# Avoid python naming confusion
Provides: %{?scl_prefix}python-%{srcname} = %{version}-%{release}

%description
Cryptography
============

``cryptography`` is a package which provides cryptographic recipes and
primitives to Python developers.  Our goal is for it to be your "cryptographic
standard library". It supports Python 2.6-2.7, Python 3.3+, and PyPy 2.6+.

%prep
%setup -n %{srcname}-%{version}

%build
# Put CFLAGS in separate macro
export CFLAGS="$RPM_OPT_FLAGS"
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
#%{python_sitelib}/*
%{python_sitearch}/*
%doc AUTHORS.rst CHANGELOG.rst CONTRIBUTING.rst LICENSE LICENSE.APACHE LICENSE.BSD README.rst
#%doc build/*

%changelog
* Mon Nov 30 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 0.8.3-0.2
- Build SRPM fro setup.py
- Activate python2.7 build and dependenies
