import random
import time
import os
from ttg import Truths
from game.utils import escrever_lentamente


# Sistema de reputação
reputacao = {
    "Lady Isolde": 0,
    "Bram": 0,
    "Sir Alaric": 0,
    "Floris": 0,
    "Gerhard": 0,
    "Morgana": 0,
    "Padre": 0
}

# Armazenamento de memórias
memorias = []

# Armazenamento de proposições
proposicoes = []

# Lista global para armazenar as proposições que o usuário considera certas e falsas
proposicoes_certas = []
proposicoes_falsas = []

def interrogar_personagensFase1():
    # Introdução
    escrever_lentamente("Sentada em uma mesa de interrogatório, Samanta observa a porta, aguardando o primeiro suspeito aparecer.\n")
    escrever_lentamente("Ela se pergunta sobre a natureza do crime e a relação de cada um com Baldwin, o cozinheiro morto.\n")
    
    # Definindo os personagens e suas falas
    personagens = {
        "Lady Isolde": [
            "Baldwin sempre foi difícil de lidar, mas fui pega de surpresa com sua morte. Não achei que ele tivesse tantos inimigos.",
            "A vida ao lado dele era cheia de desafios, mas eu nunca desejaria a morte dele.",
            "Ele era um homem complicado, e gosto de acreditar que atraímos tudo o que merecemos.",
            "A dor que eu sinto não se compara a qualquer rivalidade que alguém possa ter com ele. No final de tudo, ele ainda era meu marido...",
            "As coisas entre nós eram complicadas, mas eu nunca seria pega desejando a morte dele..."
        ],
        "Floris, o Bobo da Corte": [
            "Baldwin era um péssimo cozinheiro e uma péssima pessoa, mas nunca pensei que alguém o mataria. Não tão cedo, ao menos.",
            "Eu só fazia piadas sobre ele morrer, senhorita. Nunca achei que alguém realmente o mataria.",
            "Na verdade, a corte estava feliz com suas desventuras na cozinha. E agora ela está mais feliz que ele se foi.",
            "Eu ouvi rumores, mas isso é só conversa de bobo.",
            "Ninguém em sã consciência mataria alguém por causa de comida. Agora por outras coisas, não tenho tanta certeza."
        ],
        "Gerhard, o Carrasco": [
            "É estranho como a vida pode mudar. De repente, me vejo livre do maldito, quem diria?",
            "A morte de Baldwin é uma pena, mas ele tinha seus inimigos. Conheço alguns eu mesmo...",
            "Eu estava apenas fazendo meu trabalho, como sempre. Se ele caiu duro, o que isso tem a ver comigo?",
            "Seus problemas não eram da minha conta, mas poderia ter havido motivos por trás disso. Baldwin não era, afinal de contas, um santo.",
            "As pessoas costumam achar que só eu sou o vilão, mas nem tudo é como parece. Pode sempre haver mais que um, não concorda?"
        ],
        "Bram, o Ferreiro": [
            "Baldwin não era bem-vindo nas minhas forjas. Ele sempre queria mais do que eu poderia dar e não queria dar o que eu queria.",
            "Todos têm motivos para estarem felizes que o cozinheiro se foi. Somente o Rei que não, acho. Afinal, o Rei está triste porque o cozinheiro morreu ou porque suas comidas não serão mais as mesmas?",
            "Eu estava longe na noite do crime, apenas cuidando do meu trabalho. Baldwin não era tão importante assim, era?.",
            "As pessoas dizem que a verdade é como o fogo. Às vezes queima. Às vezes, perfura seu corpo como uma lâmina. Mas nunca, nunca, deixa de ser a verdade.",
            "Eu não gostaria de ser acusado por algo que não fiz, senhorita, mesmo que seja algo que eu gostaria de ter feito."
        ],
        "Calistus, o Padre": [
            "A morte de Baldwin é uma tragédia. As pessoas precisam de mais amor, não de ódio. Como vamos prosperar assim?",
            "Eu sempre tentei ajudar os necessitados, mas há coisas que não posso revelar. Honro meu dever e meus fiéis.",
            "Baldwin tinha seus segredos, assim como todos nós. Quem é você para julgar, senhorita?",
            "Estou aqui para guiar as almas, não para fazer julgamentos.",
            "Todos os homens são culpados, mas isso não quer dizer que mereçam morrer."
        ]
    }
    
    # Interrogando os personagens
    for personagem, falas in personagens.items():
        # Exibir comportamento inicial
        escrever_lentamente(f"{personagem} entra na sala.\n")
        escrever_lentamente("Samanta o(a) observa atentamente, tentando decifrar suas emoções.\n")

        while True:
            escrever_lentamente(f"Samanta: \"Gostaria de saber sua relação com Baldwin e o que aconteceu naquela noite.\"\n")
            resposta = random.choice(falas)  # Seleciona uma fala aleatória
            escrever_lentamente(f"{personagem}: \"{resposta}\"\n")
            
            # Pergunta se Samanta deseja insistir
            insistir = input("Você deseja insistir em mais perguntas? (s/n): ")
            if insistir.lower() != "s":
                break

            if personagem == "Lady Isolde" or personagem == "Floris, o Bobo da Corte" or personagem == "Calistus, o Padre":
                escrever_lentamente(f"{personagem}: \"Eu ouvi uma mulher com cabelos ruivos na cozinha pouco antes do ataque. Não sei quem era, mas talvez isso ajude.\"\n")
            else:
                escrever_lentamente(f"{personagem}: \"Eu ouvi um homem discutindo com Baldwin na noite do crime. Não sei quem era, mas talvez isso ajude.\"\n")

            # Limpa o console após cada interrogação
            os.system("cls")

    # Proposições após as interrogações
    proposicoes = [
        "Lady Isolde não está exatamente triste com a morte do marido.",
        "Floris parece feliz com a morte do cozinheiro",
        "Bram, o ferreiro, parece contente com a morte de Baldwin",
        "Gerhard parece satisfeito com a morte de Baldwin",
        "Calistus pode estar encobrindo o verdadeiro assassino, o que o torna suspeito.",
        "Baldwin não era uma boa pessoa."
    ]

    escrever_lentamente("\nApós as interrogações, Samanta anota algumas proposições sobre o crime:\n")
    for i, prop in enumerate(proposicoes, 1):
        escrever_lentamente(f"{i}. {prop}")

    # Pergunta ao jogador sobre quais proposições ele acha que são verdadeiras
    escolhas = input("Quais proposições você acha que são verdadeiras? (digite os números separados por vírgula): ")
    escolhas = [int(num.strip()) for num in escolhas.split(',') if num.strip().isdigit()]
    
    # Adiciona as proposições escolhidas pelo jogador à lista global
    for escolha in escolhas:
        proposicoes_certas.append(proposicoes[escolha - 1])

    # Pergunta ao jogador sobre quais proposições ele acha que são falsas
    escolhas_falsas = input("Quais proposições você acha que são falsas? (digite os números separados por vírgula): ")
    escolhas_falsas = [int(num.strip()) for num in escolhas_falsas.split(',') if num.strip().isdigit()]
    
    # Adiciona as proposições escolhidas pelo jogador à lista global
    for escolha in escolhas_falsas:
        proposicoes_falsas.append(proposicoes[escolha - 1])

