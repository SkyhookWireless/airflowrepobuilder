%{?scl:%scl_package python-py2pack}
%{!?scl:%global pkg_name %{name}}

%global srcname py2pack

Name: %{?scl_prefix}python-py2pack
Version:        0.5.0
Release:        0.1%{?dist}
Url:            http://github.com/saschpe/py2pack
Summary:        Generate distribution packages from Python packages on PyPI
License:        GPLv2
Group:          Development/Languages
Source:         http://pypi.python.org/packages/source/p/%{srcname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
# py2pack is now architecture specific
#BuildArch:      noarch
# Libraries need to be explicitly included for scl compilation
BuildRequires:  libxslt-devel
BuildRequires:  libxml2-devel
BuildRequires:  %{?scl_prefix}python-argparse
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-lxml
BuildRequires:  %{?scl_prefix}python-jinja2
BuildRequires:  %{?scl_prefix}python-setuptools
BuildRequires:  %{?scl_prefix}python(abi)
Requires:       %{?scl_prefix}python-argparse
Requires:       %{?scl_prefix}python-jinja2
Requires:       %{?scl_prefix}python(abi)
# Avoid python naming confusion
Provides: %{?scl_prefix}python-%{srcname} = %{version}-%{release}

%description
This script allows to generate RPM spec or DEB dsc files from Python modules.
It allows to list Python modules or search for them on the Python Package Index
(PyPI). Conveniently, it can fetch tarballs and change logs making it an
universal tool to package Python modules.

%prep
%setup -q -n %{srcname}-%{version}

find -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python}|'

%build
# Old, non-python27 opotions
#CFLAGS="$RPM_OPT_FLAGS"  %{__python} setup.py build
# CFLAGS requirement evaporated with BuildRequire for python-lxml
%{?scl:scl enable %{scl} "}
%{__python} setup.py build
%{?scl:"}

%install
%{__rm} -rf %{buildroot}
%{?scl:scl enable %{scl} "}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
%{?scl:"}

# The setup script installs stuff into '/usr/local', move stuff around accordingly
install -d %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_prefix}/man/man1/%{srcname}.* %{buildroot}%{_mandir}/man1
chmod 0644 %{buildroot}%{_mandir}/man1/*
install -d %{buildroot}%{_docdir}/%{name}
mv %{buildroot}/%{_docdir}/%{srcname} %{buildroot}%{_docdir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_docdir}/%{name}
%{_mandir}/man1/%{srcname}.*
%{_bindir}/%{srcname}
%{python_sitelib}/%{srcname}*

%changelog
* Tue Dec 1 2015 Nico Kadel-Garcia <nkadel@skyhookwireless.com> - 0.5.0-0.1
- Enable python27 build
- Update to 0.5.0
- Discard python3 hooks
- Disable "noarch" setting, now architecture specific
- Add python-libxml dependency, to prevent downloading tarball
- Add libxml2-devel and libxsl2-devel dependencies explicitly
- Add -I/usr/include and -L flags explicitly

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Haïkel Guémar <hguemar@fedoraproject.org> - 0.4.4-1
- upstream 0.4.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri May 20 2011 Jerome Soyer <saispo@gmail.com> - 0.3.17-1
- Update to upstream release

* Mon May  9 2011 Jerome Soyer <saispo@gmail.com> - 0.3.15-2
- Fix inconsistent use of macros
- Set properly permission for chmod and install
- Totaly commented out the check section
- Disable python3 build since it's not fixed upstream
- Convert tab into spaces
- Use macro buildroot instead of $RPM_BUILD_ROOT

* Mon May  2 2011 Jerome Soyer <saispo@gmail.com> - 0.3.15-1
- Initial build
