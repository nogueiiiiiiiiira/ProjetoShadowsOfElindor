import random
import time
import os
import ttg
from game.utils import escrever_lentamente
from prettytable import PrettyTable

# Armazenamento de respostas do jogador para análise posterior
proposicoes_escolhidas = []

def interrogar_personagensFase1():
    
    # Armazenamento de proposições com suas verdades
    proposicoes = {
        "P1": {"descricao": "A faca não pertence a Diana, a cozinheira.", "verdade": True},
        "P2": {"descricao": "Erik não gostava de Baldwin", "verdade": True},
        "P3": {"descricao": "Diana não gostava de Baldwin", "verdade": True},
        "P4": {"descricao": "Independentemente de suas intrigas com Baldwin, Erik provavelmente não o matou.", "verdade": True},
        "P5": {"descricao": "Tamanho da lâmina é pequeno, sugerindo alguém de porte pequeno.", "verdade": True}
    }


    # Opções de falas para Diana e Erik
    falasDiana = [
        "Você está sugerindo que eu o matei? Com uma faca pequena inda? Céus! Mesmo que Baldwin fosse um canalha e um pervertido, não é como se eu tivesse a coragem de tirar uma vida, detetive.",
        "Não sei de nada sobre essa lâmina pequena. Posso não estar lamentando a morte dele, mas isso não significa que estou comemorando também. Entendo o que você está insinuando, detetive.",
        "A faca pequena pode até combinar com meu gosto para lâminas, mas isso não significa que gosto de enterrá-las em mulherengos estúpidos, detetive. Pode parar com suas adivinhações agora mesmo.",
        "Está insinuando que a faca pode ser minha, detetive? Mas que... Claro que não! Acredito que atraímos tudo o que merecemos, isso é verdade, mas não sou o tipo de juíza que faz justiça com as próprias mãos, querida. Ainda mais com uma arma pequena como essa.",
        "Posso ter desejado a morte daquele ferreiro maldito um milhão de vezes, detetive, mas isso não quer dizer necessariamente que foi eu quem teve a honra de matá-lo com essa coisinha afiada aí. Já entendi o que você está insinuando."
    ]
    
    falasErik = [
        "Está sugerindo que uma faca pequena dessas poderia ser minha? Que adivinhação grotesta. Gosto de matar a distância, detetive, se é que me entende. Ainda mais se forem criaturas como Baldwin. Eu não usaria uma mísera faca para matá-lo.",
        "Está insinuando o que acho que está insinuando? Está falando sério, detetive? Baldwin me irritava, sim. E, às vezes, eu não queria mais nada além de meter uma bala na sua cabeça. Mas minha mulher, mesmo que o odiasse também, nunca me perdoaria por trair a confiança de Deus desse jeito.",
        "Se eu entendi bem o que você está insinuando, detetive, só me resta dizer que essa faca não é bem o meu estilo. E que, se eu tivesse a oportunidade de matar Baldwin, eu não teria feito desse jeito. Eu teria usado algo... Mais doloroso.",
        "Eu entendi bem o que você me perguntou? Está insinuando isso mesmo? Baldwin e eu tivemos nossas discussões sim, mas minha mulher sempre conseguia me ver a razão antes que eu fizesse algo que eu poderia me arrepender de fazer. Essa lâmina não me é familiar, detetive, mesmo que eu quisesse que fosse.",
        "Você está me acusando, detetive? Eu não usaria algo assim para matar Baldwin. Usaria algo, na verdade, que o fizesse se arrepender por todas as vezes que ele mexeu com minha esposa."
    ]
    
    # Seleciona falas aleatórias para Diana e Erik
    falaDiana = random.choice(falasDiana)
    falaErik = random.choice(falasErik)

    # Pergunta padrão
    escrever_lentamente("Depois de esperar os clientes sairem da estalagem, Samanta aproveita a brecha e se aproxima de sua primeira suspeita.")
    escrever_lentamente(f"\nDiana, a Cozinheira da Estalagem, cruza os braços com força, o tecido velho do avental esticado sob a pressão de seus músculos enquanto seus olhos encontram os de Samanta. Um olhar afiado, cheio de desconfiança, a examina como se ela tivesse acabado de insultar sua comida. Seu corpo inteiro emana irritação contida — as sobrancelhas cerradas, a boca apertada numa linha dura e o peso de sua respiração se arrasta, como se estivesse contando mentalmente até dez para não explodir.")
    escrever_lentamente("\nQuando percebe o brilho metálico da faca que Samanta segura, sua expressão muda num instante. Ela é inteligente. Ela sabe porque que Samanta está ali. Há um lampejo de surpresa que rapidamente se transforma em frustração. A incredulidade salta de seus olhos, como se a mera sugestão de que ela poderia estar envolvida na morte de Baldwin fosse uma afronta pessoal. Ela aperta os lábios até formarem uma linha reta, os dedos batendo impacientemente na lateral do avental, indicando que não toleria a conversa que se seguiria por muito tempo.")
    escrever_lentamente("O corpo de Samanta reclama com a provação que sabe que virá a seguir — músculos pesados e tensos, uma dor latejante na têmpora esquerda. O ar parece espesso e ela sente um gosto de metal na boca, reflexo do esforço e da exaustão. Diana a observa com a mesma rigidez de uma panela fervente prestes a transbordar, mas, por fim, sua expressão volta a uma calma tensa. Está claro que ela não pretende facilitar a investigação.")
    escrever_lentamente("\nIndependenetemente disso, no entanto, Samanta a questiona acerca da faca encontrada ao lado do corpo de Baldwin, observando tudo o que é dito e não dito por parte dela.")

    # Respostas dos personagens
    escrever_lentamente(f"\nDiana responde, mal-humorada: '{falaDiana}'")
    insistir = input("\nVocê deseja continuar com a conversa? (S/N): ").strip().lower()
    
    if insistir == 's' or insistir == 'S':
        probRevelacaoDiana = random.random()
        
        if probRevelacaoDiana > 0.5:
            escrever_lentamente("\nDiana revira os olhos com a insistência. Vendo que mais pessoas chegam a estalagem e prevendo uma chance de escapar do interrogatória, ela somente zomba: 'Acho que já vi sua presença intromedita aqui antes, não vi? Nunca havia reparado como você é pequena, detetive, mesmo que seja forte' e vai embora. ")
            
        else:
            escrever_lentamente("\nDiana revira os olhos com a insistência. Vendo que mais pessoas chegam a estalagem e prevendo uma chance de escapar do interrogatória, ela somente zomba: 'Acho que suas cotas de perguntas já acabaram, detetive' e vai embora.")
        
    time.sleep(2)
    os.system("cls")
    escrever_lentamente("\nCom um suspiro, Samanta parte para encontrar Erick, o Caçador.")
    time.sleep(2)
    os.system("cls")
    
    escrever_lentamente("Quando finalmente o encontra, o vento frio se faz conhecido. Erik está na saída da vila. Sua capa está marcada de lama seca e folhas, e ele se move com a inquietude de alguém que está sempre em alerta. Ao ver a faca na mão de Samanta, seu corpo enrijece por um momento, mas logo ele a examina com um desprezo controlado, como quem avalia a ameaça de um animal ferido.")
    escrever_lentamente("\nSeus olhos, afiados como os de um predador, analisam cada detalhe da lâmina. Há cautela na forma como ele ajusta o cinto e evita a encarar por muito tempo, os dedos finos deslizando brevemente sobre o cabo da própria faca de caça. O desprezo dele é evidente, mas sutil — um meio sorriso amargo que desaparece antes que se possa fixá-lo.")
    escrever_lentamente("\nA fadiga pesa sobre Samanta como um manto molhado ao prever mais discussão. A dor de cabeça aumenta  e o gosto de metal na boca se intensifica, como se a investigação estivesse a corroendo por dentro. Erik se afasta um pouco, os olhos esquadrinhando as árvores ao redor, como se estivesse pronto para sumir a qualquer sinal de perigo. A tensão é palpável, mas ele permanece, ainda que desconfortável, enquanto Samanta o encara.")
    escrever_lentamente("Ele pergunta o que Samanta quer. Ela o questiona sobre a faca encontrada ao lado do corpo de Baldwin, observando como a faca é semelhante aquela que ele segura nas mãos.")
    escrever_lentamente(f"\nErik, com os lábios em uma linha reta, responde ríspido: '{falaErik}'")
    
    insistir = input("\nVocê deseja continuar com a conversa? (S/N): ").strip().lower()

    probRevelacaoErik = random.random()

    if probRevelacaoErik > 0.5:
        escrever_lentamente("\nErik zomba com a insistência. Sem paciência, ele diz: 'Você usa uma roupa vermelha, não usa? É interessante como alguém com uma personalidade como a sua usa uma roupa tão interessante como essa' e vai embora.")

    else:
        escrever_lentamente("\nErik zomba com a insistência. Sem paciência, ele diz: 'Acho que suas cotas de perguntas já acabaram, detetive' e vai embora.")

    time.sleep(3)
    os.system("cls")
            
    # Exibe as proposições ao jogador
    print("\nEscolha as proposições que você considera verdadeiras:")
    for chave, info in proposicoes.items():
        print(f"{chave}: {info['descricao']}")
    
    # Captura as escolhas do jogador
    escolhas = input("\nDigite as letras das proposições que considera verdadeiras, separadas por vírgula: ").split(",")
    escolhas = [e.strip().upper() for e in escolhas]
    proposicoes_escolhidas.extend(escolhas)
 
