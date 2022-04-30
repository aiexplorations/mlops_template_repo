install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C src/hello.py
	pylint --disable=R,C src/gen_data.py

format:
	black src/*.py
	black tests/*.py

test:
	python -m unittest discover .
	python -m pytest -vv --cov=hello tests/test_hello.py
	python -m pytest -vv --cov=gen_data tests/test_gen_data.py
