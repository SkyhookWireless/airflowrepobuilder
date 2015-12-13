%{?scl:%scl_package python-flake8}
%{!?scl:%global pkg_name %{name}}

%global srcname flake8

Summary: the modular source code checker: pep8, pyflakes and co
Name: %{?scl_prefix}python-flake8
Version: 2.5.0
Release: 0.1%{?dist}
Source0: https://pypi.python.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Ian Cordasco <graffatcolmingov@gmail.com>
Url: https://gitlab.com/pycqa/flake8
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
Requires: %{?scl_prefix}python(abi)
# Avoid python naming confusion
Provides: %{?scl_prefix}python-%{srcname} = %{version}-%{release}

%description
======
Flake8
======

Flake8 is a wrapper around these tools:

- PyFlakes
- pep8
- Ned Batchelder's McCabe script

Flake8 runs all the tools by launching the single ``flake8`` script.
It displays the warnings in a per-file, merged output.

It also adds a few features:

- files that contain this line are skipped::

    # flake8: noqa

- lines that contain a ``# noqa`` comment at the end will not issue warnings.
- a Git and a Mercurial hook.
- a McCabe complexity checker.
- extendable through ``flake8.extension`` entry points.

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
%doc CHANGES.rst CONTRIBUTORS.txt LICENSE README.rst
#%doc build/*

%changelog
* Mon Nov 16 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 0.8.3-0.2
- Provide full URL for source
- Use wildcard for bindir files
* Mon Nov  9 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 0.8.3-0.1
- Activate python2.7 build and dependenies
