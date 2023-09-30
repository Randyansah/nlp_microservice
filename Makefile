install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_*.py

format:
	black *.py mylib/*.py
lint:
	pylint --disable=R,C --extension-pkg-whitelist='pydantic' main_one.py --ignore-patterns=test_.*?py *.py  mylib/*.py
	pylint --disable=R,C,E1120 *.py 

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile
refactor: format lint	
deploy:
	#echo "Deploy goes here" 
all: install lint test 		