def interrogar_personagensFase2():
    # Introdução
    escrever_lentamente("Samanta decide investigar mais a fundo. Ela se dirige ao local onde seus suspeitos estão e se prepara para a próxima rodada de interrogações. Sua cabeça e seu corpo ainda estão doloridos.\n")
    
    # Definindo os personagens e suas falas
    personagens = {
        "Lady Isolde": [
            "Eu sempre mantive facas em minha cozinha. É uma necessidade, não um instrumento de morte. Entendo isso tanto quanto você, detetive.",
            "Não é verdade que eu tinha algo contra Baldwin. Ele era difícil, mas eu nunca sonharia em fazer algo contra ele diretamente.",
            "Baldwin e eu tínhamos nossas diferenças, mas a morte dele não resolve nada para mim. Pode acreditar. Acha que eu já não leve i em conta as suspeitas que caíriam em cima de mim quando ele se fosse?",
            "Não gosto de lembrá-la, mas nossas brigas não dizem respeito a quem não é de fora do casamento.",
            "A vida é muito preciosa para ser desperdiçada por rivalidades mesquinhas. Ou ser desperdiçada em relacões miseráveis."
        ],
        "Floris, o Bobo da Corte": [
 "Facas? Eu apenas uso para preparar as comidas engraçadas que faço para a corte. Mas essa é uma boa ideia que você me deu.",
            "Claro que tenho algumas, mas para diversão, não para brigar. Quer uma demonstração?",
            "Nunca tive problemas com Baldwin.  Não a ponto de matá-lo., ao menos. Eu apenas gostava de fazer piadas sobre ele e como todo mundo seria mais feliz com a morte dele.",
            "Se ele não se levasse tudo tão a sério, talvez estivesse vivo hoje. Se ele soubesse quando parar... A culpa é dele, senhorita. Dele por ser do jeito que era.",
            "Minha relação com ele era baseada em humor, nada mais. Minhas facas não poderiam ser desperdiçadas nele."
 ],
        "Gerhard, o Carrasco": [
            "A lâmina do meu machado é afiada, mas eu só uso para meu trabalho. Não me envolvo com rivalidades pessoais. Ainda mais se fosse óbvio que isso me incriminaria.",
            "A morte de Baldwin é uma questão de justiça, mas não estou aqui para julgar. O padre sabe quantos erros já carrego em meus ombros.",
            "Baldwin sempre teve inimigos, mas eu não sou um deles. Não um desses que o mataria, ao menos.",
            "As pessoas têm suas razões para agir, mas eu não sou quem decide quem vive ou morre. Essa é uma decisão do Rei.",
            "Facas e machados são ferramentas. O que importa é quem as empunha. E eu as empunho na cabeça, senhorita."
        ]
    }
    
    # Interrogando os personagens
    for personagem, falas in personagens.items():
        # Exibir comportamento inicial
        escrever_lentamente("\nSamanta se aproxima, pronta para questionar sobre a relação com Baldwin e o uso de objetos cortantes. O {personagem} parece já saber o que se aproxima e se prepara para as perguntas.\n")

        while True:
            resposta = random.choice(falas)  # Seleciona uma fala aleatória
            escrever_lentamente(f"{personagem}: \"{resposta}\"\n")
            
            # Pergunta se Samanta deseja insistir
            insistir = input("Você deseja insistir em mais perguntas? (s/n): ")
            if insistir.lower() != "s":
                break

            if personagem == "Lady Isolde" or personagem == "Floris, o Bobo da Corte" or personagem == "Calistus, o Padre":
                escrever_lentamente(f"{personagem}: \"Eu ouvi uma mulher com cabelos ruivos na cozinha pouco antes do ataque. Não sei quem era, mas talvez isso ajude.\"\n")
            else:
                escrever_lentamente(f"{personagem}: \"Eu ouvi um homem discutindo com Baldwin na noite do crime. Não sei quem era, mas talvez isso ajude.\"\n")

            # Limpa o console após cada interrogação
            os.system("cls")

    # Proposições após as interrogações
    proposicoes = [
        "Lady Isolde parece já ter considerado a morte de Baldwin.",
        "Floris parece estar tentando amenizar a morte do cozinheiro.",
        "Gerhard pode estar usando sua posição para encobrir algo.",
        "As facas e objetos cortantes na cozinha podem ter sido uma armadilha disfarçada.",
        "A relação tensa entre os personagens e Baldwin pode indicar um motivo oculto para sua morte."
    ]

    escrever_lentamente("Após as interrogações, Samanta anota cinco proposições sobre suas suspeitas:\n")
    for i, prop in enumerate(proposicoes, 1):
        escrever_lentamente(f"{i}. {prop}")

    # Pergunta ao jogador sobre quais proposições ele a cha que são verdadeiras
    escolhas = input("\nQuais proposições você acha que são verdadeiras? (digite os números separados por vírgula): ")
    escolhas = [int(num.strip()) for num in escolhas.split(',') if num.strip().isdigit()]

    # Adiciona as proposições escolhidas pelo jogador à lista global
    for escolha in escolhas:
        proposicoes_certas.append(proposicoes[escolha - 1])

