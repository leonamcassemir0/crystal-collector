# 🍎 Coletor de Maçãs

## 📋 Descrição do Projeto

**Coletor de Maçãs** é um jogo 2D desenvolvido em Python utilizando a biblioteca Pygame. O jogador controla uma cesta que deve coletar maçãs que caem do topo da tela, evitando que elas toquem o chão para não perder vidas.

Este projeto foi desenvolvido como trabalho acadêmico para a disciplina de **Lógica de Programação**, demonstrando conceitos fundamentais de programação como estruturas condicionais, loops, orientação a objetos, manipulação de eventos e lógica de jogos.

## 🎯 Objetivo do Jogo

O objetivo é **coletar o maior número possível de maçãs** que caem da parte superior da tela, movimentando uma cesta horizontalmente na parte inferior. O jogo se torna progressivamente mais desafiador conforme o jogador acumula pontos.

### Regras:
- ✅ Colete maçãs para ganhar pontos
- ❤️ Você possui 3 vidas
- ⚠️ Perde uma vida quando uma maçã toca o chão
- 📈 A cada 40 pontos coletados, mais maçãs aparecem simultaneamente
- 🚀 A velocidade das maçãs aumenta conforme a pontuação
- ⚡ Use a tecla ESPAÇO para acelerar a cesta (velocidade aumenta com os pontos)

## 🕹️ Controles

| Tecla | Ação |
|-------|------|
| `←` `→` | Mover a cesta para esquerda/direita |
| `ESPAÇO` | Acelerar movimento da cesta |
| `ENTER` | Iniciar jogo / Confirmar |
| `H` | Abrir ajuda |
| `R` | Reiniciar após fim de jogo |
| `ESC` | Sair do jogo |

## 🛠️ Tecnologias Utilizadas

### Linguagem
- **Python 3.x** - Linguagem principal do projeto

### Bibliotecas
- **Pygame** - Biblioteca para desenvolvimento de jogos 2D
- **Random** - Geração de números aleatórios para posicionamento das maçãs
- **Sys** - Controle de sistema para encerramento do programa

### Recursos Gráficos
- **Imagens PNG** - Sprites da cesta (`cesta.png`) e maçã (`maca.png`)
- **Fontes do sistema** - Renderização de textos e interface

## 🎮 Funcionalidades Implementadas

### 1. **Sistema de Classes (POO)**
- **Classe Jogador**: Representa a cesta controlável
- **Classe Maca**: Representa as maçãs que caem

### 2. **Interface Completa**
- Tela inicial com menu de opções
- Tela de ajuda com instruções detalhadas
- Tela de fim de jogo com opção de reiniciar
- HUD durante o jogo (pontos, tempo, vidas)

### 3. **Sistema de Progressão**
- Dificuldade crescente baseada na pontuação
- Aumento gradual da velocidade das maçãs
- Sistema de boost progressivo para a cesta
- Geração escalonada de múltiplas maçãs

### 4. **Mecânicas de Jogo**
- Detecção de colisão precisa
- Sistema de vidas com game over
- Controle de velocidade variável
- Geração procedural de obstáculos

### 5. **Otimizações**
- Delay independente entre maçãs múltiplas
- Remoção automática de objetos fora da tela
- Controle de frame rate constante (60 FPS)
- Prevenção de sobreposição de elementos

## 💡 Conceitos de Programação Aplicados

### 1. **Programação Orientada a Objetos**
- Encapsulamento de dados e métodos
- Herança e polimorfismo conceitual
- Abstração de entidades do jogo

### 2. **Estruturas de Controle**
- Loops infinitos para game loop
- Condicionais para lógica de jogo
- Estruturas de decisão para menu

### 3. **Manipulação de Eventos**
- Captura de entrada do teclado
- Processamento de eventos do sistema
- Estados de jogo controlados por eventos

### 4. **Algoritmos e Lógica**
- Detecção de colisão 2D
- Sistemas de pontuação progressiva
- Algoritmos de movimento e física básica

### 5. **Gerenciamento de Recursos**
- Carregamento e manipulação de imagens
- Controle de memória com remoção de objetos
- Otimização de performance

## 📊 Progressão do Jogo

### Fases da Dificuldade:
| Pontos | Maçãs Simultâneas | Velocidade Boost Cesta |
|--------|-------------------|------------------------|
| 0-39   | 1                 | 2.0x                  |
| 40-79  | 2                 | 2.3x                  |
| 80-119 | 3                 | 2.6x                  |
| 120+   | 4+                | 2.9x+                 |

### Sistema de Timing:
- **Intervalo base**: Novas maçãs a cada 3 segundos
- **Delay entre maçãs**: 0.5 segundos quando múltiplas
- **Boost progressivo**: +0.3x velocidade a cada 20 pontos

## 🎓 Objetivos Acadêmicos Alcançados

### Lógica de Programação:
- ✅ Implementação de algoritmos de controle
- ✅ Uso correto de estruturas condicionais e loops
- ✅ Desenvolvimento de lógica sequencial e paralela
- ✅ Resolução de problemas computacionais

### Boas Práticas:
- ✅ Código organizado seguindo PEP 8
- ✅ Documentação adequada com comentários
- ✅ Estruturação modular do projeto
- ✅ Nomenclatura clara de variáveis e funções

### Conceitos Avançados:
- ✅ Orientação a objetos aplicada
- ✅ Gerenciamento de estados do programa
- ✅ Implementação de game loop
- ✅ Otimização de performance

## 👨‍💻 Autor

Desenvolvido pelo aluno **Leonam Uirley do Nascimento Cassemiro** como trabalho acadêmico para a disciplina de **Lógica de Programação**.

## 📄 Licença

Este projeto foi desenvolvido para fins educacionais como parte do currículo acadêmico.

---

*Projeto desenvolvido com 💙 para demonstrar conceitos fundamentais de programação através de um jogo interativo e divertido.*
