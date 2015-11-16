%{?scl:%scl_package python-future}
%{!?scl:%global pkg_name %{name}}

%global srcname future

Summary: Clean single-source support for Python 3 and 2
Name: %{?scl_prefix}python-future
Version: 0.15.2
Release: 0.2%{?dist}
Source0: http://pypi.python.org/packages/source/g/%{srcname}/%{srcname}-%{version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Ed Schofield <ed@pythoncharmers.com>
Url: https://python-future.org
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools

%description
future: Easy, safe support for Python 2/3 compatibility
=======================================================

``future`` is the missing compatibility layer between Python 2 and Python
3. It allows you to use a single, clean Python 3.x-compatible codebase to
support both Python 2 and Python 3 with minimal overhead.

It is designed to be used as follows::

    from __future__ import (absolute_import, division,
                            print_function, unicode_literals)
    from builtins import (
             bytes, dict, int, list, object, range, str,
             ascii, chr, hex, input, next, oct, open,
             pow, round, super,
             filter, map, zip)

followed by predominantly standard, idiomatic Python 3 code that then runs
similarly on Python 2.6/2.7 and Python 3.3+.

The imports have no effect on Python 3. On Python 2, they shadow the
corresponding builtins, which normally have different semantics on Python 3
versus 2, to provide their Python 3 semantics.


Standard library reorganization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``future`` supports the standard library reorganization (PEP 3108) through the
following Py3 interfaces:

    >>> # Top-level packages with Py3 names provided on Py2:
    >>> import configparser
    >>> import html.parser
    >>> import queue
    >>> import tkinter.dialog
    >>> import xmlrpc.client
    >>> # etc.

    >>> # Aliases provided for extensions to existing Py2 module names:
    >>> from future.standard_library import install_aliases
    >>> install_aliases()

    >>> from collections import Counter, OrderedDict   # backported to Py2.6
    >>> from collections import UserDict, UserList, UserString
    >>> import urllib.request
    >>> from itertools import filterfalse, zip_longest
    >>> from subprocess import getoutput, getstatusoutput


Automatic conversion
--------------------

An included script called `futurize
<http://python-future.org/automatic_conversion.html>`_ aids in converting
code (from either Python 2 or Python 3) to code compatible with both
platforms. It is similar to ``python-modernize`` but goes further in
providing Python 3 compatibility through the use of the backported types
and builtin functions in ``future``.


Documentation
-------------

See: http://python-future.org


Credits
-------

:Author:  Ed Schofield
:Sponsor: Python Charmers Pty Ltd, Australia, and Python Charmers Pte
          Ltd, Singapore. http://pythoncharmers.com
:Others:  See docs/credits.rst or http://python-future.org/credits.html


Licensing
---------
Copyright 2013-2015 Python Charmers Pty Ltd, Australia.
The software is distributed under an MIT licence. See LICENSE.txt.

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
%doc LICENSE.txt README.rst TESTING.txt
#%doc build/*

%changelog
* Mon Nov 16 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 0.15.2-0.2
- Provide full URL for source

* Mon Nov  9 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 0.15.2-0.1
- Activate python2.7 build and dependenies
