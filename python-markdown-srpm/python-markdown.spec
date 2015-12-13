%{?scl:%scl_package python-markdown}
%{!?scl:%global pkg_name %{name}}

%define name python-Markdown
%define srcname Markdown

Summary: Python implementation of Markdown.
Name: %{?scl_prefix}python-markdown
Version: 2.6.5
Release: 0.1%{?dist}
Source0: https://pypi.python.org/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz
License: BSD License
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Waylan Limberg <waylan.limberg [at] icloud.com>
Url: https://pythonhosted.org/Markdown/
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
Requires: %{?scl_prefix}python(abi)
# Avoid python naming confusion
Provides: %{?scl_prefix}python-%{srcname} = %{version}-%{release}

%description
This is a Python implementation of John Gruber's Markdown_.
It is almost completely compliant with the reference implementation,
though there are a few known issues. See Features_ for information
on what exactly is supported and what is not. Additional features are
supported by the `Available Extensions`_.

.. _Markdown: http://daringfireball.net/projects/markdown/
.. _Features: https://pythonhosted.org/Markdown/index.html#Features
.. _`Available Extensions`: https://pythonhosted.org/Markdown/extensions/index.html

Support
=======

You may ask for help and discuss various other issues on the
`mailing list`_ and report bugs on the `bug tracker`_.

.. _`mailing list`: http://lists.sourceforge.net/lists/listinfo/python-markdown-discuss
.. _`bug tracker`: http://github.com/waylan/Python-Markdown/issues


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
%doc INSTALL.md LICENSE.md README.md

%changelog
* Sat Nov 28 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 2.6.5-0.1
- Update tto 2.6.5 for airflow 1.6.1 dependencies

* Mon Nov 16 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 2.6.4-0.2
- Provide full URL for Source
- Add python(abi) dependency

* Mon Nov  9 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 2.6.4-0.1
- Activate python2.7 build and dependenies
