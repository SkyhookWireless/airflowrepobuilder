%{?scl:%scl_package python-alembic}
%{!?scl:%global pkg_name %{name}}

%global srcname alembic

Summary: A database migration tool for SQLAlchemy.
Name: %{?scl_prefix}python-alembic
Version: 0.8.3
Release: 0.3%{?dist}
Source0: https://pypi.python.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Mike Bayer <mike@zzzcomputing.com>
Url: http://bitbucket.org/zzzeek/alembic
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
Requires: %{?scl_prefix}python(abi)

%description
Alembic is a database migrations tool written by the author
of `SQLAlchemy <http://www.sqlalchemy.org>`_.  A migrations tool
offers the following functionality:

* Can emit ALTER statements to a database in order to change
  the structure of tables and other constructs
* Provides a system whereby "migration scripts" may be constructed;
  each script indicates a particular series of steps that can "upgrade" a
  target database to a new version, and optionally a series of steps that can
  "downgrade" similarly, doing the same steps in reverse.
* Allows the scripts to execute in some sequential manner.

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
%attr(755,root,root) %{_bindir}/*
%{python_sitelib}/*
%doc CHANGES LICENSE README.rst README.unittests.rst
#%doc build/*

%changelog
* Mon Nov 16 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 0.8.3-0.2
- Provide full URL for source
- Use wildcard for bindir files
* Mon Nov  9 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 0.8.3-0.1
- Activate python2.7 build and dependenies
