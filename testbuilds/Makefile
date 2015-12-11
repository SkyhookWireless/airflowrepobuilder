#
# Testing tools and setups for reviwing pip vs. RPM deployments
#

.PHONY:: testenv
testenv:: audit-non-rpm-modules.sh
	(cd ../python-airflow16-srpm; make srpm)
	mock -r airflowrepo-6-x86_64 ../python-airflow16-srpm/rpmbuild/SRPMS/*.src.rpm
	mock -r airflowrepo-6-x86_64 install python27-python-pip
	mock -r airflowrepo-6-x86_64 install python27-python-airflow16
	mock -r airflowrepo-6-x86_64 install yum sudo vim-minimal
	mock -r airflowrepo-6-x86_64 copyin audit-non-rpm-modules.sh
