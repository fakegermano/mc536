from random import sample, randint

num_torcedores = 1000
num_comentaristas = 380
num_arbitros = 36
num_times_de_futebol = 32
num_estadios = 12
num_tecnicos = 32
num_jogadores_por_time = 23
num_partidas = 64

num_assiste = 1500
num_narra = 380
num_apita = 256

#############################################
#
#	Leitura de arquivos
# 
############################################

teams_file = open("teams.txt", "r")
teams = teams_file.readlines()
for i in range(0, len(teams)):
	teams[i] = teams[i].strip()

formations_file = open("formations.txt", "r")
formations = formations_file.readlines()
for i in range(0, len(formations)):
	formations[i] = formations[i].strip()

numbers = sample(range(1, 2000001), 500000)

id_type_file = open("id_type.txt", "r")
id_type = id_type_file.readlines()
for i in range(0, len(id_type)):
	id_type[i] = id_type[i].strip()

countries_file = open("countries.txt", "r")
countries = countries_file.readlines()
for i in range(0,len(countries)):
	countries[i] = countries[i].strip()

languages_file = open("languages.txt", "r")
languages = languages_file.readlines()
for i in range(0, len(languages)):
	languages[i] = languages[i].strip()

arbitrofuncoes_file = open("arbitrofuncoes.txt", "r")
arbitrofuncoes = arbitrofuncoes_file.readlines()
for i in range(0, len(arbitrofuncoes)):
	arbitrofuncoes[i] = arbitrofuncoes[i].strip()

cidade_estadios_file = open("cidade_estadios.txt", "r")
cidade_estadios = cidade_estadios_file.readlines()
for i in range(0, len(cidade_estadios)):
	cidade_estadios[i] = cidade_estadios[i].strip()

estado_estadios_file = open("estado_estadios.txt", "r")
estado_estadios = estado_estadios_file.readlines()
for i in range(0, len(estado_estadios)):
	estado_estadios[i] = estado_estadios[i].strip()

nome_estadios_file = open("nome_estadios.txt", "r")
nome_estadios = nome_estadios_file.readlines()
for i in range(0, len(nome_estadios)):
	nome_estadios[i] = nome_estadios[i].strip()

capacidade_estadios_file = open("capacidade_estadios.txt", "r")
capacidade_estadios = capacidade_estadios_file.readlines()
for i in range(0, len(capacidade_estadios)):
	capacidade_estadios[i] = capacidade_estadios[i].strip()

pais1_partidas_file = open("pais1_partida.txt", "r")
pais1_partidas = pais1_partidas_file.readlines()
for i in range(0, len(pais1_partidas)):
	pais1_partidas[i] = pais1_partidas[i].strip()

pais2_partidas_file = open("pais2_partida.txt", "r")
pais2_partidas = pais2_partidas_file.readlines()
for i in range(0, len(pais2_partidas)):
	pais2_partidas[i] = pais2_partidas[i].strip()

rodada_partidas_file = open("rodada_partida.txt", "r")
rodada_partidas = rodada_partidas_file.readlines()
for i in range(0, len(rodada_partidas)):
	rodada_partidas[i] = rodada_partidas[i].strip()

placar_partidas_file = open("placar_partida.txt", "r")
placar_partidas = placar_partidas_file.readlines()
for i in range(0, len(placar_partidas)):
	placar_partidas[i] = placar_partidas[i].strip()

#############################################
#
#	Abertura do arquivo
# 
############################################

destfile = open("p.sql", "w")

#############################################
#
#	Times de futebol
# 
############################################

times_futebol = []
for i in range (0, num_times_de_futebol):
	time = teams[i]
	formation = formations[randint(0, len(formations)-1)]
	time_futebol = [time, formation]
	times_futebol.append(time_futebol)

for t in times_futebol:
	line = "INSERT INTO time_futebol VALUES (\"" + "\", \"".join(t) + "\")\n"
	destfile.write(line)

#############################################
#
#	Torcedores
# 
############################################

