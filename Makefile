#
# Makefile - build wrapper for airflow specific python modules on RHEL 6
#
#	git clone RHEL 6 SRPM building tools from
#	https://github.com/nkadel-skyhook/airflowrepo

# Base directory for yum repository
REPOBASEDIR="`/bin/pwd`"
# Base subdirectories for RPM deployment
REPOBASESUBDIRS+=$(REPOBASEDIR)/airflowrepo/6/SRPMS
REPOBASESUBDIRS+=$(REPOBASEDIR)/airflowrepo/6/x86_64

# These build with normal mock "epel-*" setups
# Use short name, based on RHEL naming
EPELPKGS+=pytz-srpm
# This ons is from SuSE repo
EPELPKGS+=python-gunicorn-srpm

EPELPKGS+=python-alembic-srpm
EPELPKGS+=python-argparse-srpm
EPELPKGS+=python-backports.ssl_match_hostname-srpm
EPELPKGS+=python-boto-srpm
EPELPKGS+=python-chartkick-srpm
EPELPKGS+=python-coveralls-srpm
EPELPKGS+=python-cryptography-srpm
EPELPKGS+=python-dill-srpm
EPELPKGS+=python-filechunkio-srpm
EPELPKGS+=python-flake8-srpm
EPELPKGS+=python-flask-admin-srpm
EPELPKGS+=python-flask-cache-srpm
EPELPKGS+=python-flask-login-srpm
EPELPKGS+=python-flask-srpm
EPELPKGS+=python-flask-wtf-srpm
EPELPKGS+=python-future-srpm
EPELPKGS+=python-futures-srpm
EPELPKGS+=python-gevent-srpm
EPELPKGS+=python-greenlet-srpm
EPELPKGS+=python-hive-thrift-py-srpm
EPELPKGS+=python-itsdangerous-srpm
EPELPKGS+=python-jaydebeapi-srpm
EPELPKGS+=python-jinja2-srpm
EPELPKGS+=python-ldap3-srpm
EPELPKGS+=python-librabbitmq-srpm
EPELPKGS+=python-mako-srpm
EPELPKGS+=python-markdown-srpm

# For airflow 1.5.x
EPELPKGS+=python-mysql-python-srpm
# For airflow 1.6.x
EPELPKGS+=python-mysqlclient-srpm

EPELPKGS+=python-psycopg2-srpm
EPELPKGS+=python-pydruid-srpm
EPELPKGS+=python-pygments-srpm
EPELPKGS+=python-pyhive-srpm
EPELPKGS+=python-pykerberos-srpm
EPELPKGS+=python-pymssql-srpm
EPELPKGS+=python-pysmbclient-srpm
EPELPKGS+=python-python-dateutil-srpm
EPELPKGS+=python-python-editor-srpm
EPELPKGS+=python-six-srpm
EPELPKGS+=python-sqlalchemy-srpm
EPELPKGS+=python-thrift-srpm
EPELPKGS+=python-vertica-python-srpm
EPELPKGS+=python-werkzeug-srpm

# useful airflow components and dependencies, not from airflow/requirements.txt
EPELPKGS+=babel-srpm
EPELPKGS+=python-alabaster-srpm
EPELPKGS+=python-amqp-srpm
EPELPKGS+=python-anyjson-srpm
EPELPKGS+=python-backports-srpm
EPELPKGS+=python-backports_abc-srpm
EPELPKGS+=python-beaker-srpm
EPELPKGS+=python-billiard-srpm
EPELPKGS+=python-enum-srpm
EPELPKGS+=python-enum34-srpm
EPELPKGS+=python-flower-srpm
EPELPKGS+=python-google-srpm
EPELPKGS+=python-happybase-srpm
EPELPKGS+=python-idna-srpm
EPELPKGS+=python-ipaddress-srpm
EPELPKGS+=python-keyring-srpm
EPELPKGS+=python-kombu-srpm
EPELPKGS+=python-mock-srpm
EPELPKGS+=python-ordereddict-srpm
EPELPKGS+=python-protobuf-srpm
EPELPKGS+=python-pyasn1-srpm
EPELPKGS+=python-pycparser-srpm
EPELPKGS+=python-singledispatch-srpm
EPELPKGS+=python-slackclient-srpm
EPELPKGS+=python-snakebite-srpm
EPELPKGS+=python-snowballstemmer-srpm
EPELPKGS+=python-sphinx-argparse-srpm
EPELPKGS+=python-sphinx-pypi-upload-srpm
EPELPKGS+=python-sphinx_rtd_theme-srpm
EPELPKGS+=python-statsd-srpm
EPELPKGS+=python-tornado-srpm
EPELPKGS+=python-tox-srpm
EPELPKGS+=python-unicodecsv-srpm
EPELPKGS+=python-websocket-srpm
EPELPKGS+=python-wheel-srpm

