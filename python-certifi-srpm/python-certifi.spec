%{?scl:%scl_package python-certifi}
%{!?scl:%global pkg_name %{name}}

%define srcname certifi

Summary: Python package for providing Mozilla's CA Bundle.
Name: %{?scl_prefix}python-certifi
# Lock old version for AWS compatibility!
Version: 2015.04.28
Release: 0.2%{?dist}
Source0: https://pypi.python.org/packages/source/c/%{srcname}/%{srcname}-%{version}.tar.gz
License: ISC
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Kenneth Reitz <me@kennethreitz.com>
Url: http://certifi.io/
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
Requires: %{?scl_prefix}python(abi)

%description
Certifi: Python SSL Certificates
================================

`Certifi`_ is a carefully curated collection of Root Certificates for
validating the trustworthiness of SSL certificates while verifying the identity
of TLS hosts. It has been extracted from the `Requests`_ project.

Installation
------------

``certifi`` is available on PyPI. Simply install it with ``pip``::

    $ pip install certifi

Usage
-----

To reference the installed CA Bundle, you can use the built-in function::

    >>> import certifi

    >>> certifi.where()
    '/usr/local/lib/python2.7/site-packages/certifi/cacert.pem'

Enjoy!

1024-bit Root Certificates
~~~~~~~~~~~~~~~~~~~~~~~~~~

Browsers and certificate authorities have concluded that 1024-bit keys are
unacceptably weak for certificates, particularly root certificates. For this
reason, Mozilla has removed any weak (i.e. 1024-bit key) certificate from its
bundle, replacing it with an equivalent strong (i.e. 2048-bit or greater key)
certifiate from the same CA. Because Mozilla removed these certificates from
its bundle, ``certifi`` removed them as well.

Unfortunately, old versions of OpenSSL (less than 1.0.2) sometimes fail to
validate certificate chains that use the strong roots. For this reason, if you
fail to validate a certificate using the ``certifi.where()`` mechanism, you can
intentionally re-add the 1024-bit roots back into your bundle by calling
``certifi.old_where()`` instead. This is not recommended in production: if at
all possible you should upgrade to a newer OpenSSL. However, if you have no
other option, this may work for you.

.. _`Certifi`: http://certifi.io/en/latest/
.. _`Requests`: http://docs.python-requests.org/en/latest/


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
#%attr(755,root,root) %{_bindir}/*
%{python_sitelib}/*
%doc LICENSE README.rst
#%doc build/*

%changelog
* Mon Nov 23 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 2015.04.28-0.1
- Build from setup.py
- Lock version to AWS compatible 2015.04.28
- Add python(abi) dependency

