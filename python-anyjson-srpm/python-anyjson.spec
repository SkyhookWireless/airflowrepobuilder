%{?scl:%scl_package python-anyjson}
%{!?scl:%global pkg_name %{name}}

%global srcname anyjson

Summary: Wraps the best available JSON implementation available in a common interface
Name: %{?scl_prefix}python-anyjson
Version: 0.3.3
Release: 0.2%{?dist}
Source0: https://pypi.python.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Rune Halvorsen <runefh@gmail.com>
Url: http://bitbucket.org/runeh/anyjson/
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
Requires: %{?scl_prefix}python(abi)

%description
##############################
anyjson - JSON library wrapper
##############################

Overview
--------

Anyjson loads whichever is the fastest JSON module installed and provides
a uniform API regardless of which JSON implementation is used.

Originally part of carrot (http://github.com/ask/carrot/)

Examples
--------

To serialize a python object to a JSON string, call the `serialize` function:

>>> import anyjson
>>> anyjson.serialize(["test", 1, {"foo": 3.141592}, "bar"])
'["test", 1, {"foo": 3.141592}, "bar"]'

Conversion the other way is done with the `deserialize` call.

>>> anyjson.deserialize("""["test", 1, {"foo": 3.141592}, "bar"]""")
['test', 1, {'foo': 3.1415920000000002}, 'bar']

Regardless of the JSON implementation used, the exceptions will be the same.
This means that trying to serialize something not compatible with JSON
raises a TypeError:

>>> anyjson.serialize([object()])
Traceback (most recent call last):
  <snipped traceback>
TypeError: object is not JSON encodable

And deserializing a JSON string with invalid JSON raises a ValueError:

>>> anyjson.deserialize("""['missing square brace!""")
Traceback (most recent call last):
  <snipped traceback>
ValueError: cannot parse JSON description


Contact
-------

The module is maintaned by Rune F. Halvorsen <runefh@gmail.com>.
The project resides at http://bitbucket.org/runeh/anyjson . Bugs and feature
requests can be submitted there. Patches are also very welcome.

Changelog
---------

See CHANGELOG file

License
-------

see the LICENSE file


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
%doc CHANGELOG LICENSE README
#%doc build/*

%changelog
* Mon Nov 16 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 0.8.3-0.2
- Provide full URL for source
- Use wildcard for bindir files
- Add python(abi) dependency