def interrogar_personagensFase3():
    # Introdução
    escrever_lentamente("Samanta encontrou algumas cartas de amor escondidas e decidiu interrogar os suspeitos para descobrir mais sobre elas.\n")
    
    # Definindo os personagens e suas falas
    personagens = {
        "Padre Calistus": [
            "As cartas de amor? Não tenho nada a ver com isso, sou um homem de fé. Meu único amor está para com Deus.",
            "O amor é um sentimento poderoso, mas deve ser guiado por princípios. E os princípios dos homens são questionáveis.",
            "Se alguém escreveu cartas, pode haver uma razão oculta, mas não é minha intenção investigar. E nem contar.",
            "A vida amorosa de outros não deve ser meu foco, estou aqui para ajudar os necessitados e ouvir os seus arrependimentos.",
            "Se as cartas estão ligadas à morte de Baldwin, isso é uma questão mais profunda do que aparenta. Sou um homem simples, senhorita, não espere muito de mim."
        ],
        "Lady Isolde": [
            "A-As cartas? Eu nunca as vi. Se são de amor, não são minhas.",
            "Nunca lhe disseram que é falta de privacidade invadir os aposentos de uma mulher de luto?",
            "Se alguém escreveu cartas, deveria ser entre amantes, não entre inimigos e, tampouco, intrometidos.",
            "As palavras podem ser traiç oeiras. É fácil se enganar com sentimentos ou com alucinações. Tem certeza que leu as cartas direito, detetive?",
            "Meu coração está livre de rivalidades, e não desejo ser ligada a essa situação. Sou uma mulher fiél."
        ],
        "Bram, o Ferreiro": [
            "Cartas de amor? Isso é novidade para mim. Não me importo com os relacionamentos dos outros. E não vejo porque você deveria se importar.",
            "Se alguém está apaixonado, que mantenha suas cartas em segredo. E que quem não esteja, não se intrometa.",
            "As palavras escritas são só isso, palavras. Não têm peso se não forem acompanhadas por ações.",
            "Se Isolde recebeu algo, ela provavelmente fez algo para merecer. Mas não entendo como isso tem haver comigo?",
            "Estou mais preocupado em forjar minha próxima espada do que em romances, senhorita."
        ]
    }
    
    # Interrogando os personagens
    for personagem, falas in personagens.items():
        # Exibir comportamento inicial
        escrever_lentamente(f"{personagem} entra na sala de acordo com o pedido de Samanta, parecendo intrigado e defensivo.\n")
        escrever_lentamente("Samanta observa atentamente, procurando sinais de nervosismo.\n")

        while True:
            escrever_lentamente(f"Samanta: \"Ouvi falar de algumas cartas de amor. O que você sabe sobre elas?\"\n")
            resposta = random.choice(falas)  # Seleciona uma fala aleatória
            escrever_lentamente(f"{personagem}: \"{resposta}\"\n")
            
            # Pergunta se Samanta deseja insistir
            insistir = input("Você deseja insistir em mais perguntas? (s/n): ")
            if insistir.lower() != "s":
                break

            if personagem == "Lady Isolde" or personagem == "Floris, o Bobo da Corte" or personagem == "Calistus, o Padre":
                escrever_lentamente(f"{personagem}: \"Eu ouvi uma mulher com cabelos ruivos na cozinha pouco antes do ataque. Não sei quem era, mas talvez isso ajude.\"\n")
            else:
                escrever_lentamente (f"{personagem}: \"Eu ouvi um homem discutindo com Baldwin na noite do crime. Não sei quem era, mas talvez isso ajude.\"\n")

            # Limpa o console após cada interrogação
            os.system("cls")

    # Proposições após as interrogações
    proposicoes = [
        "Padre Calistus pode estar ocultando algo sobre seus relacionamentos e responsabilidades.",
        "Lady Isolde tem motivos para mentir sobre as cartas se estiver envolvida em um romance proibido.",
        "Bram pode ter sentimentos não correspondidos que o ligam à situação das cartas.",
        "As cartas de amor podem estar ligadas a ciúmes que resultaram na morte de Baldwin.",
        "A relação entre os personagens e Baldwin pode ser mais complexa do que se imagina."
    ]

    escrever_lentamente("\nApós as interrogações, Samanta anota cinco proposições sobre o crime:\n")
    for i, prop in enumerate(proposicoes, 1):
        escrever_lentamente(f"{i}. {prop}")

    # Pergunta ao jogador sobre quais proposições ele acha que são verdadeiras
    escolhas = input("\nQuais proposições você acha que são verdadeiras? (digite os números separados por vírgula): ")
    escolhas = [int(num.strip()) for num in escolhas.split(',') if num.strip().isdigit()]

    # Adiciona as proposições escolhidas pelo jogador à lista global
    for escolha in escolhas:
        proposicoes_certas.append(proposicoes[escolha - 1])

