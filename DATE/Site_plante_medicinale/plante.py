# INCADRARE TAXONOMICA
# face tabele mici din web-site plante medicinale
# #plante medicinale, #plante, #herbs, #taxonomie, #incadrare taxonomică
# [o] = placeholder for new line
##################################################
# Fişa speciei
# #===========
Denumire
Denumire ştiinţifică: ABIES ALBA Mill. 
Denumire populară: Brad 
Sinonime ştiinţifice: 
Alte denumiri populare:

Încadrare taxonomică 
Regnul: Plantae 
Încrengătura: Spermatophyta 
Subîncrengătura: Magnoliophytina 
Clasa: Magnoliopsida 
Subclasa: Asteridae 
Ordinul: Asterales 
Familia: Asteraceae 
Subfamilia: 

Caractere morfologice:

Ecologie şi răspândire:

Organe utilizate:

Compoziţia chimică:

Acţiune terapeutică: 

Importanţa:

Utilizare:

Alte utilizări:

Toxicitate:

Contraindicaţii:

Precauţii şi reacţii adverse:

Dozare:

Supradozare:

Forme farmaceutice:

Conservare:

Cultivare:

Mod de cultivare:

Recoltare (organe şi mod):

Valorificare: 

Alte specii:

ACORUS CALAMUS L. = de aici e ok
##################################################


def scrie(text):
    with open("A.csv", "wb") as fi:
        te = bytes(t, encoding='utf-8')
        fi.write(te)
        
def ia_o_planta(i):
    f = text.find("Fişa speciei\n#===========", i+1)
    planta = text[i:f]
    return planta, f


with open("PM_1.txt", "r", encoding="utf-8") as f:
    text = f.read()

