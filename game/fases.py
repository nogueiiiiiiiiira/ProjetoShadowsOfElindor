import os
from game.interacoes import interrogar_personagensFase1, interrogar_personagensFase2, interrogar_personagensFase3, interrogar_personagensFase4, interrogar_personagensFase5
from game.utils import escrever_lentamente
import time
 

# Funções das fases
def fase1(atualizarGrafico):
    os.system("cls")
    
    escrever_lentamente("No reino de Castelon, uma pequena vila medieval é abalada por um assassinato brutal. No coração da vila, em uma estalagem afastada e de má fama, um corpo foi encontrado, sem vida e envolto em mistérios. Você, uma investigadora enigmática que raramente é vista, foi chamada para desvendar o caso. ", atualizarGrafico)
    escrever_lentamente("\nVocê é uma investigadora conhecida apenas como Samanta, uma mulher de passado nebuloso e com fama de resolver casos impossíveis. Você não é considerada uma nobre, mas também não é uma plebéia. Suas memórias estão fragmentadas, sua cabeça lateja com uma dor intensa e seu corpo, ainda que forte, parece envolto em uma névoa de cansaço e fadiga depois de ter passado uma noite nos bosques, aproveitando a breve folga que teve após desvendar outro caso estressante. ", atualizarGrafico)
    time.sleep(3)
    os.system("cls")
    
    escrever_lentamente("Samanta estava sentada à sombra de um velho carvalho quando a chamaram. Uma jovem aldeã com olhos preocupados segurava o manto de lã com força, fitando-a com desconfiança. Ela sabe quem Samanta era. O sol já se escondia entre as colinas, lançando uma luz alaranjada sobre os campos. ", atualizarGrafico)
    escrever_lentamente("\n— Preciso que venha comigo... há algo que precisa ver — disse a jovem, quase em um sussurro. Ela parecia assusstada. ", atualizarGrafico)
    escrever_lentamente("\nA dor na cabeça de Samanta, que a acompanhava desde que ela acordou nos campos aquele dia, latejou novamente. Ela olhou para a jovem e assentiu, ignorando o desconforto. Ambas caminharam em silêncio até a velha estalagem 'O Corvo e a Espada', um lugar mal-afamado, onde poucos nobres ousavam pisar. ", atualizarGrafico)
    escrever_lentamente("\nAssim que ambas cruzaram a soleira, o cheiro de sangue atingiu Samanta como um golpe. No centro do salão estava o corpo: Baldwin, o Ferreiro, um velho conhecido dela, ainda que não exatamente próximo. Ele jazia no chão, com um corte profundo no peito e marcas de luta pelos braços e rosto. A morte parecia ter ocorrido quando Baldwin, fazendo um bico de bartender, estava próximo de fechar o estabelecimento. Samanta se abaixou para observar os detalhes, já sabendo o motivo de eles desejaram a presença dela ali: eles queriam que ela descobrisse quem o matou e, se possível, o motivo disso. Samanta observou, vagamente, os arredores da estalagem que, de tempos em tempos, visitava. Era como se cada canto da estalagem, cada sombra, guardasse um fragmento esquecido de seu próprio passado. ", atualizarGrafico)
    escrever_lentamente("\nEnquanto analisava a cena, Samanta encontrou cinco pistas principais:", atualizarGrafico)
    escrever_lentamente("\nUma faca de lâmina fina: cravada na madeira próxima ao corpo, sua lâmina estava levemente torta, indicando uma luta. Mas a faca não parecia algo que Baldwin, o Ferreiro, usaria. Talvez fosse um item de cozinha ou de um caçador?", atualizarGrafico)
    escrever_lentamente("\nMarcas de pegadas: algumas pareciam frescas, vindas da direção da porta dos fundos, enquanto outras eram mais confusas. ", atualizarGrafico)
    escrever_lentamente("\nFragmentos de pano vermelho: próximos ao corpo, havia pedaços de tecido fino e vermelho, bem diferente das vestes grosseiras que Baldwin usava. ", atualizarGrafico)
    escrever_lentamente("\nUma garrafa quebrada: estilhaçada próxima ao corpo, um cheiro doce e forte exalava do líquido derramado. Provavelmente algum licor caro que só alguém com poder ou influência teria acesso. ", atualizarGrafico)
    escrever_lentamente("\nCom essas pistas em mente e com o relato de que o corpo foi achado ao amanhecer, Samanta faz uma lista mental dos principais suspeitos que ela já consegue reunir e se prepara para os interrogatórios dos dias que viriam. Cada pista levaria a uma fase de investigação com diferentes indivíduos. Seriam eles: ", atualizarGrafico)
    
    time.sleep(2)
    os.system("cls")
    
    escrever_lentamente("Diana, a Cozinheira da Estalagem: uma mulher de porte robusto, com braços fortes e mãos marcadas pelo manuseio constante de facas e panelas. Sua expressão é dura e suas sobrancelhas cerradas passam um ar de desconfiança e irritação. Ela veste um avental de tecido grosso e velho, levemente manchado, indicando as longas horas que passa na cozinha da estalagem. Diana raramente sorri e seu olhar afiado parece cortar tão fundo quanto as facas que ela domina. Murmura-se que, apesar de seu temperamento difícil, Diana tem um coração bondoso, mas que ela é conhecida por sua hostilidade com homens desordeiros, especialmente Baldwin, com quem já teve discussões acaloradas acerca de sua reputação e seu modo de lidar com suas hóspedes femininas. ", atualizarGrafico)
    escrever_lentamente("\nErik, o Caçador: um homem magro e ágil, com olhos afiados como os de uma raposa. Ele usa uma capa marrom suja de terra e folhas, sugerindo que passou a maior parte do dia na floresta. Ele sempre carrega uma pequena faca de caça presa ao cinto e suas botas estão cobertas de lama seca. Erik evita contato visual e parece estar sempre inquieto, como se estivesse pronto para desaparecer na floresta a qualquer instante. Embora reservado, os aldeões o respeitam por seu conhecimento das matas e de tudo o que vive nelas, mas sua relação com Baldwin, o ferreiro, era tensa, pois Baldwin costumava atrapalhar seus negócios com armas e mexer com sua esposa de tempos em tempos. ", atualizarGrafico)
    escrever_lentamente("\nMariana, a Donzela da Estalagem: uma jovem de aparência delicada, com cabelos castanhos trançados e um vestido simples, embora bem cuidado. Ela é ágil e discreta, movendo-se com a graça de alguém acostumada a servir e a observar em silêncio. Mariana tem um semblante nervoso e seus dedos finos se retorcem enquanto fala, o que sugere que algo a preocupa profundamente. Rumores dizem que Baldwin dava alguns avanços indesejados nela, mas que ela nunca deu indicíos de desprezá-lo. Foi ela quem encontrou o corpo de Baldwin quando entrou na estalagem, cuja porta estava destrancada, pela manhã. ", atualizarGrafico)
    escrever_lentamente("\nBoris, o Guardião da Vila: com uma expressão carrancuda e um corpo grande e musculoso, Boris é a imagem do típico guardião. Suas roupas de couro grosso e suas mãos calejadas mostram que está acostumado a trabalhos pesados. Ele usa uma barba bem aparada, e seus olhos severos revelam uma autoridade silenciosa, que poucos ousam questionar. Boris é direto e econômico nas palavras, falando apenas o necessário. Ele é conhecido por sua lealdade, mas também por seu comportamento discreto e relutante em se envolver em questões alheias. Mais de uma vez, já entrou em brigas e discussões com Baldwin pelo mesmo não respeitar as mulheres. Foi ele quem, após socorrer uma Mariana desesperada, mandou a jovem estranha encontrar Samanta. ", atualizarGrafico)
    escrever_lentamente("\nMadame Lavínia, a Nobre da Vila: uma mulher de porte elegante, de pele pálida e cabelos loiros finamente arrumados. Veste-se com roupas de linho vermelho e jóias discretas e é sempre vista com uma postura altiva e fria. Madame Lavínia raramente interage com os aldeões e poucos ousam se aproximar dela. Seus olhos calculistas analisam cada movimento das pessoas ao seu redor, como se tentassem prever cada pergunta. Aparentemente, Lavínia guarda rancores, principalmente de Baldwin, por motivos que ninguém suspeito do porquê. ", atualizarGrafico)
    escrever_lentamente("\nRodrigo, o Balcosnista: um homem robusto, com braços fortes e calejados pelo trabalho constante nas tavernas e armazéns. Ele veste roupas simples de couro marrom, manchadas por anos de manipulação de barris de vinho e licores. Uma túnica de linho grosso cobre seu peito e uma faixa de tecido vermelho em torno da cintura sugere um toque pessoal de orgulho em seu ofício. Seu cabelo é curto e escuro, já mostrando sinais de grisalho nas têmporas e uma barba rala cobre seu queixo, sempre perfumada pelo leve aroma de especiarias e álcool. O licor encontrado junto ao corpo de Baldwin provém de seus negócios. ", atualizarGrafico)
    
    time.sleep(3)
    os.system("cls")

    escrever_lentamente("Uma investigação em torno da faca será o primeiro passo que Samanta tomará. Dentre os suspeitos que ela já reuniu pistas, somente dois podem ser ligados à lâmica: Diana, a Cozinheira, e Erik, o Caçador. ", atualizarGrafico)
    time.sleep(3)
    os.system("cls")
    interrogar_personagensFase1(atualizarGrafico)
    pass 

