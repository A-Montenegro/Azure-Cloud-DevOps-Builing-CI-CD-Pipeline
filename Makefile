install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_hello.py


lint:                                         
/home/ana/.local/bin/pylint --disable=R,C hello.py

all: install lint test