x = text.count("""Fişa speciei\n#===========""")#; print(x)
j = 0
t = ""
for i in range(x):
    text_planta, k = ia_o_planta(j)
    j = k
    initial = 0
    # 1. FISA PLANTEI
    if "Denumire ştiinţifică:" in text_planta:
        ds_i = text_planta.find("Denumire ştiinţifică:", initial)
        ds_f = text_planta.find("\n", ds_i)
        ds = (text_planta[ds_i+21:ds_f]).strip()
        t += ds + "|"
    else:
        ds = ""
        t += ds + "|"
        
    #if "Denumire populară:" in text_planta:
    #    dp_i = text_planta.find("Denumire populară:", ds_f+1)
    #    dp_f = text_planta.find("\n", dp_i)
    #    dp = (text_planta[dp_i+19:dp_f]).strip()
    #    t += dp + "|"
    #else:
    #    dp = ""
    #    t += dp + "|"
    #    
    #if "Sinonime ştiinţifice:" in text_planta:
    #    ss_i = text_planta.find("Sinonime ştiinţifice:", dp_f+1)
    #    ss_f = text_planta.find("\n", ss_i)
    #    ss = (text_planta[ss_i+21:ss_f]).strip()
    #    t += ss + "|"
    #else:
    #    ss = ""
    #    t += ss + "|"
    #    
    #if "Alte denumiri populare:" in text_planta:
    #    adp_i = text_planta.find("Alte denumiri populare:", ss_f+1)
    #    adp_f = text_planta.find("Încadrare taxonomică", adp_i)
    #    adp = (text_planta[adp_i+24:adp_f]).strip()
    #    t += adp + "\n"
    #else:
    #    adp = ""
    #    t += adp + "\n"
    #
    # 2. INCADRARE TAXONOMICA
    #if "Regnul:" in text_planta:
    #    regnul_i = text_planta.find("Regnul:", ds_f+1)
    #    regnul_f = text_planta.find("\n", regnul_i)
    #    regnul = (text_planta[regnul_i+7:regnul_f]).strip()
    #    t += regnul + "|"
    #else:
    #    regnul = ""
    #    t += regnul + "|"
    #    
    #if "Încrengătura:" in text_planta:
    #    increngatura_i = text_planta.find("Încrengătura:", regnul_f+1)
    #    increngatura_f = text_planta.find("\n", increngatura_i)
    #    increngatura = (text_planta[increngatura_i+13:increngatura_f]).strip()
    #    t += increngatura + "|"
    #else:
    #    increngatura = ""
    #    t += increngatura + "|"
    #    
    #if "Subîncrengătura:" in text_planta:
    #    subincrengatura_i = text_planta.find("Subîncrengătura:", increngatura_f+1)
    #    subincrengatura_f = text_planta.find("\n", subincrengatura_i)
    #    subincrengatura = (text_planta[subincrengatura_i+16:subincrengatura_f]).strip()
    #    t += subincrengatura + "|"
    #else:
    #    subincrengatura = ""
    #    t += subincrengatura + "|"
    #    
    #if "Clasa:" in text_planta:
    #    clasa_i = text_planta.find("Clasa:", subincrengatura_f+1)
    #    clasa_f = text_planta.find("\n", clasa_i)
    #    clasa = (text_planta[clasa_i+6:clasa_f]).strip()
    #    t += clasa + "|"
    #else:
    #    clasa = ""
    #    t += clasa + "|"
    #    
    #if "Subclasa:" in text_planta:
    #    subclasa_i = text_planta.find("Subclasa:", clasa_f+1)
    #    subclasa_f = text_planta.find("\n", subclasa_i)
    #    subclasa = (text_planta[subclasa_i+9:subclasa_f]).strip()
    #    t += subclasa + "|"
    #else:
    #    subclasa = ""
    #    t += subclasa + "|"
    #    
    #if "Ordinul:" in text_planta:
    #    ordinul_i = text_planta.find("Ordinul:", subclasa_f+1)
    #    ordinul_f = text_planta.find("\n", ordinul_i)
    #    ordinul = (text_planta[ordinul_i+8:ordinul_f]).strip()
    #    t += ordinul + "|"
    #else:
    #    ordinul = ""
    #    t += ordinul + "|"
    #    
    #if "Familia:" in text_planta:
    #    familia_i = text_planta.find("Familia:", ordinul_f+1)
    #    familia_f = text_planta.find("\n", familia_i)
    #    familia = (text_planta[familia_i+8:familia_f]).strip()
    #    t += familia + "|"
    #else:
    #    familia = ""
    #    t += familia + "|"
    #    
    #if "Subfamilia:" in text_planta:
    #    subfamilia_i = text_planta.find("Subfamilia:", familia_f+1)
    #    subfamilia_f = text_planta.find("Caractere morfologice", subfamilia_i)
    #    subfamilia = (text_planta[subfamilia_i+11:subfamilia_f]).strip()
    #    t += subfamilia + "\n"
    #else:
    #    subfamilia = ""
    #    t += subfamilia + "\n"
    # 3. CARACTERE MORFOLOGIGE
    #if "Caractere morfologice" in text_planta:
    #    cm_i = text_planta.find("Caractere morfologice", ds_f)
    #    cm_f = text_planta.find("Ecologie şi răspândire", cm_i)
    #    cm = (text_planta[cm_i+21:cm_f]).strip()
    #    t += cm + "\n"
    #else:
    #    cm = ""
    #    t += cm + "\n"
    # 4. ECOLOGIE SI RASPANDIRE
    #if "Ecologie şi răspândire" in text_planta:
    #    er_i = text_planta.find("Ecologie şi răspândire", ds_f)
    #    er_f1 = text_planta.find("\n", er_i)
    #    er_f = text_planta.find("\n", er_f1+1)
    #    er = (text_planta[er_f1:er_f]).strip()
    #    t += er + "\n"            
    #else:
    #    er = ""
    #    t += er + "\n"
    # 5. ORGANE UTILIZATE
    #if "Denumire ştiinţifică:" in text_planta:
    #    ou_i = text_planta.find("Organe utilizate", ds_f)
    #    ou_f = text_planta.find("Compoziţia chimică", ou_i)
    #    ou = (text_planta[ou_i+16:ou_f]).strip()
    #    t += ou + "\n"
    #else:
    #    ou = ""
    #    t += ou + "\n"
    # 6. COMPOZITIA CHIMICA
    #if "Compoziţia chimică " in text_planta:
    #    ou_i = text_planta.find("Compoziţia chimică ", ds_f)
    #    ou_f = text_planta.find("Acţiune terapeutică", ou_i)
    #    ou = (text_planta[ou_i+18:ou_f]).strip()
    #    if "Detalii..." in ou:
    #        ou1 = ou.replace("Detalii...", "").strip()
    #        if "\n" in ou1:
    #            ou2 = ou1.replace("\n", " [o] ") # [o] placeholder linie noua
    #            t += ou2 + "\n"
    #        else:
    #            t += ou1 + "\n"
    #    else:
    #        if "\n" in ou:
    #            ou1 = ou.replace("\n", " [o] ") # [o] placeholder linie noua
    #            t += ou1 + "\n"
    #        else:
    #            t += ou + "\n"
    #        
    #else:
    #    ou = ""
    #    t += ou + "\n"
    # 7. ACTIUNE TERAPEUTICA, IMPORTANTA, UTILIZARE
    #if "Acţiune terapeutică " in text_planta:
    #    at_i = text_planta.find("Acţiune terapeutică ", ds_f)
    #    at_f = text_planta.find("Importanţa", at_i)
    #    at = (text_planta[at_i+20:at_f]).strip()
    #    if "\n" in at:
    #        at1 = at.replace("\n", " [o] ") # [o] placeholder linie noua
    #        t += at1 + "|"
    #    else:
    #        t += at + "|"
    #else:
    #    at = ""
    #    t += at + "|"
    #    
    #if "Importanţa \n" in text_planta:
    #    imp_i = text_planta.find("Importanţa \n", at_f)
    #    imp_f = text_planta.find("Utilizare", imp_i)
    #    imp = (text_planta[imp_i+10:imp_f]).strip()
    #    if "\n" in imp:
    #        imp1 = imp.replace("\n", " ") 
    #        t += imp1 + "|"
    #    else:
    #        t += imp + "|"
    #else:
    #    imp = ""
    #    t += imp + "|"
    #
    #if "Utilizare" in text_planta:
    #    uz_i = text_planta.find("Utilizare", imp_f)
    #    uz_f = text_planta.find("\n\n", uz_i)
    #    uz = (text_planta[uz_i+9:uz_f]).strip()
    #    if "\n" in uz:
    #        uz1 = uz.replace("\n", " [o] ") # [o] placeholder linie noua
    #        t += uz1 + "\n"
    #    else:
    #        t += uz + "\n"
    #else:
    #    uz = ""
    #    t += uz + "\n"
    # 8. 
    
                
print(t)
#scrie(t)


