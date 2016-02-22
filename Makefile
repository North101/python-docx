BEHAVE = behave
MAKE   = make
PYTHON = python
SETUP  = $(PYTHON) ./setup.py

.PHONY: accept clean coverage docs readme register sdist test upload

help:
	@echo "Please use \`make <target>' where <target> is one or more of"
	@echo "  accept    run acceptance tests using behave"
	@echo "  clean     delete intermediate work product and start fresh"
	@echo "  coverage  run nosetests with coverage"
	@echo "  docs      generate documentation"
	@echo "  readme    update README.html from README.rst"
	@echo "  register  update metadata (README.rst) on PyPI"
	@echo "  test      run tests using setup.py"
	@echo "  sdist     generate a source distribution into dist/"
	@echo "  upload    upload distribution tarball to PyPI"

accept:
	$(BEHAVE) --stop

clean:
	find . -type f -name \*.pyc -exec rm {} \;
	rm -rf dist *.egg-info .coverage .DS_Store

cleandocs:
	$(MAKE) -C docs clean

coverage:
	py.test --cov-report term-missing --cov=docx tests/

docs:
	$(MAKE) -C docs html

readme:
	rst2html README.rst >README.html
	open README.html

register:
	$(SETUP) register

sdist:
	$(SETUP) sdist

test:
	$(SETUP) test

upload:
	$(SETUP) sdist upload
