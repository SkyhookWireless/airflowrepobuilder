%{?scl:%scl_package python-pysmbclient}
%{!?scl:%global pkg_name %{name}}

%global srcname PySmbClient

Summary: A convenient smbclient wrapper
Name: %{?scl_prefix}python-pysmbclient
Version: 0.1.3
Release: 0.1%{?dist}
Source0: https://pypi.python.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: nosklo <bucket.t.nosklo@0sg.net>
Url: http://bitbucket.org/nosklo/pysmbclient
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
Requires: %{?scl_prefix}python(abi)

%description
Python smbclient wrapper.

This is a wrapper that works by running the "smbclient" subprocess and providing
an API similar to the one provided by python `os` module.

It is an ugly hack, but it is here for anyone that finds it useful.

The programmer before me was using a "bash" file with lots of smbclient calls, 
so I think my solution is at least better.

Usage example:

>>> smb = smbclient.SambaClient(server="MYSERVER", share="MYSHARE", 
                                username='foo', password='bar', domain='baz')
>>> print smb.listdir("/")
[u'file1.txt', u'file2.txt']
>>> f = smb.open('/file1.txt')
>>> data = f.read()
>>> f.close()
>>> smb.rename(u'/file1.txt', u'/file1.old')


%prep
%setup -n %{srcname}-%{version}

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
%doc README
#%doc build/*

%changelog
* Mon Nov 30 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 0.1.3-0.1
- Build SRPM from setup.py
