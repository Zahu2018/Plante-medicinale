# Face tabel mare
#recursive, #return recursive, #return, #function
cuvinte = ['Denumire ştiinţifică', 'Denumire populară', 'Sinonime ştiinţifice', 'Alte denumiri populare', 'Regnul', 'Încrengătura', 'Subîncrengătura', 'Clasa', 'Subclasa', 'Ordinul', 'Familia', 'Subfamilia', 'Caractere morfologice', 'Ecologie şi răspândire', 'Organe utilizate','Compoziţia chimică','Acţiune terapeutică', 'Importanţa','Utilizare','Alte utilizări','Toxicitate','Contraindicaţii','Precauţii şi reacţii adverse','Dozare','Supradozare','Forme farmaceutice','Conservare','Cultivare','Mod de cultivare','Recoltare (organe şi mod)','Valorificare', 'Alte specii'] # = 32
def ia_o_planta(i):
    f = text.find("Fişa speciei\n#===========", i+1)
    planta = text[i:f]
    return planta, f
def incearca(tp, k): # tp=text_planta;
    try:
        ku2 = cuvinte[k+1]
        if ku2 in tp:
            
            return ku2
            
        else:
            k += 1
########################################################
#            FUNCTIE RECURSIVA !!!                     #            
            return incearca(tp, k) # not just incearca #
########################################################        
    except IndexError:
        
        return "Final"
    
with open("PM_3.txt", "r", encoding="utf-8") as f:
    text = f.read()

lista_dictionare = []
x = text.count("""Fişa speciei\n#===========""")
j = 0
t = ""

for i in range(x):
    dictionar = {}
    text_planta, k = ia_o_planta(j)
    j = k
    initial = 0
    for k in range(len(cuvinte)):
        ku = cuvinte[k]
        if ku in text_planta:
            ini = text_planta.find(ku) + len(ku) + 1
            ku2 = incearca(text_planta, k)
            fin = text_planta.find(ku2)
            dictionar.setdefault(ku, (text_planta[ini:fin]).strip())
       
        else:
            dictionar.setdefault(ku, "")

    lista_dictionare.append(dictionar)

#import csv
#
#with open('MARE-TOT.csv', 'w', encoding='utf8', newline='') as output_file:
#    fc = csv.DictWriter(output_file, fieldnames=lista_dictionare[0].keys())
#    fc.writeheader()
#    fc.writerows(lista_dictionare)