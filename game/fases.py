# fases.py

import time # importa a biblioteca time para manipulação de tempo
import os # importa a biblioteca os para manipulação de sistema operacional
from game.interacoes import interrogar1, interrogar2, interrogar3, interrogar4, interrogar5 # importa as funções de interrogação
from game.utils import escrever_lentamente, mostrar_imagem, limpar_console # importa funções auxiliares para escrita lenta, mostrar imagem e limpar o console

LARGURA_TERMINAL = 110 # largura do terminal para centralizar o texto

def instrucoes():
        
    limpar_console()
    
    escrever_lentamente("    Bem-vindo ao jogo, detetive! Prepare-se para desvendar um mistério ambientado na era medieval, onde cada detalhe pode esconder uma pista crucial. Siga as instruções abaixo e embarque nessa intrigante jornada. ", espacosEsquerda = 4) 
    escrever_lentamente("    Você é Samanta, uma detetive astuta e sagaz, conhecida por seu faro aguçado para desvendar segredos e intrigas. O jogo se passa em uma pequena vila medieval cercada por bosques misteriosos e imponentes castelos de pedra. A calmaria da vila foi interrompida por um crime, e cabe a você descobrir quem é o responsável. Mas cuidado: nem tudo é o que parece, e os suspeitos são mestres na arte de esconder suas verdadeiras intenções. ", espacosEsquerda = 4)
    escrever_lentamente("    Seu objetivo é resolver o mistério principal identificando o culpado e o motivo por trás do crime. Para isso, você precisará examinar todas as pistas, decidir entre o que é verdadeiro e falso e interrogar os suspeitos com cuidado. ", espacosEsquerda = 4)
    
    time.sleep(5)
    limpar_console()
    
    escrever_lentamente("    - Mecânica do Jogo: O jogo começa com uma breve introdução sobre a história e o cenário. Isso inclui detalhes sobre o crime, o local e o clima de tensão entre os habitantes da vila. Fique atento: detalhes aparentemente comuns podem esconder pistas importantes! ", espacosEsquerda = 4)
    escrever_lentamente("    - Personagens Suspeitos: Após a introdução, você conhecerá os principais suspeitos. Cada um possui uma personalidade distinta, um possível motivo e histórias entrelaçadas que podem ajudar (ou confundir) em sua investigação. ", espacosEsquerda = 4)
    escrever_lentamente("    - Sistema de Proposições Verdadeiras e Falsas: Ao longo do jogo, você encontrará 20 proposições – afirmações que poderão ou não ser verdadeiras. A cada proposição, você terá a chance de decidir se acredita nela ou não. Se você optar por marcar uma proposição como verdadeira, ela será considerada como parte das pistas para solucionar o caso. As proposições que você não marcar como verdadeiras serão automaticamente atribuídas como falsas", espacosEsquerda = 4)

    time.sleep(5)
    limpar_console()
    
    escrever_lentamente("    Interrogando os Suspeitos: Ao conversar com os suspeitos, você poderá receber informações variadas: ", espacosEsquerda = 4)
    escrever_lentamente("    - Pistas confirmadas: algumas serão essenciais para avançar na trama. ", espacosEsquerda = 4)
    escrever_lentamente("    - Pistas aleatórias baseadas na “sorte”: se insistir nas perguntas, pode acabar obtendo respostas que dependem de um pouco de sorte, como informações extras ou contradições sutis que só surgem quando você pergunta no momento certo. ", espacosEsquerda = 4)

    time.sleep(5)
    limpar_console()
    
    escrever_lentamente("    Detalhes na Narração: Fique atento à narração do jogo, pois nem todas as pistas estão nas proposições ou falas diretas dos personagens. Muitas vezes, os detalhes estão descritos na ambientação, nos gestos dos personagens e nas mudanças de humor ou expressão. ", espacosEsquerda = 4)

    time.sleep(5)
    limpar_console()
    
    escrever_lentamente("    Ao final da sua investigação, você poderá fazer suas acusações e descrever o que acredita ser o desenrolar dos fatos. Se desejar, o jogo lhe dará a opção de comparar suas respostas com a solução real. Essa comparação revelará quais proposições eram verdadeiras ou falsas, ajudando você a entender o que deixou passar e aperfeiçoar suas habilidades de detetive para a próxima partida!", espacosEsquerda = 4)

    time.sleep(5)
    limpar_console()

    escrever_lentamente("    Boa Sorte, Detetive! ", espacosEsquerda = 4)
    escrever_lentamente("    Use seu instinto, raciocínio lógico e sua habilidade de ler nas entrelinhas. Boa sorte em resolver o mistério e trazer justiça à vila! ", espacosEsquerda = 4)
    escrever_lentamente("    Preparada? O jogo está prestes a começar! ", espacosEsquerda = 4)
    
    time.sleep(2)

