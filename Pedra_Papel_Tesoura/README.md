Pedra Papel Tesoura
Instruções
Faça um jogo de pedra, papel, tesoura.

Dentro do arquivo main.py, você encontrará a arte ASCII para os sinais de mão já salvos em uma variável correspondente: rocha, papel e tesoura. Isso facilitará a impressão do console.

Comece o jogo perguntando ao jogador:

"O que você escolhe? Tipo 0 para rock, 1 para papel ou 2 para tesoura."

A partir daí, você precisará descobrir:

Como você armazenará a entrada do usuário.
Como você gerará uma escolha aleatória para o computador.
Como você comparará a escolha do usuário e do computador para determinar o vencedor (ou um empate).
E também como você dará feedback ao jogador.
Você pode encontrar as regras "oficiais" do jogo no site da World Rock Paper Scissors Association.

Desafio de depuração
Tente executar este código e tipo 5.

Ele fornecerá um IndexError e apontará para a linha 32 como o problema.

Mas na linha 38 estamos tentando evitar uma falha detectando qualquer número grande ou igual a 3 ou menos que 0.

Então o que está acontecendo? Você pode depurar o código e consertá -lo?

Solução para o desafio de depuração