from operator import itemgetter

# VARIAVEIS
posicao = 0
posicao1 = 0
selecionados = list()
lista = list()
s1 = [2, 3, 6, 7, 10]
s2 = [1, 4, 5, 8, 9]

# LISTA DOS TIPOS DE HEROIS
atiradores = list()
soldados = list()
tanks = list()
magos = list()
assassinos = list()
suportes = list()
tudo = list()

# COR
branco = '\033[1;97m'
vermelho = '\033[1;31m'
verde = '\033[1;32m'
amarelo = '\033[1;33m'
azul = '\033[1;34m'
roxo = '\033[1;35m'
ciano = '\033[1;36m'
cinza = '\033[1;37m'

# LISTA DE HEROIS
herois = [{'heroi': 'miya', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['a'],
           'counter': ['saber', 'kaja', 'karina', 'chou', 'helcurt'], 'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'bruno', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['a'], 'counter': ['karina'],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'clint', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['a'], 'counter': [],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'layla', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['a'], 'counter': [],
           'favoraveis': [], 'situacao': 'disponivel'},          {'heroi': 'roger', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['a', 's', 'ass'], 'counter': [],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'irithel', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['a'], 'counter': [],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'granger', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['a'], 'counter': [],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'wanwan', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['a'],
           'counter': ['natalia', 'zilong', 'phoveus'], 'favoraveis': ['tigreal', 'belerick'],
           'situacao': 'disponivel'}, {'heroi': 'hanabi', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['a'],
                                       'counter': ['benedetta', 'vale'], 'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'yi sun-shin', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['a', 'ass'],
           'counter': ['zilong'], 'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'moskov', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['a'], 'counter': [],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'karrie', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['a'], 'counter': ['benedetta'],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'lesley', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['a'], 'counter': [],
           'favoraveis': ['harley'], 'situacao': 'disponivel'},
          {'heroi': 'claude', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['a'], 'counter': ['lesley'],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'kimmy', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['a'], 'counter': ['lancelot'],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'popol e kupa', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['a'],
           'counter': ['hanzo', 'helcurt', 'gusion'], 'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'brody', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['a'], 'counter': ['gusion'],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'beatrix', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['a'],
           'counter': ['clint', 'mathilda', 'benedetta', 'natalia', 'chou'], 'favoraveis': [],
           'situacao': 'disponivel'},
          {'heroi': 'natan', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['a'], 'counter': [],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'tigreal', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['t'],
           'counter': ['nana', 'wanwan', 'miya', 'harley', 'kagura'],
           'favoraveis': ['guinevere', 'wanwan', 'luo yi', 'alice'], 'situacao': 'disponivel'},
          {'heroi': 'franco', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['t'],
           'counter': ['kagura', 'alpha', 'ruby', 'wanwan', 'chou'], 'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'johnson', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['t'], 'counter': ['esmeralda'],
           'favoraveis': ['odette'], 'situacao': 'disponivel'},
          {'heroi': 'uranus', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['t'], 'counter': [],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'atlas', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['t'], 'counter': [],
           'favoraveis': ['alice'], 'situacao': 'disponivel'},
          {'heroi': 'lolita', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['t', 'su'], 'counter': [],
           'favoraveis': ['luo yi'], 'situacao': 'disponivel'},
          {'heroi': 'akai', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['t'],
           'counter': ['diggie', 'moskov', 'kagura', 'karrie', 'eudora'], 'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'grock', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['t'], 'counter': [],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'minotauro', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['t', 'su'], 'counter': [],
           'favoraveis': ['guinevere', 'alice'], 'situacao': 'disponivel'},
          {'heroi': 'hilda', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['t', 's'], 'counter': [],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'gatotkaca', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['t', 's'], 'counter': [],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'hylos', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['t'], 'counter': [],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'belerick', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['t'], 'counter': [],
           'favoraveis': ['wanwan'], 'situacao': 'disponivel'},
          {'heroi': 'khufra', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['t'], 'counter': [],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'baxia', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['t'], 'counter': [],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'barats', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['t', 's'], 'counter': ['selena'],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'gloo', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['t'], 'counter': [],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'nana', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['m', 'su'],
           'counter': ['natalia', 'helcurt', 'kaja', 'hayabusa', 'lesley'], 'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'eudora', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['m'], 'counter': [],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'gord', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['m'],
           'counter': ['irithel', 'kimmy'], 'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'kagura', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['m'], 'counter': ['esmeralda'],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'harley', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['m', 'ass'],
           'counter': ['eudora', 'lancelot', 'ling', 'nana', 'lunox'], 'favoraveis': ['lesley'],
           'situacao': 'disponivel'},
          {'heroi': 'odette', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['m'], 'counter': [],
           'favoraveis': ['johnson'], 'situacao': 'disponivel'},
          {'heroi': 'zhask', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['m'], 'counter': ['valentina'],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'change', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['m'], 'counter': [],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'selena', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['m', 'su'], 'counter': [],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'faramis', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['m', 'su'], 'counter': [],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'cecilion', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['m'], 'counter': [],
           'favoraveis': ['carmilla'], 'situacao': 'disponivel'},
          {'heroi': 'luo yi', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['m'], 'counter': [],
           'favoraveis': ['tigreal', 'lolita'], 'situacao': 'disponivel'},
          {'heroi': 'harith', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['m'], 'counter': ['phoveus'],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'cyclops', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['m'], 'counter': [],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'aurora', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['m'], 'counter': [],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'vexana', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['m'], 'counter': [],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'pharsa', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['m'], 'counter': ['zilong'],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'valir', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['m'],
           'counter': ['irithel', 'kimmy'], 'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'vale', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['m'],
           'counter': ['kagura', 'kadita'], 'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'lunox', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['m'], 'counter': ['eudora'],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'kadita', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['m'], 'counter': [],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'esmeralda', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['m', 's'],
           'counter': ['baxia'], 'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'lylia', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['m'], 'counter': [],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'yve', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['m'], 'counter': [],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'alice', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['m', 's'],
           'counter': ['aurora', 'atlas', 'jawhead', 'argus', 'harley'],
           'favoraveis': ['atlas', 'tigreal', 'minotauro'], 'situacao': 'disponivel'},
          {'heroi': 'balmond', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['s'],
           'counter': ['dyrroth', 'uranus', 'change', 'leomord', 'cyclops'], 'favoraveis': [],
           'situacao': 'disponivel'},
          {'heroi': 'alucard', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['s', 'ass'],
           'counter': ['fanny', 'zhask', 'eudora', 'selena', 'khufra'], 'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'zilong', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['s', 'ass'],
           'counter': ['valentina', 'yu zhong'], 'favoraveis': ['angela'], 'situacao': 'disponivel'},
          {'heroi': 'chou', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['s'], 'counter': [],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'argus', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['s'], 'counter': ['valentina'],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'x.borg', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['s'], 'counter': [],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'silvanna', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['s'], 'counter': ['esmeralda'],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'yu zhong', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['s'], 'counter': ['valentina'],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'badang', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['s'], 'counter': [],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'bane', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['s'],
           'counter': ['alucard', 'bruno', 'zilong', 'chou', 'alpha'], 'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'freya', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['s', 'ass'], 'counter': [],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'sun', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['s'], 'counter': ['odette'],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'alpha', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['s'], 'counter': [],
           'favoraveis': ['angela'], 'situacao': 'disponivel'},
          {'heroi': 'ruby', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['s'],
           'counter': ['aurora', 'barats', 'kagura', 'kaja', 'baxia'], 'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'lapu-lapu', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['s'], 'counter': [],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'jawhead', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['s', 't', 'ass'],
           'counter': ['guinevere', 'diggie', 'lancelot', 'lunox', 'sun'], 'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'martis', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['s'], 'counter': [],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'kaja', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['s', 'su'], 'counter': [],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'aldous', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['s'], 'counter': [],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'leomord', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['s'], 'counter': ['valentina'],
           'favoraveis': ['angela'], 'situacao': 'disponivel'},
          {'heroi': 'thamuz', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['s'], 'counter': [],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'minsitthar', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['s'], 'counter': [],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'terizla', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['s'], 'counter': [],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'dyrroth', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['s'], 'counter': [],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'masha', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['s'], 'counter': ['aldous'],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'khaleed', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['s'], 'counter': [],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'paquito', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['s'], 'counter': [],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'phoveus', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['s'], 'counter': [],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'guinevere', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['s'],
           'counter': ['balmond', 'ruby', 'sun', 'badang', 'diggie'], 'favoraveis': ['minotauro', 'tigreal'],
           'situacao': 'disponivel'},
          {'heroi': 'angela', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['su'], 'counter': ['esmeralda'],
           'favoraveis': ['zilong', 'ling', 'leomord', 'alpha'], 'situacao': 'disponivel'},
          {'heroi': 'rafaela', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['su'], 'counter': [],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'estes', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['su'],
           'counter': ['saber', 'luo yi'], 'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'mathilda', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['m', 'su'], 'counter': [],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'diggie', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['su'], 'counter': [],
           'favoraveis': ['karina'], 'situacao': 'disponivel'},
          {'heroi': 'carmilla', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['su'],
           'counter': ['harith', 'masha', 'wanwan'], 'favoraveis': ['cecilion'], 'situacao': 'disponivel'},
          {'heroi': 'lancelot', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['ass'], 'counter': [],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'saber', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['ass'],
           'counter': ['eudora', 'benedetta', 'diggie', 'faramis', 'minsitthar'], 'favoraveis': [],
           'situacao': 'disponivel'},
          {'heroi': 'hayabusa', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['ass'], 'counter': [],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'helcurt', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['ass'], 'counter': [],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'gusion', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['ass'], 'counter': ['chou'],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'hanzo', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['ass'],
           'counter': ['natalia', 'benedetta', 'aamon', 'ling', 'valentina'], 'favoraveis': [],
           'situacao': 'disponivel'},
          {'heroi': 'ling', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['ass'], 'counter': [],
           'favoraveis': ['angela'], 'situacao': 'disponivel'},
          {'heroi': 'karina', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['ass'],
           'counter': ['x.borg', 'kaja', 'khaleed', 'chou', 'lunox'], 'favoraveis': ['diggie'],
           'situacao': 'disponivel'},
          {'heroi': 'fanny', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['ass'],
           'counter': ['akai', 'franco', 'eudora', 'lesley'], 'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'benedetta', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['s', 'ass'],
           'counter': ['harith', 'kaja', 'wanwan'], 'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'natalia', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['s', 'ass'],
           'counter': ['hylos', 'kaja', 'alice', 'thamuz', 'aldous'], 'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'aulus', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['s'],
           'counter': ['hayabusa', 'hanabi', 'popol e kupa'], 'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'yin', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['s'],
           'counter': ['valentina', 'khaleed'], 'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'aamon', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['ass'], 'counter': [],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'valentina', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['m'],
           'counter': ['kagura', 'miya', 'wanwan', 'harith'], 'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'edith', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['s'], 'counter': ['valentina'],
           'favoraveis': [], 'situacao': 'disponivel'},
          {'heroi': 'floryn', 'pontos_positivos': 0, 'pontos_negativos': 0, 'classe': ['sup'], 'counter': [],
           'favoraveis': [], 'situacao': 'disponivel'}]