# funções das fases
def fase1():
    limpar_console()
    escrever_lentamente("    No reino de Elindor, uma pequena vila medieval é abalada por um assassinato brutal. No coração da vila, em uma estalagem afastada e de má fama, um corpo foi encontrado, sem vida e envolto em mistérios. ", espacosEsquerda = 4)
    escrever_lentamente("\n   Você é uma investigadora conhecida apenas como Samanta, uma mulher de passado nebuloso e com fama de resolver casos impossíveis. Você não é considerada uma nobre, mas também não é uma plebéia. Suas memórias estão fragmentadas, sua cabeça lateja com uma dor intensa e seu corpo, ainda que forte, parece envolto em uma névoa de cansaço e fadiga depois de ter passado uma noite nos bosques, aproveitando a breve folga que teve após desvendar outro caso estressante. ", espacosEsquerda = 4)
    mostrar_imagem("../data/samanta.webp")
    time.sleep(3)
    limpar_console()
    
    escrever_lentamente("    Samanta estava sentada à sombra de um velho carvalho quando a chamaram. Uma jovem aldeã com olhos preocupados segurava o manto de lã com força, fitando-a com desconfiança. Ela sabia quem Samanta era. ", espacosEsquerda = 4)
    escrever_lentamente("\n   — Preciso que venha comigo... há algo que precisa ver — disse a jovem, quase em um sussurro. Ela parecia assusstada. ", espacosEsquerda = 4)
    escrever_lentamente("\n   A dor na cabeça de Samanta, que a acompanhava desde que ela acordou nos campos aquele dia, latejou novamente. Ela olhou para a jovem e assentiu, ignorando o desconforto. Ambas caminharam em silêncio até a velha estalagem 'O Corvo e a Espada', um lugar mal-afamado, onde poucos nobres ousavam pisar. ", espacosEsquerda = 4)
    escrever_lentamente("\n   Assim que ambas cruzaram a soleira, o cheiro de sangue atingiu Samanta como um golpe. No centro do salão estava o corpo: Baldwin, o Ferreiro, um velho conhecido dela, ainda que não exatamente próximo. Ele jazia no chão, com um corte profundo no peito e marcas de luta pelos braços e rosto. A morte parecia ter ocorrido quando Baldwin, fazendo um bico de bartender, estava próximo de fechar o estabelecimento. Samanta se abaixou para observar os detalhes, já sabendo o motivo de eles desejaram a presença dela ali: eles queriam que ela descobrisse quem o matou e, se possível, o motivo disso. Samanta observou, vagamente, os arredores da estalagem que, de tempos em tempos, visitava. Era como se cada canto da estalagem, cada sombra, guardasse um fragmento esquecido de seu próprio passado. ", espacosEsquerda = 4)
    escrever_lentamente("\n   Enquanto analisava a cena, Samanta encontrou cinco pistas principais: ", espacosEsquerda = 4)
    escrever_lentamente("\n   - Uma faca de lâmina fina: cravada na madeira próxima ao corpo, sua lâmina estava levemente torta, indicando uma luta. Mas a faca não parecia algo que Baldwin, o Ferreiro, usaria. Talvez fosse um item de cozinha ou de um caçador? ", espacosEsquerda = 4)
    escrever_lentamente("\n   - Marcas de pegadas: algumas pareciam frescas, vindas da direção da porta dos fundos, enquanto outras eram mais confusas. ", espacosEsquerda = 4)
    escrever_lentamente("\n   - Fragmentos de pano vermelho: próximos ao corpo, havia pedaços de tecido fino e vermelho, bem diferente das vestes grosseiras que Baldwin usava. ", espacosEsquerda = 4)
    escrever_lentamente("\n   - Uma garrafa quebrada: estilhaçada próxima ao corpo, um cheiro doce e forte exalava do líquido derramado. Provavelmente algum licor caro que só alguém com poder ou influência teria acesso. ", espacosEsquerda = 4)
    escrever_lentamente("\n   Com essas pistas em mente e com o relato de que o corpo foi achado ao amanhecer, Samanta faz uma lista mental dos principais suspeitos que ela já consegue reunir e se prepara para os interrogatórios dos dias que viriam. Cada pista levaria a uma fase de investigação com diferentes indivíduos. Seriam eles: ", espacosEsquerda = 4)
    
    time.sleep(2)
    limpar_console()
    
    mostrar_imagem("../data/isolde.webp")  # exibe a imagem de Samanta
    escrever_lentamente("     - Isolde, a Cozinheira da Estalagem: uma mulher de porte robusto, com braços fortes e mãos marcadas pelo manuseio constante de facas e panelas. Sua expressão é dura e suas sobrancelhas cerradas passam um ar de desconfiança e irritação. Ela veste um avental de tecido grosso e velho, levemente manchado, indicando as longas horas que passa na cozinha da estalagem. Isolde raramente sorri e seu olhar afiado parece cortar tão fundo quanto as facas que ela domina. Murmura-se que, apesar de seu temperamento difícil, Isolde tem um coração bondoso, mas que ela é conhecida por sua hostilidade com homens desordeiros, especialmente Baldwin, com quem já teve discussões acaloradas acerca de sua reputação e seu modo de lidar com suas hóspedes femininas. ", espacosEsquerda = 4)
    mostrar_imagem("../data/calistus.webp")  # exibe a imagem de Calistus
    escrever_lentamente("\n   - Calistus, o Caçador: um homem magro e ágil, com olhos afiados como os de uma raposa. Ele usa uma capa marrom suja de terra e folhas, sugerindo que passou a maior parte do dia na floresta. Ele sempre carrega uma pequena faca de caça presa ao cinto e suas botas estão cobertas de lama seca. Calistus evita contato visual e parece estar sempre inquieto, como se estivesse pronto para desaparecer na floresta a qualquer instante. Embora reservado, os aldeões o respeitam por seu conhecimento das matas e de tudo o que vive nelas, mas sua relação com Baldwin, o ferreiro, era tensa, pois Baldwin costumava atrapalhar seus negócios com armas e mexer com sua esposa de tempos em tempos. ", espacosEsquerda = 4)
    mostrar_imagem("../data/mariana.webp")  # exibe a imagem de Mariana
    escrever_lentamente("\n   - Mariana, a Donzela da Estalagem: uma jovem de aparência delicada, com cabelos castanhos trançados e um vestido simples, embora bem cuidado. Ela é ágil e discreta, movendo-se com a graça de alguém acostumada a servir e a observar em silêncio. Mariana tem um semblante nervoso e seus dedos finos se retorcem enquanto fala, o que sugere que algo a preocupa profundamente. Rumores dizem que Baldwin dava alguns avanços indesejados nela, mas que ela nunca deu indicíos de desprezá-lo. Foi ela quem encontrou o corpo de Baldwin quando entrou na estalagem, cuja porta estava destrancada, pela manhã. ", espacosEsquerda = 4)
    mostrar_imagem("../data/gerhard.webp")  # exibe a imagem de Gerhard
    escrever_lentamente("\n   - Gerhard, o Guardião da Vila: com uma expressão carrancuda e um corpo grande e musculoso, Gerhard é a imagem do típico guardião. Suas roupas de couro grosso e suas mãos calejadas mostram que está acostumado a trabalhos pesados. Ele usa uma barba bem aparada, e seus olhos severos revelam uma autoridade silenciosa, que poucos ousam questionar. Gerhard é direto e econômico nas palavras, falando apenas o necessário. Ele é conhecido por sua lealdade, mas também por seu comportamento discreto e relutante em se envolver em questões alheias. Mais de uma vez, já entrou em brigas e discussões com Baldwin pelo mesmo não respeitar as mulheres. Foi ele quem, após socorrer uma Mariana desesperada, mandou a jovem estranha encontrar Samanta. ", espacosEsquerda = 4)
    mostrar_imagem("../data/morgana.webp")  # exibe a imagem de Morgana
    escrever_lentamente("\n   - Madame Morgana, a Nobre da Vila: uma mulher de porte elegante, de pele pálida e cabelos loiros finamente arrumados. Veste-se com roupas de linho vermelho e jóias discretas e é sempre vista com uma postura altiva e fria. Madame Morgana raramente interage com os aldeões e poucos ousam se aproximar dela. Seus olhos calculistas analisam cada movimento das pessoas ao seu redor, como se tentassem prever cada pergunta. Aparentemente, Morgana guarda rancores, principalmente de Baldwin, por motivos que ninguém suspeita do porquê. ", espacosEsquerda = 4)
    mostrar_imagem("../data/floris.webp")  # exibe a imagem de Calistus
    escrever_lentamente("\n   - Floris, o Balcosnista: um homem robusto, com braços fortes e calejados pelo trabalho constante nas tavernas e armazéns. Ele veste roupas simples de couro marrom, manchadas por anos de manipulação de barris de vinho e licores. Uma túnica de linho grosso cobre seu peito e uma faixa de tecido vermelho em torno da cintura sugere um toque pessoal de orgulho em seu ofício. Seu cabelo é curto e escuro, já mostrando sinais de grisalho nas têmporas e uma barba rala cobre seu queixo, sempre perfumada pelo leve aroma de especiarias e álcool. O licor encontrado junto ao corpo de Baldwin provém de seus negócios. ", espacosEsquerda = 4)
    time.sleep(3)
    limpar_console()

    escrever_lentamente("     Uma investigação em torno da faca será o primeiro passo que Samanta tomará. Dentre os suspeitos que ela já reuniu pistas, somente dois podem ser ligados à lâmica: Isolde, a Cozinheira, Calistus, o Caçador. ", espacosEsquerda = 4)
    time.sleep(3)
    limpar_console()
    interrogar1()
    pass 

