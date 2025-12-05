include Makefile.inc

ZENSICAL := zensical

.PHONY: serve build deploy clean

## Serve site locally
serve: build
	@$(RUN) $(ZENSICAL) serve

## Build site
build: clean
	@$(RUN) $(ZENSICAL) build

##! Deploy site
deploy: clean
	@${RUN} $(ZENSICAL) gh-deploy

## Clean site
clean:
	@rm -rf site
