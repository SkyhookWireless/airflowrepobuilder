%{?scl:%scl_package python-billiard}
%{!?scl:%global pkg_name %{name}}

%global srcname billiard

Name: %{?scl_prefix}python-billiard
Version:        0.3.1
Release:        0.1%{?dist}
Summary:        Multiprocessing Pool Extensions

Group:          Development/Languages
License:        BSD
URL:            https://pypi.python.org/pypi/billiard
Source0:        https://pypi.python.org/packages/source/b/%{srcname}/%{srcname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools

%description
This package contains extensions to the multiprocessing Pool.

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
%doc AUTHORS Changelog LICENSE README TODO docs/
%{python_sitelib}/%{srcname}/
%{python_sitelib}/%{srcname}*.egg-info

%changelog
* Tue Nov 24 2015 Nico Kadel-Garcia <nkadel@skyhookwireless.com> - 0.3.1-0.1
- Port to python27

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Aug 14 2010 Fabian Affolter <fabian@bernewireless.net> - 0.3.1-2
- TODO removed

* Sat Jul 03 2010 Fabian Affolter <fabian@bernewireless.net> - 0.3.1-1
- Initial package