def encontrarposicao(h):  # ENCONTRAR ONDE O HEROI ESTÁ NA LISTA
    global posicao
    for laco in range(len(herois)):
        if herois[laco]['heroi'] == h:
            posicao = laco


def encontrarposicao1(h1):  # ENCONTRAR ONDE O HEROI COUNTERADO ESTÁ NA LISTA
    global posicao1
    for laco in range(len(herois)):
        if herois[laco]['heroi'] == h1:
            posicao1 = laco


def pontuacao_positiva():
    for heroi in herois[posicao]['counter']:
        encontrarposicao1(heroi)
        if heroi == herois[posicao1]['heroi']:
            herois[posicao1]['pontos_positivos'] += 1


def pontuacao_negativa(h2):
    for laco in range(len(herois)):
        if h2 in herois[laco]['counter']:
            herois[laco]['pontos_negativos'] -= 1


def pontuacao_favoraveis(h3):
    for laco in range(len(herois)):
        if h3 in herois[laco]['favoraveis']:
            herois[laco]['pontos_positivos'] += 0.1


def mostra(h_classe1):
    if h_classe1 == 'a':
        h_classe1 = atiradores
    if h_classe1 == 's':
        h_classe1 = soldados
    if h_classe1 == 't':
        h_classe1 = tanks
    if h_classe1 == 'm':
        h_classe1 = magos
    if h_classe1 == 'ass':
        h_classe1 = assassinos
    if h_classe1 == 'sup':
        h_classe1 = suportes
    for laco in range(len(h_classe1)):
        if h_classe1[laco]["pontos_positivos"] != 0 or h_classe1[laco]["pontos_negativos"] != 0:
            print(f'        {branco}{h_classe1[laco]["heroi"].title():<17}', end='')
            print(f'{verde}{h_classe1[laco]["pontos_positivos"]:<12}', end='')
            print(f'{vermelho}{h_classe1[laco]["pontos_negativos"]:>10}')

