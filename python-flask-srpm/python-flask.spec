%{?scl:%scl_package python-flask}
%{!?scl:%global pkg_name %{name}}

%global srcname Flask

Summary: A microframework based on Werkzeug, Jinja2 and good intentions
Name: %{?scl_prefix}python-flask
# Set for RHEL 7 updates
Epoch: 1
Version: 0.10.1
Release: 0.4%{?dist}
Source0: https://pypi.python.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Armin Ronacher <armin.ronacher@active-4.com>
Url: http://github.com/mitsuhiko/flask/
# Added for compilation
BuildRequires: %{?scl_prefix}python-devel
BuildRequires: %{?scl_prefix}python-setuptools
Requires: %{?scl_prefix}python(abi)
# Avoid python naming confusion
Provides: %{?scl_prefix}python-%{srcname} = %{version}-%{release}

%description
Flask
-----

Flask is a microframework for Python based on Werkzeug, Jinja 2 and good
intentions. And before you ask: It's BSD licensed!

Flask is Fun
````````````

.. code:: python

    from flask import Flask
    app = Flask(__name__)

    @app.route("/")
    def hello():
        return "Hello World!"

    if __name__ == "__main__":
        app.run()

And Easy to Setup
`````````````````

.. code:: bash

    $ pip install Flask
    $ python hello.py
     * Running on http://localhost:5000/

Links
`````

* `website <http://flask.pocoo.org/>`_
* `documentation <http://flask.pocoo.org/docs/>`_
* `development version
  <http://github.com/mitsuhiko/flask/zipball/master#egg=Flask-dev>`_



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
%{python_sitelib}/*
%doc AUTHORS CHANGES LICENSE README
#%doc build/*

%changelog
* Sun Dec 13 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 0.8.3-0.3
- Add Epoch of 1 to avoid RHEL 7 deployment ocnflicts.

* Mon Nov 16 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 0.8.3-0.2
- Provide full URL for source
- Add python(abi) dependency

* Mon Nov  9 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 0.8.3-0.1
- Activate python2.7 build and dependenies
