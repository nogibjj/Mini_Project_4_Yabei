install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python3 -m pytest -vv --cov=main test_*.py

format:	
	black *.py 

lint:
	pylint --disable=R,C,locally-disabled --ignore-patterns=test_.*?py *.py
		

		
all: install lint test format deploy
