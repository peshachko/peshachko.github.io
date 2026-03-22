include Makefile.inc

ZENSICAL := zensical

.PHONY: serve build clean

## Serve site locally
serve: build
	@$(RUN) $(ZENSICAL) serve

## Build site
build: clean members
	@$(RUN) $(ZENSICAL) build --clean

## Clean site
clean:
	@rm -rf site docs/members.md

members: ## Generate members table from JSON
	@$(RUN) utils/members_table.py docs/data/members.json docs/members.md

## Resize images
resize:
	$(if $(strip $(IMG_DIR)),,$(error IMG_DIR is not set.))
	cd $(IMG_DIR) && \
	for image in *; do \
		magick "$$image" \
		-resize 1000x800 \
		-quality 72 \
		"_resized_$$image"; \
	done