# awscli critical components
EPELPKGS+=python-certifi-srpm
EPELPKGS+=python-awscli-srpm

# py2pack critical component
EPELPKGS+=python-lxml-srpm

# Cloudera integration and access tools
EPELPKGS+=python-cm-api-srpm
EPELPKGS+=python-pyhs2-srpm
EPELPKGS+=python-sasl-srpm

# Update to 1.7.x release
EPELPKGS+=python-pip-srpm

# Updated for new pypi.org URL
PYTHONPKGS+=python-py2pack-srpm

# These require customized airflowrepo local repository for compilation
# Needed by various packages
PYTHONPKGS+=python-celery-srpm
PYTHONPKGS+=python-croniter-srpm
PYTHONPKGS+=python-eventlet-srpm
PYTHONPKGS+=python-pandas-srpm
PYTHONPKGS+=python-requests-srpm
PYTHONPKGS+=python-sphinx-srpm
PYTHONPKGS+=python-wtforms-srpm

# Disabled, requires locally installed Oracle
#PYTHONPKGS+=python-cx_oracle-srpm

# These do not really require all the packages for compilaiton,
# but reuqie them all for isntallation, so put them last
PYTHONPKGS+=python-airflow-srpm
PYTHONPKGS+=python-airflow16-srpm

# Populate airflowrepo with packages that require airflowrepo
# Verify build setup first!
all:: /usr/bin/createrepo
all:: airflowrepo-6-x86_64.cfg
all:: sclpy27-6-x86_64.cfg

all:: python-install

install:: epel-install python-install

epel-install:: $(EPELOKGS)
python-install:: $(PYTHONPKGS)

airflowrepo-6-x86_64.cfg:: airflowrepo-6-x86_64.cfg.in
	sed "s|@@@REPOBASEDIR@@@|$(REPOBASEDIR)|g" $? > $@

airflowrepo-6-x86_64.cfg:: FORCE
	@diff -u $@ /etc/mock/$@ || \
		(echo Warning: /etc/mock/$@ does not match $@, exiting; exit 1)

sclpy27-6-x86_64.cfg:: sclpy27-6-x86_64.cfg.in
	sed "s|@@@REPOBASEDIR@@@|$(REPOBASEDIR)|g" $? > $@

sclpy27-6-x86_64.cfg:: FORCE
	@diff -u $@ /etc/mock/$@ || \
		(echo Warning: /etc/mock/$@ does not match $@, exiting; exit 1)

# Used for make build with local components
airflowrepo.repo:: airflowrepo.repo.in
	sed "s|@@@REPOBASEDIR@@@|$(REPOBASEDIR)|g" $? > $@

airflowrepo.repo:: FORCE
	@diff -u $@ /etc/yum.repos.d/$@ || \
		(echo Warning: /etc/yum.repos.d/$@ does not match $@, exiting; exit 1)

epel:: $(EPELPKGS)

$(REPOBASESUBDIRS)::
	mkdir -p $@

epel-install:: $(REPOBASESUBDIRS)

epel-install:: FORCE
	@for name in $(EPELPKGS); do \
		(cd $$name && $(MAKE) all install) || exit 1; \
	done

python:: $(PYTHONPKGS)

python-install:: FORCE
	@for name in $(PYTHONPKGS); do \
		(cd $$name && $(MAKE) all install) || exit 1; \
	done

# pandas will compile without pytz, but far less effecieintly
python-pandas-srpm:: pytz-srpm

python-celery-srpm:: python-kombu-srpm

python-eventlet-srpm:: python-greenlet-srpm
# Upstream version is recent enough to build
#python-eventlet-srpm:: python-sphinx-srpm

# Upstream version is recent enough to build
#python-jinja2-srpm:: python-sphinx-srpm

# Upstream version is recent enough to build
#python-chartkick-srpm:: python-sphinx-srpm

python-wtforms-srpm:: babel-srpm

# Upsream python-six is sufficient for python-singledispatch
#python-singledispatch-srpm:: python-six-arpm

