usage:
	@echo "usage: make [clean|site|serve]"

clean:
	git clean -dfx

site:
	hugo --minify

serve:
	hugo serve

# create a new recipe for guacamole:
# $ hugo new --kind recipe-bundle recipes/guacamole