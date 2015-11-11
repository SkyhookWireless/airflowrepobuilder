airflowrepobuilder - Python Module builder RHEL 5, 6, and 7

License:  GPLv3
	  (Except where noted in subpackages)
Maintainer:   Nico Kadel-Garcia
Maintainer Email: nkadel@gmail.com

Many of the upsteam components for these, or for older versions of
these, are available at:

       http://vault.centos.org/cenots/6.7/SCL/Source/SPackages/

Usage:
    make install - build, and install for local access, the
    full build requirements for RT4. This is the normal bootstrap
    operation.

    make build - try and build all the components in the local
    environment, without using "mock"

    make all - build all comopnents using "mock" and the local
    RT4 repository, called "rt4repo"

    make epel - build only the compoenents that can be built
    from EPEL, without additional comopnents from this toolkit.

    make python - buld the compnents that require the local EPEL
    compatible and python component dependent packages.


Requirements: This toolkit requires the following tools:

     * The "mock" software for building RPM's, available from EPEL for
       RHEL based cystems.

     * Spare diskspace at /var/lib/mock and /var/cache/mock for the
       builky builds of mock chroot environments.

     * Reliable access to yum repositories for CentOS, RHEL, or
       Scietific Linux repositories, for the standard "mock"
       configuration.

     * Membership in the "mock" group for permissions to exucute the
       mock software.

     * PATH setting or an alias that accfess "/usr/bin/mock", not
       "/usr/sbin/mock".

     * "sudo" Permissions to clear the mock cache for pythonrepo build
       environments without having to supply passwords. For example:

	 %mock ALL=(ALL)	NOPASSWD: /bin/touch /etc/mock/pythonrepo-6-x86_64.cfg
	 %mock ALL=(ALL)	NOPASSWD: /bin/touch /etc/mock/pythonrepo-7-x86_64.cfg
