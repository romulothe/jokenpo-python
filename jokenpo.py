import random

# Opções do jogo
opcoes = ["pedra", "papel", "tesoura"]

# Regras: quem vence quem
# regras[a][b] = True significa que 'a' vence 'b'
regras = {
    "pedra": {"tesoura": True, "papel": False, "pedra": False},
    "papel": {"pedra": True, "tesoura": False, "papel": False},
    "tesoura": {"papel": True, "pedra": False, "tesoura": False},
}

def escolha_computador():
    return random.choice(opcoes)

def determinar_vencedor(jogador, computador):
    if jogador == computador:
        return "empate"
    elif regras[jogador][computador]:
        return "jogador"
    else:
        return "computador"

def exibir_placar(vitorias, derrotas, empates):
    print("\n📊 Placar:")
    print(f" Você: {vitorias} vitória(s)")
    print(f" Computador: {derrotas} vitória(s)")
    print(f" Empates: {empates}")

def jokenpo():
    print("=" * 40)
    print(" ✊ ✋ ✌️ JO KEN PO!")
    print("=" * 40)
    print("Escolhas disponíveis: pedra, papel, tesoura")
    print("Digite 'sair' para encerrar o jogo.\n")

    vitorias = 0
    derrotas = 0
    empates = 0

    while True:
        jogador = input("Sua escolha: ").strip().lower()

        if jogador == "sair":
            print("\nObrigado por jogar! Até a próxima. 👋")
            exibir_placar(vitorias, derrotas, empates)
            break

        if jogador not in opcoes:
            print("❌ Opção inválida! Escolha entre: pedra, papel ou tesoura.\n")
            continue

        computador = escolha_computador()
        print(f"💻 Computador escolheu: {computador}")

        resultado = determinar_vencedor(jogador, computador)

        if resultado == "empate":
            print("🤝 Empate!")
            empates += 1
        elif resultado == "jogador":
            print("🎉 Você venceu!")
            vitorias += 1
        else:
            print("😢 Computador venceu!")
            derrotas += 1

        exibir_placar(vitorias, derrotas, empates)
        print()

if __name__ == "__main__":
    jokenpo()