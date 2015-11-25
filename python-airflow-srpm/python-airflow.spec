%{?scl:%scl_package python-airflow}
%{!?scl:%global pkg_name %{name}}

%global srcname airflow

Summary: Programmatically author, schedule and monitor data pipelines
Name: %{?scl_prefix}python-airflow
Version: 1.5.1
Release: 0.6%{?dist}
Source0: https://pypi.python.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
License: Apache
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{srcname}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Maxime Beauchemin <maximebeauchemin@gmail.com>
Url: https://github.com/airbnb/airflow
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools

# Manually added from setup.py
Requires:  %{?scl_prefix}python-alembic >= 0.8.0
Requires:  %{?scl_prefix}python-alembic < 0.9
Requires:  %{?scl_prefix}python-chartkick >= 0.4.2
Requires:  %{?scl_prefix}python-chartkick < 0.5
Requires:  %{?scl_prefix}python-dill >= 0.2.2
Requires:  %{?scl_prefix}python-dill < 0.3
Requires:  %{?scl_prefix}python-flask >= 0.10.1
Requires:  %{?scl_prefix}python-flask < 0.11
Requires:  %{?scl_prefix}python-flask-admin >= 1.2.0
Requires:  %{?scl_prefix}python-flask-admin < 1.2.1
Requires:  %{?scl_prefix}python-flask-cache >= 0.13.1
Requires:  %{?scl_prefix}python-flask-cache < 0.14
Requires:  %{?scl_prefix}python-flask-login >= 0.2.11
Requires:  %{?scl_prefix}python-future >= 0.15.0
Requires:  %{?scl_prefix}python-future < 0.16
Requires:  %{?scl_prefix}python-gunicorn >= 19.3.0
Requires:  %{?scl_prefix}python-gunicorn < 20.0
Requires:  %{?scl_prefix}python-jinja2 >= 2.7.3
Requires:  %{?scl_prefix}python-jinja2 < 3.0
Requires:  %{?scl_prefix}python-markdown >= 2.5.2
Requires:  %{?scl_prefix}python-markdown < 3.0
Requires:  %{?scl_prefix}python-pandas >= 0.15.2
Requires:  %{?scl_prefix}python-pandas < 1.0.0
Requires:  %{?scl_prefix}python-pygments >= 2.0.1
Requires:  %{?scl_prefix}python-pygments < 3.0
Requires:  %{?scl_prefix}python-python-dateutil >= 2.3
Requires:  %{?scl_prefix}python-python-dateutil < 3
Requires:  %{?scl_prefix}python-requests >= 2.5.1
Requires:  %{?scl_prefix}python-requests < 3
# Included in base python package
#Requires:  %{?scl_prefix}python-setproctitle >= 1.1.8
#Requires:  %{?scl_prefix}python-setproctitle < 2
Requires:  %{?scl_prefix}python-sqlalchemy >= 0.9.8
Requires:  %{?scl_prefix}python-thrift >= 0.9.2
Requires:  %{?scl_prefix}python-thrift < 0.10
# Added for authentication
Requires:  cyrus-sasl-gssapi
Requires:  cyrus-sasl-plain


# Manually added to ease installation
Provides: airflow

%description
Airflow is a platform to programmatically author, schedule and monitor workflows.

When workflows are defined as code, they become more maintainable,
versionable, testable, and collaborative.

Use airflow to author workflows as directed acyclic graphs (DAGs) of
tasks. The airflow scheduler executes your tasks on an array of
workers while following the specified dependencies. Rich command line
utilities make performing complex surgeries on DAGs a snap. The rich
user interface makes it easy to visualize pipelines running in
production, monitor progress, and troubleshoot issues when needed.

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
%attr(755,root,root) %{_bindir}/*
%{python_sitelib}/*
# Currently no documentaiton
#%doc CHANGES LICENSE README.rst README.unittests.rst
#%doc build/*

%changelog
* Mon Nov 23 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 1.5.1-0.6
- Activate python-thrift dependency
- Add cyrus-sasl-gssapi and cyrus-sasl-plain dependencies

* Fri Nov 20 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 1.5.1-0.4
- Introduce python-pyhs2 dependency

* Mon Nov 16 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 1.5.1-0.3
- Roll back to 1.5.1 for compatibility reasons

* Fri Nov 13 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 1.5.2-0.2
- Reset dependencies for python-thrift, which is on 

* Mon Nov  9 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 1.5.2-0.1
- Activate python2.7 build and dependenies
