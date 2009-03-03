#
# oombailout filesystem
#
# RPM spec file
#
#

%define url $URL: https://sapanb@poppins/svn/oombailout/trunk/oombailout.spec $

%define name oombailout
%define version 0.1
%define taglevel 0

%define release %{taglevel}%{?pldistro:.%{pldistro}}%{?date:.%{date}}

Vendor: PlanetLab
Packager: PlanetLab Central <support@planet-lab.org>
Distribution: PlanetLab %{plrelease}
URL: %(echo %{url} | cut -d ' ' -f 2)

Summary: oombailout script to prevent OOMs because of explosions in kernel memory
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: System Environment/Kernel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
#Requires: 

Source0: oombailout-%{version}.tar.gz

%description
oombailout aims to avert OOMs that the kernel is not aggressive enough to stop. This script came into existence on mlab, on which we were seeing TCP flooding attacks that would run the kernel out of memory. The system would run out of memory even though enough memory was available across various caches, because the kernel would not empty these caches fast enough.

%prep
%setup

%build

%install
install -D -m 755 oombailout $RPM_BUILD_ROOT/usr/bin/oombailout
install -D -m 755 oombailout-initscript $RPM_BUILD_ROOT/%{_sysconfdir}/init.d/oombailout
install -D -m 644 oombailout.logrotate $RPM_BUILD_ROOT/%{_sysconfdir}/logrotate.d/oombailout

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/bin/oombailout
%{_sysconfdir}/init.d/oombailout
%{_sysconfdir}/logrotate.d/oombailout

%post
chkconfig --add oombailout
chkconfig oombailout on
if [ "$PL_BOOTCD" != "1" ] ; then
        service oombailout restart
fi

%postun

%changelog

