%{?scl:%scl_package python-enum34}
%{!?scl:%global pkg_name %{name}}

%global srcname enum34

Name: %{?scl_prefix}python-enum34
Version:        1.0
Release:        0.1%{?dist}
Group:          Development/Libraries
Summary:        Backport of Python 3.4 Enum
License:        BSD
BuildArch:      noarch
URL:            https://pypi.python.org/pypi/enum34
Source0:        https://pypi.python.org/packages/source/e/%{srcname}/%{srcname}-%{version}.tar.gz
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
Requires: %{?scl_prefix}python(abi)

%description
Python 3.4 introduced official support for enumerations.  This is a
backport of that feature to Python 3.3, 3.2, 3.1, 2.7, 2.5, 2.5, and 2.4.

An enumeration is a set of symbolic names (members) bound to unique,
constant values. Within an enumeration, the members can be compared by
identity, and the enumeration itself can be iterated over.

This module defines two enumeration classes that can be used to define
unique sets of names and values: Enum and IntEnum. It also defines one
decorator, unique, that ensures only unique member names are present
in an enumeration.


%prep
%setup -q -n %{srcname}-%{version}

%build
%{?scl:scl enable %{scl} "}
%{__python} setup.py build
%{?scl:"}

%check
pushd %{buildroot}/%{python2_sitelib}
%{?scl:scl enable %{scl} "}
%{__python} enum/test_enum.py
%{?scl:"}
popd

%install
%{__rm} -rf %{buildroot}
%{?scl:scl enable %{scl} "}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
%{?scl:"}
# remove docs from sitelib, we'll put them in doc dir instead
rm -rf %{buildroot}%{python2_sitelib}/enum/{LICENSE,README,doc}

%files
%doc PKG-INFO enum/LICENSE enum/README enum/doc/enum.rst
%{python2_sitelib}/*

%changelog
* Tue Dec  1 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 1.0-0.1
- Activate python2.7 build and dependenies

* Mon Jul 21 2014 Matěj Cepl <mcepl@redhat.com> - 1.0-4
- No, we don’t have python3 in RHEL-7 :'(

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon May 26 2014 Eric Smith <brouhaha@fedoraproject.org> 1.0-1
- Updated to latest upstream.

* Mon Mar 17 2014 Eric Smith <brouhaha@fedoraproject.org> 0.9.23-1
- Updated to latest upstream.
- Spec updated per review comments (#1033975).

* Sun Nov 24 2013 Eric Smith <brouhaha@fedoraproject.org> 0.9.19-1
- Initial version.
