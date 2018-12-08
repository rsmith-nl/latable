# file: Makefile
# Makefile for Python module
# vim:fileencoding=utf-8:fdm=marker:ft=make
#
# Copyright © 2018 R.F. Smith <rsmith@xs4all.nl>
# Created: 2018-11-05T23:07:20+0100
# Last modified: 2018-12-09T00:14:25+0100

.PHONY: all install uninstall clean check tags format test
.SUFFIXES: .ps .pdf .py

MOD= latable
SRCS:= ${MOD}.py
PKGPATH!=python3 -c "import site; print(site.getsitepackages()[0])"

all::
	@echo 'you can use the following commands:'
	@echo '* test: run the built-in tests.'
	@echo '* install'
	@echo '* uninstall'
	@echo '* dist: create a distribution file.'
	@echo '* clean: remove all generated files.'
	@echo '* check: run pylama on all python files.'
	@echo '* tags: run exctags.'
	@echo '* format: format the source with yapf.'

install::
	@if [ `id -u` != 0 ]; then \
		echo "You must be root to install the module!"; \
		exit 1; \
	fi
# Let Python do the install work.
	python3 -B setup.py install
	rm -rf build dist *.egg-info

uninstall::
	@if [ `id -u` != 0 ]; then \
		echo "You must be root to deinstall the program!"; \
		exit 1; \
	fi
	rm -f ${PKGPATH}/${MOD}.py ${PKGPATH}/${MOD}.egg*

# Create distribution file. Use zip format to make deployment easier on windoze.
dist:
	python3 -B setup.py sdist --format=zip
	rm -f MANIFEST

clean::
	rm -rf dist build backup-*.tar* MANIFEST *.egg-info
	find . -type f -name '*.pyc' -delete
	find . -type d -name __pycache__ -delete

check:: .IGNORE
	env PYTHONWARNINGS=ignore::FutureWarning pylama -i E501,W605 ${MOD}.py tests/*.py

tags::
	exctags -R  --verbose

format::
	yapf-3.7 -i ${MOD}.py setup.py tests/*.py

test::
	pytest-3.7 -v tests
