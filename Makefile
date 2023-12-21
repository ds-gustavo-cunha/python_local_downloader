download:
	python main.py

black:
	black main.py

install_dependencies:
	pip install -r requirements.txt

reinstall_dependencies:
	pip uninstall -y -r <(pip freeze)