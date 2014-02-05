install: 50-audio.rules asound.state
	install asound.state -D ${DESTDIR}/var/lib/alsa/asound.state
	install 50-audio.rules -D ${DESTDIR}/etc/udev/rules.d/50-audio.rules

.PHONY: install
