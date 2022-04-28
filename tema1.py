import sys

def readTM(encode_lines):  # encode_lines sunt liniile cu configuratia masinii
    m = {}  # m este un dictionar corespunzator codificarii masinii
    m["nr_states"] = encode_lines[0].strip("\n")  #  nr de stari
    final_states = encode_lines[1].split()  # starile finale
    m["final_states"] = final_states
    for line in encode_lines[2:]:  #liniile 2: sunt cele n tranzitii 
        line = line.split()  # separam tranzitia cu " " ca despartitor
        if not line[0] in m:  # line[0] este starea curenta
            m[line[0]] = {}
        m[line[0]][line[1]] = line[2:]  # line[1] este simbolul curent
        # line[2:] fac parte din tranzitia urmatoare
    return m

def step(m, curr_config):
    config = curr_config.split(',')  #curr_config este configuratia masinii
    # config[1] este starea in care se afla masina
    if not config[1] in m:  # verifica daca starea se afla printre tranzitii
        return curr_config
    # config[2][0] este simbolul curent
    if not config[2][0] in m[config[1]]: # verifica daca masina are o stare urmatoare
        return curr_config
    ''' m[config[1]][config[2][0]] este o lista cu starea urmatoare, simbolul nou
    si pozitia cursorului'''
    # verifica directia in care se muta cursorul si creeaza noua configuratie
    transition = m[config[1]][config[2][0]]
    if transition[2] == 'R':
        new_config = config[0] + transition[1] + ',' + transition[0] + ','
        if len(config[2]) == 2:
            new_config += "#)"
        else:
            new_config += config[2][1:]
    elif transition[2] == 'L':
        if len(config[0]) == 2:
            new_config = "(#"
        else:
            new_config = config[0][0:-1]
        new_config += ',' + transition[0] + ',' + config[0][-1] + transition[1]
        new_config += config[2][1:]
    else:
        new_config = config[0] + ',' + transition[0] + ',' + transition[1]
        new_config += config[2][1:]
    if config != new_config:
        return new_config

def accept(m, word):
    config = "(#,0," + word + ')'  # configuratia initiala a masinii
    new_config = ""
    ''' realizeaza cate un pas al masinii, si executa cat timp aceasta nu este
    intr-o stare finala sau nu a intrat intr-un ciclu infinit'''
    while config.split(',')[1] not in m["final_states"]:
        new_config = step(m, config)
        if config != new_config:
            config = new_config
        else:
            return False
    return True


def accept_k(m, word, k):
    config = "(#,0," + word + ')'  # configuratia initiala a masinii
    new_config = ""
    ''' realizeaza cate un pas al masinii, daca se ajunge intr-o stare finala
    se opreste si intoarce true, daca nu, continua pana se depaseste numarul de 
   	k pasi si intoarce false'''
    for i in range(0, int(k)):
        new_config = step(m, config)
        if config != new_config:
            config = new_config
        else:
            return False
        # config.split(',')[1] este starea curenta
        if config.split(',')[1] in m["final_states"]:
            return True
    return False

def main():
    lines = sys.stdin.readlines()  # citeste fiecare linie de la stdin
    m = readTM(lines[2:])  # lines[2:] sunt liniile cu configuratia masinii
    #lines[0] este tipul taskului
    if "step" in lines[0]:  # verificam tipul taskului
        configs = lines[1].split()  # lines[1] - configuratiile pe care rulam
        for config in configs: # rulam pe fiecare configuratie
            new_config = step(m, config)
            if config == new_config:
                print(False, end = " ")
            else:
                print(new_config, end = " ")
    elif "k_accept" in lines[0]:
        words_with_k = lines[1].split()
        for word_with_k in words_with_k:
            word = word_with_k.split(',')[0]  # cuvantul pe care rulam
            k = word_with_k.split(',')[1]  # k - numarul de pasi
            print(accept_k(m, word, k), end = " ")
    else:
        words = lines[1].split()
        for word in words:
            print(accept(m, word), end = " ")

if __name__ == "__main__":
    main()