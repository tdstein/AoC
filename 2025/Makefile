.SECONDARY:

%: %a/main.go %b/main.go %.in %.sample
	@echo "Generated files for $*"

%a/main.go:
	mkdir -p $*a
	[ -e $@ ] || cp main.go.template $@

%b/main.go:
	mkdir -p $*b
	[ -e $@ ] || cp main.go.template $@

%.in:
	[ -e $@ ] || touch $@

%.sample:
	[ -e $@ ] || touch $@
