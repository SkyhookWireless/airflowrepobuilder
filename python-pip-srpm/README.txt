***WARNING***

Packages installed with pip may overwrite or conflict with packages
installed with RPM. To avoid this, review contents of python
"site-packages" with "rpm -q -f *" to deduce non-RPM packages, then
replace them with RPM's wherever possible.

Also be aware that RPM replacements may be older releases than the
current pip installed versions. And be aware that using "pip
uninstall" carelessly can delete components from RPM installed
packages. Please be prepared to run "yum reinstall rpmname" in order
to correctly reset files accidentally cleared by "pip install"

	  Nico Kadel-Garcia
	  <nkadel@skyhookwireless.com>
	  2015-11-20


