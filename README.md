# 🌒 Shadows of Elindor

## 🧩 Visão Geral do Projeto
**Shadows of Elindor** é um jogo de investigação baseado em terminal, ambientado em uma vila medieval mergulhada em mistérios. Você assume o papel de **Samanta**, uma detetive sagaz encarregada de solucionar um assassinato intrigante. Ao longo de **cinco fases investigativas**, você reunirá pistas, interrogará suspeitos e buscará revelar a verdade por trás do crime.

## 🛠️ Requisitos
- Python 3.x
- [`colorama`](https://pypi.org/project/colorama/) → `pip install colorama`
- [`windows-curses`](https://pypi.org/project/windows-curses/) (apenas no Windows) → `pip install windows-curses`
- [`prettytable`](https://pypi.org/project/prettytable/) → `pip install prettytable`
- [`matplotlib`](https://pypi.org/project/matplotlib/) → `pip install matplotlib`

## ▶️ Como Rodar
1. Certifique-se de ter o Python e os pacotes acima instalados.
2. Execute o jogo com:
```bash
python main.py
```
3. Utilize um terminal com pelo menos **80 colunas de largura** e **15 linhas de altura** para uma melhor experiência.

## 🎮 Jogabilidade
- O jogo inicia com uma introdução à história e ao ambiente medieval.
- Investigue o assassinato coletando pistas e interrogando suspeitos.
- Dividido em cinco fases, cada uma com novos desafios e personagens.
- Suas escolhas influenciarão diretamente o desfecho da história.
- Preste atenção a falas, expressões e detalhes narrativos sutis para desvendar o mistério.

## 📁 Estrutura de Pastas
```
Shadows/
│
├── main.py                 # Arquivo principal de execução do jogo
├── README.md               # Este arquivo
│
├── game/                   # Lógica do jogo
│   ├── fases.py            # Definição das fases e instruções
│   ├── interacoes.py       # Interações e interrogatórios
│   └── utils.py            # Funções auxiliares e utilitárias
│
└── data/                   # Arquivos de imagem usados no jogo
```

## ✅ Tabela-Verdade das Proposições

| Fase | Prop | Descrição | Valor | Importância |
|------|------|-----------|-------|-------------|
| 1 | P1 | A faca não pertence a Isolde, a cozinheira. | ✅ | Essencial |
| 1 | P2 | Calistus não gostava de Baldwin. | ✅ | Nenhuma |
| 1 | P3 | Isolde não gostava de Baldwin. | ✅ | Nenhuma |
| 1 | P4 | Apesar das intrigas, Calistus provavelmente não matou Baldwin. | ✅ | Essencial |
| 1 | P5 | Lâmina pequena sugere alguém de porte pequeno. | ✅ | Importante |
| 2 | P6 | Gerhard não está mentindo conscientemente. | ✅ | Essencial |
| 2 | P7 | Mariana não guarda rancor de Baldwin. | ✅ | Essencial |
| 2 | P8 | Pegadas pequenas indicam presença feminina. | ✅ | Importante |
| 2 | P9 | Os relatos se contradizem. | ✅ | Nenhuma |
| 2 | P10 | Devido à idade, não se pode confiar em Gerhard. | ❌ | Nenhuma |
| 3 | P11 | Tecido é da capa de Morgana — ela pode ser culpada. | ❌ | Nenhuma |
| 3 | P12 | Tecido caro sugere alguém de classe média/alta. | ✅ | Média |
| 3 | P13 | Morgana está na defensiva, mas não é culpada. | ✅ | Essencial |
| 3 | P14 | Relação de Morgana e Baldwin não era complicada. | ❌ | Nenhuma |
| 3 | P15 | Baldwin era violento e manipulador. | ✅ | Pouco |
| 4 | P16 | O licor foi adquirido por uma mulher. | ✅ | Nenhuma |
| 4 | P17 | Quem comprou o licor foi Morgana. | ✅ | Média |
| 4 | P18 | Floris não parece envolvido no crime. | ✅ | Essencial |
| 4 | P19 | Baldwin não usaria o licor de forma indevida. | ❌ | Nenhuma |
| 4 | P20 | O licor pode ser usado para dopar alguém. | ✅ | Nenhuma |

## 🧠 Conclusão

Para vencer o jogo, o jogador deve considerar como **verdadeiras** as proposições abaixo:
- **P1**, **P4**, **P6**, **P7**, **P13**

Essas proposições revelam que nenhum dos suspeitos se encaixa no perfil do assassino, levando à verdadeira conclusão do mistério. As demais proposições ajudam na ambientação e aprofundam a investigação, mas não afetam diretamente o final correto.

> **Conclusão lógica:** `(P1 ∧ P4 ∧ P6 ∧ P7 ∧ P13)`