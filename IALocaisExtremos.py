# Importando a voz
import pyttsx3
# Importando o time, para definir um tempo
import time

# Função para fazer a IA falar
def falar(texto):
    engine = pyttsx3.init()  # Inicializando o engine TTS
    engine.setProperty('rate', 250)  # Definindo a velocidade da fala (normal: 150)
    engine.setProperty('volume', 1)  # Volume máximo (0.0 a 1.0)
    engine.setProperty('voice', 'brazil')
    engine.say(texto)  # A IA irá falar o texto
    engine.runAndWait()  # Espera até que a fala seja concluída

engine = pyttsx3.init()

voices = engine.getProperty('voices')

for voice in voices:
    if "brazil" in voice.name.lower() or "portuguese" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

# Função para que o texto apareça mais devagar
def print_lento(texto, intervalo= 0.01):
    for caractere in texto:
        print(caractere, end='', flush= True)  # end= '' para que o print saia horizontalmente
        time.sleep(intervalo)  # pausa a execução do programa pelo tempo determinado pelo intervalo
    falar(texto)  # Falar o texto que foi impresso lentamente

# lista de locais 
locais = ['1. Yakutsk', ' 2. Deserto de Lut', ' 3. Lahore']

#  Yakutsk > Julio
#  Deserto de Lut > Diogo
#  Lahore > Miguel

# palavras chaves sobre Yakutsk
inferno_gelado = 'Ao nordeste da região Siberiana, a 450Km de distância do Polo Norte e com aproximadamente 300 mil habitantes, esta cidade é um "inferno gelado" na Terra, porque tudo que estiver do lado de fora das casas estará congelado.'
temperatura_yakutsk = 'Em Yakutsk, o clima é comumente congelante, já que na maior parte do tempo a temperatura está abaixo de 0°C. Mas, nem tudo são pedras de gelo, porque no verão a temperatura pode chegar nos verdadeiramente agradáveis 20°C.'
paisagem_yakutsk = 'Uma paisagem branca tomará conta da sua visão em qualquer direção que você olhe, a paleta de cores é bem limitada, composta apenas em escalas de cinza.'
visão_yakutsk = 'O campo de visão é extremamente curto por causa da névoa ao seu redor causada pela emissão de carbono dos veículos, como é um lugar muito gelado, os veículos precisam estar constantemente ligados para que o motor continue aquecido e não fique coberto de gelo, assim como o óleo.'
temperatura_minima_yakutsk = 'O verdadeiro "inferno gelado" na Terra começa quando chega o inverno, onde a temperatura pode facilmente chegar aos 40°C/ 50°C. A menor temperatura registrada neste local foi de -71°C.'
crença_yakutsk = 'O estilo de vida do povo Yakut gira em torno de cuidar da natureza, eles acreditam que há espíritos nela, quando vão colher frutas na floresta, por exemplo, eles levam um pouco de comida e deixam lá como uma oferenda para que o espírito da natureza compartilhe sua comida com eles. Não pode falar alto, beber, jogar lixo, se divertir lá, pois pode perturbar os espíritos. Sua religião não está em um livro ou igreja, não há reza, ela está centrada em seu estilo de vida com a natureza, os deuses são a natureza.'
curiosidades_yakutsk = 'Se você estiver na rua e jogar água líquida de dentro de um recipiente para fora, a água instantaneamente virará vapor congelado.\n\n Se você estender roupas molhadas no varal do lado de fora da casa, a roupa congelará e parecerá uma placa de metal.\n\n Se você deixar uma banana por alguns minutos do lado de fora da casa, a banana ficará tâo dura que você poderá usá-la como um martelo.\n\n Se você usar óculos de metal neste lugar, irá se arrepender, pois ele só vai sair do seu rosto se a sua pele for junto.\n\n Os canos que transportam água pela cidade ficam acima do chão, porque o subterrâneo está totalmente congelado.\n\n Não é necessário usar geladeira, é só deixar a comida pendurada na janela e ela ficará conservada.\n\n Os edifícios são construídos sob pilares acima do chão por causa da camada de gelo que aumenta e diminui ao longo dos anos, evitando que fiquem tortos.\n\n Se você ficar do lado de fora por mais de 15 minutos, terá problemas como queimadura de pele e dificuldade para respirar.\n\n Aparelhos eletrônicos como celular, câmera, microfone param de funcionar se ficarem expostos por muito tempo também.\n\n Há duas camadas de vidro dentro dos carros para que o calor do aquecedor seja mantido por mais tempo.\n\n Os cavalos nesta região são mais baixos devido ao clima, chegando a parecer pôneis, burros ou jumentos; gatos não conseguem sobreviver no clima extremo de Yakutsk, apenas mamíferos com pelagem grossa.\n\n Se andar de carro em Yakutsk, tenha certeza de estar levando uma caixa de ferramentas para poder consertar o carro e, claro, saber mexer com isso. Se o carro der problema em um lugar distante de outras pessoas, sem sinal de telefone e você não conseguir consertá-lo, você ficará preso, e vai congelar até a morte.\n\n 20% das reservas totais de diamantes do mundo estão em Yakutsk, além de poder encontrar todos os elementos da tabela periódica lá.\n\n Muitos fósseis de mamutes e dinossauros são encontrados pela região de Yakutia, totalmente conservados por causa do gelo.\n\n Nesta terra, as pessoas não se envolvem com agricultura e agropecuária, elas comem peixes, coelhos, patos, carne de cavalo.\n\n Os Yakutianos, que compõem a maioria da população de Yakutia, são de origem turca e 38% de sua população é de origem russa.\n\n'

