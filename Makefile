VERSION=8
RELEASE=1
PROGRAMMNAME=olaf-system-post-init
BUILDNAME=$(PROGRAMMNAME)-$(VERSION)-$(RELEASE)

cleanup:
	rm -Rvf ./$(BUILDNAME)
	rm -fv ./$(BUILDNAME).tar.gz

dist-tar: cleanup
	mkdir ./$(BUILDNAME)
	cp -Rv ./files/* ./$(BUILDNAME)/
	tar -cvzf ./$(BUILDNAME).tar.gz ./$(BUILDNAME)/

dist-rpm: dist-tar
	rm -Rvf ~/rpmbuild/*
	mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
	rpmbuild -vv -ta ./$(BUILDNAME).tar.gz