def interrogar_personagensFase4():
    # Introdução
    escrever_lentamente("Samanta decide investigar as bebidas de Morgana, a Curandeira, e como elas podem estar ligadas à morte de Baldwin. Ela também decide investigar mais sobre a pessoa de Baldwin em si.\n")
    
    # Definindo os personagens e suas falas
    personagens = {
        "Morgana": [
            "Minhas bebidas são feitas com ervas raras, mas não sou responsável pelo que os outros fazem com elas. Elas podem tanto curar quanto matar, sim, mas isso não é problema meu.",
            "Baldwin era um homem forte, mas todos têm fraquezas, não é mesmo? A sua, infelizmente, estava na bebida.",
            "Se ele se deixou levar por algo que eu preparei, isso é culpa dele. Só faço o que me pedem.",
            "As pessoas buscam poder nas bebidas, mas não podem se esquecer das consequências. Esse erro é unicamente de Baldwin.",
            "Não posso controlar o que as pessoas fazem depois de beberem, mas o conhecimento é poder. "
        ],
        "Floris, o Bobo da Corte": [
            "Baldwin era, como já suspeito que você saiba, senhorita, incrivelmente desprezado.",
            "Ele não era fácil de lidar; muitos o achavam insuportável. Eu me incluo nessa lista admiravelmente longa.",
            "A corte sempre teve uma relação complicada com Baldwin. Ele tinha seu jeito de desagradar assim como também sabia cozinhar incrivelmente bem.",
            "Dizem que ele poderia intimidar até o mais corajoso dos homens se sua autoestima não fosse tão baixa.",
            "Se você se opusesse a ele, é melhor estar preparado para a luta. Não que eu ache que você perderia, senhorita. Você parece ter talento para quebrar alguns rostos."
        ],
        "Gerhard, o Carrasco": [
            "Baldwin era um homem grande e imponente, mas todos têm um ponto fraco. A dele estava na inteligência dele.",
            "Já vi homens maiores do que ele caírem se forem pegos de surpresos. No entanto, é admirável que sua surpresa fosse sempre a bebida.",
            "A força nem sempre garante a vitória. Estratégia é essencial. E, felizmente, Baldwin era carente nesse aspecto.",
            "Não posso dizer que ele era fácil de derrubar, mas não era impossível. Eu saberia. Já quebrei ossos dele o suficiente para que isso fosse uma segunda natureza nesse ponto.",
            "Uma luta pode mudar rapidamente; você nunca pode subestimar seu oponente, seja homem ou mulher. Ainda mais se o oponente não for burro."
        ]
    }
    
    # Interrogando os personagens
    for personagem, falas in personagens.items():
        # Exibir comportamento inicial
        escrever_lentamente(f"{personagem} entra na sala, olhando intrigado para Samanta.\n")
        escrever_lentamente("Samanta, por sua vez, observa atentamente, aval iando suas reações.\n")

        while True:
            # Interação
            if personagem == "Morgana":
                escrever_lentamente(f"Samanta: \"Morgana, eu quero saber sobre suas bebidas e se elas têm alguma ligação com a morte de Baldwin.\"\n")
            elif personagem == "Floris":
                escrever_lentamente(f"Samanta: \"Floris, qual é a reputação de Baldwin na corte? Por que ele tinha tantos inimigos?\"\n")
            elif personagem == "Gerhard":
                escrever_lentamente(f"Samanta: \"Gerhard, Baldwin era fácil de derrubar em uma luta? O que você sabe sobre isso?\"\n")
            
            resposta = random.choice(falas)  # Seleciona uma fala aleatória
            escrever_lentamente(f"{personagem}: \"{resposta}\"\n")
            
            # Pergunta se Samanta deseja insistir
            insistir = input("Você deseja insistir em mais perguntas? (s/n): ")
            if insistir.lower() != "s":
                break

            if personagem == "Lady Isolde" or personagem == "Floris, o Bobo da Corte" or personagem == "Calistus, o Padre":
                escrever_lentamente(f"{personagem}: \"Eu ouvi uma mulher com cabelos ruivos na cozinha pouco antes do ataque. Não sei quem era, mas talvez isso ajude.\"\n")
            else:
                escrever_lentamente(f"{personagem}: \"Eu ouvi um homem discutindo com Baldwin na noite do crime. Não sei quem era, mas talvez isso ajude.\"\n")

            # Limpa o console após cada interrogação
            os.system("cls")

    # Proposições após as interrogações
    proposicoes = [
        "Morgana pode estar escondendo algo sobre a verdadeira natureza de suas bebidas.",
        "Floris acredita que Baldwin tinha muitos inimigos, o que o tornaria um alvo fácil.",
        "Gerhard sabe mais sobre a força de Baldwin do que admite, e isso pode ser relevante.",
        "As fraquezas de Baldwin podem ter sido exploradas por aqueles que o cercavam ou que fossem minimamente inteligentes.",
        "As bebidas de Morgana podem ter contribuído para a morte de Baldwin de uma forma inesperada."
    ]

    escrever_lentamente("\nApós as interrogações, Samanta anota cinco proposições sobre o crime:\n")
    for i, prop in enumerate(proposicoes, 1):
        escrever_lentamente(f"{i}. {prop}")

    # Pergunta ao jogador sobre quais proposições ele acha que são verdadeiras
    escolhas = input("\nQuais proposições você acha que são verdadeiras? (digite os números separados por vírgula): ")
    escolhas = [int(num.strip()) for num in escolhas.split(',') if num.strip().isdigit()]

    # Adiciona as proposições escolhidas pelo jogador à lista global
    for escolha in escolhas:
        proposicoes_certas.append(proposicoes[escolha - 1])

