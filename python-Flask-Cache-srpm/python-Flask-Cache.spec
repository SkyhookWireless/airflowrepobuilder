%define name python-Flask-Cache
%define realname Flask-Cache
%define version 0.13.1
%define unmangled_version 0.13.1
%define unmangled_version 0.13.1
%define release 0.1

Summary: Adds cache support to your Flask application
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{realname}-%{unmangled_version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Thadeus Burgess <thadeusb@thadeusb.com>
Url: http://github.com/thadeusb/flask-cache
# Added for compilation
BuildRequires: python-setuptools

%description

Flask-Cache
-----------

Adds cache support to your Flask application



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