torcedores = []
for i in range (0, num_torcedores):
	number = numbers[randint(0, len(numbers)-1)]
	numbers.remove(number)
	number = str(number)
	id_type_temp = id_type[randint(0, len(id_type)-1)]
	country = countries[randint(0, len(countries)-1)]
	team = teams[randint(0, len(teams)-1)]
	person = [number, id_type_temp, country, team]
	torcedores.append(person)

for t in torcedores:
	line = "INSERT INTO torcedor VALUES (\"" + "\", \"".join(t) + "\")\n"
	destfile.write(line)

#############################################
#
#	Comentatristas
# 
############################################

comentaristas = []
for i in range(0, num_comentaristas):
	number = numbers[randint(0, len(numbers)-1)]
	numbers.remove(number)
	number = str(number)
	id_type_temp = id_type[randint(0, len(id_type)-1)]
	country = countries[randint(0, len(countries)-1)]
	language = languages[randint(0, len(languages)-1)]
	comentarista = [number, id_type_temp, country, language]
	comentaristas.append(comentarista)

for c in comentaristas:
	line = "INSERT INTO comentarista VALUES (\"" + "\", \"".join(c) + "\")\n"
	destfile.write(line)

#############################################
#
#	Árbitros
# 
############################################

arbitros = []
for i in range(0, num_arbitros):
	number = numbers[randint(0, len(numbers)-1)]
	numbers.remove(number)
	number = str(number)
	id_type_temp = id_type[randint(0, len(id_type)-1)]
	country = countries[randint(0, len(countries)-1)]
	funcao = arbitrofuncoes[randint(0, len(arbitrofuncoes)-1)]
	arbitro = [number, id_type_temp, country, funcao]
	arbitros.append(arbitro)

for a in arbitros:
	line = "INSERT INTO arbitro VALUES (\"" + "\", \"".join(a) + "\")\n"
	destfile.write(line)

#############################################
#
#	Estádios
# 
############################################

estadios = []
for i in range(0, num_estadios):
	cidade = cidade_estadios[i]
	estado = estado_estadios[i]
	nome = nome_estadios[i]
	capacidade = capacidade_estadios[i]
	estadio = [cidade, estado, nome, capacidade]
	estadios.append(estadio)

for e in estadios:
	line = "INSERT INTO estadio VALUES (\"" + "\", \"".join(e) + "\")\n"
	destfile.write(line)

#############################################
#
#	Jogadores e técnicos
# 
############################################

jogadores = []
jogadores_defesa = []
jogadores_ataque = []
tecnicos = []
for i in range (0, num_times_de_futebol): # len(teams)
	number = numbers[randint(0, len(numbers)-1)]
	numbers.remove(number)
	number = str(number)
	id_type_temp = id_type[randint(0, len(id_type)-1)]
	country = teams[i]
	tecnico = [number, id_type_temp, country]
	tecnicos.append(tecnico)
	shirt_numbers = sample(range(1, 23), 22)
	for j in range (1, num_jogadores_por_time):
		number = numbers[randint(0, len(numbers)-1)]
		numbers.remove(number)
		number = str(number)
		id_type_temp = id_type[randint(0, len(id_type)-1)]
		country = teams[i]
		shirt_number = shirt_numbers[randint(0, len(shirt_numbers)-1)]
		shirt_numbers.remove(shirt_number)
		shirt_number = str(shirt_number)
		yellow_cards = 0
		yellow_cards = str(yellow_cards)
		red_cards = 0
		red_cards = str(red_cards)
		jogador = [number, id_type_temp, country, shirt_number, yellow_cards, red_cards]
		jogadores.append(jogador)
		if j<=11:
			desarmes = 0
			desarmes = str(desarmes)
			faltas = 0
			faltas = str(faltas)
			jogador_defesa = [number, id_type_temp, country, desarmes, faltas]
			jogadores_defesa.append(jogador_defesa)
		else:
			gols = 0
			gols = str(gols)
			assistencias = 0
			assistencias = str(assistencias)
			jogador_ataque = [number, id_type_temp, country, gols, assistencias]
			jogadores_ataque.append(jogador_ataque)

