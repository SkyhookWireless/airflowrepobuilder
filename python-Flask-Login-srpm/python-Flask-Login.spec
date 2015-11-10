%define name python-Flask-Login
%define realname Flask-Login
%define version 0.3.2
%define unmangled_version 0.3.2
%define unmangled_version 0.3.2
%define release 0.1

Summary: User session management for Flask
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{realname}-%{unmangled_version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Matthew Frazier <leafstormrush@gmail.com>
Url: https://github.com/maxcountryman/flask-login
# Added for compilaton
BuildRequires: python-setuptools

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
%setup -n %{realname}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
