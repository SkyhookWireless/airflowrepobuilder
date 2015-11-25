%{?scl:%scl_package python-unicodecsv}
%{!?scl:%global pkg_name %{name}}

%global srcname unicodecsv

Summary: Python2's stdlib csv module is nice, but it doesn't support unicode. This module is a drop-in replacement which *does*.
Name: %{?scl_prefix}python-unicodecsv
Version: 0.14.1
Release: 0.2%{?dist}
Source0: https://pypi.python.org/packages/source/u/%{srcname}/%{srcname}-%{version}.tar.gz
License: BSD License
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Jeremy Dunck <jdunck@gmail.com>
Url: https://github.com/jdunck/python-unicodecsv
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
Requires: %{?scl_prefix}python(abi)

%description
unicodecsv
==========

The unicodecsv is a drop-in replacement for Python 2.7's csv module which supports unicode strings without a hassle.  Supported versions are python 2.7, 3.3, 3.4, 3.5, and pypy 2.4.0.

More fully
----------

Python 2's csv module doesn't easily deal with unicode strings, leading to the dreaded "'ascii' codec can't encode characters in position ..." exception.

You can work around it by encoding everything just before calling write (or just after read), but why not add support to the serializer?

.. code-block:: pycon

   >>> import unicodecsv as csv
   >>> from io import BytesIO
   >>> f = BytesIO()
   >>> w = csv.writer(f, encoding='utf-8')
   >>> _ = w.writerow((u'é', u'ñ'))
   >>> _ = f.seek(0)
   >>> r = csv.reader(f, encoding='utf-8')
   >>> next(r) == [u'é', u'ñ']
   True

Note that unicodecsv expects a bytestream, not unicode -- so there's no need to use `codecs.open` or similar wrappers.  Plain `open(..., 'rb')` will do.

(Version 0.14.0 dropped support for python 2.6, but 0.14.1 added it back.  See c0b7655248c4249 for the mistaken, breaking change.)


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
%doc README.rst
#%doc build/*

%changelog
* Fri Nov 20 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 0.14.1-0.2
- Create base RPM from setup.py
- Activate python2.7 build and dependenies
- Add python(abi) dependency