def interrogar_personagensFase5():
    # Introdução
    escrever_lentamente("Samanta decide interrogar o Padre Calistus e Bram sobre bebidas calmantes e seus paradeiros no dia da morte de Baldwin.\n")
    
    # Definindo os personagens e suas falas
    personagens = {
        "Calistus, o Padre": [
            "As bebidas são uma maneira de aliviar o estresse, mas não tenho nada a esconder. Não sou perfeito, senhorita, e preciso me acalmar acerca das confissões que recebo.",
            "Estava na igreja, orando e ajudando aqueles que precisavam de conforto e desejando para mim mesmo conforto também.",
            "Se alguém roubou bebidas, não sei quem poderia ter sido. Sou um homem de Deus, senhorita. Essas ações estão abaixo de mim.",
            "A vida é cheia de provações, mas não acho que isso tenha a ver com a morte de Baldwin. Se sua morte foi trazida pela bebida, por que não me diz logo?",
            "Acredito que as bebidas devem ser usados com responsabilidade, mas o que aconteceu foi uma tragédia. Morgana, como uma mulher respeit ável, deveria saber melhor."
        ],
        "Bram, o Ferreiro": [
            "Tomar bebidas calmantes é uma prática comum, especialmente para lidar com o estresse do trabalho.",
            "Eu estava em minha forja, longe de qualquer problema que não fosse o meu próprio. Me perdoe se uma garrafa discarça um pouco o cheiro de fumaça, senhorita.",
            "Se as bebidas foram roubadas, isso é preocupante, mas não posso estar por trás disso. Meus calçados deixariam marcas, tenho certeza disso.",
            "Baldwin e eu não éramos amigos, mas não tenho motivos para querer que ele morresse, mesmo que ele me desse vários.",
            "Eu sempre achei  que bebidas eram apenas uma forma de escape, não uma solução para os problemas. Por que não me disse isso antes?"
        ]
    }
    
    # Interrogando os personagens
    for personagem, falas in personagens.items():
        # Exibir comportamento inicial
        escrever_lentamente(f"{personagem} entra na sala, com uma expressão cautelosa.\n")
        escrever_lentamente("Samanta observa atentamente, buscando sinais de desonestidade.\n")

        while True:
            # Interação
            if personagem == "Calistus, o Padre":
                escrever_lentamente(f"Samanta: \"Calistus, quero saber sobre as bebidas calmantes que você toma e onde estava no dia em que Baldwin morreu.\"\n")
            elif personagem == "Bram":
                escrever_lentamente(f"Samanta: \"Bram, você pode me contar sobre as bebidas calmantes e seu paradeiro no dia da morte de Baldwin?\"\n")
            
            resposta = random.choice(falas)  # Seleciona uma fala aleatória
            escrever_lentamente(f"{personagem}: \"{resposta}\"\n")
            
            # Pergunta se Samanta deseja insistir
            insistir = input("Você deseja insistir em mais perguntas? (s/n): ")
            if insistir.lower() != "s":
                break

            if personagem == "Lady Isolde" or personagem == "Floris, o Bobo da Corte" or personagem == "Calistus, o Padre":
                escrever_lentamente(f"{personagem}: \"Eu ouvi uma mulher com cabelos ruivos na cozinha pouco antes do ataque. Não sei quem era, mas talvez isso ajude.\"\n")
            else:
                escrever_lentamente(f"{personagem}: \"Eu ouvi um homem discutindo com Baldwin na noite do crime. Não sei quem era, mas talvez isso ajude.\"\n")

            # Limpa o console após cada interrogação
            os.system("cls")

    # Proposições após as interrogações
    proposicoes = [
        "Calistus pode estar escondendo o fato de que estava envolvido com os chás roubados.",
        "Bram afirma estar trabalhando na forja, mas não há testemunhas que confirmem isso.",
        "Ambos têm acesso as bebidas e poderiam tê-las usadas como parte de um plano.",
        "A relação de Bram com Baldwin poderia ter motivado uma ação drástica.",
        "As bebidas são um tema comum, não tem como eles, de fato, terem sido usados propositalmente com Balwin."
    ]

    escrever_lentamente("Após as interrogações, Samanta anota cinco proposições sobre o crime:\n")
    for i, prop in enumerate(proposicoes, 1):
        escrever_lentamente(f"{i}. {prop}")

    # Pergunta ao jogador sobre quais proposições ele acha que são verdadeiras
    escolhas = input("Quais proposições você acha que são verdadeiras? (digite os números separados por vírgula): ")
    escolhas = [int (num.strip()) for num in escolhas.split(',') if num.strip().isdigit()]

    # Adiciona as proposições escolhidas pelo jogador à lista global
    for escolha in escolhas:
        proposicoes_certas.append(proposicoes[escolha - 1])

