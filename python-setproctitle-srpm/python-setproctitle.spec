%{?scl:%scl_package python-setproctitle}
%{!?scl:%global pkg_name %{name}}

%global srcname setproctitle

# Deal with python(abi) requirement
%{?scl:%filter_from_requires /^python(abi)/d}

# See if this helps lib64/libpython27.so discovery!
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}

Name: %{?scl_prefix}python-setproctitle
Version:        1.1.9
Release:        0.6%{?dist}
Summary:        Python module to customize a process title

License:        BSD
URL:            http://pypi.python.org/pypi/%{srcname}
Source0:        https://pypi.python.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
BuildRequires:  %{?scl_prefix}python-nose
BuildRequires:  %{?scl_prefix}python-tools
#Requires: %{?scl_prefix}python(abi)
# Avoid python naming confusion
Provides: %{?scl_prefix}python-%{srcname} = %{version}-%{release}
%{?filter_setup:
%filter_provides_in %{python_sitearch}/.*\.so$
%filter_setup
}

%description
Python module allowing a process to change its title as displayed by
system tool such as ps and top.

It's useful in multiprocess systems, allowing to identify tasks each forked
process is busy with. This technique has been used by PostgreSQL and OpenSSH.

It's based on PostgreSQL implementation which has proven to be portable.

%prep
%setup -q -n %{srcname}-%{version}

%build
# Remove CFLAGS=... for noarch packages (unneeded)
CFLAGS="$RPM_OPT_FLAGS"
%{?scl:scl enable %{scl} "}
%{__python} setup.py build
%{?scl:"}

%install
%{__rm} -rf %{buildroot}
export CFLAGS="%{optflags}"
%{?scl:scl enable %{scl} "}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
%{?scl:"}
chmod 0755 %{buildroot}%{python_sitearch}/setproctitle.so

#%check
#%{?scl:scl enable %{scl} "}
#make tests/pyrun2
## FIXME: tests are broken with python3
#%{?scl:"}

%files
%doc README.rst COPYRIGHT
# For arch-specific packages: sitearch
%{python_sitearch}/%{srcname}.so
%{python_sitearch}/%{srcname}-%{version}-*.egg-info

%changelog
* Wed Dec 16 2015 Nico Kadel-Garcia <nkadel@skyhookwireless.com> - 1.1.9-0.6
- Filtier out default pytyon(abi) requirement for scl build

* Sun Dec 13 2015 Nico Kadel-Garcia <nkadel@skyhookwireless.com> - 1.1.9-0.5
- Update to 1.1.9

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 1.1.6-5
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.1.6-4
- Mass rebuild 2013-12-27

* Wed Aug 7 2013 Andy Grover <agrover@redhat.com> - 1.1.6-3
- Remove with_python3 if rhel > 6

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug  4 2012 Haïkel Guémar <hguemar@fedoraproject.org> - 1.1.6-1
- upstream 1.1.6

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 05 2012 Haïkel Guémar <hguemar@fedoraproject.org> - 1.1.3-2
- enable tests execution
- spec cleaning

* Sun Jan 29 2012 Haïkel Guémar <hguemar@fedoraproject.org> - 1.1.3-1
- initial packaging