def interrogar_personagensFase2():
    
     # Armazenamento de proposições com suas verdades
    proposicoes = {
        "P6": {"descricao": "Boris não está mentindo conscientemente. Ele não pode ser culpado.", "verdade": True},
        "P7": {"descricao": "Mariana não parece guardar rancor de Baldwin. Ela não é culpada.", "verdade": True},
        "P8": {"descricao": "Pegadas pequenas sugerem uma presença feminina.", "verdade": True},
        "P9": {"descricao": "O relato de ambos se contradizem ", "verdade": True},
        "P10": {"descricao": "Dado a sua idade, não é possível confiar no que Boris fala", "verdade": True}
    }
    
    # Opções de falas para Mariana e Boris
    falasMariana = [
        "Admito que não me lembro de muita coisa daquele dia ou do dia anterior e sei como isso soa meio... Estranho. Mas foram dias corridos e muito chocantes, sabe, detetive? Mas acho que vi alguém saindo pela portas do fundo antes de encontrar o corpo do senhor Baldwin. Acho que poderia ser uma mulher...",
        "Reconheço que tenho poucas lembranças daquele dia. E sei como isso me faz parecer. Mas foi um dia agitado e bastante impactante, entende, detetive? Mas creio que avistei alguém saindo pela porta dos fundos antes de descobrir o corpo do senhor Baldwin. Havia também algumas pegadas pequenas, não é? Talvez de uma mulher...?",
        "Confesso que não recordo muitos detalhes daquele dia e sei que isso pode soar meio... Incriminador. Mas foi um dia intenso e muito surpreendente, você entende, detetive? Porém, acho que vi uma pessoa deixando o local pela porta dos fundos antes de encontrar o corpo do senhor Baldwin. Havia que vi algumas pegadas de mulher antes também...",
        "Aceito que não me recordo de muita coisa do que aconteceu naquele dia e sei que isso pode me fazer parecer culpada. Mas foi um dia corrido e extremamente perturbador, não acha, detetive? Mas tenho a impressão de que vi alguém saindo pela porta de trás antes de encontrar o corpo do senhor Baldwin. Acho que notei algumas pegadas pequenas também... Acho que pareciam de botas femininas.",
        "Admito que minha memória daquele dia é um pouco nebulosa e sei que isso pode me incrimar. Mas foi um dia cheio de acontecimentos e muito chocante, compreende, detetive? No entanto, acho que percebi alguém saindo pela porta dos fundos antes de eu me deparar com o corpo do senhor Baldwin. Acho que havia algumas pegadas pequenas também do lado de fora... Talvez de uma mulher?"
    ]
    
    falasBoris = [
        "Lembro-me de ter visto um homem saindo da estalagem pouco antes de ouvir os gritos da senhorita Mariana, mas não me lembro. E sou um homem de idade, senhorita, então perdoe-me pela minha falta de utilidade nesse momento",
        "Tenho a impressão de que vi um homem deixando a estalagem logo antes de ouvir os gritos da senhorita Mariana, mas não consigo me lembrar bem. E, como sou um homem idoso, senhorita, peço desculpas por não ser de muita ajuda neste momento.",
        "Recordo de ter avistado um homem saindo da estalagem pouco antes de ouvir os gritos da senhorita Mariana, mas a memória não é clara. E, sendo um homem mais velho, senhorita, peço que me perdoe por não conseguir ser mais útil agora.",
        "Acho que vi um homem saindo da estalagem momentos antes dos gritos da senhorita Mariana, mas não tenho certeza. E, como sou um homem de idade, senhorita, espero que compreenda minha falta de clareza neste instante.",
        "Lembro de ter visto um homem sair da estalagem pouco antes dos gritos da senhorita Mariana, mas minha memória é vaga. E, sendo um homem mais velho, senhorita, desculpe-me por não conseguir ajudar mais neste momento."
    ]
    
    # Seleciona falas aleatórias para Mariana e Boris
    falaMariana = random.choice(falasMariana)
    falaBoris = random.choice(falasBoris)

    # Pergunta padrão
    escrever_lentamente("Depois dos dois primeiros interrogatórios, Samanta volta novamente a estalagem para encontrar Mariana. Não demora muito para encontrá-la e deixar claro a intenção de questioná-la.")
    escrever_lentamente("\nMariana está encolhida em um canto da estalagem, os dedos finos torcendo-se nervosamente enquanto Samanta se aproxima. Seus olhos grandes parecem oscilar entre medo e hesitação, como se cada pergunta fosse um peso invisível aumentando sua angústia. A maneira como ela abaixa a cabeça e evita contato visual deixa evidente que algo a perturba.")
    escrever_lentamente("\nSeus movimentos são rápidos e nervosos — ajeita a barra do vestido, toca nas tranças e seus pés se mexem inquietos, como se quisesse escapar dali. Quando Samanta fala da manhã do incidente, seus dedos apertam o tecido do vestido com tanta força que os nós dos dedos ficam brancos. Está claro que a memória do encontro com Baldwin a assombra, mas ela parece estar se debatendo entre o medo de falar demais e a necessidade de ser honesta.")
    escrever_lentamente("O corpo de Samanta está à beira da exaustão, e a dor de cabeça se mistura ao gosto amargo que Samanta não consegue tirar da boca. Mariana percebe a sua condição e, por um momento, parece se compadecer, mas sua própria ansiedade logo a consome novamente. Ela sabe porque Samanta está ali, na frente dela.")
    escrever_lentamente(f"\Samanta pergunta a ela se ela se lembra de ter visto algo suspeito nos dias que se antecederam a morte de Baldwin")
    
    # Respostas dos personagens
    escrever_lentamente(f"\nMariana diz, tímida: '{falaMariana}'")
    
    insistir = input("\nVocê deseja insistir na conversa? (S/N): ").strip().lower()
 
    if insistir == 's' or insistir == 'S':
        # Simulação de probabilidade para revelar mais informações
        probRevelacaoMariana = random.random()

        if probRevelacaoMariana > 0.5:
            escrever_lentamente("\nMariana se encolhe, meio desconfortável com a insistência. Hesitante, ela muda de assunto: 'Se me permite dizer, detetive, de mulher para mulher, seu hálito cheira a licor. Você bebe?'. Samanta pisca por um momento e, então, entendendo a dica, vai embora.")
            
        else:
            escrever_lentamente("\nMariana se encolhe, meio desconfortável com a insistência. Hesitante, ela confessa: 'Se me permite dizer, detetive, de mulher para mulher, acho que não consigo responder mais perguntas por hoje. Samanta pisca por um momento e, então, entendendo a dica, vai embora.")
        
    time.sleep(2)
    os.system("cls")
    escrever_lentamente("Com um suspiro, Samanta vai para o lado de fora da estalagem, onde sabe que encontrará seu próximo suspeito: Boris.")
    time.sleep(2)
    os.system("cls")
    
    escrever_lentamente("Ela o encontra rapidamente. Boris está de pé, as mãos grossas descansando nos quadris, como se a força de sua presença fosse suficiente para intimidar qualquer um. Há algo incerto em seus movimentos, no modo como ajusta a postura mais de uma vez, tentando parecer seguro, mas falhando em disfarçar a tensão quando a vê.")
    escrever_lentamente("Ao mencionar a manhã em que ele acompanhou Mariana e o momento dos gritos que se seguiram, Boris franze a testa e desvia o olhar por um instante, pensativo. Ele cruza os braços e, em seguida, muda de posição, como se quisesse acabar logo com aquela conversa. Embora relutante em se envolver, é claro que a memória do que aconteceu o incomoda. Ou a falta dela. ")
    escrever_lentamente("\nSamanta o questiona acerca da mesma coisa sobre o que questionou Mariana.")
        
    escrever_lentamente(f"\nSuspirando, Boris admite: '{falaBoris}'")
        
    insistir = input("\nVocê deseja insistir na conversa? (S/N): ").strip().lower()
 
    if insistir == 's' or insistir == 'S':
        probRevelacaoBoris = random.random()
 
        if probRevelacaoBoris > 0.5:
            escrever_lentamente("\nBoris, com um sorriso cansado, se afasta da conversa insistente, dizendo apenas: 'Você sempre usa essa roupa vermelha, senhorita? É uma escolha ousada para alguém que se aventura em lugares como este. Não sabia que você vinha de uma família boa' e vai embora.")

        else:
            escrever_lentamente("\nBoris, com um sorriso cansado, se afasta da conversa insistente, dizendo apenas: 'Acredito que tenho mais coisas para fazer do que ficar respondendo perguntas, senhorita' e vai embora.")
            

    time.sleep(3)
    os.system("cls")
    
    # Exibe as proposições ao jogador
    print("\nEscolha as proposições que você considera verdadeiras:")
    for chave, info in proposicoes.items():
        print(f"{chave}: {info['descricao']}")
    
    # Captura as escolhas do jogador
    escolhas = input("\nDigite as letras das proposições que considera verdadeiras, separadas por vírgula: ").split(",")
    escolhas = [e.strip().upper() for e in escolhas]
    proposicoes_escolhidas.extend(escolhas)

