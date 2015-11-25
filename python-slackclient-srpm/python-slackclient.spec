%{?scl:%scl_package python-slackclient}
%{!?scl:%global pkg_name %{name}}

%global srcname slackclient

Summary: Python client for Slack.com
Name: %{?scl_prefix}python-slackclient
Version: 0.16
Release: 0.2%{?dist}
Source0: https://pypi.python.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Ryan Huber <ryan@slack-corp.com>
Url: http://github.com/slackhq/python-slackclient
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
#%attr(755,root,root) %{_bindir}/*
%{python_sitelib}/*
# No doc files currently
#%doc CHANGES LICENSE README.rst
#%doc build/*

%changelog
* Mon Nov 16 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 0.16-0.1
- Build SRPM from setup.py
- Adapt to python27
- Add python(abi) dependency
