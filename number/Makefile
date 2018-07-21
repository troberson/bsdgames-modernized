build:
	docker build -t bsdnumber .
	
run: build
	docker run -it --rm --name bsdnumber bsdnumber
	
build-test: build
	docker build -t bsdnumber-test -f ./Dockerfile.test .

test: build-test
	docker run -it --rm --name bsdnumber-test bsdnumber-test
