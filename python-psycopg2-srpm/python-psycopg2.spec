%{?scl:%scl_package python-psycopg2}
%{!?scl:%global pkg_name %{name}}

%global srcname psycopg2

Summary: psycopg2 - Python-PostgreSQL Database Adapter
Name: %{?scl_prefix}python-psycopg2
Version: 2.6.1
Release: 0.1%{?dist}
Source0: https://pypi.python.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
License: LGPL with exceptions or ZPL
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Federico Di Gregorio <fog@initd.org>
Url: http://initd.org/psycopg/
BuildRequires:  postgresql-devel
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
Requires: %{?scl_prefix}python(abi)
# Avoid python naming confusion
Provides: %{?scl_prefix}python-%{srcname} = %{version}-%{release}

%description
Psycopg is the most popular PostgreSQL database adapter for the Python
programming language.  Its main features are the complete implementation of
the Python DB API 2.0 specification and the thread safety (several threads can
share the same connection).  It was designed for heavily multi-threaded
applications that create and destroy lots of cursors and make a large number
of concurrent "INSERT"s or "UPDATE"s.

Psycopg 2 is mostly implemented in C as a libpq wrapper, resulting in being
both efficient and secure.  It features client-side and server-side cursors,
asynchronous communication and notifications, "COPY TO/COPY FROM" support.
Many Python types are supported out-of-the-box and adapted to matching
PostgreSQL data types; adaptation can be extended and customized thanks to a
flexible objects adaptation system.

Psycopg 2 is both Unicode and Python 3 friendly.


Documentation
-------------

Documentation is included in the 'doc' directory and is `available online`__.

.. __: http://initd.org/psycopg/docs/


Installation
------------

If all the dependencies are met (i.e. you have the Python and libpq
development packages installed in your system) the standard::

    python setup.py build
    sudo python setup.py install

should work no problem.  In case you have any problem check the 'install' and
the 'faq' documents in the docs or online__.

.. __: http://initd.org/psycopg/docs/install.html

For any other resource (source code repository, bug tracker, mailing list)
please check the `project homepage`__.

.. __: http://initd.org/psycopg/


%prep
%setup -n %{srcname}-%{version}

%build
#env CFLAGS="$RPM_OPT_FLAGS" python setup.py build
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
#%attr(755,root,root) %{_bindir}/*
%{python_sitearch}/*
#%{python_sitelib}/*
%doc AUTHORS INSTALL LICENSE NEWS README.rst
#%doc build/*

%changelog
* Mon Nov 30 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 2.6.1-0.1
- Build SRPM from setup.py
- Activate python2.7 build and dependenies
