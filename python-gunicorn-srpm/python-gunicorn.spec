%global srcname gunicorn

Name:           python-gunicorn
Version:        19.3.0
Release:        0.1
Url:            http://gunicorn.org
Summary:        WSGI HTTP Server for UNIX
License:        MIT
Group:          Development/Languages/Python
Source:         %{srcname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  python-devel
BuildRequires:  python-distribute
BuildRequires:  python-nose
BuildArch:      noarch
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

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

%build
python setup.py build

%install
python setup.py install -O1 --skip-build --prefix=%{_prefix} --root=%{buildroot}

%check
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
