# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       sailfishos-patch-force-largecovers

# >> macros
# << macros

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}
Summary:    Force largecovers
Version:    1.1.9.28
Release:    1
Group:      Applications/Productivity
License:    GPLv2+
BuildArch:  noarch
URL:        http://me.medesimo.eu
Source0:    %{name}-%{version}.tar.bz2
Source100:  sailfishos-patch-force-largecovers.yaml
Requires:   patchmanager
Requires:   sailfish-version >= 1.1.9-10.33.28.jolla

%description
Patch that forces the large covers in the application switcher


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qtc_qmake5 

%qtc_make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post

%preun
# >> preun
if [ -x /usr/sbin/patchmanager ]; then
/usr/sbin/patchmanager -u eugenio-force-largecovers || true
fi
# << preun

%files
%defattr(-,root,root,-)
%{_datadir}/patchmanager
# >> files
# << files
