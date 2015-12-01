%{?scl:%scl_package python-eventlet}
%{!?scl:%global pkg_name %{name}}

%global srcname eventlet

Name: %{?scl_prefix}python-eventlet
Version:        0.15.2
Release:        0.1%{?dist}
Summary:        Highly concurrent networking library
Group:          Development/Libraries
License:        MIT
URL:            http://eventlet.net
Source0:        https://pypi.python.org/packages/source/e/eventlet/eventlet-%{version}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
#BuildArch:      noarch
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-greenlet
BuildRequires:  %{?scl_prefix}python-setuptools
#BuildRequires:  %{?scl_prefix}python-sphinx10
BuildRequires:  %{?scl_prefix}python-sphinx
BuildRequires:  %{?scl_prefix}python(abi)
Requires: %{?scl_prefix}python-greenlet
Requires: %{?scl_prefix}python(abi)

%description
Eventlet is a networking library written in Python. It achieves high
scalability by using non-blocking io while at the same time retaining
high programmer usability by using coroutines to make the non-blocking
io operations appear blocking at the source code level.

#%package doc
#Summary:        Documentation for %{name}
#Group:          Documentation
#Requires:       %{name} = %{version}-%{release}
#
#%description doc
#Documentation for the python-eventlet package.


%prep
%setup -q -n %{srcname}-%{version}
find -name '.*' -type f -exec rm {} \;
sed -i -e 's///g' tests/mock.py
sed -i -e '1d' eventlet/support/greendns.py

%build
%{?scl:scl enable %{scl} "}
%{__python} setup.py build
%{?scl:"}
# Disable doc building until sphix10 is available
##export PYTHONPATH="$( pwd ):$PYTHONPATH"
#pushd doc
#%{?scl:scl enable %{scl} "}
#make SPHINXBUILD=sphinx-1.0-build html
#%{?scl:"}
#rm _build/html/.buildinfo
#popd
chmod a-x tests/mock.py

%install
%{__rm} -rf %{buildroot}
%{?scl:scl enable %{scl} "}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
%{?scl:"}
# Do *not* put these in RPM!
rm -rf %{buildroot}/%{python_sitelib}/tests

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS LICENSE NEWS README.rst README.twisted
%{python_sitelib}/eventlet
%{python_sitelib}/eventlet*.egg-info

#%files doc
#%defattr(-,root,root,-)
#%doc doc/_build/html examples tests

%changelog
* Tue Dec  1 2015 Nico Kadel-Garcia <nkadel@skyhookwireless.com> 0.15.2-0.1
- Port to python27
- Disable doc building until sphinx10 available

* Tue Sep 02 2014 Pádraig Brady <pbrady@redhat.com> - 0.15.2-1
- Latest upstream

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Oct 28 2013 Alan Pevec <apevec@redhat.com> - 0.14.0-1
- Update to 0.14.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 20 2013 Pádraig Brady <P@draigBrady.com - 0.12.0-1
- Update to 0.12.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 12 2012 Pádraig Brady <P@draigBrady.com - 0.9.17-2
- fix waitpid() override to not return immediately

* Fri Aug 03 2012 Pádraig Brady <P@draigBrady.com - 0.9.17-1
- Update to 0.9.17

* Tue Mar 27 2012 Pádraig Brady <P@draigBrady.com - 0.9.16-5
- Update patch to avoid leak of _DummyThread objects

* Wed Feb 29 2012 Pádraig Brady <P@draigBrady.com - 0.9.16-4
- Apply a patch to avoid leak of _DummyThread objects

* Wed Nov 09 2011 Pádraig Brady <P@draigBrady.com - 0.9.16-3
- Apply a patch to support subprocess.Popen implementations
  that accept the timeout parameter, which is the case on RHEL >= 6.1

* Fri Oct 21 2011 Pádraig Brady <P@draigBrady.com> - 0.9.16-2
- Changed python-sphinx build dependency to python-sphinx10

* Sat Aug 27 2011 Kevin Fenzi <kevin@scrye.com> - 0.9.16-1
- Update to 0.9.16

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 08 2010 Lev Shamardin <shamardin@gmail.com> - 0.9.12-1
- Updated to version 0.9.12.

* Wed Jul 28 2010 Lev Shamardin <shamardin@gmail.com> - 0.9.9-1
- Updated to version 0.9.9.

* Wed Apr 14 2010 Lev Shamardin <shamardin@gmail.com> - 0.9.7-1
- Initial package version.
