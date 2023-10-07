install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main test.py
format:
	black *.py
lint:
	pylint --disable=R,C,E1120 *.py 

container-lint:
	#docker run --rm -i hadolint/hadolint < Dockerfile
refactor: format lint	
deploy:
	#echo "Deploy goes here" 
all: install lint test 		