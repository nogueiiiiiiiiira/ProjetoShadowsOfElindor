import os
from game.interacoes import interrogar_personagensFase1, interrogar_personagensFase2, interrogar_personagensFase3, interrogar_personagensFase4
from game.utils import escrever_lentamente
import time
 

# Funções das fases
def fase1():
    os.system("cls")
    escrever_lentamente("O corpo de Baldwin, o cozinheiro real, foi encontrado próximo ao castelo, envolto por uma aura de mistério e temor que rapidamente se espalhou por todo o reino. A tragédia abalou profundamente o rei Edgar III, que, tomado pela dor e pela urgência de justiça, convocou Samanta, a investigadora mais habilidosa da corte, para solucionar o caso. Com o semblante sombrio, o rei deu a ordem: ela teria apenas três dias para desvendar o assassino.\n\n")
    escrever_lentamente("No entanto, Samantha estava cansada e estranhamente dolorida. As noites de investigação se acumulavam, e cada detalhe do dia lhe escapava como água entre os dedos. Fazia poucos minutos desde que ela foi arrastada rudemente de sua cama, onde sonhava com o calor de uma lareira, para a cena do crime. A lembrança do sonho se dissipou rapidamente, e, ao abrir os olhos, tudo o que conseguiu focar e lembrar foi no caso que lhe foi atribuído, um fardo pesado que a mantinha em movimento, mesmo quando suas forças começavam a falhar. Um gosto metálico e o residual de chá estavam presentes em sua boca, como um lembrete das horas que passou imersa em investigações anteriores. Sua camisa estava manchada de tinta vermelha, embora ela não se lembrasse exatamente do que aconteceu para ficar assim.\n\n")
    escrever_lentamente("Ela encarou o corpo de Baldwin, ainda estendido no chão. As mãos dela estavam sujas de sangue, um testemunho sombrio de que ela havia tocado o corpo em busca de indícios sobre sua morte. Era uma cena que poderia desestabilizar qualquer um, mas Samantha se forçou a se manter firme. Analisando o cadáver, ela notou sinais claros de uma luta: o cozinheiro havia bebido algo antes de sua morte, e seu corpo apresentava marcas de um conflito físico, uma luta desesperada pela vida. Finalmente, o que mais a chocou foi a facada na barriga, um golpe fatal que confirmava a brutalidade do ato. Naquele momento, a arma do crime ainda não havia sido encontrada, mas Samantha sabia que cada segundo era precioso.\n\n")
    escrever_lentamente("Com o peso do tempo se esvaindo e o pânico crescendo entre os súditos, Samantha se viu diante de cinco suspeitos, cada um mais intrigante que o outro:\n\n")
    escrever_lentamente("- Padre Calistus: Um homem de fé, mas cuja devoção rígida parecia esconder segredos sombrios.\n")
    escrever_lentamente("- Floris, o Bobo da Corte: Sempre com uma piada pronta, mas seu comportamento excêntrico escondia algo desconcertante.\n")
    escrever_lentamente("- Bram, o Ferreiro: Famoso por sua força e habilidades, mas também por seu temperamento explosivo e imprevisível.\n")
    escrever_lentamente("- Gerhard, o Carrasco: Um homem familiarizado com a morte, cuja frieza era tão afiada quanto seu machado.\n")
    escrever_lentamente("- Lady Isolde: A bela e distante esposa de Baldwin, cujo luto parecia carregar mais que simples tristeza.\n")
    escrever_lentamente("- Morganna, a Curandeira: Uma figura enigmática, conhecida por seus remédios milagrosos, e que tinha uma verruga proeminente no nariz e olhos que pareciam enxergar além das aparências.\n\n")
    escrever_lentamente("O tempo corria como areia fina pelos dedos de Samantha, enquanto a sombra do prazo imposto pelo rei pairava sobre ela, pesada como um manto. Cada suspeito carregava um motivo oculto, uma história enterrada em seu passado, e, talvez, a chave para a verdade. A investigadora sabia que a solução do crime não traria apenas justiça para Baldwin, mas poderia ser crucial para salvar o reino de algo maior – forças invisíveis que rondavam o castelo e ameaçavam não apenas sua missão, mas sua própria vida.\n\n")
    escrever_lentamente("Agora, mais do que nunca, Samanta precisava escolher em quem confiar, desmascarar mentiras e enfrentar os segredos que se entrelaçavam à medida que o tempo se esgotava. O verdadeiro assassino poderia estar mais próximo do que ela imaginava – e um passo em falso poderia custar não só o sucesso da investigação, mas a segurança de todo o reino.\n")

    time.sleep(5)
    os.system("cls")
    interrogar_personagensFase1()
    pass