def interrogar_personagensFase3():
    
    proposicoes = {
        "P11": {"descricao": "O tecido é da capa de Madame Lavínia. Ela pode ser culpada. ", "verdade": False},
        "P12": {"descricao": "De acordo com a Lavínia, o tecido é mesmo caro, indicando alguém de classe elevada ou média.", "verdade": True},
        "P13": {"descricao": "Madame Lavínia está na defensiva com a acusação. Ela não é culpada.", "verdade": True},
        "P14": {"descricao": "Madame Lavínia dá a entender que sua relação com Baldwin não era complicada", "verdade": False},
        "P15": {"descricao": "Baldwin era um homem violento. Madame Lavínia dá a entender que ele se aproveitava de mulheres.", "verdade": True}
    }
     
    # Opções de falas para Madame Lavínia
    falasLavinia = [
        "Baldwin sempre foi um homem... peculiar, detetive. Ele frequentemente procurava consolo e autoestima em locais que não eram apropriados e muitas vezes a força. E, se eu estiver entendendo bem o que a senhorita está insinuando, posso lhe dizer, sem dúvidas, que eu não sou a única vitíma de Baldwin que tem certo prestigío na vida.",
        "O Baldwin sempre foi um sujeito... peculiar, detetive. Ele buscava conforto e autoestima em lugares pouco apropriados e muitas vezes a força. Se estou captando o que a senhorita está errôneamente insinuando, posso lhe garantir que não sou a única pessoa de prestígio que sofreu nas mãos de Baldwin.",
        "Baldwin sempre teve um comportamento... diferente, detetive. Frequentemente, ele procurava segurança e reconhecimento em lugares inapropriados e muitas vezes a força. Se entendi bem a sua insinuação, uma da qual não estou contente em participar, posso dizer que não sou a única pessoa de posição que foi alvo de Baldwin.",
        "Sempre considerei Baldwin um homem... peculiar, detetive. Ele costumava buscar consolo e autoafirmação em locais inadequados e muitas vezes a força. Se estou certa quanto ao que está sugerindo, posso lhe assegurar que não fui a única pessoa de destaque que teve problemas com Baldwin. Vá fazer melhores suposições, detetive. De preferência, críveis.",
        "aldwin sempre teve um jeito... singular, detetive. Ele buscava apoio e validação em contextos que não eram apropriados e muitas vezes a força. E se eu estiver interpretando corretamente o que a senhorita insinua, posso afirmar que não sou a única pessoa de prestígio a quem ele causou transtornos."
    ]
    
    # Seleciona uma fala aleatória para Madame Lavínia
    falaLavinia = random.choice(falasLavinia)

    # Pergunta padrão
    escrever_lentamente("No dia seguinte, Samanta se aventura na casa de Madame Lavínia após conseguir uma licença para investigar mais afundo o caso de Baldwin.")
    escrever_lentamente("\nMadame Lavínia a recebe com a frieza de um mármore esculpido. Seus olhos, calculistas e atentos, a medem como se ela estivesse ali para uma negociação que já estivesse decidida antes mesmo de começar. Sua postura é impecável, sem um único gesto que não seja deliberadamente controlado.")
    escrever_lentamente("\nQuando Samanta mostra o pedaço de tecido vermelho silenciosamente, seus dedos finos e adornados com anéis mal se movem, mas há uma rigidez sutil nos ombros, como se aquela evidência fosse uma afronta inesperada. O rosto dela permanece impassível, embora seus olhos brilhem brevemente com uma sombra de irritação. Ela entende a insinuação que Samanta faz silenciosamente.")
    escrever_lentamente("Os músculos de Samanta protestam com cada movimento que ela faz ao ver o desprezo de Madame Lavínia sobre ela. Sua dor de cabeça latejante aumenta, deixado tudo levemente desfocado. Lavínia continua imperturbável, a analisando como se tentasse adivinhar seus próximos passos, jogando um xadrez mental onde cada palavra vale uma jogada.")
    escrever_lentamente(f"\nSamanta questiona Madame Lavínia sobre Baldwin e seu comportamento.")
    
    # Resposta de Madame Lavínia
    escrever_lentamente(f"\nMadame Lavínia, com uma careta, responde: '{falaLavinia}'")

    # Pergunta se o jogador deseja insistir em mais perguntas
    insistir = input("\nVocê deseja na conversa? (S/N): ").strip().lower()
    
    if insistir == 's' or insistir == 'S':
        # Simulação de probabilidade para revelar mais informações
        probRevelacaoLavinia = random.random()

        if probRevelacaoLavinia > 0.5:
            escrever_lentamente("\nMadame Lavínia, com mãos pesadas, a empurra levemente para fora de sua casa após perceber a insistência, dizendo: 'É curioso, detetive, muito curioso você ter a audácia de me acusar e, ainda assim, eu ter te visto na companhia de Baldwin diversas vezes, bebendo com ele' e fecha a porta. ")

        else:
            escrever_lentamente("\nMadame Lavínia, com mãos pesadas, a empurra levemente para fora de sua casa após perceber a insistência, dizendo apenas: 'Acho que suas cotas de perguntas já acabaram, detetive' e fecha a porta.")

    time.sleep(3)
    os.system("cls")
    
    # Exibe as proposições ao jogador
    print("\nEscolha as proposições que você considera verdadeiras:")
    for chave, info in proposicoes.items():
        print(f"{chave}: {info['descricao']}")
    
    # Captura as escolhas do jogador
    escolhas = input("\nDigite as letras das proposições que considera verdadeiras, separadas por vírgula: ").split(",")
    escolhas = [e.strip().upper() for e in escolhas]
    proposicoes_escolhidas.extend(escolhas)

