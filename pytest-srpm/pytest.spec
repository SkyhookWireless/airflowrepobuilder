%{?scl:%scl_package pytest}
%{!?scl:%global pkg_name %{name}}

%global srcname pytest

%global pylib_version 1.4.12

Name: %{?scl_prefix}pytest
Version:        2.3.5
Release:        0.2%{?dist}
Summary:        Simple powerful testing with Python

Group:          Development/Languages
License:        MIT
URL:            http://pytest.org
Source0: https://pypi.python.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
BuildRequires:  %{?scl_prefix}python-py >= %{pylib_version}
BuildRequires:  %{?scl_prefix}python-docutils
BuildRequires:  %{?scl_prefix}python-sphinx
Requires:       %{?scl_prefix}python-setuptools
# Added for python27 build
BuildRequires:  %{?scl_prefix}python-alabaster
BuildRequires:  %{?scl_prefix}python-sphinx_rtd_theme
BuildRequires:  %{?scl_prefix}pytz

# Avoid python naming confusion
Provides: %{?scl_prefix}python-%{srcname} = %{version}-%{release}
# pytest was separated from pylib at that point
Conflicts:      %{?scl_prefix}python-py < 1.4.0

# used by the testsuite, if present:
%if 0%{?fedora}
# if pexpect is present, the testsuite fails on F19 due to
# http://bugs.python.org/issue17998
#BuildRequires:  %{?scl_prefix}python-pexpect
BuildRequires:  %{?scl_prefix}python-mock
BuildRequires:  %{?scl_prefix}python-twisted-core
%endif # fedora
# Deal with old python-pytest module name
Provides: python-pytest = %{version}-%{release}
Obsoletes: python-pytest < %{version}-%{release}

%description
py.test provides simple, yet powerful testing for Python.


%prep
%setup -q -n %{srcname}-%{version}

%build
%{?scl:scl enable %{scl} "}
%{__python} setup.py build
%{?scl:"}

for l in doc/* ; do
%{?scl:scl enable %{scl} "}
   make -C $l html PYTHONPATH=$(pwd)
%{?scl:"}
done

%install
%{__rm} -rf %{buildroot}
%{?scl:scl enable %{scl} "}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
%{?scl:"}

# remove shebangs from all scripts
find %{buildroot}%{python_sitelib} -name '*.py' \
     -exec sed -i -e '1{/^#!/d}' {} \;

mkdir -p _htmldocs/html
for l in doc/* ; do
  # remove hidden file
  rm ${l}/_build/html/.buildinfo
  mv ${l}/_build/html _htmldocs/html/${l##doc/}
done

%{?scl:scl enable %{scl} "}
rst2html README.rst > README.html
%{?scl:"}

# use 2.X per default
pushd %{buildroot}%{_bindir}
ln -snf py.test-2.* py.test
popd

%clean
%{__rm} -rf %{buildroot}

%check
%{?scl:scl enable %{scl} "}
PYTHONPATH=%{buildroot}%{python_sitelib} \
  %{buildroot}%{_bindir}/py.test -r s
%{?scl:"}

%files
%defattr(-,root,root,-)
%doc CHANGELOG LICENSE README.html
%doc _htmldocs/html
%{_bindir}/py.test
%{_bindir}/py.test-2.*
%{python_sitelib}/*


%if 0%{?with_python3}
%files -n python3-pytest
%defattr(-,root,root,-)
%doc CHANGELOG LICENSE README.html
%doc _htmldocs/html
%{_bindir}/py.test-3.*
%{python3_sitelib}/*
%endif # with_python3


%changelog
* Sat Dec 12 2015 Nico Kadel-Garcia <nkadel@skyhookwireless.com> - 2.3.5-0.2
- Activate sphinx_rtd_theme dependency

* Fri Nov 26 2015 Nico Kadel-Garcia <nkadel@skyhookwireless.com> - 2.3.5-0.1
- Port to python27

* Thu Jun 13 2013 Thomas Moschny <thomas.moschny@gmx.de> - 2.3.5-3
- Disable tests using pexpect for now, fails on F19.

* Wed Jun 12 2013 Thomas Moschny <thomas.moschny@gmx.de> - 2.3.5-2
- Use python-sphinx for rhel > 6 (rhbz#973318).
- Update BR to use python-pexpect instead of pexpect.

* Sat May 25 2013 Thomas Moschny <thomas.moschny@gmx.de> - 2.3.5-1
- Update to 2.3.5.
- Docutils needed now to build README.html.
- Add some BR optionally used by the testsuite.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 23 2012 Thomas Moschny <thomas.moschny@gmx.de> - 2.3.4-1
- Update to 2.3.4.

* Sun Oct 28 2012 Thomas Moschny <thomas.moschny@gmx.de> - 2.3.2-1
- Update to 2.3.2.

* Sun Oct 21 2012 Thomas Moschny <thomas.moschny@gmx.de> - 2.3.1-1
- Update to 2.3.1.
- Re-enable some tests, ignore others.
- Docs are available in English and Japanese now.

* Thu Oct 11 2012 Thomas Moschny <thomas.moschny@gmx.de> - 2.2.4-4
- Add conditional for sphinx on rhel.
- Remove rhel logic from with_python3 conditional.
- Disable failing tests for Python3.

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 2.2.4-3
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun  6 2012 Thomas Moschny <thomas.moschny@gmx.de> - 2.2.4-1
- Update to 2.2.4.

* Wed Feb  8 2012 Thomas Moschny <thomas.moschny@gmx.de> - 2.2.3-1
- Update to 2.2.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Dec 17 2011 Thomas Moschny <thomas.moschny@gmx.de> - 2.2.1-1
- Update to 2.2.1.

* Tue Dec 13 2011 Thomas Moschny <thomas.moschny@gmx.de> - 2.2.0-1
- Update to 2.2.0.

* Wed Oct 26 2011 Thomas Moschny <thomas.moschny@gmx.de> - 2.1.3-1
- Update to 2.1.3.

* Tue Sep 27 2011 Thomas Moschny <thomas.moschny@gmx.de> - 2.1.2-1
- Update to 2.1.2.

* Sat Sep  3 2011 Thomas Moschny <thomas.moschny@gmx.de> - 2.1.1-2
- Fix: python3 dependencies.

* Sun Aug 28 2011 Thomas Moschny <thomas.moschny@gmx.de> - 2.1.1-1
- Update to 2.1.1.

* Thu Aug 11 2011 Thomas Moschny <thomas.moschny@gmx.de> - 2.1.0-2
- Update Requires and BuildRequires tags.

* Tue Aug  9 2011 Thomas Moschny <thomas.moschny@gmx.de> - 2.1.0-1
- Update to 2.1.0.

* Mon May 30 2011 Thomas Moschny <thomas.moschny@gmx.de> - 2.0.3-1
- Update to 2.0.3.

* Thu Mar 17 2011 Thomas Moschny <thomas.moschny@gmx.de> - 2.0.2-1
- Update to 2.0.2.

* Sun Jan 16 2011 Thomas Moschny <thomas.moschny@gmx.de> - 2.0.0-1
- New package.