# palavras chaves sobre Deserto de Lut
temperatura_desertolut = 'O deserto de Lut, localizado no Irã, é conhecido por suas temperaturas extremas. É um dos lugares mais quentes do mundo. Em algumas áreas, as temperaturas do solo já alcançaram impressionantes 70,7 °C (159,3 °F), e as medições de temperatura do ar também são muito altas.'
desertodelut_introduçao = 'Localizado no sudeste Irã, próximo às fronteiras com o Paquistão e o Afeganistão, está o lugar mais quente da superfície do planeta, facilmente atingindo 50 °C e podendo chegar até mesmo a 70 °C. Esse local é o Deserto de Lut, ou Dasht-e Lut, que abriga paisagens impressionantes atraindo muitos turistas, mesmo com as altas temperaturas.'
kaluts = 'As formações de kaluts são uma das características mais marcantes do deserto. São estruturas de solo e rocha que foram moldadas pelo vento ao longo dos anos, criando colunas e desfiladeiros dramáticos. Essas formações podem chegar a até 70 metros de altura.'
dunasareia = 'O deserto abriga dunas extensas, algumas delas com formas onduladas que se alteram constantemente devido aos ventos. Essas dunas podem ser bastante altas e criam um contraste impressionante com o solo árido.'
terrenosrachados = 'Em algumas áreas, o solo se quebra em padrões geométricos, criando uma superfície que parece quase alienígena. Esses terrenos rachados são resultado da intensa evaporação da água subterrânea.'
corestextura = 'A paleta de cores do deserto é variada, com tons de marrom, laranja e amarelo predominando. Durante o amanhecer e o pôr do sol, as cores se intensificam, criando uma vista espetacular.'
extensoesareia = 'O deserto é composto por extensas áreas de areia que parecem infinitas. Essas regiões são muitas vezes solitárias e tranquilas, oferecendo uma sensação de vastidão.'
ceunoturno = 'Devido à baixa poluição luminosa, o céu noturno no deserto de Lut é deslumbrante. As estrelas são extremamente visíveis, criando um espetáculo celestial.'
visaodesertolut = 'A vastidão do deserto é uma das características mais marcantes. Ao olhar ao redor, você pode ver extensões intermináveis de areia e rochas, criando uma sensação de desolação e tranquilidade.'
nomades = 'Existem grupos nômades que habitam áreas ao redor do Deserto de Lut, embora a vida nômade nesse ambiente extremo seja bastante desafiadora. Esses nômades, como os Bakhtiaris e outros grupos, costumam se deslocar em busca de pastagens e água para seus rebanhos. A cultura nômade na região é rica e adaptada às condições áridas, utilizando técnicas tradicionais de sobrevivência e migração. Eles são conhecidos por suas habilidades em lidar com o clima severo e a escassez de recursos.'
crença_desertolut = 'No Deserto de Lut e nas áreas circundantes, a principal religião é o islamismo, com a maioria da população seguindo o ramo xiita, já que o deserto está localizado no Irã. Além disso, o zoroastrismo, embora seja uma religião minoritária atualmente, tem raízes profundas na história do Irã e ainda é praticado por alguns grupos, especialmente entre os persas.'
animais_deserto = 'O Deserto de Lut, com suas condições extremas de calor e aridez, abriga uma fauna adaptada a esse ambiente severo. Alguns dos animais que podem ser encontrados nessa região incluem: ' '\n' '\n' 'Ratos do Deserto' '\n' 'Lagartos' '\n' 'Serpentes' '\n' 'Falcões e Águias' 

