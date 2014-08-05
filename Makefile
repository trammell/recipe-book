usage:
	@echo "usage: make [clean|book]"

clean:
	rm -f *.pdf

book: susans-recipes.rst
	rst2pdf susans-recipes.rst


