
default:	build

clean:
	rm -rf Makefile objs

build:
	$(MAKE) -f objs/Makefile
	$(MAKE) -f objs/Makefile manpage

install:
	$(MAKE) -f objs/Makefile install

upgrade:
	/usr/bin/nginx -t

	kill -USR2 `cat /run/nginx.pid`
	sleep 1
	test -f /run/nginx.pid.oldbin

	kill -QUIT `cat /run/nginx.pid.oldbin`