# palavras chaves sobre Lahore
inferno_de_poeira = 'Localizada no Paquistão, é a capital e a cidade mais populosa da provincia do Panjabe, nas margens do rio Ravi.'
populacao_de_lahore = 'Aproximadamente, Lahore apresenta um índice populacional de 11,12 milhões de habitantes.'
temperatura_lahore = 'Sua temperatura varia entre 32°C a 19°C.'
visao_lahore = 'Por conta dos índices de poluição, afeta o campo de visão por conta da fumaça das fábricas e dos veículos que transitam constantemente.'
qualidade_do_ar_lahore = 'A qualidade do ar da cidade está em níveis altamente consideráveis para risco de bandeira vermelha para a saúde dos seus habitantes por conta da poluição. Respirar em Lahore é como fumar 15 cigarros. Para as pessoas que vivem nesta cidade, elas estão habituadas com tanta poluição, mas para um estrangeiro é impossível se sentir confortável.'
saude_de_lahore = 'A combustão de metais tóxicos, como: Cobre, Magnésio, Zinco, Selênio e Arsênico produzem partículas mais leves e mais finas que um fio de cabelo, o que significa que elas ficam no ar por mais tempo e entram com mais facilidade pela filtragem do nariz, penetrando nos pulmões, e através da rede capilar; elas causam doenças cardíacas, câncer de pulmão, infecções oculares, asma, bronquite, distúrbios respiratórios, nascimentos prematuros com efeitos negativos no desenvolvimento cerebral, podendo criar distúrbios genéticos nas próximas gerações. '
curiosidades_lahore = 'Culinária: Lahore é famosa por sua deliciosa culinária, incluindo pratos como haleem, nihari, kebabs e falooda.\n\nMuseu de Lahore: O Museu de Lahore é um dos mais antigos do Paquistão e abriga uma vasta coleção de artefatos históricos.\n\nTeatro e Dança: Lahore tem uma rica tradição de teatro e dança, com várias companhias de teatro e escolas de dança.\n\nMúsica: A cidade é berço de muitos músicos renomados do Paquistão.\n\n Esportes: Lahore é sede do Estádio Gaddafi, um dos principais estádios de críquete do Paquistão.\n\nPatrimônio Mundial: O Forte de Lahore e o Jardim de Shalimar foram declarados Patrimônio Mundial pela UNESCO em 1981.\n\nCidade dos Poetas: Lahore é conhecida como a "Cidade dos Poetas", devido à sua rica tradição de poesia e literatura.\n\nMúsica Clássica: Lahore é berço da música clássica paquistanesa, com muitos músicos renomados.\n\nDança Clássica: A cidade é famosa por sua dança clássica, incluindo o "Kathak" e o "Bharatanatyam".\n\nArtesanato: Lahore é conhecida por seu artesanato, incluindo tecidos, joias, cerâmica e madeira esculpida.\n\nFestivais: Lahore celebra muitos festivais, incluindo o "Festival de Lahore", "Eid-al-Fitr" e "Eid-al-Azha".\n\nGastronomia de Rua: A cidade é famosa por sua gastronomia de rua, com pratos como "Kebabs", "Samosas" e "Golgappas".\n\nMercados: Lahore tem muitos mercados históricos, como o "Anarkali Bazaar" e o "Lahore Cantonment Railway Station Market".\n\nEsportes Tradicionais: A cidade tem uma rica tradição de esportes tradicionais, incluindo o "Kabaddi" e o "Gatka".\n\nEducação em Inglês: Lahore foi uma das primeiras cidades do Paquistão a introduzir a educação em inglês.'