# Início do jogo
def fase2():
    time.sleep(5)
    os.system("cls")
    
    escrever_lentamente("Depois das primeiras interrogações, Samanta conseguiu a permissão do Rei para investigar a cozinha por si só, na esperança de encontrar algo que a levasse adiante em suas investigações, sem que outros a atrapalhassem. Agora, abandonada e repleta de vestígios de uma rotina abruptamente interrompida, a cozinha a encarava silenciosa. Samanta se perguntou, silenciosamente, onde ela esconderia uma faca se fosse um assassino correndo contra o tempo.\n")
    escrever_lentamente("Afinal, dado como o crime foi cometido durante um horário em que ainda havia pessoas perambulando pelos corredores, era evidente que o ato não foi pensado de antemão; algo ocorreu de forma inesperada e em um momento de desespero. De repente, tendo uma ideia, um presságio, Samanta se aproximou de determinado local. Entre facas mal guardadas e panelas esquecidas, uma faca quebrada chamou sua atenção.\n")
    escrever_lentamente("A lâmina, partida próximo ao cabo, parecia ter se rompido recentemente. Não havia ferrugem, e a fratura indicava que algo duro havia forçado a lâmina além de seu limite – como se tivesse sido usada com violência ou em um momento de pânico. A brutalidade do crime sugeria que o assassino não teve tempo ou oportunidade para planejar sua ação.\n\n")
    escrever_lentamente("Samanta pegou a faca com cuidado, examinando-a com o olhar treinado.\n")
    escrever_lentamente("O mais intrigante era que, apesar de ser um utensílio comum, não havia marcas de dedos visíveis no cabo.\n")
    escrever_lentamente("A ausência de impressões parecia quase proposital, como se o objeto tivesse sido cuidadosamente limpo.\n\n")
    escrever_lentamente("Quem limparia uma faca com tanto cuidado após usá-la? Isso indicava uma intenção clara: alguém queria apagar seus rastros.\n\n")
    escrever_lentamente("Enquanto analisava, Samanta não pôde deixar de pensar que aquilo era estranho.\n")
    escrever_lentamente("Os principais suspeitos não costumavam usar luvas – algo que ela achava um tanto bobo.\n")
    escrever_lentamente("O frio se intensificava a cada dia, e as manhãs já traziam o ar cortante típico do outono avançado.\n")
    escrever_lentamente("Ela mesma sempre usava luvas para se proteger do vento gelado. Por que eles não faziam o mesmo?\n")
    escrever_lentamente("Seria orgulho, descuido... ou uma tentativa deliberada de parecerem naturais?\n\n")
    escrever_lentamente("Com a faca quebrada nas mãos, Samanta começou a traçar algumas possibilidades.\n")
    escrever_lentamente("De acordo com conversas rápidas e observações cuidadosas entre os servos, três suspeitos tinham potencial ligação com facas:\n\n")
    escrever_lentamente("- Lady Isolde: Apesar de sua aparência refinada, era conhecida por um hábito incomum: gostava de cortar os cabelos dos homens e mulheres da corte.\n")
    escrever_lentamente("Para isso, precisava de lâminas afiadas, e, quem sabe, a faca encontrada pudesse ter pertencido a ela.\n\n")
    escrever_lentamente("- Floris, o Bobo da Corte: Floris era muito mais do que um simples palhaço.\n")
    escrever_lentamente("Praticava malabarismo com facas para manter suas habilidades afiadas e, às vezes, brincava nos corredores do castelo.\n")
    escrever_lentamente("Uma faca quebrada poderia ser tanto resultado de uma falha em seu treinamento quanto de algo mais sinistro.\n\n")
    escrever_lentamente("- Gerhard, o Carrasco: Acostumado a lidar com instrumentos afiados diariamente, Gerhard sempre carregava facas.\n")
    escrever_lentamente("A faca quebrada poderia ter sido dele – ou ter passado por suas mãos, dado seu conhecimento profundo sobre lâminas.\n\n")
    escrever_lentamente("Samanta passou o dedo pela superfície fria do cabo, pensativa.\n")
    escrever_lentamente("Por que não havia marcas de dedos? Será que o responsável havia usado uma luva apenas durante o crime?\n")
    escrever_lentamente("Ou, ainda mais intrigante, alguém poderia ter limpado a faca depois?\n")
    escrever_lentamente("Um detalhe quase imperceptível, mas que mudava toda a dinâmica da investigação. Um ato deliberado – não de impulso, mas de alguém que sabia exatamente o que estava fazendo.\n\n")
    escrever_lentamente("O quebra-cabeça ganhava mais peças, mas algumas continuavam fora de lugar.\n")
    escrever_lentamente("A faca quebrada era, ao mesmo tempo, uma pista promissora e uma distração perigosa.\n")
    escrever_lentamente("O responsável poderia estar por perto, escondido à vista de todos, e a cada minuto perdido, Samanta sentia o prazo do rei pesar mais em seus ombros.\n\n")
    escrever_lentamente("Agora, com a faca como chave para a verdade – ou uma armadilha cuidadosamente plantada – Samanta precisava descobrir:\n")
    escrever_lentamente("Quem a usou, por quê, e, acima de tudo, quem foi meticuloso o suficiente para apagar suas pegadas... e ainda assim deixar a faca para ser encontrada?\n")

    interrogar_personagensFase2()
    
    pass

