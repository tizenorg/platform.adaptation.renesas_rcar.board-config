SUBDIRS=sound video

all:
	for d in ${SUBDIRS}; do $(MAKE) -C $$d; done

install:
	for d in ${SUBDIRS}; do $(MAKE) install -C $$d; done
