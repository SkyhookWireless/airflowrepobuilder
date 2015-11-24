%{?scl:%scl_package python-enum}
%{!?scl:%global pkg_name %{name}}

%global srcname enum

Summary: Robust enumerated type support in Python.
Name: %{?scl_prefix}python-enum
Version: 0.4.6
Release: 0.1%{?dist}
Source0: https://pypi.python.org/packages/source/e/%{srcname}/%{srcname}-%{version}.tar.gz
License: Choice of GPL or Python license
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Ben Finney <ben+python@benfinney.id.au>
Url: http://pypi.python.org/pypi/enum/
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools

%description
..  Important:: Superseded by Python standard library.

    Python 3 now has in its standard library an `enum`_
    implementation (also available for older Python versions as
    the third-party `flufl.enum`_ distribution) that supersedes
    this library.

    ..  _enum: https://docs.python.org/3/library/enum.html
    ..  _flufl.enum: https://pypi.python.org/pypi/flufl.enum

This package provides a module for robust enumerations in Python.

An enumeration object is created with a sequence of string arguments
to the Enum() constructor::

    >>> from enum import Enum
    >>> Colours = Enum('red', 'blue', 'green')
    >>> Weekdays = Enum('mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun')

The return value is an immutable sequence object with a value for each
of the string arguments. Each value is also available as an attribute
named from the corresponding string argument::

    >>> pizza_night = Weekdays[4]
    >>> shirt_colour = Colours.green

The values are constants that can be compared only with values from
the same enumeration; comparison with other values will invoke
Python's fallback comparisons::

    >>> pizza_night == Weekdays.fri
    True
    >>> shirt_colour > Colours.red
    True
    >>> shirt_colour == "green"
    False

Each value from an enumeration exports its sequence index
as an integer, and can be coerced to a simple string matching the
original arguments used to create the enumeration::

    >>> str(pizza_night)
    'fri'
    >>> shirt_colour.index
    2

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
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
#%attr(755,root,root) %{_bindir}/*
%{python_sitelib}/*
%doc LICENSE.GPL-3
#%doc build/*

%changelog
* Mon Nov 23 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 0.4.6-0.1
- Build RPM with setup.py
