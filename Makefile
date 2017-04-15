pip-compile:
	pip-compile --output-file requirements.txt requirements/prod.in
	pip-compile --output-file test-requirements.txt requirements/test.in
	pip-compile --output-file dev-requirements.txt requirements/dev.in

flake8:
	flake8 . --ignore=E501

clean:
	find -regex '.*\.pyc' -exec rm {} \;
	find -regex '.*~' -exec rm {} \;
	rm -rf reg-settings.py
	rm -rf MANIFEST dist build *.egg-info
