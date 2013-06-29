#
# spec file for package udhcp
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           udhcp
Summary:        Micro DHCP client / server
License:        GPL-2.0
Group:          System/Emulators/PC
Version:        0.9.8
Release:        2
Url:            http://udhcp.busybox.net
Source0:        %{name}-%{version}.tar.gz
Source1001:     %{name}.manifest
Patch0:         oracle-rpmbuild-makefile-changes.patch
Patch1:         %{name}_usermac.patch
Patch2:         %{name}-outputpy.patch
Patch3:         %{name}-update-scripts.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#BuildRequires: 
#Requires: 
#ExclusiveArch: i386 i686 x86_64

%description
Udhcp is a small dhcp client / server mainly used to support Xen
para-virtualized PXE booting.



Authors:
--------
    Russ Dill <Russ.Dill@asu.edu>
    Matthew Ramsay  <matthewr@moreton.com.au>
    Chris Trew <christ@moreton.com.au>

%prep 
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
cp %{SOURCE1001} .
%{__make}

%install
%{make_install} SBINDIR=%{buildroot}/%{_sbindir}
mv %{buildroot}/sbin/udhcpc %{buildroot}/%{_bindir}
mv %{buildroot}/%{_sbindir}/udhcpd %{buildroot}/%{_bindir}

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%manifest %{name}.manifest
%{_bindir}/*
%doc %{_mandir}/man?/*
%dir %{_datadir}/udhcpc
%{_datadir}/udhcpc/*

%changelog
