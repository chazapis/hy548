.PHONY: all html

all: html

html:
	(cd html && hugo -D)

clean:
	rm -rf html/public