def linha__():  # LINHA =
    print(f'{branco}'+'=' * 62)


def linha_():  # LINHA -
    print(f'{branco}'+'-' * 62)


# QUEM COMECA BANINDO
linha__()
print(f'{branco}{"QUEM COMEÇA BANINDO?":^50}')
print(f'                 {verde}[TIME] {branco}ou {vermelho}[ADV]{branco}')
while True:
    comeco = str(input('\033[1;97m> ')).lower().strip()
    if comeco == 'time' or comeco == 'adv':
        break
linha_()
print(f'{branco}{"BANIMENTO":^50}')
print(f'{branco}{"NÃO DIGITE NADA SE O HERÓI NÃO FOR BANIDO":^50}\n')

# BANS
qnt = 0
for c in range(6):
    posicao = 0
    qnt += 1
    heroi_banido = str(input(f'{branco}{qnt}º HERÓI {vermelho}BANIDO: '))
    encontrarposicao(heroi_banido)
    if heroi_banido == herois[posicao]['heroi']:
        herois.pop(posicao)
        print(f'{branco}{heroi_banido.title()}{vermelho} banido!\n')
linha_()

# SELEÇÃO DE HEROIS E PONTUAÇÃO
print(f'{branco}{"SELEÇÃO DE HERÓIS":^50}')
print(f' {branco}(DIGITE "{verde}ok{branco}" PARA ENCERRAR A SELEÇÃO DE HERÓIS)\n')
qnt = 0
if comeco == 'time':
    while True:
        qnt += 1
        verdade = 'nao'
        s = 0
        while verdade == 'nao':
            s = str(input(f'{azul}{qnt}º{branco} herói selecionado: ')).lower().strip()
            if s == 'ok':
                verdade = 'sim'
            for laco1 in range(len(herois)):
                if herois[laco1]['heroi'] == s:
                    verdade = 'sim'
        if s == 'ok':
            break
        encontrarposicao(s)
        if s == herois[posicao]['heroi']:
            herois[posicao]['situacao'] = 'indisponivel'
            if qnt in s1:
                pontuacao_positiva()
                pontuacao_negativa(s)
            if qnt in s2:
                pontuacao_favoraveis(s)
                lista.append(s)
        if qnt == 8:
            break
