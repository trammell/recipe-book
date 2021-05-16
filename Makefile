usage:
	@echo "usage: make [clean|site|serve]"

clean:
	git clean -f

site:
	hugo --minify

serve:
	hugo serve