# introdução
print('\n') # \n para quebrar linha
print_lento('ALE'.center(200), 0.01) # .center(200) para centralizar o print
print('\n') 
print_lento('Olá! Eu me chamo "IALE": Inteligência Artificial sobre Lugares Extremos., ou: ALE; e irei te contar sobre lugares de vivência extrema no planeta Terra.'.center(200), 0.01)
print('\n')
print_lento('Aqui está a lista de lugares que eu posso informar sobre:', 0.01)
print('\n')

# função while para criar loop
while True:
    # interagindo com a IA
    print_lento(locais, 0.01)
    print('\n')

    local = (input('Escolha um dos lugares: '))
    print('\n')

    if local.lower().strip() in ['1', 'yakutsk']: #.lower() para deixar tudo em minúsculo e .strip() para não contar os espaços.
        print_lento(f'{inferno_gelado}', 0.01)
        print('\n') 
        print_lento('Gostaria de saber mais? Posso te contar sobre como é ver em um lugar assim, como é a paisagem, temperatura, uma curiosidade, etc...', 0.01)
        print('\n')
               
        while True:
            escolha = input()
            print('\n')
                    
            if escolha.lower().strip() in ['vista', 'visão', 'visao', 'ver', 'enxergar']:
                print_lento(f'{visão_yakutsk}\n', 0.01)
                print('\n')
                continue

            elif escolha.lower().strip() in ['paisagem', 'branco', 'branca', 'neve', 'cores', 'cor']:
                print_lento(f'{paisagem_yakutsk}\n', 0.01)
                print('\n')
                continue

            elif escolha.lower().strip() in ['temperatura', 'clima', 'tempo']:
                print_lento(f'{temperatura_yakutsk}\n', 0.01)
                print('\n')
                continue

            elif escolha.lower().strip() in ['temperatura mínima', 'recorde de temperatura mínima', 'recorde temperatura mínima', 'recorde temperatura mais baixa', 'recorde de temperatura mais baixa', 'temperatura minima', 'recorde de temperatura minima', 'recorde temperatura minima']:
                print_lento(f'{temperatura_minima_yakutsk}\n', 0.01)
                print('\n')
                continue

            elif escolha.lower().strip() in ['crença', 'religião', 'religiao', 'deus', 'deuses']:
                print_lento(f'{crença_yakutsk}', 0.01)
                print('\n')
                continue

            elif escolha.lower().strip() in ['curiosidade', 'curiosidades', 'me conte uma curiosidade', 'diga uma curiosidade', 'conte uma curiosidade']:
                print_lento(f'{curiosidades_yakutsk}\n', 0.01)
                print('\n')
                continue

            elif escolha.lower().strip() in ['voltar', 'sair']:
                print('\n')
                print_lento('Voltando para a lista de cidades...', 0.01)
                print('\n')
                break
            
            else:
                print('\n')
                print_lento('Desculpe, não entendi, poderia repetir?', 0.01)
                print('\n')
                continue

    elif local.lower().strip() in ['parar', 'sair', 'encerrar', 'interromper']:
        print('\n')
        print_lento('Entendido. Até a próxima!\n', 0.01)
        print('\n')
        print_lento('...Fim do programa...\n'.center(200), 0.01)
        print('\n')
        print_lento('Fonte: Ruhi Çenet do YouTube')
        print('\n')
        break
    
    elif local.lower().strip() in ['2', 'deserto', 'lut', 'deserto de lut']:
        print_lento(f'{desertodelut_introduçao}', 0.01)
        print('\n') 
        print_lento('Gostaria de saber mais? Posso te contar sobre como é ver em um lugar assim, como é a paisagem, temperatura, uma curiosidade, etc...', 0.01)
        print('\n')

        while True:
            escolha = input()
            print('\n')

            if escolha.lower().strip() in ['céu' , 'como é o céu?' , 'ceu']:
                print_lento(f'{ceunoturno}', 0.01)
                print('\n')
                continue

            elif escolha.lower().strip() in ['animais' , 'fauna local' , 'fauna' , 'animal' , 'bixo']:
                print_lento(f'{animais_deserto}', 0.01)
                print('\n')
                continue

            elif escolha.lower().strip() in ['formação' , 'feito' , 'do que é feito' , 'do que ele é feito' , 'do que ele e feito' , 'do que e feito', 'formaçao']:
                print_lento(f'{extensoesareia}', 0.01)
                print('\n')
                continue

            elif escolha.lower().strip() in ['vista', 'visão', 'visao', 'ver', 'enxergar']:
                print_lento(f'{visaodesertolut}\n', 0.01)
                print('\n')
                continue

            elif escolha.lower().strip() in ['curiosidade' , 'sidade' , 'curi' , 'curiosin' , 'curiozidade' ,  'me conte uma curiosidade', 'diga uma curiosidade', 'conte uma curiosidade']:
                print_lento(f'{nomades}', 0.01)
                print('\n')
                continue

            elif escolha.lower().strip() in ['religião' , 'crença' , 'religiao' , 'deus' , 'deuses']:
                print_lento(f'{crença_desertolut}', 0.01)
                print('\n')
                continue

            elif escolha.lower().strip() in ['temperatura' , 'clima' , 'tempo']:
                print_lento(f'{temperatura_desertolut}', 0.01)
                print('\n')
                continue
                
            elif escolha.lower().strip() in ['paisagem']:
                print('\n')
                print_lento(f'{kaluts}', 0.01)
                print('\n')
                print_lento(f'{dunasareia}', 0.01)
                print('\n')
                print_lento(f'{terrenosrachados}', 0.01)
                print('\n')
                print_lento(f'{corestextura}', 0.01)
                print('\n')
                continue
            
            elif escolha.lower().strip() in ['voltar', 'sair']:
                print('\n')
                print_lento('Voltando para a lista de cidades...', 0.01)
                print('\n')
                break

            else:
                print('\n')
                print_lento('Desculpe, não entendi, poderia repetir?', 0.01)
                print('\n')
                continue

    elif local.lower().strip() in ['parar', 'sair', 'encerrar', 'interromper']:
        print('\n')
        print_lento('Entendido. Até a próxima!', 0.01)
        print('\n\n')
        print_lento('...Fim do programa...'.center(200), 0.01)
        print('\n\n')
        print_lento('Fonte: Ruhi Çenet do YouTube')
        print('\n\n')
        break

    elif local.lower().strip() in ['3', 'lahore']:
        print_lento(f'{inferno_de_poeira}', 0.01)
        print('\n') 
        print_lento('Gostaria de saber mais? Posso te contar sobre como é ver em um lugar assim, como é a paisagem, temperatura, uma curiosidade, etc...', 0.01)
        print('\n')

        while True:
            escolha = input()
            print('\n')

            if escolha.lower().strip() in ['população' , 'populacao' , 'populaçao' , 'habitantes' , 'numero de habitantes' , 'número de habitantes']:
                print_lento(f'{populacao_de_lahore}\n', 0.01)
                print('\n')
                continue

            elif escolha.lower().strip() in ['paisagem', 'vista', 'visão', 'visao']:
                print_lento(f'{visao_lahore}\n', 0.01)
                print('\n')
                continue

            elif escolha.lower().strip() in ['temperatura', 'clima', 'tempo']:
                print_lento(f'{temperatura_lahore}\n', 0.01)
                print('\n')
                continue

            elif escolha.lower().strip() in ['ar', 'qualidade do ar']:
                print_lento(f'{qualidade_do_ar_lahore}\n', 0.01)
                print('\n')
                continue

            elif escolha.lower().strip() in ['saude', 'saúde']:
                print_lento(f'{saude_de_lahore}\n', 0.01)
                print('\n')
                continue

            elif escolha.lower().strip() in ['curiosidade', 'curiosidades', 'me conte uma curiosidade', 'diga uma curiosidade', 'conte uma curiosidade']:
                print_lento(f'{curiosidades_lahore}\n', 0.01)
                print('\n')
                continue
            
            elif escolha.lower().strip() in ['voltar', 'sair']:
                print('\n')
                print_lento('Voltando para a lista de cidades...', 0.01)
                print('\n')
                break

            else:
                print('\n')
                print_lento('Desculpe, não entendi, poderia repetir?', 0.01)
                print('\n')
                continue            

    elif local.lower().strip() in ['parar', 'sair', 'encerrar', 'interromper']:
        print('\n')
        print_lento('Entendido. Até a próxima!\n', 0.01)
        print('\n')
        print_lento('...Fim do programa...\n'.center(200), 0.01)
        print('\n')
        print_lento('Fonte: Ruhi Çenet do YouTube')
        print('\n')
        break

    else:
        print('\n')
        print_lento('\nDesculpe, não entendi. Escolha uma cidade:')
        print('\n')
        continue