def fase2():
    limpar_console()
    escrever_lentamente("     Após o interrogatório inicial, Samanta reflete sobre o que descobriu. Isolde e Calistus, os dois que lidavam com facas, mostraram reações diferentes. Isolde admitiu ter tido conflitos com Baldwin, e sua irritação ficou evidente, embora ela aparentemente não reconhecesse a faca. Já Calistus, que parecia mais cauteloso, também confessou um histórico de desavenças com o ferreiro, embora insistisse que aquele tipo de faca não era seu. As suas suspeitas se intensificam enquanto Samanta se recorda que a lâmina parecia fina, mais próxima de uma faca de cozinha do que de uma arma de caça. ", espacosEsquerda = 4)
    escrever_lentamente("\n    Independentemente disso, as pegadas são o próximo passo a ser investigado; Samanta decide que a próxima investigação será sobre as pegadas próximas à porta dos fundos e que estavam próximos do estabelecimento pela manhã. Dentre os suspeitos que ela já reuniu pistas, as próximas pessoas que Samanta irá investigar serão: Mariana, a Donzela, e Gerhard, o Guardião. ", espacosEsquerda = 4)
    
    time.sleep(3)
    limpar_console()
    interrogar2()
    pass

def fase3():
    limpar_console()
    escrever_lentamente("     Após conversar com Mariana e Gerhard, Samanta recolheu mais informações sobre as pegadas na porta dos fundos. Mariana menciona ter visto uma figura saindo apressadamente, mas não conseguiu ver detalhes. Gerhard, mesmo hesitante, confirma ter avistado alguém encapuzado saindo com algo nas mãos, mas reluta em dar mais detalhes por não ter confiança em suas lembranças. ", espacosEsquerda = 4)
    escrever_lentamente("\n   As pegadas eram pequenas e leves. Como Samanta sente que está esquecendo detalhes importantes, ela decide seguir a próxima pista: os fragmentos de pano vermelho, o que a leva à figura imponente de Madame Morgana. ", espacosEsquerda = 4)
    
    time.sleep(3)
    limpar_console()
    interrogar3()
    pass 

def fase4():
    limpar_console()
    escrever_lentamente("     Após conversar com Madame Morgana, que é fria e altiva em suas respostas, Samanta decide seguir adiante com suas investigações. ", espacosEsquerda = 4)
    escrever_lentamente("\n   A cor e a qualidade do tecido apontam para alguém de recursos ou posição elevada. Independentemente disso, no entanto, Samanta decide que é hora de investigar a garrafa quebrada e o licor, que talvez possa levá-la a mais informações sobre a possível conexão de Morgana ou outra pessoa com Baldwin. É hora de interrogar a figura simples de Floris, o Balconista. ", espacosEsquerda = 4)
    
    time.sleep(3)
    limpar_console()
    interrogar4()
    pass

def fase5():
    limpar_console()
    escrever_lentamente("\n    Finalmente, com todas as peças do quebra-cabeças reunidas, Samanta percebe que chegou a hora de escolher um assassino. Ela sente que cada detalhe aponta para uma verdade oculta e a dor de cabeça lateja como um tambor de advertência. ", espacosEsquerda = 4)

    time.sleep(3)
    limpar_console()
    interrogar5()
    pass