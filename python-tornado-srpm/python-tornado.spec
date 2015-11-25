%{?scl:%scl_package python-tornado}
%{!?scl:%global pkg_name %{name}}

%global srcname tornado

Summary: Tornado is a Python web framework and asynchronous networking library, originally developed at FriendFeed.
Name: %{?scl_prefix}python-tornado
Version: 4.3
Release: 0.2%{?dist}
Source0: https://pypi.python.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
License: https://www.apache.org/licenses/LICENSE-2.0
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Facebook <python-tornado@googlegroups.com>
Url: http://www.tornadoweb.org/
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
Requires: %{?scl_prefix}python(abi)

%description
Tornado Web Server
==================

`Tornado <http://www.tornadoweb.org>`_ is a Python web framework and
asynchronous networking library, originally developed at `FriendFeed
<http://friendfeed.com>`_.  By using non-blocking network I/O, Tornado
can scale to tens of thousands of open connections, making it ideal for
`long polling <http://en.wikipedia.org/wiki/Push_technology#Long_polling>`_,
`WebSockets <http://en.wikipedia.org/wiki/WebSocket>`_, and other
applications that require a long-lived connection to each user.

Hello, world
------------

Here is a simple "Hello, world" example web app for Tornado:

.. code-block:: python

    import tornado.ioloop
    import tornado.web

    class MainHandler(tornado.web.RequestHandler):
        def get(self):
            self.write("Hello, world")

    def make_app():
        return tornado.web.Application([
            (r"/", MainHandler),
        ])

    if __name__ == "__main__":
        app = make_app()
        app.listen(8888)
        tornado.ioloop.IOLoop.current().start()

This example does not use any of Tornado's asynchronous features; for
that see this `simple chat room
<https://github.com/tornadoweb/tornado/tree/stable/demos/chat>`_.

Documentation
-------------

Documentation and links to additional resources are available at
http://www.tornadoweb.org


%prep
%setup -q -n %{srcname}-%{version}

%build
export CLAGS="$RPM_OPT_FLAGS"
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
#%{python_sitelib}/*
%{python_sitearch}/*
# No license included yet
#%doc CHANGES LICENSE README.rst
#%doc build/*

%changelog
* Tue Nov 24  2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 4.3-0.1
- Build RPM from setup.py
- Adapt for python2
- Add python(abi) dependency
