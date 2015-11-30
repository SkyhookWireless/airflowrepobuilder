%{?scl:%scl_package python-sphinx-argparse}
%{!?scl:%global pkg_name %{name}}

%global srcname sphinx-argparse

Summary: Sphinx extension that automatically document argparse commands and options
Name: %{?scl_prefix}python-sphinx-argparse
Version: 0.1.15
Release: 0.1%{?dist}
Source0: https://pypi.python.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Aleksandr Rudakov <ribozz@gmail.com>
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
Requires: %{?scl_prefix}python(abi)

%description
Sphinx extension that automatically document argparse commands and options

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
#%doc CHANGES LICENSE README.rst README.unittests.rst
#%doc build/*

%changelog
* Mon Nov 30 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 0.8.3-0.2
- Provide full URL for source
- Use wildcard for bindir files
- Manually add description

