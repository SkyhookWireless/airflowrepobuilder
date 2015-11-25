%{?scl:%scl_package python-beaker}
%{!?scl:%global pkg_name %{name}}

%global srcname Beaker

#%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name: %{?scl_prefix}python-beaker
Version: 1.3.1
#Release: 7%{?dist}
Release: 0.1%{?dist}
Summary: WSGI middleware layer to provide sessions

Group: Development/Languages
License: BSD
URL: http://beaker.groovie.org/
Source0: https://pypi.python.org/packages/source/B/Beaker/Beaker-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
#BuildRequires: python-setuptools-devel
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
Requires: %{?scl_prefix}python(abi)
Patch0: beaker-hmac2.4.patch
Patch1: python-beaker-absimport.patch
Patch2: python-beaker-middleware-config.patch
Patch3: bz983292-Session-id-based-on-sha1-base64-instead-of-md5-2.patch

%description
Beaker is a caching library that includes Session and Cache objects built on
Myghty's Container API used in MyghtyUtils. WSGI middleware is also included to
manage Session objects and signed cookies.


%prep
%setup -q -n Beaker-%{version}
%patch0 -p1 -b .hashlib
%patch1 -p0 -b .absimport
%patch2 -p1 -b .middleconfig
%patch3 -p1 -b .bz983292


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
%doc LICENSE CHANGELOG
%{python_sitelib}/beaker/
%{python_sitelib}/Beaker*


%changelog
* Wed Nov 25 2015 Nico Kadel-Garcia <nkadel@skyhookwireless.com> - 1.3.1=0.1
- Port to python27

* Tue Aug 6 2013 Jan Pokorny <jpokorny@redhat.com> - 1.3.1-7
- Fix python-beaker does not work in FIPS environment
Resolves: rhbz#983292
Related:  rhbz#956360

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 21 2009 Kyle VanderBeek <kylev@kylev.com> - 1.3.1-5
- Add patch based on upstream hg 403ef7c82d32 for config overwriting that
  breaks Pylons unit tests

* Sat Jun 27 2009 Luke Macken <lmacken@redhat.com> - 1.3.1-4
- Add a patch to remove the use of __future__.absolute_import in the google
  backend

* Sat Jun 20 2009 Toshio Kuratomi <toshio@fedoraproject.org> - 1.3.1-3
- Different hmac patch suitable for upstream inclusion.

* Tue Jun 02 2009 Luke Macken <lmacken@redhat.com> - 1.3.1-2
- Add a patch to remove Beaker's use of hashlib on Python2.4,
  due to incompatiblities with Python's hmac module (#503772)

* Sun May 31 2009 Luke Macken <lmacken@redhat.com> - 1.3.1-1
- Update to 1.3.1

* Tue Apr 07 2009 Felix Schwarz <felix.schwarz@oss.schwarz.eu> - 1.3-1
- Update to 1.3
 
* Sun Apr 05 2009 Felix Schwarz <felix.schwarz@oss.schwarz.eu> - 1.2.3-1
- Update to 1.2.3
 
* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 06 2009 Luke Macken <lmacken@redhat.com> - 1.1.3-1
- Update to 1.1.3

* Sat Dec 20 2008 Felix Schwarz <felix.schwarz@oss.schwarz.eu> - 1.1.2-1
- Update to 1.1.2
 
* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.0.3-2
- Rebuild for Python 2.6

* Tue Jun 24 2008 Felix Schwarz <felix.schwarz@oss.schwarz.eu> - 1.0.3-1
- Update to 1.0.3.

* Tue Jun 24 2008 Kyle VanderBeek <kylev@kylev.com> - 0.9.5-1
- Update to 0.9.5.
- Remove license patch which is now corrected upstream.

* Mon May 12 2008 Kyle VanderBeek <kylev@kylev.com> - 0.9.4-4
- Fix files to not use wildcard, fixing dir ownership

* Mon May 12 2008 Kyle VanderBeek <kylev@kylev.com> - 0.9.4-3
- Corrected license

* Mon May 12 2008 Kyle VanderBeek <kylev@kylev.com> - 0.9.4-2
- More restrictive file includes for safety

* Sun May 11 2008 Kyle VanderBeek <kylev@kylev.com> - 0.9.4-1
- Update to 0.9.4 (security fix)
- Fix rpmlint complaints, add CHANGELOG and LICENSE

* Wed Apr  9 2008 Kyle VanderBeek <kylev@kylev.com> - 0.9.3-1
- Initial version.
