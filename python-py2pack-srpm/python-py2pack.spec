%if (0%{?fedora} > 12 || 0%{?rhel} > 6)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

#doesn't support python3 at this time
%global with_python3 0

%define mod_name py2pack

Name:           python-%{mod_name}
Version:        0.4.10
Release:        0.1%{?dist}
Url:            http://github.com/saschpe/py2pack
Summary:        Generate distribution packages from Python packages on PyPI
License:        GPLv2
Group:          Development/Languages
Source:         http://pypi.python.org/packages/source/p/%{mod_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  python-argparse
BuildRequires:  python-devel
BuildRequires:  python-jinja2
Requires:       python-argparse
Requires:       python-jinja2
%if 0%{?with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-jinja2
%endif # with_python3

%description
This script allows to generate RPM spec or DEB dsc files from Python modules.
It allows to list Python modules or search for them on the Python Package Index
(PyPI). Conveniently, it can fetch tarballs and change logs making it an
universal tool to package Python modules.

%if 0%{?with_python3}
%package -n python3-%{mod_name}
Summary:        General purpose template engine
Group:          Development/Languages
Requires:       python3-argparse
Requires:       python3-jinja2

%description -n python3-%{mod_name}
This script allows to generate RPM "spec" or DEB "dsc" files from Python modules.
It allows to list Python modules or search for them on the Python Package Index
(PyPI). Conveniently, it can fetch tarballs and change logs making it an
universal tool to package Python modules.
%endif #with_python3

%prep
%setup -q -n %{mod_name}-%{version}

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
find %{py3dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'
%endif # with_python3

find -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python}|'

%build
CFLAGS="$RPM_OPT_FLAGS"  %{__python} setup.py build

%if 0%{?with_python3}
pushd %{py3dir}
CFLAGS="$RPM_OPT_FLAGS" %{__python3} setup.py build
popd
%endif # with_python3

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --prefix %{_prefix} --root %{buildroot}
# The setup script installs stuff into '/usr/local', move stuff around accordingly
install -d %{buildroot}%{_mandir}/man1
mv %{buildroot}/usr/man/man1/%{mod_name}.* %{buildroot}%{_mandir}/man1
chmod 0644 %{buildroot}%{_mandir}/man1/*
install -d %{buildroot}%{_docdir}/%{name}
mv %{buildroot}/%{_docdir}/%{mod_name} %{buildroot}%{_docdir}/%{name}
# No longer published in 0.4.10
#chmod 0755 %{buildroot}/%{_bindir}/* %{buildroot}/%{python_sitelib}/%{mod_name}/%{mod_name}*

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install -O1 --skip-build --prefix %{__prefix} --root %{buildroot}
# The setup script installs stuff into '/usr/local', move stuff around accordingly
install -d %{buildroot}%{_mandir}/man1
mv %{buildroot}/usr/man/man1/%{mod_name}.* %{buildroot}%{_mandir}/man1
chmod 0644 %{buildroot}%{_mandir}/man1/*
install -d %{buildroot}%{_docdir}/%{name}
mv %{buildroot}/%{_docdir}/%{mod_name} %{buildroot}%{_docdir}/%{name}
chmod 0755 %{buildroot}/%{_bindir}/* %{buildroot}/%{python_sitelib}/%{mod_name}/%{mod_name}*
popd
%endif # with_python3


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_docdir}/%{name}
%{_mandir}/man1/%{mod_name}.*
%{_bindir}/%{mod_name}
%{python_sitelib}/%{mod_name}*

%if 0%{?with_python3}
%files -n python3-%{mod_name}
%defattr(-,root,root,-)
%{_docdir}/%{name}
%{_mandir}/man1/%{mod_name}.*
%{_bindir}/%{mod_name}
%{python3_sitelib}/%{mod_name}*
%endif # with_python3


%changelog
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
