%{?scl:%scl_package python-flask-wtf}
%{!?scl:%global pkg_name %{name}}

%global srcname Flask-WTF

Summary: Simple integration of Flask and WTForms
Name: %{?scl_prefix}python-flask-wtf
Version: 0.12
Release: 0.1%{?dist}
Source0: https://pypi.python.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Hsiaoming Yang <me@lepture.com>
Url: http://github.com/lepture/flask-wtf
# Added for compilation
BuildRequires: %{?scl_prefix}python-devel
BuildRequires: %{?scl_prefix}python-setuptools
Requires: %{?scl_prefix}python-flask
Requires: %{?scl_prefix}python-werkzeug
Requires: %{?scl_prefix}python-wtforms
Requires: %{?scl_prefix}python(abi)
# Avoid python naming confusion
Provides: %{?scl_prefix}python-%{srcname} = %{version}-%{release}

%description

Flask-WTF
=========

Simple integration of Flask and WTForms, including CSRF, file upload
and Recaptcha integration.

Links
-----

* `documentation <https://flask-wtf.readthedocs.org>`_
* `development version
  <http://github.com/lepture/flask-wtf>`_


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
%{python_sitelib}/*
%doc LICENSE README.rst
#%doc build/*
#%doc docs/*

%changelog
* Fri Nov 27 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 0.12-0.l1
- Build RPM from setup.py
- Add python27 requirements

