Name: olaf-system-post-init
Summary: Eigene Konfigurationen für das System.
Version: 6
Group: system
License: GPL
Release: 1
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
Source:%{name}-%{version}-%{release}.tar.gz
BuildArch: noarch
Requires: automake, autoconf, aspell-de, calibre, dia, doxygen-doxywizard, emacs-nox, gcc-c++.x86_64,  gnucash, git, gitk, gitg, gimp, gftp, gparted, hunspell-de, iptraf-ng, kate, kile, kcoloredit, ksnapshot,  ktorrent, kwrite, keepassx, kfilereplace, kdiff3, libreoffice, libreoffice-langpack-de.x86_64, libreoffice-calc, libreoffice-draw, libreoffice-impress, libreoffice-writer, libtool, mc, mercurial, mozilla-noscript, openssl-devel, okular, postgresql, postgresql-server, pgadmin3, postgresql-devel, pandoc, pandoc-pdf, rpmrebuild, system-config-boot, system-config-firewall, system-config-firewall-tui, system-config-keyboard, system-config-language, system-config-network, system-config-services, splix, sigil, vlc, tortoisehg, texlive, texlive-tocbibind, texlive-multirow, texlive-babel-german, texlive-german texlive, zlib-devel  


%description
Dummy-Paket mit dem ich mein System verwalte. Es benötigt als Pakrtquelle rpmfusion.

%prep

%setup  -n %{name}-%{version}-%{release}


%build

%install
echo "Hallo Welt"

%post


%clean
#rm -fr $RPM_BUILD_ROOT

%postun

%files


%changelog
* Tue Nov 12 2013 olaf - 6
- Splix hinzugefügt für Samsung-Drucker ML-1520. 
* Sun Nov 10 2013 olaf - 5
- kdiff3 hinzugefügt
* Sun Nov 10 2013 olaf - 4
- texlive-tocbibind und texlive-multirow hinzugefügt
* Wed Oct 23 2013 olaf - 3
- pandoc und pandoc-pdf hinzugefügt
* Sun Oct 20 2013 olaf - 2
- changelog hinzugefühgt.

* Sun Oct 20 2013 olaf - 1
- Init-Version.

