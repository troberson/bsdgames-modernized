build:
	docker build -t bsdnumber .

build-test: build
	docker build -t bsdnumber-test -f ./Dockerfile.test .

test: build-test
	docker run -it --rm bsdnumber-test
