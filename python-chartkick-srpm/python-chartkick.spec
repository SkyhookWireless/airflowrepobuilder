%{?scl:%scl_package python-chartkick}
%{!?scl:%global pkg_name %{name}}

%global srcname chartkick
%define version 0.4.2
%define unmangled_version 0.4.2
%define release 1

Summary: Create beautiful Javascript charts with minimal code
Name: %{?scl_prefix}python-chartkick
Version: %{version}
Release: 0.1%{?dist}
Source0: %{srcname}-%{unmangled_version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Mher Movsisyan <mher.movsisyan@gmail.com>
Url: https://github.com/mher/chartkick.py
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
BuildRequires:  %{?scl_prefix}python-sphinx

%description
Chartkick.py
============

.. image:: https://badge.fury.io/py/chartkick.png
        :target: http://badge.fury.io/py/chartkick
.. image:: https://travis-ci.org/mher/chartkick.py.png?branch=master
        :target: https://travis-ci.org/mher/chartkick.py
.. image:: https://pypip.in/d/chartkick/badge.png
        :target: https://crate.io/packages/chartkick/
.. image:: https://d2weczhvl823v0.cloudfront.net/mher/chartkick.py/trend.png
   :alt: Bitdeli badge
   :target: https://bitdeli.com/free

Create beautiful Javascript charts with minimal code. Demo_!

Supports `Google Charts`_ and Highcharts_

Works with Django, Flask/Jinja2 and most browsers (including IE 6).
Also available in Ruby_ and pure JavaScript_

.. _Chartkick: http://chartkick.com
.. _Google Charts: https://developers.google.com/chart/
.. _Highcharts: http://highcharts.com
.. _Demo: http://mher.github.io/chartkick.py/
.. _Ruby: http://chartkick.com
.. _Javascript: https://github.com/ankane/chartkick.js

Usage
-----

Line chart: ::

    {% line_chart data %}

Pie chart: ::

    {% pie_chart data with id='chart-1' height='400px' %}

Column chart: ::

    {% column_chart data with min=400 max=1000 %}

Bar chart: ::

    {% bar_chart data %}

Area chart: ::

    {% area_chart data %}

Data
----

Data can be a dictionary or a list: ::

    {'Chrome': 52.9, 'Opera': 1.6, 'Firefox': 27.7}

    [['Chrome', 52.9], ['Firefox', 27.7], ['Opera', 1.6]]

For multiple series: ::

    [{'data': [['2013-04-01 00:00:00 UTC', 52.9], ['2013-05-01 00:00:00 UTC', 50.7]], 'name': 'Chrome'},
     {'data': [['2013-04-01 00:00:00 UTC', 27.7], ['2013-05-01 00:00:00 UTC', 25.9]], 'name': 'Firefox'}]

Options
-------

Charting library options can be passed through the *library* variable: ::

    {% column_chart data with library={"title":"Super chart","width":"400px"} %}

.. Note:: Google Charts and Highcharts have different APIs. You may need
          to change the value of `library` when you switch from one
          library to another.

Or using *chartkick.json* file. Chartkick tries to locate *chartkick.json*
file in template path and match options by id.

Installation
------------

Install chartkick: ::

    $ pip install chartkick

- Django: Add chartkick to *INSTALLED_APPS* and *STATICFILES_DIRS*: ::

    INSTALLED_APPS = (
        'chartkick',
    )

    import chartkick
    STATICFILES_DIRS = (
        chartkick.js(),
    )

- Flask: Add chartkick to *jinja_env* and *static_folder*: ::

    ck = Blueprint('ck_page', __name__, static_folder=chartkick.js(), static_url_path='/static')
    app.register_blueprint(ck, url_prefix='/ck')
    app.jinja_env.add_extension("chartkick.ext.charts")

Load JS scripts:

- Google Charts ::

    <script src="http://www.google.com/jsapi"></script>
    <script src="ck/static/chartkick.js"></script>

- Highcharts ::

    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"></script>
    <script src="http://code.highcharts.com/highcharts.js"></script>
    <script src="ck/static/chartkick.js"></script>



%prep
%setup -n %{srcname}-%{unmangled_version}

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
%doc README.rst
%{python_sitelib}/*