def interrogar_personagensFase4():
    
    proposicoes = {
        "P16": {"descricao": "O licor achado junto ao corpo de Baldwin foi comprado por intermédio de uma mulher. ", "verdade": True},
        "P17": {"descricao": "Quem comprou o licor foi Madame Lavínia. ", "verdade": True},
        "P18": {"descricao": "Rodrigo, apesar de parecer não gostar de Baldwin, não parece estar ligado a sua morte. ", "verdade": True},
        "P19": {"descricao": "Dado aos rumores das ações de Baldwin, ele provavelmente utilizaria o licor de modo indevido", "verdade": True},
        "P20": {"descricao": "O licor tem propriedades adormecedoras, indicando que poderia ser usado para dopar alguém.", "verdade": True}
    }
    
    # Opções de falas para Rodrigo
    falasRodrigo = [
        "Baldwin... Ele não era bem-vindo por aqui, então não vendi nada para ele. Não que eu saiba, ao menos. Quero dizer, não tenho nada contra ele, pessoalmente. Na verdade, tenho sim... Afinal, suas escolhas e ações com mulheres eram... digamos, questionáveis. A única pessoa que me lembro de ter comprado esse licor - sabia que ele tem propriedades adormecedoras, detetive? - era uma mulher com vestes vermelhas, mas ela tinha alguma coisa no rosto, então... Não posso te falar quem era exatamente.",
        "Baldwin… Ele não era exatamente bem-vindo por aqui, então não cheguei a vender nada para ele. Ou, pelo menos, não que eu lembre. Quer dizer, não tenho nada contra ele, pessoalmente. Bem, talvez até tenha… Afinal, suas atitudes com mulheres eram, digamos, duvidosas. Enfim, a única pessoa que me lembro de ter comprado esse licor - sabia que ele tem propriedades adormecedoras, detetive? - foi uma mulher vestida de vermelho, mas ela tinha algo cobrindo o rosto, então… Não posso dizer quem era com certeza.",
        "Baldwin… Ele não era muito aceito por essas partes, então nunca vendi nada diretamente para ele. Ao menos, não que eu saiba. Não que eu tenha algo contra ele, pessoalmente… Bem, na verdade, até tenho. Até porque suas ações com mulheres eram, digamos, discutíveis. Mas, é... Bem, a única pessoa que lembro de ter comprado esse licor - sabia que ele tem propriedades adormecedoras, detetive? - foi uma mulher de vermelho, mas ela usava algo no rosto, então… Não sei exatamente quem era.",
        "Baldwin… Não era alguém bem-recebido por aqui, então não cheguei a vender nada a ele. Pelo menos, não que eu me recorde. Quer dizer, não tenho algo contra ele, exatamente. Na verdade, talvez tenha… Mas, é, bem... Enfim, suas atitudes com as mulheres eram, digamos, um tanto suspeitas. Mas, né... Eh... A única pessoa que lembro de ter comprado esse licor - sabia que ele tem propriedades adormecedoras, detetive? - era uma mulher vestida de vermelho, mas ela tinha algo cobrindo o rosto, então… Não consigo dizer com certeza quem era.",
        "Baldwin… Ele não era bem-visto por aqui, então nunca vendi nada a ele, ao menos que eu saiba. Não que eu tivesse algo contra ele… Bem, talvez tenha, tivesse, sim. Suas ações com mulheres eram, afinal, questionáveis. Mas bem... A única pessoa que lembro de ter comprado esse licor - sabia que ele tem propriedades adormecedoras, detetive? - foi uma mulher de roupas vermelhas, mas ela tinha o rosto coberto por algo, então… Não posso afirmar quem era, exatamente."
    ]
    
    # Seleciona uma fala aleatória para Rodrigo
    falaRodrigo = random.choice(falasRodrigo)

    # Pergunta padrão
    escrever_lentamente("No último dia de sua investigação, Samanta parte para a adega onde costuma-se vender o licor que foi encontrado junto ao corpo de Baldwin.")
    escrever_lentamente("\nQuando Samanta entra pela porta, Rodrigo se encontra encostado preguiçosamente em um barril, os braços musculosos cruzados sobre o peito. Seu olhar é pesado, mas desinteressado. Ele se movimenta devagar, sem pressa, como quem tem certeza de que nada o atinge.")
    escrever_lentamente("\nAo mencionar o  licor encontrado com o corpo de Baldwin para o mesmo, ele apenas ergue uma sobrancelha com uma mistura de enfado e curiosidade. ELe ajusta a faixa vermelha na cintura, como se quisesse enfatizar que nada o preocupa. A respiração dele é tranquila e ele não parece intimidado com a acusação silenciosa que é feita, embora a postura relaxada esconda certa vigilância.")
    escrever_lentamente("A sensação de peso nos ombros é quase insuportável, e o gosto amargo da bebida na boca nos faz sentir cada vez mais exaustos. Rodrigo continua ali, imperturbável, como se estivesse disposto a ouvir o tempo que fosse necessário, sem nunca se envolver mais do que o estritamente necessário.")
    escrever_lentamente(f"\nSamanta questiona Rodrigo sobre seu conhecimento a respeito de Baldwin e sobre o licor que ela se lembra de ver na cena do crime")
    
    # Resposta de Rodrigo
    escrever_lentamente(f"\nRodrigo, depois de pensar por um momento, responde: '{falaRodrigo}'")

    # Pergunta se o jogador deseja insistir em mais perguntas
    insistir = input("\nVocê deseja insistir na conversa? (S/N): ").strip().lower()
    
    if insistir == 's' or insistir == 'S':
        # Simulação de probabilidade para revelar mais informações
        probRevelacaoRodrigo = random.random()

        if probRevelacaoRodrigo > 0.8:
            escrever_lentamente("\nRodrigo boceja com a insistência. Ao ver que alguns clientes entram na loga, ele diz apenas: 'Você sabe os efeitos colaterais que esse licor causa, detetive? Como é muito forte, depois que é tomado, as pessoas costumam reclamar de dores e amnésia' e a deixa para atender os clientes.")

        else:
            escrever_lentamente("\nRodrigo boceja com a insistência. Ao ver que alguns clientes entram na loga, ele diz apenas: 'Acho que suas cotas de perguntas já acabaram, detetive' e a deixa para atender os clientes.")

    time.sleep(3)
    os.system("cls")
    
    # Exibe as proposições ao jogador
    print("\nEscolha as proposições que você considera verdadeiras:")
    for chave, info in proposicoes.items():
        print(f"{chave}: {info['descricao']}")
    
    # Captura as escolhas do jogador
    escolhas = input("\nDigite as letras das proposições que considera verdadeiras, separadas por vírgula: ").split(",")
    escolhas = [e.strip().upper() for e in escolhas]
    proposicoes_escolhidas.extend(escolhas)


