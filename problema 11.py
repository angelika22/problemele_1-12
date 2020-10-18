nr_la_inceput=int(input("numarul iepurilor la inceput de luna:"))
nr_de_nascuti=int(input("numar iepurilor nascuti in timpul lunii:"))
nr_de_morti=int(input("numar iepurilor de morti la sfirsitul lunii:"))
nr_la_sfirsit=nr_la_inceput+nr_de_nascuti-nr_de_morti
print("numarul de iepuri la sfirsit de luna este", nr_la_sfirsit)