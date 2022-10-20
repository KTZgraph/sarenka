.PHONY: build
build:
	docker build -t sarenka .

.PHONY: run
run:
	docker run -p 8000:8000 sarenka