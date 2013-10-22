Name: olaf-system-post-init
Summary: Eigene Konfigurationen für das System.
Version: 2
Group: system
License: GPL
Release: 1
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
Source:%{name}-%{version}-%{release}.tar.gz
BuildArch: noarch
Requires: rpmrebuild,  gcc-c++.x86_64, kate, kile, emacs-nox, mc,  doxygen-doxywizard, postgresql, postgresql-server, libreoffice, libreoffice-langpack-de.x86_64, libreoffice-calc, libreoffice-draw, libreoffice-impress, libreoffice-writer, iptraf-ng, vlc, mozilla-noscript, aspell-de, hunspell-de, automake, autoconf, libtool, postgresql-devel, zlib-devel, openssl-devel, calibre, gnucash, git, gitk, gitg, tortoisehg, mercurial, pgadmin3, dia, okular, gimp, kcoloredit, ksnapshot, gftp, ktorrent, gparted, system-config-boot, system-config-firewall, system-config-firewall-tui, system-config-keyboard, system-config-language, system-config-network, system-config-services, kwrite, keepassx, kfilereplace, sigil 


%description
Dummy-Paket mit dem ich mein System verwalte. Es benötigt als Pakrtquelle rpmfusion.

%prep
%setup


%build

%install
echo "Hallo Welt"


%post


%clean
rm -fr $RPM_BUILD_ROOT

%postun

%changelog
* Sun Oct 20 2013 olaf - 2
- changelog hinzugefühgt.

* Sun Oct 20 2013 olaf - 1
- Init-Version.

