%{?scl:%scl_package python-pip}
%{!?scl:%global pkg_name %{name}}

%global srcname pip

Summary: The PyPA recommended tool for installing Python packages.
Name: %{?scl_prefix}python-pip
Version: 7.1.2
Release: 0.1%{?dist}
Source0: http://pypi.python.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: The pip developers <python-virtualenv@groups.google.com>
Url: https://pip.pypa.io/
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools

%description
pip
===

The `PyPA recommended
<https://python-packaging-user-guide.readthedocs.org/en/latest/current.html>`_
tool for installing Python packages.

* `Installation <https://pip.pypa.io/en/stable/installing.html>`_
* `Documentation <https://pip.pypa.io/>`_
* `Changelog <https://pip.pypa.io/en/stable/news.html>`_
* `Github Page <https://github.com/pypa/pip>`_
* `Issue Tracking <https://github.com/pypa/pip/issues>`_
* `User mailing list <http://groups.google.com/group/python-virtualenv>`_
* `Dev mailing list <http://groups.google.com/group/pypa-dev>`_
* User IRC: #pypa on Freenode.
* Dev IRC: #pypa-dev on Freenode.


.. image:: https://pypip.in/v/pip/badge.png
        :target: https://pypi.python.org/pypi/pip

.. image:: https://secure.travis-ci.org/pypa/pip.png?branch=develop
   :target: http://travis-ci.org/pypa/pip


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
%attr(755,root,root) %{_bindir}/*
%{python_sitelib}/*
%doc AUTHORS.txt CHANGES.txt LICENSE.txt README.rst
#%doc build/*

%changelog
* Fri Nov 20 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 7.1.2-0.1
- Build RPM from setup.py for python2.7 pip
- Activate python2.7 build and dependenies
