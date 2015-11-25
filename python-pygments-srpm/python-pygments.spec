%{?scl:%scl_package python-pygments}
%{!?scl:%global pkg_name %{name}}

%global srcname Pygments

Summary: Pygments is a syntax highlighting package written in Python.
Name: %{?scl_prefix}python-pygments
Version: 2.0.2
Release: 0.3%{?dist}
Source0: https://pypi.python.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
License: BSD License
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Georg Brandl <georg@python.org>
Url: http://pygments.org/
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
Requires: %{?scl_prefix}python(abi)

%description
Pygments
    ~~~~~~~~

    Pygments is a syntax highlighting package written in Python.

    It is a generic syntax highlighter suitable for use in code hosting, forums,
    wikis or other applications that need to prettify source code.  Highlights
    are:

    * a wide range of over 300 languages and other text formats is supported
    * special attention is paid to details, increasing quality by a fair amount
    * support for new languages and formats are added easily
    * a number of output formats, presently HTML, LaTeX, RTF, SVG, all image       formats that PIL supports and ANSI sequences
    * it is usable as a command-line tool and as a library

    :copyright: Copyright 2006-2014 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.


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
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%attr(755,root,root) %{_bindir}/*
%{python_sitelib}/*
%doc AUTHORS CHANGES LICENSE README.rst
#%doc build/*

%changelog
* Mon Nov 16 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 2.0.2-0.2
- Provide full URL for source
- Replace "realname" with "srcname" for consistency
- Add python(abi) dependency

* Mon Nov  9 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 2.0.2-0.1
- Activate python2.7 build and dependenies
