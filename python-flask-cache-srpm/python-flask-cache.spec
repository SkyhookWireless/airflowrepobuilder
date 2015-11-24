%{?scl:%scl_package python-flask-cache}
%{!?scl:%global pkg_name %{name}}

%global srcname Flask-Cache

Summary: Adds cache support to your Flask application
Name: %{?scl_prefix}python-flask-cache
Version: 0.13.1
Release: 0.2%{?dist}
Source0: https://pypi.python.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Thadeus Burgess <thadeusb@thadeusb.com>
Url: http://github.com/thadeusb/flask-cache
# Add for python27 use and compilation
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools

%description

Flask-Cache
-----------

Adds cache support to your Flask application


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
%{python_sitelib}/*
%doc CHANGES LICENSE README

%changelog
* Mon Nov 16 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 0.13.11-0.2
- Provide full URL for source
- Replace "realname" with "srcname" for consistency

* Mon Nov  9 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 0.13.1l-0.1
- Activate python2.7 build and dependenies