def fase2(atualizarGrafico):
    os.system("cls")
    escrever_lentamente("Após o interrogatório inicial, Samanta reflete sobre o que descobriu. Diana e Erik, os dois que lidavam com facas, mostraram reações diferentes. Diana admitiu ter tido conflitos com Baldwin, e sua irritação ficou evidente, embora ela aparentemente não reconhecesse a faca. Já Erik, que parecia mais cauteloso, também confessou um histórico de desavenças com o ferreiro, embora insistisse que aquele tipo de faca não era seu. As suas suspeitas se intensificam enquanto Samanta se recorda que a lâmina parecia fina, mais próxima de uma faca de cozinha do que de uma arma de caça. ", atualizarGrafico)
    escrever_lentamente("\nIndependentemente disso, as pegadas são o próximo passo a ser investigado; Samanta decide que a próxima investigação será sobre as pegadas próximas à porta dos fundos e que estavam próximos do estabelecimento pela manhã. Dentre os suspeitos que ela já reuniu pistas, as próximas pessoas que Samanta irá investigar serão: Mariana, a Donzela, e Boris, o Guardião. ", atualizarGrafico)
    
    time.sleep(3)
    os.system("cls")
    interrogar_personagensFase2(atualizarGrafico)
    pass

def fase3(atualizarGrafico):
    os.system("cls")
    escrever_lentamente("Após conversar com Mariana e Boris, Samanta recolheu mais informações sobre as pegadas na porta dos fundos. Mariana menciona ter visto uma figura saindo apressadamente, mas não conseguiu ver detalhes. Boris, mesmo hesitante, confirma ter avistado alguém encapuzado saindo com algo nas mãos, mas reluta em dar mais detalhes por não ter confiança em suas lembranças. ", atualizarGrafico)
    escrever_lentamente("\nAs pegadas eram pequenas e leves. Como Samanta sente que está esquecendo detalhes importantes, ela decide seguir a próxima pista: os fragmentos de pano vermelho, o que a leva à figura imponente de Madame Lavínia. ", atualizarGrafico)
    
    time.sleep(3)
    os.system("cls")
    interrogar_personagensFase3(atualizarGrafico)
    pass

def fase4(atualizarGrafico):
    os.system("cls")
    escrever_lentamente("Após conversar com Madame Lavínia, que é fria e altiva em suas respostas, Samanta decide seguir adiante com suas investigações. ", atualizarGrafico)
    escrever_lentamente("\nA cor e a qualidade do tecido apontam para alguém de recursos ou posição elevada. Independentemente disso, no entanto, Samanta decide que é hora de investigar a garrafa quebrada e o licor, que talvez possa levá-la a mais informações sobre a possível conexão de Lavínia ou outra pessoa com Baldwin. É hora de interrogar a figura simples de Rodrigo, o Balconista. ", atualizarGrafico)
    
    time.sleep(3)
    os.system("cls")
    interrogar_personagensFase4(atualizarGrafico)
    pass

def fase5(atualizarGrafico):
    os.system("cls")
    escrever_lentamente("\nFinalmente, com todas as peças do quebra-cabeças reunidas, Samanta percebe que chegou a hora de escolher um assassino. Ela sente que cada detalhe aponta para uma verdade oculta e a dor de cabeça lateja como um tambor de advertência. ", atualizarGrafico)

    time.sleep(3)
    os.system("cls")
    interrogar_personagensFase5(atualizarGrafico)
    pass
