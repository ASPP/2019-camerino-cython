


install:
	python setup.py install

in: inplace

inplace:
	python setup.py build_ext -i


test: test-code

test-code: in
	pytest -v fancy_means


clean:
