%{?scl:%scl_package python-flask-login}
%{!?scl:%global pkg_name %{name}}

%global srcname Flask-Login

Summary: User session management for Flask
Name: %{?scl_prefix}python-flask-login
Version: 0.2.11
Release: 0.1%{?dist}
Source0: https://pypi.python.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Matthew Frazier <leafstormrush@gmail.com>
Url: https://github.com/maxcountryman/flask-login

BuildRequires: %{?scl_prefix}python-devel
BuildRequires: %{?scl_prefix}python-setuptools
BuildRequires: %{?scl_prefix}python(abi)
Requires: %{?scl_prefix}python(abi)

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
#%{python_sitelib}/%{srcname}
# Foolish tarball is named Flask-Login, deployed module is named Flask_Login
%{python_sitelib}/Flask_Login-%{version}-*.egg-info
%{python_sitelib}/flask_login.*
%doc LICENSE README.markdown

%changelog
* Sun Dec  6 2015  Nico Kadel-Garcia <nkadel@skyhookireless.com> - 0.2.1-0.1
- Roll back to 0.2.1 for compatibility with airflow

* Tue Dec  1 2015  Nico Kadel-Garcia <nkadel@skyhookireless.com> - 0.3.2-0.4
- Simplify dependencies with scl_prefix

* Mon Nov 16 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 0.3.2-0.2
- Provide full URL for source
- Add python(abi) dependency

* Mon Nov  9 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 0.3.2-0.1
- Activate python2.7 build and dependenies
