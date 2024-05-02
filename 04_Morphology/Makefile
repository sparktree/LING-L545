all: esp.gen.hfst

esp.lexc.hfst: esp.lexc
		hfst-lexc esp.lexc -o esp.lexc.hfst
esp.twol.hfst: esp.twol
		hfst-twolc esp.twol -o esp.twol.hfst
esp.gen.hfst: esp.lexc.hfst esp.twol.hfst
		hfst-compose-intersect -1 esp.lexc.hfst -2 esp.twol.hfst -o esp.gen.hfst