else:
    while True:
        qnt += 1
        verdade = 'nao'
        s = 0
        while verdade == 'nao':
            s = str(input(f'{azul}{qnt}º{branco} herói selecionado: ')).lower().strip()
            if s == 'ok':
                verdade = 'sim'
            for laco1 in range(len(herois)):
                if herois[laco1]['heroi'] == s:
                    verdade = 'sim'
        if s == 'ok':
            break
        encontrarposicao(s)
        if s == 'ok':
            break
        if s == herois[posicao]['heroi']:
            herois[posicao]['situacao'] = 'indisponivel'
            if qnt in s1:
                pontuacao_favoraveis(s)
                lista.append(s)
            if qnt in s2:
                pontuacao_positiva()
                pontuacao_negativa(s)
        if qnt == 9:
            break
linha_()

# HERÓIS SÃO SEPARADOS EM LISTAS
for heroi1 in herois:
    if 'a' in heroi1['classe'] and heroi1['situacao'] == 'disponivel':
        atiradores.append(heroi1)
    elif 's' in heroi1['classe'] and heroi1['situacao'] == 'disponivel':
        soldados.append(heroi1)
    elif 't' in heroi1['classe'] and heroi1['situacao'] == 'disponivel':
        tanks.append(heroi1)
    elif 'm' in heroi1['classe'] and heroi1['situacao'] == 'disponivel':
        magos.append(heroi1)
    elif 'ass' in heroi1['classe'] and heroi1['situacao'] == 'disponivel':
        assassinos.append(heroi1)
    elif 'su' in heroi1['classe'] and heroi1['situacao'] == 'disponivel':
        suportes.append(heroi1)
