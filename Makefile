# file: Makefile
# Makefile for Python module
# vim:fileencoding=utf-8:fdm=marker:ft=make
#
# Copyright © 2018 R.F. Smith <rsmith@xs4all.nl>
# Created: 2018-11-05T23:07:20+0100
# Last modified: 2018-11-06T23:02:11+0100

.PHONY: all install tests dist clean backup deinstall check tags format
.SUFFIXES: .ps .pdf .py

MOD = latable
SRCS = ${MOD}.py

all::
	@echo 'you can use the following commands:'
	@echo '* tests'
	@echo '* install'
	@echo '* deinstall'
	@echo '* dist'
	@echo '* clean'
	@echo '* check'
	@echo '* tags'
	@echo '* format'

PYSITE!=python3 -B -c 'import site; print(site.getsitepackages()[0])'

install: setup.py ${MOD}.py
	@if [ `id -u` != 0 ]; then \
		echo "You must be root to install the module!"; \
		exit 1; \
	fi
# Let Python do the install work.
	python3 -B setup.py install
	rm -rf build

deinstall::
	@if [ `id -u` != 0 ]; then \
		echo "You must be root to deinstall the program!"; \
		exit 1; \
	fi
	rm -f ${PYSITE}/${MOD}.py

dist:
# Create distribution file. Use zip format to make deployment easier on windoze.
	python3 -B setup.py sdist --format=zip
	rm -f MANIFEST

clean::
	rm -rf dist build backup-*.tar.gz MANIFEST __pycache__

check::
	env PYTHONWARNINGS=ignore::FutureWarning pylama -i E501 ${MOD}.py tests/*.py

tags::
	exctags -R

format::
	yapf-3.7 -i ${MOD}.py setup.py tests/*.py

tests::
	pytest-3.7 -v tests