# upstream python27-python-sphinx is not recent enough
python-sphinx-srpm:: babel-srpm
python-sphinx-srpm:: python-alabaster-srpm
python-sphinx-srpm:: python-mock-srpm
python-sphinx-srpm:: python-sphinx_rtd_theme-srpm
python-sphinx-srpm:: pytz-srpm

python-croniter-srpm:: python-python-dateutil-srpm
python-croniter-srpm:: pytz-srpm
# Upstream python-six is recent enough to build
#python-croniter-srpm:: python-six-srpm

python-mako-srpm:: pytz-srpm

python-kombu-srpm:: python-ordereddict-srpm

python-requests-srpm:: python-ordereddict-srpm

python-py2pack-srpm:: python-argparse-srpm
python-py2pack-srpm:: python-jinja2-srpm
python-py2pack-srpm:: python-lxml-srpm

# Current sphinx has dependency loop with sphinx_rtd_theme
#python-sphinx_rtd_theme-srpm:: python-sphinx-srpm

python-py-srpm:: python-pytest-srpm
# Upstream python-sphinx is recent enough to build
#python-py-srpm:: python-sphinx-srpm

# python-py and python-pytest have circular dependency,
# disabled by not running tests of python-pytest
#python-pytest-srpm:: python-py-srpm

# Upstream python-sphinx is recent enough to build
#python-werkzeug-srpm:: python-sphinx-srpm

# Direct installation requirements for python-airflow
python-airflow-srpm:: python-alembic-srpm
python-airflow-srpm:: python-argparse-srpm
python-airflow-srpm:: python-boto-srpm
python-airflow-srpm:: python-celery-srpm
python-airflow-srpm:: python-chartkick-srpm
python-airflow-srpm:: python-cryptography-srpm
python-airflow-srpm:: python-dill-srpm
python-airflow-srpm:: python-flask-srpm
python-airflow-srpm:: python-flask-admin-srpm
python-airflow-srpm:: python-flask-cache-srpm
# 0.2.11 specifically required
python-airflow-srpm:: python-flask-login-srpm
python-airflow-srpm:: python-flower-srpm
python-airflow-srpm:: python-future-srpm
python-airflow-srpm:: python-gunicorn-srpm
python-airflow-srpm:: python-hive-thrift-py-srpm
python-airflow-srpm:: python-jaydebeapi-srpm
python-airflow-srpm:: python-jinja2-srpm
python-airflow-srpm:: python-librabbitmq-srpm
python-airflow-srpm:: python-markdown-srpm
python-airflow-srpm:: python-mysql-python-srpm
python-airflow-srpm:: python-pandas-srpm
python-airflow-srpm:: python-psycopg2-srpm
python-airflow-srpm:: python-pydruid-srpm
python-airflow-srpm:: python-pygments-srpm
python-airflow-srpm:: python-pyhive-srpm
python-airflow-srpm:: python-pyhs2-srpm
python-airflow-srpm:: python-pymssql-srpm
python-airflow-srpm:: python-pysmbclient-srpm
python-airflow-srpm:: python-python-dateutil-srpm
python-airflow-srpm:: python-requests-srpm
python-airflow-srpm:: python-slackclient-srpm
python-airflow-srpm:: python-snakebite-srpm
python-airflow-srpm:: python-sphinx-srpm
python-airflow-srpm:: python-sphinx-argparse-srpm
python-airflow-srpm:: python-sphinx-pypi-upload-srpm
python-airflow-srpm:: python-sphinx_rtd_theme-srpm
python-airflow-srpm:: python-sqlalchemy-srpm
python-airflow-srpm:: python-statsd-srpm
python-airflow-srpm:: python-thrift-srpm
python-airflow-srpm:: python-unicodecsv-srpm

