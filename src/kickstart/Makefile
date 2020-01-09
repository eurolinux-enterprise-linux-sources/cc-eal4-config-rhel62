all: configs

configs:
	./Make-kickstart-configs.sh

clean:
	rm -f ks-*.cfg

floppy:
	if [ ! -f kickstart.img ]; then dd if=/dev/zero of=kickstart.img bs=1k count=1440; fi
	/sbin/mkfs.msdos kickstart.img
	mcopy -i kickstart.img ks-*.cfg ::
	mcopy -i kickstart.img ks-i386.cfg ::ks
