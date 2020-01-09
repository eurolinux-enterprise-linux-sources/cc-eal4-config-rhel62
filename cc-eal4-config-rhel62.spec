Summary: RHEL 6.2 / EAL4+ Certified Config
Name: cc-eal4-config-rhel62
Version: 0.33
Release: 1%{?dist}
License: GPLv2 and MIT
Group: Applications/System
Source0: %{name}-%{version}.tar.gz
Source1: RHEL6.2_TestPlan.pdf
Source2: audit-test.tar.bz2 
BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(%{__id_u} -n)
BuildArch: noarch
Requires: kernel = 2.6.32

%description
This package contains various artifacts from the RHEL 6.2 Common Criteria
evaluation. It includes a kickstart script to put the system into the certified
configuration. It also includes the configuration guide to explain system
admin details in managing the certified system. There is also a test plan that
describes how the system was tested. It also contains the test suite used for
the evaluation. The test suite is stored as documentation and must be installed
to a test directory by an admin.

%prep
%setup -q
cp -p %{SOURCE1} .
cp -p %{SOURCE2} .

%build

%install
rm -rf $RPM_BUILD_ROOT
make NAME=cc-eal4-config-rhel62 ECG=RHEL62-Evaluated-Configuration-Guide RPM_SITE=http://192.168.120.1:8080/RHEL62 DESTDIR=${RPM_BUILD_ROOT} VERSION=%{version} RELEASE=%{release} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc doc/*
%doc audit-test.tar.bz2
%attr(0750,root,root) %{_sbindir}/cc-config
%attr(0755,root,root) %dir %{_datadir}/cc
%attr(0755,root,root) %dir %{_datadir}/cc/kickstart
%attr(0644,root,root) %{_datadir}/cc/kickstart/*
%attr(0644,root,root) %{_datadir}/cc/*.pam*
%attr(0644,root,root) %{_datadir}/cc/*.xinetd
%attr(0644,root,root) %{_datadir}/cc/*.defs
%attr(0644,root,root) %{_datadir}/cc/*.conf
%attr(0644,root,root) %{_datadir}/cc/*.te
%attr(0644,root,root) %{_datadir}/cc/mime.*
%attr(0644,root,root) %{_datadir}/cc/sshd_config
%attr(0644,root,root) %{_datadir}/cc/sshd
%attr(0644,root,root) %{_datadir}/cc/*-addon
%attr(0644,root,root) %{_datadir}/cc/*.*sh
%attr(0755,root,root) %{_datadir}/cc/*.service

%changelog
* Tue Aug 07 2012 Steve Grubb <sgrubb@redhat.com> 0.33-1 
- Initial build.

