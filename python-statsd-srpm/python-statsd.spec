%{?scl:%scl_package python-statsd}
%{!?scl:%global pkg_name %{name}}

%global srcname statsd

Summary: A simple statsd client.
Name: %{?scl_prefix}python-statsd
Version: 3.2.1
Release: 0.1%{?dist}
Source0: https://pypi.python.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: James Socol <james@mozilla.com>
Url: https://github.com/jsocol/pystatsd
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools

%description
======================
A Python statsd client
======================

statsd_ is a friendly front-end to Graphite_. This is a Python client
for the statsd daemon.

.. image:: https://travis-ci.org/jsocol/pystatsd.png?branch=master
   :target: https://travis-ci.org/jsocol/pystatsd
   :alt: Travis-CI build status

.. image:: https://pypip.in/v/statsd/badge.png?style=flat
   :target: https://pypi.python.org/pypi/statsd/
   :alt: Latest release

.. image:: https://pypip.in/py_versions/statsd/badge.svg?style=flat
   :target: https://pypi.python.org/pypi/statsd/
   :alt: Supported Python versions

.. image:: https://pypip.in/wheel/statsd/badge.svg?style=flat
   :target: https://pypi.python.org/pypi/statsd/
   :alt: Wheel Status

.. image:: https://pypip.in/d/statsd/badge.png?style=flat
   :target: https://pypi.python.org/pypi/statsd/
   :alt: Downloads

:Code:          https://github.com/jsocol/pystatsd
:License:       MIT; see LICENSE file
:Issues:        https://github.com/jsocol/pystatsd/issues
:Documentation: http://statsd.readthedocs.org/

Quickly, to use::

    >>> import statsd
    >>> c = statsd.StatsClient('localhost', 8125)
    >>> c.incr('foo')  # Increment the 'foo' counter.
    >>> c.timing('stats.timed', 320)  # Record a 320ms 'stats.timed'.

You can also add a prefix to all your stats::

    >>> import statsd
    >>> c = statsd.StatsClient('localhost', 8125, prefix='foo')
    >>> c.incr('bar')  # Will be 'foo.bar' in statsd/graphite.


Installing
==========

The easiest way to install statsd is with pip!

You can install from PyPI::

    $ pip install statsd

Or GitHub::

    $ pip install -e git+https://github.com/jsocol/pystatsd#egg=statsd

Or from source::

    $ git clone https://github.com/jsocol/pystatsd
    $ cd statsd
    $ python setup.py install


Docs
====

There are lots of docs in the ``docs/`` directory and on ReadTheDocs_.


.. _statsd: https://github.com/etsy/statsd
.. _Graphite: http://graphite.readthedocs.org/
.. _ReadTheDocs: http://statsd.readthedocs.org/en/latest/index.html


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
%doc AUTHORS CHANGES LICENSE README.rst
#%doc build/*

%changelog
* Tue Nov 24 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 3.2.1-0.1
- Build RPM from setup.py
- Adapt for python27
