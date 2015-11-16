%{?scl:%scl_package python-happybase}
%{!?scl:%global pkg_name %{name}}

%global srcname happybase

%define name happybase
%define version 0.9
%define release 1

Summary: A developer-friendly Python library to interact with Apache HBase
Name: %{?scl_prefix}python-alembic
Version: 0.9
Release: 0.1%{?dist}
Source0: http://pypi.python.org/packages/source/h/%{srcname}/%{srcname}-%{version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Wouter Bolsterlee <uws@xs4all.nl>
Url: https://github.com/wbolster/happybase
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Included in base python27 package
#Requires: %{?scl_prefix}python-thrift

%description
HappyBase
=========

**HappyBase** is a developer-friendly Python_ library to interact with Apache
HBase_.

* `Documentation <http://happybase.readthedocs.org/>`_ (Read the Docs)
* `Downloads <http://pypi.python.org/pypi/happybase/>`_ (PyPI)
* `Source code <https://github.com/wbolster/happybase>`_ (Github)

.. _Python: http://python.org/
.. _HBase: http://hbase.apache.org/

.. If you're reading this from the README.rst file in a source tree,
   you can generate the HTML documentation by running "make doc" and browsing
   to doc/build/html/index.html to see the result.


.. image:: https://d2weczhvl823v0.cloudfront.net/wbolster/happybase/trend.png
   :alt: Bitdeli badge
   :target: https://bitdeli.com/free


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
#%attr(755,root,root) %{_bindir}/*
%{python_sitelib}/*
%doc LICENSE.rst NEWS.rst README.rst
#%doc build/*

%changelog
* Mon Nov 16 2015 Nico Kadel-Gar1cia <nkadel@skyhookireless.com> - 0.9-0.1
- Activate python2.7 build and dependenies