def interrogar_personagensFase5():
    
    os.system("cls")
    escrever_lentamente("Chegou a hora de escolher um assassino:")
    time.sleep(2)
    os.system("cls")
    
    # Proposições corretas para desbloquear a opção "Ninguém é culpado"
    proposicoes_corretas = [
        "P1",  # "A faca não pertence a Diana, a cozinheira."
        "P4",  # "Independentemente de suas intrigas com Baldwin, Erik provavelmente não o matou."
        "P6",  # "Boris não está mentindo conscientemente. Ele não pode ser culpado."
        "P7",  # "Mariana não parece guardar rancor de Baldwin. Ela não é culpada."
        "P13", # "Madame Lavínia está na defensiva com a acusação. Ela não é culpada."
        "P18"  # "Rodrigo, apesar de parecer não gostar de Baldwin, não parece estar ligado a sua morte."
    ]
  
    # Verifica se o jogador selecionou todas as proposições corretas
    desbloqueiaNinguem = all(proposicao in proposicoes_escolhidas for proposicao in proposicoes_corretas)
    
    # Lista de suspeitos interrogados
    suspeitos = ["Diana", "Erik", "Mariana", "Boris", "Madame Lavínia", "Rodrigo"]
    
    # Opção final de escolha do assassino
    print("\nCom base em suas investigações, quem você acredita ser o assassino?")
    for idx, suspeito in enumerate(suspeitos, 1):
        print(f"{idx}. {suspeito}")
    
    # Adiciona a opção de "ninguém é culpado" se o jogador tiver desbloqueado essa possibilidade
    if desbloqueiaNinguem:
        print(f"{len(suspeitos) + 1}. Ninguém é culpado")
    
    # Captura a escolha final do jogador
    escolha = input("\nDigite o número correspondente à sua escolha: ").strip()
    
    # Define finais diferentes para cada escolha
    if escolha.isdigit():
        escolha = int(escolha)
        if escolha in range(1, len(suspeitos) + 1):
            suspeito_escolhido = suspeitos[escolha - 1]
            print(f"\nVocê escolheu {suspeito_escolhido}.")
            # Final individual para cada suspeito
            if suspeito_escolhido == "Diana":
                escrever_lentamente("Quando a algema é colocada e a sentença é feita, Diana perde o controle. Seu rosto, normalmente endurecido, se contorce de raiva. Ela grita e se debate como se lutasse contra uma injustiça, os braços tentando se livrar das amarras. O olhar que ela lança sobre Samanta é cheio de ódio — não pela prisão, mas pelo insulto à sua honra.")
                time.sleep(2)
                os.system("cls")
                escrever_lentamente("Você perdeu... Diana não é a assassina.")
                
            elif suspeito_escolhido == "Erik":
                escrever_lentamente("Quando a algema é colocada e a sentença é feita, Erik não se debate. Seus olhos se estreitam, no entanto, frios e calculistas, como se estivesse medindo todas as rotas de fuga possíveis. Há um desprezo silencioso enquanto é levado, mas ele sabe que brigar não ajudaria. Mesmo assim, o olhar que ele lança para Samanta é um aviso: ela cometeu um erro ao acusá-lo.")
                time.sleep(2)
                os.system("cls")
                escrever_lentamente("Você perdeu... Erik não é o assassino.")
                
            elif suspeito_escolhido == "Mariana":
                escrever_lentamente("Quando a algema é colocada e a sentença é feita, Mariana desmorona ao ser levada. Os olhos marejam e seu corpo parece perder toda a força. Ela olha para Samanta com uma expressão de desespero e traição, como se esperasse que tudo fosse um engano e que ainda pudesse acordar daquele pesadelo.")
                time.sleep(2)
                os.system("cls")
                escrever_lentamente("Você perdeu... Mariana não é a assassina.")
                
            elif suspeito_escolhido == "Boris":
                escrever_lentamente("Quando a algema é colocada e a sentença é feita,  Boris permanece em silêncio, mas a tensão em seu corpo é evidente. Ele aperta os punhos e respira fundo, como se estivesse segurando toda a frustração para não explodir. O olhar que ele dirige a Samanta é frio e cheio de decepção, como se esperasse mais dela.")
                time.sleep(2)
                os.system("cls")
                escrever_lentamente("Você perdeu... Boris não é o assassino.")
                
            elif suspeito_escolhido == "Madame Lavínia":
                escrever_lentamente("Quando a algema é colocada e a sentença é feita, Lavínia mantém a compostura até o último instante. Não há lágrimas, nem gritos. Apenas um olhar de puro desprezo direcionado a Samanta, como se ela fosse um verme ousando perturbá-la. Ela caminha com dignidade, mas seus olhos prometem uma vingança silenciosa.")
                time.sleep(2)
                os.system("cls")
                escrever_lentamente("Você perdeu... Madame Lavínia não é a assassina.")
                
            elif suspeito_escolhido == "Rodrigo":
                escrever_lentamente("Quando a algema é colocada e a sentença é feita, Rodrigo se deixa levar sem resistência, um sorriso cansado e cínico dorme em seus lábios. Ele encara tudo como uma inconveniência temporária. Mas o brilho nos olhos mostra que ele não pretende ser uma vítima passiva por muito tempo.")
                time.sleep(2)
                os.system("cls")
                escrever_lentamente("Você perdeu... Rodrigo não é o assassino.")
                
        elif desbloqueiaNinguem and escolha == len(suspeitos) + 1:
            
            escrever_lentamente("A verdade surge na mente de Samanta como uma faca fria atravessando a neblina da exaustão. Não há mais dúvidas. Enquanto cada rosto acusado desfilava diante dela — Diana furiosa, Erik cauteloso, Mariana desesperada, Boris incerto, Lavínia arrogante e um Rodrigo indiferente — a conclusão era inevitável. Nenhum deles matou Baldwin. Eles carregam seus segredos e pecados, sim, mas a culpa verdadeira... é dela.")
            escrever_lentamente("A dor de cabeça lateja com mais força agora, como se as próprias lembranças, até então fragmentadas e distantes, finalmente se alinhassem. O gosto metálico que insiste em não sair da boca de Samanta é mais do que um reflexo da fadiga. É o sabor da culpa.")
            escrever_lentamente("\nSamanta se lembra do licor. Ela se lembra de ter passado a noite bebendo na estalagem e Baldwin, como um bartender adequado, se aproximando dela. Ela se lembra do jeito que Baldwin sorriu e lhe ofereceu uma bebibda, confiante e cruel, enquanto despejava o líquido âmbar em um copo e dava. 'Apenas um pouco para relaxar' foi o que ele disse — uma gentileza traiçoeira, que ela só foi perceber, muito cansada e exausta de trabalhos e de expectativas, um pouco tarde demais. Samanta sentiu a tensão crescente em seu próprio corpo quando percebeu o ardor falso na garganta e o olhar predador de Baldwin, fixo demais, invasivo demais, sobre ela naquela madrugada.")
            escrever_lentamente("Ele tentou a silenciar com o álcool. Tentou transformar a sua resistência em obediência quando estavam a sós. Mas ela não deixou. Agimndo antes que ele pudesse tomar o que queria. Agindo sem pensar, com uma mão trêmula e um coração disparado. Samanta pegou a faca mais próxima. A lâmina perfurou a carne dele como um ato desesperado — rápido, brutal e inevitável.")
            escrever_lentamente("\nAgora, tudo parecia mais claro e, ao mesmo tempo, distorcido. Recordar não traz alívio. Só torna o peso mais insuportável. Ela fez aquilo para sobreviver, mas não foi apenas a lâmina que cortou Baldwin. Com ele, ela matou uma parte de si mesma também.")
            escrever_lentamente("\nE ela não sabe como se sentir a respeito disso...")
            
            time.sleep(2)
            os.system("cls")
            escrever_lentamente("Você ganhou... Você é a assassina...")
            
        else:
            print("Escolha inválida.")
    else:
        print("Escolha inválida.")
        
    mostrar_tabelas(proposicoes_escolhidas)

