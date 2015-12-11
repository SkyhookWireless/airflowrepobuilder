#!/bin/sh
#
# Report non-RPM based modules
#

export DIRS=''
DIRS="$DIRS /usr/lib/python2.6/site-packages"
DIRS="$DIRS /opt/rh/python27/root/usr/lib/python2.7/site-packages"

for dir in $DIRS; do
    [ -d $dir ] || continue
    rpm -q -f $dir/* | grep 'not owned'
done
