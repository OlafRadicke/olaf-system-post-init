VERSION=2
PROGRAMMNAME=olaf-system-post-init

dist-tar:
	mkdir ./$(PROGRAMMNAME)-$(VERSION)
	cp -Rv ./files/* ./$(PROGRAMMNAME)-$(VERSION)/
	tar -cvzf ./$(PROGRAMMNAME)-$(VERSION).tar.gz ./$(PROGRAMMNAME)-$(VERSION)/

dist-rpm: dist-tar
	rm -Rvf ~/rpmbuild/*
	mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
	rpmbuild -vv -ta ./$(PROGRAMMNAME)-$(VERSION).tar.gz
