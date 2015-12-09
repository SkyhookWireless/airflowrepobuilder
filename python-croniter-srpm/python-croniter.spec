%{?scl:%scl_package python-alembic}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-1.0.1
%global srcname croniter

Name: %{?scl_prefix}python-%{srcname}
Version:        0.3.10
Release:        0.3%{?dist}
Summary:        Iteration for datetime object with cron like format

License:        MIT
URL:            http://github.com/kiorky/croniter
Source0:        https://pypi.python.org/packages/source/c/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# Not listed in tarball requirements
BuildRequires:  %{?scl_prefix}python-six

# For tests
BuildRequires:  %{?scl_prefix}python-dateutil
BuildRequires:  %{?scl_prefix}pytz

Requires:       %{?scl_prefix}python-dateutil

%description
Croniter provides iteration for datetime object with cron like format.


%prep
%setup -q -n %{srcname}-%{version}
# Remove bundled egg-info
rm -rf %{srcname}.egg-info
# Remove reundant script header to avoid rpmlint warnings
find -name \*.py -exec sed -i '/\/usr\/bin\/env python/{d;q}' {} +

%build
%{?scl:scl enable %{scl} "}
%{__python} setup.py build
%{?scl:"}

%install
%{__rm} -rf %{buildroot}
%{?scl:scl enable %{scl} "}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
%{?scl:"}

# Not courrently working <nkadel@skyhokwirelss.com>
#%check
#%{?scl:scl enable %{scl} "}
#PYTHONPATH=%{buildroot}%{python_sitelib}/ %{__python} -m unittest %{srcname}.tests.test_croniter
#%{?scl:"}
#rm -fr %{buildroot}%{python_sitelib}/%{srcname}/tests/

%files
%doc README.rst docs/LICENSE
%{python_sitelib}/%{srcname}
%{python_sitelib}/%{srcname}-%{version}-py?.?.egg-info

%changelog
* Wed Dec  9 2015 Nico Kadel-Garcia <nkadel@skyhookwireless.com> - 0.3.10-0.3
- Change python-python-dateutil back to python-dateutil

* Sat Dec  5 2015 Nico Kadel-Garcia <nkadel@skyhookwireless.com> - 0.3.10-0.2

* Tue Dec  1 2015 Nico Kadel-Garcia <nkadel@skyhookwireless.com> - 0.3.10-0.1
- Update to 0.3.10 for airflow 1.6.1 dependency

* Fri Nov 27 2015 Nico Kadel-Garcia <nkadel@skyhookwireless.com> - 0.3.4-0.1
- Migrate to pyton27
- Change "python-dateutil" to "python-python-dateutil", to match
  actual tarball name.
- Add "python-six" dependency
- Disable check

* Fri Feb 21 2014 Pádraig Brady <P@draigBrady.com> - 0.3.4-2
- Initial package.