def fase3():
    
    escrever_lentamente("Após as interrogações com Isolde, Gerhard e Floris, Samantha decide investigar o quarto de Baldwin e Lady Isolde, intrigada pelos rumores sobre o casamento conturbado do casal. Antes mesmo das especulações envolvendo Isolde e Bram surgirem, já era quase um segredo de estado que Baldwin tinha suas aventuras extraconjugais.")
    escrever_lentamente("Com cautela, ela adentra o ambiente, o cheiro suave de lavanda a envolve, mas uma sensação de desconforto a persegue. O quarto, embora bem decorado, parece carregar um peso emocional que a deixa inquieta.")
    escrever_lentamente("Enquanto examina a escrivaninha, seus olhos se deparam com uma pequena caixa de madeira, adornada com delicados entalhes. Curiosa, ela a abre, e um misto de excitação e apreensão a invade ao encontrar diversos bilhetes de amor, todos endereçados a Lady Isolde.")
    escrever_lentamente("Um dos bilhetes é particularmente apaixonado, suas palavras transbordando um desejo ardente e quase desesperado. Samantha se vê absorvida pela intensidade das declarações, refletindo sobre a profundidade da conexão que Isolde poderia ter tido com seu amante.")
    escrever_lentamente("Ela não pode deixar de se perguntar: quem seria o amante de Lady Isolde? E, ao descobrir a traição, será que Baldwin confrontou o rival com a mesma paixão que parecia transbordar dos bilhetes?")
    escrever_lentamente("Enquanto examina os bilhetes, fragmentos de conversas entre os servos ecoam em sua mente, revelando que Bram e Lady Isolde eram muito próximos.")
    escrever_lentamente("Com essa nova informação, Samantha percebe que os bilhetes podem ser a chave para entender o que realmente aconteceu na fatídica noite do assassinato. Uma rede de paixões e desilusões parece se formar diante dela, e ela precisa desvendar os segredos que todos tentam esconder.")
    escrever_lentamente("Determinada, Samantha decide que precisa confrontar o padre, na esperança de que ele possa ter recebido alguma confissão que lance luz sobre essa intrincada teia de amores e ciúmes. O destino de Isolde e a verdade sobre Baldwin dependem de suas próximas palavras.")

    interrogar_personagensFase3()
    pass

def fase4():
    escrever_lentamente("Depois de não obter muitas respostas sobre as cartas, Samantha decidiu investigar mais sobre Baldwin em si, focando em seu temperamento explosivo e possíveis desentendimentos com outros moradores do castelo.")
    escrever_lentamente("Em sua busca por informações, ela se lembra de sua conversa com o padre, que mencionou que Baldwin era, de fato, conhecido por seu comportamento explosivo. Essa revelação faz com que Samantha reflita sobre Floris, que havia insinuado que Baldwin costumava se forçar nas mulheres. Uma sensação de desconforto a invade ao perceber que, vagamente, Baldwin também havia tentado forçá-la em algumas ocasiões, embora sem sucesso.")
    escrever_lentamente("Com essas lembranças, uma dúvida começa a assolar sua mente. O que Bram havia dito a ela anteriormente, um pouco depois dela ter o dispensado — para cuidar de sua própria vida e observar onde realmente estava na noite do crime? A irritação a consome por um momento, mas ela não pode deixar de reconhecer que, na verdade, não se lembrava bem daquele dia. O que a incomodava ainda mais era o fato de que foi chamada logo após resolver outro mistério, e estava cheia de sangue por ter tocado o corpo de Baldwin.")
    escrever_lentamente("Embora a memória fosse turva e um pouco desgostosa, um pensamento perturbador se forma: seria possível que Bram e Lady Isolde tivessem conspirado juntos para a morte de Baldwin? Essa hipótese a inquieta, mas ela ainda não consegue conectar todos os pontos, deixando-a numa confusão crescente.")
    escrever_lentamente("Determinada a desvendar a verdade, Samantha sabe que precisará conversar com Morgana, a curandeira que tratava de seus ferimentos e dava chás para seu temperamento; Floris, que sabe tudo de todo mundo; e o Carrasco, que, apesar de seu gênio difícil, sempre tinha algo a dizer.")
    interrogar_personagensFase4()
    pass

