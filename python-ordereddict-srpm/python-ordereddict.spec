%{?scl:%scl_package python-ordereddict}
%{!?scl:%global pkg_name %{name}}

%global srcname ordereddict

#%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name: %{?scl_prefix}python-ordereddict
Version:        1.1
Release:        0.2%{?dist}
Summary:        Implementation of Python 2.7's OrderedDict
Group:          Development/Languages
License:        MIT
URL:            https://pypi.python.org/pypi/ordereddict
Source0:        https://pypi.python.org/packages/source/o/ordereddict/ordereddict-1.1.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
Requires: %{?scl_prefix}python(abi)

%description
Drop-in substitute for Py2.7's new collections.OrderedDict.
Originally based on http://code.activestate.com/recipes/576693/

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
%doc LICENSE
%{python_sitelib}/*

%changelog
* Tue Nov 24 2015 Nico Kadel-Garcia <nkadel@skyhookwireless.com> - 1.1-0.1
- Port to python27
- Add python(abi) dependency

* Thu Oct 28 2010 James Ni <jni@redhat.com> 1.1-2
- Modify the spec file and update to upstream source

* Wed Jul 14 2010 James Ni <jni@redhat.com> 1.1-1
- Initial RPM release
