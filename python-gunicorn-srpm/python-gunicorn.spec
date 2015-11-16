%{?scl:%scl_package python-gunicorn}
%{!?scl:%global pkg_name %{name}}

%global srcname gunicorn

Name: %{?scl_prefix}python-gunicorn
Version:        19.3.0
Release:        0.2%{?dist}
Url:            http://gunicorn.org
Summary:        WSGI HTTP Server for UNIX
License:        MIT
Group:          Development/Languages/Python
Source0:        http://pypi.python.org/packages/source/g/%{srcname}/%{srcname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
#BuildRequires:  python-devel
#BuildRequires:  python-distribute
#BuildRequires:  python-nose
BuildArch:      noarch
#%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%description
Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX. It's a pre-fork
worker model ported from Ruby's Unicorn_ project. The Gunicorn server is broadly
compatible with various web frameworks, simply implemented, light on server
resource usage, and fairly speedy.

%package        doc
Summary:        Documentation for %{mod}
Group:          Documentation/Other
Requires:       %{name} = %{version}

%description doc
This package contains Gunicorn documentation in reST and HTML formats.

%prep
%setup -q -n %{srcname}-%{version}
# coverage is disabled until pytest-cov in Fedora is updated to 1.7
sed -i -e '/pytest-cov/d' requirements_dev.txt

# need to remove gaiohttp worker from the Python 2 version, it is supported on 
# Python 3 only and it fails byte compilation on 2.x due to using "yield from"
rm gunicorn/workers/_gaiohttp.py*

%build
%{?scl:scl enable %{scl} "}
%{__python} setup.py build
%{?scl:"}

%install
%{__rm} -rf %{buildroot}
%{?scl:scl enable %{scl} "}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
%{?scl:"}

#%check
#python setup.py test

%files
%defattr(-,root,root,-)
%doc LICENSE NOTICE README.rst THANKS
%{_bindir}/gunicorn*
%{python_sitelib}/*

%files doc
%defattr(-,root,root,-)
#%doc doc/htdocs examples
%doc examples

%changelog
* Mon Nov 16 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 19.3.0-0.2
- Use full URL for Source

* Mon Nov  9 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 19.3.0-0.1
- Activate python2.7 build and dependenies
- Delete gunicorn/workers/_gaiohttp.py*, it requires python3.3 and is disabled
  in Fedora RPMs
