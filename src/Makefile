# variables intended to be overridden from spec file / make-rpm script,
# don't modify them here
NAME=cc-config
ECG=RHEL-Evaluated-Configuration-Guide
VERSION=0.0
RELEASE=0
RPM_SITE=http://example.com

# other variables

DESTDIR=
PREFIX=/usr

BINDIR=$(PREFIX)/sbin
SCRIPT=cc-config

SHAREDIR=$(PREFIX)/share/cc
KSDIR=$(SHAREDIR)/kickstart

DOCDIR=$(PREFIX)/share/doc/$(NAME)-$(VERSION)

ECG_MANSECT=8
ECG_MANDIR=$(PREFIX)/share/man/man$(ECG_MANSECT)

all: kickstart-files

kickstart-files: 
	echo $(NAME)-$(VERSION)-$(RELEASE).noarch.rpm > kickstart/rpm-name.lst
	make RPM_SITE=$(RPM_SITE) -C kickstart

install: all
	install -d $(DESTDIR)$(BINDIR) $(DESTDIR)$(DOCDIR) $(DESTDIR)$(SHAREDIR)
	install -d $(DESTDIR)$(ECG_MANDIR) $(DESTDIR)$(KSDIR)
	perl -pe s!--BASE--!$(SHAREDIR)! < bin/$(SCRIPT).in > $(DESTDIR)$(BINDIR)/$(SCRIPT)
	chmod 555 $(DESTDIR)$(BINDIR)/$(SCRIPT)
	install `ls -d cc/* | grep -v CVS` $(DESTDIR)$(SHAREDIR)
	install kickstart/ks-* $(DESTDIR)$(KSDIR)
	-install `ls -d doc/* | grep -v CVS` $(DESTDIR)$(DOCDIR)
	-gzip < doc/$(ECG).man > $(DESTDIR)$(ECG_MANDIR)/$(ECG).$(ECG_MANSECT).gz