def interrogar_personagensFase6():
    # Proposições que Samanta considerou certas durante o jogo
    global proposicoes_certas

    # Introdução à interrogação
    escrever_lentamente("Samanta entra na sala, sentindo o peso das suas investigações. Ela olha para os suspeitos que estão presentes e começa a refletir sobre tudo que ouviu.\n")

    # Exibindo as proposições que ela considerou certas
    escrever_lentamente("Após refletir, Samanta lista as proposições que considera verdadeiras:\n")
    for i, prop in enumerate(proposicoes_certas, 1):
        escrever_lentamente(f"{i}. {prop}")

    # Lista dos personagens suspeitos
    personagens = ["Lady Isolde", "Floris", "Gerhard", "Bram", "Padre"]
    escrever_lentamente("\nSamanta deve escolher um culpado entre os presentes. Quem você acha que ela deve escolher?")

    # Exibir lista numerada dos personagens
    for i, personagem in enumerate(personagens, 1):
        escrever_lentamente(f"{i}. {personagem}")
    escrever_lentamente(f"{len(personagens) + 1}. Nenhum")

    # Obter escolha do jogador pelo número
    while True:
        try:
            escolha_num = int(input("Digite o número correspondente ao suspeito: "))
            if 1 <= escolha_num <= len(personagens) + 1:
                break
            else:
                escrever_lentamente("Escolha inválida. Digite um número da lista.")
        except ValueError:
            escrever_lentamente("Por favor, digite um número.")

    # Mapeando a escolha do jogador para o nome do personagem
    escolha = personagens[escolha_num - 1] if escolha_num <= len(personagens) else "nenhum"

    # Reações baseadas na escolha de Samanta
    if escolha == "Lady Isolde":
        escrever_lentamente("\nA sala está abafada, as chamas nas tochas dançam de forma inquieta, projetando sombras alongadas nas paredes de pedra.\n")
        escrever_lentamente("Samanta lança um olhar decidido a Lady Isolde, a viúva ainda envolta em luto, com o rosto pálido e as mãos apertadas no regaço.\n")
        escrever_lentamente("Samanta, com uma voz fria, dispara: \"Você sempre teve razões para desejar a morte de Baldwin, não é?\"")
        escrever_lentamente("Lady Isolde ergue o olhar, as lágrimas lutando para escapar: \"Você ousa? Ele era meu marido! Eu o amava... ao menos, tentei amá-lo.\"\n")
        escrever_lentamente("Nesse momento, Bram, o ferreiro robusto, baixa o olhar, desconfortável. Todos sabem do caso entre ele e Lady Isolde.\n")
        escrever_lentamente("O padre limpa a garganta, perturbado. Ele também sabia da traição, mas nunca pensou que Lady Isolde fosse capaz de algo assim.\n")
        escrever_lentamente("O ar está pesado, as suspeitas giram no ambiente, e alguns começam a sussurrar entre si.\n")
        escrever_lentamente("Finalmente, Lady Isolde solta um grito abafado: \"Vocês não entendem... sim, eu tive sentimentos, mas jamais o teria matado!\"")
        escrever_lentamente("A tensão atinge seu auge, mas Samanta percebe que não há evidências suficientes. Aos poucos, as acusações se esvaem, deixando um rastro de incerteza.\n")

    elif escolha == "Floris":
        escrever_lentamente("\nO ambiente parece mais sombrio enquanto Samanta se aproxima de Floris, o bobo da corte, que usualmente trazia alegria, mas agora mantém um sorriso tenso.\n")
        escrever_lentamente("Samanta, com olhar penetrante, o acusa: \"Sempre fez piadas sobre a morte de Baldwin... Seria possível que isso fosse uma pista para algo mais sério?\"")
        escrever_lentamente("Floris solta uma risada nervosa, quase histérica: \"Ora, sou apenas um bobo da corte, não um assassino! Minha vida é entreter, Samanta!\"\n")
        escrever_lentamente("Os outros presentes trocam olhares desconfortáveis, e Gerhard, o carrasco, revira os olhos, murmurando algo sobre 'brincadeiras sem graça'.\n")
        escrever_lentamente("Lady Isolde observa de canto de olho, claramente perturbada. Ela, mais do que qualquer um, sabe o quanto Baldwin desprezava Floris e o quanto o bobo suportava com desprezo.\n")
        escrever_lentamente("Floris então se encolhe, mais pálido, e murmura: \"Era só piada... eu juro... eu nunca o faria...\"")
        escrever_lentamente("Mas a suspeita persiste por um momento antes de se desfazer em um silêncio embaraçoso. Todos na sala sentem a tensão entre Samanta e Floris, mas a dúvida lentamente desaparece, deixando um clima de desconforto no ar.\n")

    elif escolha == "Gerhard":
        escrever_lentamente("\nO ambiente parece ainda mais carregado quando Samanta se vira para Gerhard, o carrasco de aparência severa e semblante fechado.\n")
        escrever_lentamente("Samanta, em tom acusatório, aponta: \"Você sempre estava por perto... sabia de tudo. Diga, Gerhard, o que realmente aconteceu na noite em que Baldwin morreu?\"")
        escrever_lentamente("Gerhard ergue o olhar, seus olhos são frios, como aço: \"Meu trabalho é executar sob ordens, não matar por vontade própria. Eu sou um carrasco, não um assassino!\"")
        escrever_lentamente("Ele cerra os punhos, o corpo inteiro tenso, como se estivesse tentando reprimir uma raiva profunda. Floris, à distância, engole em seco, evitando o olhar de Gerhard.\n")
        escrever_lentamente("Bram o observa cauteloso, enquanto o padre parece recitar silenciosamente uma prece, perturbado pela brutalidade que Gerhard representa.\n")
        escrever_lentamente("O silêncio é quase palpável, como se a sala inteira estivesse à beira de explodir. Samanta hesita por um instante, percebendo que, embora Gerhard pareça capaz de matar, ele o faz sob ordens, e não há evidência suficiente para ligá-lo ao crime.\n")

    elif escolha == "Bram":
        escrever_lentamente("\nA sala parece encolher enquanto Samanta se aproxima de Bram, o ferreiro. Ele limpa as mãos sujas de fuligem na túnica, mas seu olhar permanece firme, sem desviar.\n")
        escrever_lentamente("Samanta, com a voz baixa e acusadora, diz: \"Você amava Lady Isolde... e Baldwin era o único obstáculo. É fácil ver o que isso significa, Bram.\"")
        escrever_lentamente("Bram estreita os olhos, sua voz sai grave e controlada: \"Amar alguém não significa que eu tiraria uma vida por ela.\"")
        escrever_lentamente("Lady Isolde arregala os olhos, as mãos trêmulas, e olha para Bram, dividida entre a culpa e a surpresa.\n")
        escrever_lentamente("O padre se benze, e Floris observa com o olhar baixo, claramente desconfortável, mas não surpreso.\n")
        escrever_lentamente("O ar é pesado, e todos sentem o peso da acusação. Mas Samanta percebe, pouco a pouco, que Bram não carrega qualquer culpa, apenas um amor proibido e imprudente. A suspeita sobre ele se dissolve, mas o impacto de sua acusação permanece no ar, criando um clima de desconfiança sutil.\n")

    elif escolha == "Padre":
        escrever_lentamente("\nA sala inteira sente um frio repentino quando Samanta se aproxima do padre, cuja expressão piedosa contrasta com a atmosfera sombria.\n")
        escrever_lentamente("Samanta, encarando-o fixamente, murmura: \"Você sabia dos pecados de todos, inclusive de Baldwin... Será que tomou as dores de quem ele feriu?\"")
        escrever_lentamente("O padre recua um passo, a voz trêmula mas firme: \"Meu dever é oferecer salvação, não julgamento. Eu perdoei Baldwin, assim como perdoaria qualquer um de vocês.\"")
        escrever_lentamente("Os outros trocam olhares desconfiados; Bram parece particularmente inquieto, lembrando-se de suas próprias confissões.\n")
        escrever_lentamente("Floris afasta-se sutilmente, o semblante desconfortável, enquanto Gerhard observa em silêncio, com um olhar de desprezo.\n")
        escrever_lentamente("O padre fecha os olhos, balbuciando uma oração, e Samanta percebe que, apesar das suspeitas, não há nada que realmente ligue o padre ao crime. A tensão começa a se dissipar, mas o peso de suas palavras continua.\n")

    elif escolha == "nenhum":
        escrever_lentamente("\nO silêncio na sala é denso, e o ar parece vibrar com a ansiedade e o medo de cada um ali presente.\n")
        escrever_lentamente("Samanta respira fundo, seus olhos percorrendo cada rosto. Ela percebe que, por mais que todos pareçam culpados em algum momento, nada realmente se encaixa.\n")
        escrever_lentamente("Ela se vira, decidida a investigar mais um pouco, enquanto os outros a observam com um misto de alívio e apreensão.\n")

    # Finalizando a interrogação
    escrever_lentamente("A sala mergulha em um silêncio intenso, com todos, inclusive Samanta, ponderando sobre o que acabaram de testemunhar e sobre o preço da verdade.\n")

def gerar_tabela_verdade():
    # Definindo as proposições
    proposicoes = [
        "Lady Isolde não está exatamente triste com a morte do marido.",
        "Floris parece feliz com a morte do cozinheiro",
        "Bram, o ferreiro, parece contente com a morte de Baldwin",
        "Gerhard parece satisfeito com a morte de Baldwin",
        "Calistus pode estar encobrindo o verdadeiro assassino, o que o torna suspeito.",
        "Baldwin não era uma boa pessoa."
    ]

    # Definindo as proposições verdadeiras e falsas
    verdadeiros = proposicoes_certas
    falsos = proposicoes_falsas

    # Gerando a tabela verdade
    tabela_verdade = Truths(verdadeiros, falsos)

    # Exibindo a tabela verdade
    escrever_lentamente("\nTabela Verdade:\n")
    escrever_lentamente(tabela_verdade)

def mostrar_tabela_verdade():
    # Pergunta ao usuário se ele deseja ver a tabela verdade
    resposta = input("Deseja ver a tabela verdade que você deveria ter chegado e a que você realmente chegou? (s/n): ")
    if resposta.lower() == "s":
        gerar_tabela_verdade()
