%{?scl:%scl_package python-airflow16}
%{!?scl:%global pkg_name %{name}}

%global srcname airflow

Summary: Programmatically author, schedule and monitor data pipelines
Name: %{?scl_prefix}python-airflow16
Version: 1.6.1
Release: 0.1%{?dist}
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
Requires:  %{?scl_prefix}python-alembic
Requires:  %{?scl_prefix}python-boto
Requires:  %{?scl_prefix}python-chartkick
Requires:  %{?scl_prefix}python-cryptography
Requires:  %{?scl_prefix}python-coverage
Requires:  %{?scl_prefix}python-coveralls
Requires:  %{?scl_prefix}python-croniter
Requires:  %{?scl_prefix}python-dill
Requires:  %{?scl_prefix}python-filechunkio
Requires:  %{?scl_prefix}python-flake8
Requires:  %{?scl_prefix}python-flask
Requires:  %{?scl_prefix}python-flask-admin
Requires:  %{?scl_prefix}python-flask-cache
Requires:  %{?scl_prefix}python-flask-login
Requires:  %{?scl_prefix}python-flower
Requires:  %{?scl_prefix}python-future
Requires:  %{?scl_prefix}python-gunicorn
Requires:  %{?scl_prefix}python-hive-thrift-py
Requires:  %{?scl_prefix}python-ipython
Requires:  %{?scl_prefix}python-jinja2
Requires:  %{?scl_prefix}python-markdown
Requires:  %{?scl_prefix}python-nose
Requires:  %{?scl_prefix}python-nose-exclude
Requires:  %{?scl_prefix}python-pandas
Requires:  %{?scl_prefix}python-pygments
Requires:  %{?scl_prefix}python-pyhive
Requires:  %{?scl_prefix}python-pydruid
Requires:  %{?scl_prefix}python-pysmbclient
Requires:  %{?scl_prefix}python-psycogp2
Requires:  %{?scl_prefix}python-python-dateutil >= 2.3
Requires:  %{?scl_prefix}python-python-dateutil < 3
Requires:  %{?scl_prefix}python-requests >= 2.5.1
Requires:  %{?scl_prefix}python-requests < 3
Requires:  %{?scl_prefix}python-redis
Requires:  %{?scl_prefix}python-setproctitle
Requires:  %{?scl_prefix}python-statsd
Requires:  %{?scl_prefix}python-sphinx
Requires:  %{?scl_prefix}python-sphinx-argparse
Requires:  %{?scl_prefix}python-sphinx_rtd_theme
Requires:  %{?scl_prefix}python-sphinx-pypi-upload
# Included in base python package
#Requires:  %{?scl_prefix}python-setproctitle >= 1.1.8
#Requires:  %{?scl_prefix}python-setproctitle < 2
Requires:  %{?scl_prefix}python-sqlalchemy
Requires:  %{?scl_prefix}python-thrift
Requires:  %{?scl_prefix}python-thrift
Requires:  %{?scl_prefix}python-jaydebeapi
Requires:  %{?scl_prefix}python-mysqlclient
Requires:  %{?scl_prefix}python-unicodecsv
Requires:  %{?scl_prefix}python-slackclient
Requires:  %{?scl_prefix}python-ldap3
Requires:  %{?scl_prefix}python-flask-wtf
Requires:  %{?scl_prefix}python-lxml
Requires:  %{?scl_prefix}python-pykerberos

# Manually added to ease installation
Provides: airflow
# Avoid conflicting with airflow15
Conflicts: %{?scl_prefix}python-airflow
Conflicts: %{?scl_prefix}python-airflow15

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
* Mon Nov 23 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 1.5.1-0.4
- Activate python-thrift dependency

* Fri Nov 20 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 1.5.1-0.4
- Introduce python-pyhs2 dependency

* Mon Nov 16 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 1.5.1-0.3
- Roll back to 1.5.1 for compatibility reasons

* Fri Nov 13 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 1.5.2-0.2
- Reset dependencies for python-thrift, which is on 

* Mon Nov  9 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 1.5.2-0.1
- Activate python2.7 build and dependenies
