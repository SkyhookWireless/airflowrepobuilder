%{?scl:%scl_package python-pycparser}
%{!?scl:%global pkg_name %{name}}

%global srcname pycparser

Name: %{?scl_prefix}python-pycparser
Summary: C parser in Python
Version: 2.14
Release: 0.1%{?dist}
Source0: http://pypi.python.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Eli Bendersky <eliben@gmail.com>
Url: https://github.com/eliben/pycparser
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools

%description
        pycparser is a complete parser of the C language, written in
        pure Python using the PLY parsing library.
        It parses C code into an AST and can serve as a front-end for
        C compilers or analysis tools.

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
%doc CHANGES LICENSE README.rst
#%doc build/*

%changelog
* Mon Nov 23 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 2.14-0.1
- Provide full URL for source
- Use wildcard for bindir files
