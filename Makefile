VERSION=2
RELEASE=1
PROGRAMMNAME=olaf-system-post-init

cleanup:
	rm -Rvf ./$(PROGRAMMNAME)-$(VERSION)-$(RELEASE)
	rm -fv ./$(PROGRAMMNAME)-$(VERSION)-$(RELEASE).tar.gz 

dist-tar: cleanup
	mkdir ./$(PROGRAMMNAME)-$(VERSION)-$(RELEASE)
	cp -Rv ./files/* ./$(PROGRAMMNAME)-$(VERSION)-$(RELEASE)/
	tar -cvzf ./$(PROGRAMMNAME)-$(VERSION)-$(RELEASE).tar.gz ./$(PROGRAMMNAME)-$(VERSION)-$(RELEASE)/

dist-rpm: dist-tar
	rm -Rvf ~/rpmbuild/*
	mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
	rpmbuild -vv -ta ./$(PROGRAMMNAME)-$(VERSION)-$(RELEASE).tar.gz
