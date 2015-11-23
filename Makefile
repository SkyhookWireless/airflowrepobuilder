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
EPELPKGS+=python-chartkick-srpm
EPELPKGS+=python-dill-srpm
EPELPKGS+=python-flask-admin-srpm
EPELPKGS+=python-flask-cache-srpm
EPELPKGS+=python-flask-login-srpm
EPELPKGS+=python-flask-srpm
EPELPKGS+=python-future-srpm
EPELPKGS+=python-itsdangerous-srpm
EPELPKGS+=python-jinja2-srpm
EPELPKGS+=python-mako-srpm
EPELPKGS+=python-markdown-srpm
EPELPKGS+=python-pygments-srpm
EPELPKGS+=python-python-dateutil-srpm
EPELPKGS+=python-python-editor-srpm
EPELPKGS+=python-requests-srpm
EPELPKGS+=python-six-srpm
EPELPKGS+=python-sqlalchemy-srpm
EPELPKGS+=python-werkzeug-srpm

# Optional add-ons
EPELPKGS+=python-alabaster-srpm
EPELPKGS+=python-amqp-srpm
EPELPKGS+=python-backports-srpm
EPELPKGS+=python-backports_abc-srpm
EPELPKGS+=python-happybase-srpm
EPELPKGS+=python-keyring-srpm
EPELPKGS+=python-thrift-srpm
EPELPKGS+=python-unicodecsv-srpm

# Cloudera integration and access tools
EPELPKGS+=python-cm-api-srpm
EPELPKGS+=python-pyhs2-srpm
EPELPKGS+=python-sasl-srpm

# Discarded: python-pip and python27-python-pip are available from upstream
#EPELPKGS+=python-pip-srpm

# These require customized airflowrepo local repository for compilation
# Needed by various packages
PYTHONPKGS+=python-pandas-srpm
PYTHONPKGS+=python-airflow-srpm

# Populate airflowrepo with packages that require airflowrepo
# Verify build setup first!
all:: /usr/bin/createrepo
all:: airflowrepo-6-x86_64.cfg
all:: epel-6-sclpy27-x86_64.cfg

all:: python-install

install:: epel-install python-install

epel-install:: $(EPELOKGS)
python-install:: $(PYTHONPKGS)

airflowrepo-6-x86_64.cfg:: airflowrepo-6-x86_64.cfg.in
	sed "s|@@@REPOBASEDIR@@@|$(REPOBASEDIR)|g" $? > $@

airflowrepo-6-x86_64.cfg:: FORCE
	@cmp -s $@ /etc/mock/$@ || \
		(echo Warning: /etc/mock/$@ does not match $@, exiting; exit 1)

epel-6-sclpy27-x86_64.cfg:: epel-6-sclpy27-x86_64.cfg.in
	sed "s|@@@REPOBASEDIR@@@|$(REPOBASEDIR)|g" $? > $@

epel-6-sclpy27-x86_64.cfg:: FORCE
	@cmp -s $@ /etc/mock/$@ || \
		(echo Warning: /etc/mock/$@ does not match $@, exiting; exit 1)

# Used for make build with local components
airflowrepo.repo:: airflowrepo.repo.in
	sed "s|@@@REPOBASEDIR@@@|$(REPOBASEDIR)|g" $? > $@

airflowrepo.repo:: FORCE
	@cmp -s $@ /etc/yum.repos.d/$@ || \
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

# pandas will compile without pytz, but less effecieintly
python-pandas-srpm:: pytz-srpm

python-airflow-srpm:: python-alembic-srpm
python-airflow-srpm:: python-chartkick-srpm
python-airflow-srpm:: python-dill-srpm
python-airflow-srpm:: python-flask-admin-srpm
python-airflow-srpm:: python-flask-cache-srpm
python-airflow-srpm:: python-flask-login-srpm
python-airflow-srpm:: python-flask-srpm
python-airflow-srpm:: python-future-srpm
python-airflow-srpm:: python-gunicorn-srpm
python-airflow-srpm:: python-itsdangerous-srpm
python-airflow-srpm:: python-jinja2-srpm
python-airflow-srpm:: python-mako-srpm
python-airflow-srpm:: python-markdown-srpm
python-airflow-srpm:: python-pandas-srpm
python-airflow-srpm:: python-pygments-srpm
python-airflow-srpm:: python-python-dateutil-srpm
python-airflow-srpm:: python-python-editor-srpm
python-airflow-srpm:: python-requests-srpm
python-airflow-srpm:: python-six-srpm
python-airflow-srpm:: python-sqlalchemy-srpm
python-airflow-srpm:: python-werkzeug-srpm

# Git clone operations, not normally required
# Targets may change

# Build EPEL compatible softwaer in place
$(EPELPKGS):: FORCE
	(cd $@ && $(MAKE) $(MLAGS)) || exit 1

$(PYTHONPKGS):: airflowrepo-6-x86_64.cfg
$(PYTHONPKGS):: epel-6-sclpy27-x86_64.cfg

$(PYTHONPKGS):: FORCE
	(cd $@ && $(MAKE) $(MLAGS)) || exit 1

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

