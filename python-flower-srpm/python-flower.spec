%{?scl:%scl_package python-flower}
%{!?scl:%global pkg_name %{name}}

%global srcname flower

Summary: Celery Flower
Name: %{?scl_prefix}python-flower
Version: 0.8.3
Release: 0.2%{?dist}
Source0: https://pypi.python.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Mher Movsisyan <mher.movsisyan@gmail.com>
Url: https://github.com/mher/flower
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
Requires: %{?scl_prefix}python(abi)
Requires:  %{?scl_prefix}python-celery >= 2.5.0
Requires:  %{?scl_prefix}python-tornado >= 4.5.0
Requires:  %{?scl_prefix}python-babel
Requires:  %{?scl_prefix}python-pytz

%description
Celery Flower
=============

.. image:: https://img.shields.io/pypi/v/flower.svg
    :target: https://pypi.python.org/pypi/flower

.. image:: https://img.shields.io/pypi/dm/flower.svg
        :target: https://pypi.python.org/pypi/flower

.. image:: https://travis-ci.org/mher/flower.svg?branch=master
        :target: https://travis-ci.org/mher/flower

Flower is a web based tool for monitoring and administrating Celery clusters.

Features
--------

- Real-time monitoring using Celery Events

    - Task progress and history
    - Ability to show task details (arguments, start time, runtime, and more)
    - Graphs and statistics

- Remote Control

    - View worker status and statistics
    - Shutdown and restart worker instances
    - Control worker pool size and autoscale settings
    - View and modify the queues a worker instance consumes from
    - View currently running tasks
    - View scheduled tasks (ETA/countdown)
    - View reserved and revoked tasks
    - Apply time and rate limits
    - Configuration viewer
    - Revoke or terminate tasks

- Broker monitoring

    - View statistics for all Celery queues
    - Queue length graphs

- HTTP API
- Basic Auth and Google OpenID authentication

API
---

Flower API enables to manage the cluster via REST API, call tasks and
receive task events in real-time via WebSockets.

For example you can restart worker's pool by: ::

    $ curl -X POST http://localhost:5555/api/worker/pool/restart/myworker

Or call a task by: ::

    $ curl -X POST -d '{"args":[1,2]}' http://localhost:5555/api/task/async-apply/tasks.add

Or terminate executing task by: ::

    $ curl -X POST -d 'terminate=True' http://localhost:5555/api/task/revoke/8a4da87b-e12b-4547-b89a-e92e4d1f8efd

Or receive task completion events in real-time:

.. code-block:: javascript 

    var ws = new WebSocket('ws://localhost:5555/api/task/events/task-succeeded/');
    ws.onmessage = function (event) {
        console.log(event.data);
    }

For more info checkout `API Reference`_ and `examples`_.

.. _API Reference: http://flower.readthedocs.org/en/latest/api.html
.. _examples: http://nbviewer.ipython.org/urls/raw.github.com/mher/flower/master/docs/api.ipynb

Installation
------------

PyPI version: ::

    $ pip install flower

Development version: ::

    $ pip install https://github.com/mher/flower/zipball/master

Usage
-----

Launch the server and open http://localhost:5555: ::

    $ flower --port=5555

Or launch from celery: ::

    $ celery flower -A proj --address=127.0.0.1 --port=5555

Broker URL and other configuration options can be passed through the standard Celery options: ::

    $ celery flower -A proj --broker=amqp://guest:guest@localhost:5672//

Documentation
-------------

Documentation is available at `Read the Docs`_ and `IPython Notebook Viewer`_

.. _Read the Docs: http://flower.readthedocs.org
.. _IPython Notebook Viewer: http://nbviewer.ipython.org/urls/raw.github.com/mher/flower/master/docs/api.ipynb

Screenshots
-----------

.. image:: https://raw.github.com/mher/flower/master/docs/screenshots/dashboard.png
   :width: 100%

.. image:: https://raw.github.com/mher/flower/master/docs/screenshots/pool.png
   :width: 100%

.. image:: https://raw.github.com/mher/flower/master/docs/screenshots/tasks.png
   :width: 100%

.. image:: https://raw.github.com/mher/flower/master/docs/screenshots/task.png
   :width: 100%

.. image:: https://raw.github.com/mher/flower/master/docs/screenshots/monitor.png
   :width: 100%

More screenshots_

.. _screenshots: https://github.com/mher/flower/tree/master/docs/screenshots

Getting help
------------

Please head over to #celery IRC channel on irc.freenode.net or
`open an issue`_.

.. _open an issue: https://github.com/mher/flower/issues

Contributing
------------

If you'd like to contribute, simply fork `the repository`_, commit your
changes, run the tests (`python -m tests`) and send a pull request.
Make sure you add yourself to AUTHORS_.

If you are interested in maintaining the project please contact.

.. _`the repository`: https://github.com/mher/flower
.. _AUTHORS: https://github.com/mher/flower/blob/master/AUTHORS


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
%attr(755,root,root) %{_bindir}/*
%{python_sitelib}/*
%doc AUTHORS CHANGES LICENSE README.rst
#%doc build/*

%changelog
* Mon Nov 23 2015 Nico Kadel-Garcia <nkadel@skyhookireless.com> - 0.8.3-0.1
- Build RPM from setup.py
- Add dependencies form requirements/default.txt
- Add python(abi) dependency

