usage:
	@echo "usage: make [clean|book]"

clean:
	rm -f *.pdf

toc: susans-recipes.md
	doctoc susans-recipes.md