def fase5():
    escrever_lentamente("Samantha se senta em um canto da cozinha, perdida em pensamentos sobre as revelações que ouviu de Morgana. A curandeira mencionou que alguns de seus chás foram roubados na noite do assassinato. Chás bons, com sabor de ervas relaxantes, que ajudavam a manter a calma em momentos de tensão. O que teria acontecido com eles?")
    escrever_lentamente("Enquanto reflete sobre isso, um peso começa a se acumular em seu coração. A lembrança do relacionamento de Lady Isolde a faz sentir um misto de compaixão e indignação. Isolde, presa em um casamento repleto de abusos e desentendimentos, parece ser uma vítima nas circunstâncias. No entanto, essa empatia a leva a uma conclusão alarmante: será que a dor de Isolde a incrimina ainda mais?")
    escrever_lentamente("Samantha não pode ignorar que o desespero e a busca por liberdade poderiam ter levado Lady Isolde a se envolver com Bram, especialmente quando percebe que, naquele momento, os dois estavam claramente em um caso. A traição se entrelaça na dor, e as sombras da culpa começam a se formar ao redor de todos os envolvidos.")
    escrever_lentamente("Com a mente agitada, ela se pergunta: o que motivou essa traição? Seria um plano para escapar das garras de Baldwin? Ou será que Bram, em sua própria busca por poder e controle, também estava envolvido em algo muito mais sinistro?")
    escrever_lentamente("As peças do quebra-cabeça começam a se encaixar, mas Samantha ainda não consegue ver a imagem completa. O fato de que os chás calmantes desapareceram e a natureza tumultuada do casamento de Isolde se tornam questões cruciais em sua investigação, ligando os três de uma maneira que ela nunca imaginou.")
    escrever_lentamente("Determinada a descobrir a verdade, Samantha levanta-se e deixa esses questionamentos para trás, decidida, por enquanto, a confrontar o Padre e Bram sobre os chás e achar qualquer outra pista que possa ajudar a desvendar o emaranhado de relações que culminou naquela noite fatídica. Suas opiniões sobre Bram e Lady Isolde já estão formadas.")
    pass

def fase6():
    escrever_lentamente("Samantha observa a faca quebrada na mesa, sem impressões digitais visíveis. A lâmina brilha à luz fraca, mas o que mais a intriga é o mistério que a cerca. Diversas possibilidades começam a se formar em sua mente.")
    escrever_lentamente("Ela considera a ideia de que Morgana poderia ter envenenado Baldwin, usando bebidas que o levariam à loucura. A imagem de Baldwin, consumido pela fúria, é perturbadora; poderia ele mesmo ter se matado nesse estado? Essa teoria a assusta, mas parece plausível.")
    escrever_lentamente("Enquanto os pensamentos se entrelaçam, Samantha também não pode ignorar o que Lady Isolde e Bram poderiam ter feito. O desejo de viver juntos, longe da sombra do marido abusivo, poderia ter sido um forte motivador para que eles se unissem em um ato desesperado.")
    escrever_lentamente("E o Carrasco? Samantha se lembra das dívidas que Baldwin acumulou e como isso poderia tê-lo colocado em perigo. O Carrasco, ao sentir que sua reputação estava em jogo, poderia ter visto no assassinato uma solução para seus próprios problemas.")
    escrever_lentamente("Contudo, um único detalhe não se encaixa: a possível luva que o assassino pode ter usado. Nenhum dos suspeitos costuma usar luvas em suas ocupações; Floris, o Bobo da Corte, têm ofícios que exigem o toque das mãos, seja em combate ou na performance. O Carrasco também não usaria luvas, considerando sua natureza brutal e direta.")
    escrever_lentamente("Samantha se sente frustrada. Essa incongruência a perturba. Por que alguém usaria luvas em uma situação tão íntima e caótica? O assassinato na cozinha não foi, de forma alguma, planejado, então como o assassino poderia ter pensado em esconder as impressões digitais com uma morte tão impensada? Tudo o que Samanta pode concluir é que o assassino deveria usar luvas diariamente, mas  nenhum dos suspeitos usam luvas...")
    escrever_lentamente("Com a mente agitada, ela percebe que nem todos os pontos da morte de Baldwin podem ser interligados, não com o pouco tempo que lhe foi dado. De qualquer forma, no entanto, ela já tomou a decisão de quem ela acha que o assassino é.")
    pass

