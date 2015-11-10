%define name python-Markdown
%define realname Markdown
%define version 2.6.4
%define unmangled_version 2.6.4
%define release 0.1

Summary: Python implementation of Markdown.
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{realname}-%{unmangled_version}.tar.gz
License: BSD License
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Waylan Limberg <waylan.limberg [at] icloud.com>
Url: https://pythonhosted.org/Markdown/
# Added for compilation
BuildRequires: python-setuptools
# Added for poorly named RHEL module
Obsoletes: python-markdown <= %{version}
Conflicts: python-markdown
Provides: python-markdown = %{name}-%{version}

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
%setup -n %{realname}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