def mostrar_tabelas(proposicoes_escolhidas):
    todas_proposicoes = {
        "P1": {"descricao": "A faca não pertence a Diana, a cozinheira.", "verdade": True},
        "P2": {"descricao": "Erik não gostava de Baldwin.", "verdade": True},
        "P3": {"descricao": "Diana não gostava de Baldwin.", "verdade": True},
        "P4": {"descricao": "Independentemente de suas intrigas com Baldwin, Erik provavelmente não o matou.", "verdade": True},
        "P5": {"descricao": "Tamanho da lâmina é pequeno, sugerindo alguém de porte pequeno.", "verdade": True},
        "P6": {"descricao": "Boris não está mentindo conscientemente. Ele não pode ser culpado.", "verdade": True},
        "P7": {"descricao": "Mariana não parece guardar rancor de Baldwin. Ela não é culpada.", "verdade": True},
        "P8": {"descricao": "Pegadas pequenas sugerem uma presença feminina.", "verdade": True},
        "P9": {"descricao": "O relato de ambos se contradizem.", "verdade": True},
        "P10": {"descricao": "Dado a sua idade, não é possível confiar no que Boris fala.", "verdade": True},
        "P11": {"descricao": "O tecido é da capa de Madame Lavínia. Ela pode ser culpada.", "verdade": False},
        "P12": {"descricao": "De acordo com a Lavínia, o tecido é mesmo caro, indicando alguém de classe elevada ou média.", "verdade": True},
        "P13": {"descricao": "Madame Lavínia está na defensiva com a acusação. Ela não é culpada.", "verdade": True},
        "P14": {"descricao": "Madame Lavínia dá a entender que sua relação com Baldwin não era complicada.", "verdade": False},
        "P15": {"descricao": "Baldwin era um homem violento. Madame Lavínia dá a entender que ele se aproveitava de mulheres.", "verdade": True},
        "P16": {"descricao": "O licor achado junto ao corpo de Baldwin foi comprado por intermédio de uma mulher.", "verdade": True},
        "P17": {"descricao": "Quem comprou o licor foi Madame Lavínia.", "verdade": True},
        "P18": {"descricao": "Rodrigo, apesar de parecer não gostar de Baldwin, não parece estar ligado a sua morte.", "verdade": True},
        "P19": {"descricao": "Dado aos rumores das ações de Baldwin, ele provavelmente utilizaria o licor de modo indevido.", "verdade": True},
        "P20": {"descricao": "O licor tem propriedades adormecedoras, indicando que poderia ser usado para dopar alguém.", "verdade": True},
    }

    time.sleep(2)
    os.system("cls")

    resposta = input("Você gostaria de ver as respostas que deu e compará-las com as respostas verdadeiras? (S/N): ").strip().lower()
    if resposta == 's':
        tabela = PrettyTable()
        tabela.field_names = ["Proposição", "Descrição", "Verdade", "Sua Resposta"]

        for chave, info in todas_proposicoes.items():
            estado = "Verdadeiro" if info["verdade"] else "Falso"
            resposta_jogador = "Verdadeiro" if chave in proposicoes_escolhidas else "Falso"
            tabela.add_row([chave, info["descricao"], estado, resposta_jogador])

        time.sleep(2)
        os.system("cls")
        print(tabela)
