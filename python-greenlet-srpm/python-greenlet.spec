%{?scl:%scl_package python-greenlet}
%{!?scl:%global pkg_name %{name}}

%global srcname greenlet

Summary: Lightweight in-process concurrent programming
Name: %{?scl_prefix}python-greenlet
Version: 0.4.9
Release: 0.1%{?dist}
Source0: https://pypi.python.org/packages/source/g/%{srcname}/%{srcname}-%{version}.tar.gz
License: MIT License
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Alexey Borzenkov <snaury@gmail.com>
Url: https://github.com/python-greenlet/greenlet
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
Requires: %{?scl_prefix}python(abi)

%description
The greenlet package is a spin-off of Stackless, a version of CPython
that supports micro-threads called "tasklets". Tasklets run
pseudo-concurrently (typically in a single or a few OS-level threads)
and are synchronized with data exchanges on "channels".

A "greenlet", on the other hand, is a still more primitive notion of
micro-thread with no implicit scheduling; coroutines, in other
words. This is useful when you want to control exactly when your code
runs. You can build custom scheduled micro-threads on top of greenlet;
however, it seems that greenlets are useful on their own as a way to
make advanced control flow structures. For example, we can recreate
generators; the difference with Python's own generators is that our
generators can call nested functions and the nested functions can
yield values too. Additionally, you don't need a "yield" keyword. See
the example in tests/test_generator.py.

Greenlets are provided as a C extension module for the regular
unmodified interpreter.

Greenlets are lightweight coroutines for in-process concurrent
programming.

Who is using Greenlet?
======================

There are several libraries that use Greenlet as a more flexible
alternative to Python's built in coroutine support:

 - `Concurrence`_
 - `Eventlet`_
 - `Gevent`_

.. _Concurrence: http://opensource.hyves.org/concurrence/
.. _Eventlet: http://eventlet.net/
.. _Gevent: http://www.gevent.org/

Getting Greenlet
================

The easiest way to get Greenlet is to install it with pip or
easy_install::

  pip install greenlet
  easy_install greenlet


Source code archives and windows installers are available on the
python package index at https://pypi.python.org/pypi/greenlet

The source code repository is hosted on github:
https://github.com/python-greenlet/greenlet

Documentation is available on readthedocs.org:
https://greenlet.readthedocs.org


%prep
%setup -q -n %{srcname}-%{version}

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
%{_includedir}/*
%{python_sitearch}/*
#%{python_sitelib}/*
%doc AUTHORS LICENSE LICENSE.PSF NEWS  README.rst
#%doc build/*