atiradores = sorted(atiradores, key=itemgetter('pontos_positivos'), reverse=True)
soldados = sorted(soldados, key=itemgetter('pontos_positivos'), reverse=True)
tanks = sorted(tanks, key=itemgetter('pontos_positivos'), reverse=True)
magos = sorted(magos, key=itemgetter('pontos_positivos'), reverse=True)
assassinos = sorted(assassinos, key=itemgetter('pontos_positivos'), reverse=True)
suportes = sorted(suportes, key=itemgetter('pontos_positivos'), reverse=True)

# ESCOLHA DO TIPO DE HERÓI
print(f'{branco}{"TIPO DO HERÓI":^50}'
      f'\n{amarelo}[A] {branco}para atiradores'
      f'\n{roxo}[S] {branco}para soldados'
      f'\n{verde}[T] {branco}para tanks'
      f'\n{azul}[M] {branco}para magos'
      f'\n{vermelho}[ASS] {branco}para assassinos'
      f'\n{ciano}[SUP] {branco}para suportes'
      f'\n{cinza}[TUDO] {branco}para tudo')
while True:
    h_classe = str(input(f'{branco}> ')).lower().strip()
    if h_classe == 'a' or h_classe == 's' or h_classe == 't' or h_classe == 'm'\
            or h_classe == 'ass' or h_classe == 'sup' or h_classe == 'tudo':
        break
linha__()

# MOSTRA OS HERÓIS
print(f'        {branco}HERÓI     {verde}PONTOS POSITIVOS     {vermelho}PONTOS NEGATIVOS')
linha_()
if h_classe != 'tudo':
    mostra(h_classe)
else:
    print(f'{branco}{"ATIRADORES":^50}')
    mostra('a')
    linha_()
    print(f'{branco}{"SOLDADOS":^50}')
    mostra('s')
    linha_()
    print(f'{branco}{"TANKS":^50}')
    mostra('t')
    linha_()
    print(f'{branco}{"MAGOS":^50}')
    mostra('m')
    linha_()
    print(f'{branco}{"ASSASSINOS":^50}')
    mostra('ass')
    linha_()
    print(f'{branco}{"SUPORTES":^50}')
    mostra('sup')
linha__()

# MOSTRA OS DETALHES
print(f'{branco}{"DIGITE O NOME DO HERÓI PARA VER OS DETALHES":^50}')
print(f'''                {branco}{f'("{vermelho}sair{branco}" PARA SAIR)'}''')
linha__()
while True:
    imp = str(input(f'{branco}> ')).strip().lower()
    if imp == 'sair':
        break
    counterado_por = list()
    for c in range(len(herois)):
        if imp in herois[c]['counter']:
            counterado_por.append(herois[c]['heroi'])
    for c in range(len(herois)):
        if herois[c]['heroi'] == imp:
            print(f'{branco}{imp.title():^50}')
            print(f'{branco}Counter de: {herois[c]["counter"]}')
            print(f'{branco}Counterado(a) por: {counterado_por}')
            print(f'{branco}Bons aliados: {herois[c]["favoraveis"]}')
            linha_()
linha__()
