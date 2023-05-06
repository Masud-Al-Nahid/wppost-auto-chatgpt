def ppa():
    with open('people_also.txt', 'r') as file:
        readline = file.readlines()
        for line in readline:
            ppa_file = line.strip()
            return ppa_file