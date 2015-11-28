%{?scl:%scl_package python-filechunkio}
%{!?scl:%global pkg_name %{name}}

%global srcname filechunkio

Summary: FileChunkIO represents a chunk of an OS-level file containing bytes data
Name: python-%{srcname}
Version: 1.6
Release: 0.1%{?dist}
Source0: https://pypi.python.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
License: MIT license
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Fabian Topfstedt <topfstedt@schneevonmorgen.com>
Url: http://bitbucket.org/fabian/filechunkio
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
Requires: %{?scl_prefix}python(abi)

%description
FileChunkIO represents a chunk of an OS-level file containing bytes data.
Python 2.6+ is required.

BACKGROUND:
I wrote FileChunkIO to upload huge files to Amazon S3 in multiple parts
without having to split them physically upfront (which requires more time and
twice the disk space) or creating in-memory chunks as StringIO instances.

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
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
#%attr(755,root,root) %{_bindir}/*
%{python_sitelib}/*
%doc README
#%doc build/*

%changelog
* Fri Nov 27 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 0.8.3-0.2
- Build SRPM from setup.py
- Modify for python27

