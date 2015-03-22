Name: olaf-system-post-init
Summary: Eigene Konfigurationen für das System.
Version: 8
Group: system
License: GPL
Release: 1
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
Source:%{name}-%{version}-%{release}.tar.gz
BuildArch: noarch
Requires: automake, autoconf, aspell-de, calibre, dia, doxygen-doxywizard, emacs-nox, fedora-arm-installer-helper, gcc-c++.x86_64,  gnucash, git, gitk, gitg, gimp, gftp, gparted, hunspell-de, iptraf-ng, kate, kile, kcoloredit, ksnapshot,  ktorrent, kwrite, keepassx, kfilereplace, kdiff3, libreoffice, libreoffice-langpack-de.x86_64, libreoffice-calc, libreoffice-draw, libreoffice-impress, libreoffice-writer, libtool, mc, mercurial, mozilla-noscript, openssl-devel, okular, postgresql, postgresql-devel, postgresql-server, pgadmin3, pandoc, pandoc-pdf, rpmrebuild, system-config-boot, system-config-firewall, system-config-firewall-tui, system-config-keyboard, system-config-language, system-config-network, system-config-services, splix, sigil, vlc, tortoisehg, texlive, texlive-tocbibind, texlive-multirow, texlive-babel-german, texlive-german texlive, w3m, zlib-devel


%description
Dummy-Paket mit dem ich mein System verwalte. Es benötigt als Pakrtquelle rpmfusion.

%prep

%setup  -n %{name}-%{version}-%{release}


%build

%install
echo "Hallo Welt"
mkdir -p %{buildroot}/usr/share/doc/olaf-system-post-init/
ls -lah
cp %{_builddir}/%{buildsubdir}/releasenote.md %{buildroot}/usr/share/doc/olaf-system-post-init/releasenote.md
ls -lah %{buildroot}

%post
postgresql-setup initdb
systemctl start postgresql.service
systemctl  enable  postgresql.service
# switch off selinux
sed -i 's/SELINUX=.*/SELINUX=disabled/' /etc/selinux/config


%clean
#rm -fr $RPM_BUILD_ROOT

%postun


%files
%dir  /usr/share/doc/olaf-system-post-init/
/usr/share/doc/olaf-system-post-init/releasenote.md

%changelog
* Sun Mar 22 2015 Olaf Radicke <briefkasten@olaf-radicke.de> - 8
- Noch eine Release-Note-Datei hinzugefühgt mit das RPM auch unter Sude baut.
* Fri Dec 13 2013 - 7
- fedora-arm-installer-helper hinzugefühgt.
* Tue Nov 12 2013 olaf - 6
- splix hinzugefügt für Samsung-Drucker ML-1520.
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

