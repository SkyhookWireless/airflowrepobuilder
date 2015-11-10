%define name python-Pygments
%define realname Pygments
%define version 2.0.2
%define unmangled_version 2.0.2
%define unmangled_version 2.0.2
%define release 0.1

Summary: Pygments is a syntax highlighting package written in Python.
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{realname}-%{unmangled_version}.tar.gz
License: BSD License
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Georg Brandl <georg@python.org>
Url: http://pygments.org/
# Added for mock compilation
BuildRequires: python-setuptools
# Deal with RHEL python-pygments package
Obsoletes: python-pygments <= %{version}
Provides: python-pygments = %{version}

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
%setup -n %{realname}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