for j in jogadores:
	line = "INSERT INTO jogador VALUES (\"" + "\", \"".join(j) + "\")\n"
	destfile.write(line)

for j in jogadores_ataque:
	line = "INSERT INTO jogador_defesa VALUES (\"" + "\", \"".join(j) + "\")\n"
	destfile.write(line)

for j in jogadores_defesa:
	line = "INSERT INTO jogador_ataque VALUES (\"" + "\", \"".join(j) + "\")\n"
	destfile.write(line)

for t in tecnicos:
	line = "INSERT INTO tecnico VALUES (\"" + "\", \"".join(t) + "\")\n"
	destfile.write(line)

#############################################
#
#	Partidas
# 
############################################

partidas = []
for i in range(0, num_partidas):
	pais1 = pais1_partidas[i]
	pais2 = pais2_partidas[i]
	placar = placar_partidas[i]
	rodada = rodada_partidas[i]
	a = randint(0, len(cidade_estadios)-1)
	cidade = cidade_estadios[a]
	estado = estado_estadios[a]
	partida = [pais1, pais2, rodada, placar, cidade, estado]
	partidas.append(partida)

for p in partidas:
	line = "INSERT INTO partida VALUES (\"" + "\", \"".join(p) + "\")\n"
	destfile.write(line)

#############################################
#
#	Assiste
# 
############################################

assiste = []
for j in range(0, num_partidas):
	torcedores_temp = []
	for t in torcedores:
		torcedores_temp.append(t)
	# print("\n", partidas[j])
	for i in range(0, int(num_assiste/num_partidas)):
		torcedores_temp_unit =  torcedores_temp[randint(0, len(torcedores_temp)-1)]
		assiste_temp = torcedores_temp_unit[0:3] + partidas[j][0:3]
		torcedores_temp.remove(torcedores_temp_unit)
		# print(assiste_temp)
		assiste.append(assiste_temp)

for a in assiste:
	line = "INSERT INTO assiste VALUES (\"" + "\", \"".join(a) + "\")\n"
	destfile.write(line)


#############################################
#
#	Narra
# 
############################################

narra = []
for j in range(0, num_partidas):
	comentaristas_temp = []
	for c in comentaristas:
		comentaristas_temp.append(c)
	# print(partidas[j])
	for i in range(0, int(num_narra/num_partidas)):
		comentaristas_temp_unit =  comentaristas_temp[randint(0, len(comentaristas_temp)-1)]
		narra_temp = comentaristas_temp_unit[0:3] + partidas[j][0:3]
		comentaristas_temp.remove(comentaristas_temp_unit)
		# print(narra_temp)
		narra.append(narra_temp)

for n in narra:
	line = "INSERT INTO narra VALUES (\"" + "\", \"".join(n) + "\")\n"
	destfile.write(line)

#############################################
#
#	Apita
# 
############################################

apita = []
for j in range(0, num_partidas):
	arbitros_temp = []
	for a in arbitros:
		arbitros_temp.append(a)
	# print(partidas[j])
	for i in range(0, int(num_apita/num_partidas)):
		arbitros_temp_unit =  arbitros_temp[randint(0, len(arbitros_temp)-1)]
		apita_temp = arbitros_temp_unit[0:3] + partidas[j][0:3]
		arbitros_temp.remove(arbitros_temp_unit)
		# print(apita_temp)
		apita.append(apita_temp)

for a in apita:
	line = "INSERT INTO apita VALUES (\"" + "\", \"".join(a) + "\")\n"
	destfile.write(line)

#############################################
#
#	Joga_contra
# 
############################################

joga_contra = []
for i in range(0, len(pais1_partidas)):
	joga_contra_temp = [pais1_partidas[i], pais2_partidas[i]]
	joga_contra.append(joga_contra_temp) 

for j in joga_contra:
	line = "INSERT INTO joga_contra VALUES (\"" + "\", \"".join(j) + "\")\n"
	destfile.write(line)

#############################################
#
#	Fechamento do arquivo
# 
############################################

destfile.close()
