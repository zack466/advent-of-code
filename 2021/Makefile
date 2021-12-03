.PHONY: all
all: day1 day2 day3

day1:
	ghc -o day1 day1.hs && ./day1 < day1.in

day2:
	ocamlopt -o day2 day2.ml && ./day2

day3:
	gcc -o day3 day3.c && ./day3

.PHONY: clean
clean:
	rm -f day1 day1.hi day1.o \
		day2 day2.cmx day2.cmi day2.o \
		day3
