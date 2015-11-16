%{?scl:%scl_package python-python-editor}
%{!?scl:%global pkg_name %{name}}

%global srcname python-editor

Summary: Programmatically open an editor, capture the result.
Name: %{?scl_prefix}python-python-editor
Version: 0.4
Release: 0.2%{?dist}
Source0: http://pypi.python.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
License: Apache
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{srcname}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Peter Ruibal <ruibalp@gmail.com>
Url: https://github.com/fmoo/python-editor
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools

%description
`python-editor` is a library that provides the `editor` module for programmatically
interfacing with your system's $EDITOR.

Examples
--------

```python
import editor
commit_msg = editor.edit(contents="# Enter commit message here")
```
Opens an editor, prefilled with the contents, `# Enter commit message here`.
When the editor is closed, returns the contents in variable `commit_msg`.


```python
import editor
editor.edit(file="README.txt")
```

%prep
%setup -q -n %{srcname}-%{version}
%{__sed} -i 's/\r//' LICENSE

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
#%attr(755,root,root) %{_bindir}/*
%{python_sitelib}/*
%doc LICENSE README.md
#%doc build/*

%changelog
* Mon Nov 16 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 0.4-0.2
- Provide full URL for source

* Mon Nov  9 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 0.4-0.1
- Build from setup.py

