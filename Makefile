usage:
	@echo "usage: make [clean|site|serve]"

clean:
	git clean -dfx

site:
	hugo --minify

serve:
	hugo serve