# Direct installation requirements for python-airflow16
python-airflow16-srpm:: python-alembic-srpm
python-airflow16-srpm:: python-boto-srpm
python-airflow16-srpm:: python-celery-srpm
python-airflow16-srpm:: python-chartkick-srpm
python-airflow16-srpm:: python-coveralls-srpm
python-airflow16-srpm:: python-croniter-srpm
python-airflow16-srpm:: python-cryptography-srpm
python-airflow16-srpm:: python-dill-srpm
python-airflow16-srpm:: python-eventlet-srpm
python-airflow16-srpm:: python-filechunkio-srpm
python-airflow16-srpm:: python-flake8-srpm
python-airflow16-srpm:: python-flask-admin-srpm
python-airflow16-srpm:: python-flask-cache-srpm
# 0.2.11 specifically required
python-airflow16-srpm:: python-flask-login-srpm
python-airflow16-srpm:: python-flask-srpm
python-airflow16-srpm:: python-flask-wtf-srpm
python-airflow16-srpm:: python-flower-srpm
python-airflow16-srpm:: python-future-srpm
python-airflow16-srpm:: python-gevent-srpm
python-airflow16-srpm:: python-gunicorn-srpm
python-airflow16-srpm:: python-hive-thrift-py-srpm
python-airflow16-srpm:: python-itsdangerous-srpm
python-airflow16-srpm:: python-jaydebeapi-srpm
python-airflow16-srpm:: python-jinja2-srpm
python-airflow16-srpm:: python-ldap3-srpm
python-airflow16-srpm:: python-librabbitmq-srpm
python-airflow16-srpm:: python-mako-srpm
python-airflow16-srpm:: python-markdown-srpm
python-airflow16-srpm:: python-mysqlclient-srpm
python-airflow16-srpm:: python-pandas-srpm
python-airflow16-srpm:: python-psycopg2-srpm
python-airflow16-srpm:: python-pydruid-srpm
python-airflow16-srpm:: python-pygments-srpm
python-airflow16-srpm:: python-pyhive-srpm
python-airflow16-srpm:: python-pyhs2-srpm
python-airflow16-srpm:: python-pykerberos-srpm
python-airflow16-srpm:: python-pymssql-srpm
python-airflow16-srpm:: python-pysmbclient-srpm
python-airflow16-srpm:: python-python-dateutil-srpm
python-airflow16-srpm:: python-requests-srpm
python-airflow16-srpm:: python-slackclient-srpm
python-airflow16-srpm:: python-snakebite-srpm
python-airflow16-srpm:: python-sphinx-argparse-srpm
python-airflow16-srpm:: python-sphinx-pypi-upload-srpm
python-airflow16-srpm:: python-sphinx-srpm
python-airflow16-srpm:: python-sphinx_rtd_theme-srpm
python-airflow16-srpm:: python-sqlalchemy-srpm
python-airflow16-srpm:: python-statsd-srpm
python-airflow16-srpm:: python-thrift-srpm
python-airflow16-srpm:: python-unicodecsv-srpm
python-airflow16-srpm:: python-vertica-python-srpm

# Git clone operations, not normally required
# Targets may change

# Build EPEL compatible softwaer in place
$(EPELPKGS):: FORCE
	(cd $@ && $(MAKE) $(MLAGS) all install) || exit 1

$(PYTHONPKGS):: airflowrepo-6-x86_64.cfg
$(PYTHONPKGS):: sclpy27-6-x86_64.cfg

$(PYTHONPKGS):: FORCE
	(cd $@ && $(MAKE) $(MLAGS) all install) || exit 1

# Needed for local compilation, only use for dev environments
build:: airflowrepo.repo

build clean realclean distclean:: FORCE
	@for name in $(EPELPKGS) $(PYTHONPKGS); do \
	     (cd $$name && $(MAKE) $(MFLAGS) $@); \
	done

realclean distclean:: clean

clean::
	find . -name \*~ -exec rm -f {} \;

# Use this only to build completely from scratch
# Leave the rest of airflowrepo alone.
maintainer-clean:: clean
	@echo Clearing local yum repository
	find airflowrepo -type f ! -type l -exec rm -f {} \; -print

# Leave a safe repodata subdirectory
maintainer-clean:: FORCE

safe-clean:: maintainer-clean FORCE
	@echo Populate airflowrepo with empty, safe repodata
	find airflowrepo -noleaf -type d -name repodata | while read name; do \
		createrepo -q $$name/..; \
	done

# This is only for upstream repository publication.
# Modify for local use as needed, but do try to keep passwords and SSH
# keys out of the git repository fo this software.
RSYNCTARGET=rsync://localhost/airflowrepo
RSYNCOPTS=-a -v --ignore-owner --ignore-group --ignore-existing
RSYNCSAFEOPTS=-a -v --ignore-owner --ignore-group
publish:: all
publish:: FORCE
	@echo Publishing RPMs to $(RSYNCTARGET)
	rsync $(RSYNCSAFEOPTS) --exclude=repodata $(RSYNCTARGET)/

publish:: FORCE
	@echo Publishing repodata to $(RSYNCTARGET)
	find repodata/ -type d -name repodata | while read name; do \
	     rsync $(RSYNCOPTS) $$name/ $(RSYNCTARGET)/$$name/; \
	done

FORCE::

