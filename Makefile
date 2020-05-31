.PHONY: rai raip 

rai:
	@echo "Rebuid and install plerr package."
	@rm -rf build dis plerr.egg-info 2>/dev/null
	@python3 -m pip uninstall -y plerr Pygments
	@python3 setup.py install

raip:
	@echo "Rebuild and install plerr package to pipx."
	@rm -rf build dis plerr.egg-info 2>/dev/null
	@python3 setup.py bdist_wheel
	@python3 -m pipx uninstall plerr
	@python3 -m pipx install -f dist/*
