#!/bin/sh
#
# report-non-rpm-python27.sh - report non-RPM based python27 modules
#

rpm -q -f /opt/rh/python27/root/usr/lib/python2.7/site-packages/* | \
    grep ' '

rpm -q -f /opt/rh/python27/root/usr/lib64/python2.7/* | \
    grep ' '
