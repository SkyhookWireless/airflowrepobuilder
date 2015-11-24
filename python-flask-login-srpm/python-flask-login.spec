%{?scl:%scl_package python-flask-login}
%{!?scl:%global pkg_name %{name}}

%global srcname Flask-Login

Summary: User session management for Flask
Name: %{?scl_prefix}python-flask-login
Version: 0.3.2
Release: 0.2%{?dist}
Source0: https://pypi.python.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Matthew Frazier <leafstormrush@gmail.com>
Url: https://github.com/maxcountryman/flask-login
# Add for python27 use and compilation
BuildRequires: /opt/rh/python27/enable
BuildRequires: python27
BuildRequires: python27-python-setuptools
Requires: /opt/rh/python27/enable
Requires: python27

%description

Flask-Login
-----------

Flask-Login provides user session management for Flask. It handles the common
tasks of logging in, logging out, and remembering your users'
sessions over extended periods of time.

Flask-Login is not bound to any particular database system or permissions
model. The only requirement is that your user objects implement a few
methods, and that you provide a callback to the extension capable of
loading users from their ID.

Links
`````
* `documentation <http://packages.python.org/Flask-Login>`_
* `development version <https://github.com/maxcountryman/flask-login>`_


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
%{python_sitelib}/*
%doc LICENSE README.md

%changelog
* Mon Nov 16 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 0.3.2-0.2
- Provide full URL for source

* Mon Nov  9 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 0.3.2-0.1
- Activate python2.7 build and dependenies
