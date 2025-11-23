
# Recomendador simples de filmes usando uma lógica de IA baseada em regras

def recomendar_filme(genero):
    genero = genero.lower()

    filmes = {
        "ação": ["John Wick", "Mad Max: Fury Road", "Gladiador"],
        "comédia": ["Gente Grande", "As Branquelas", "Superbad"],
        "terror": ["Invocação do Mal", "Hereditário", "O Exorcista"],
        "drama": ["À Procura da Felicidade", "O Pianista", "Clube da Luta"],
        "ficção": ["Interestelar", "Matrix", "Duna"],
        "romance": ["Como Eu Era Antes de Você", "Diário de uma Paixão", "La La Land"]
    }

    if genero in filmes:
        print(f"\n🎬 Recomendações para gênero '{genero}':")
        for filme in filmes[genero]:
            print(f"- {filme}")
    else:
        print("\n❌ Gênero não encontrado.")
        print("Tente: ação, comédia, terror, drama, ficção ou romance.")


print("=== Recomendador Inteligente de Filmes ===")
genero_usuario = input("Digite um gênero de filme: ")
recomendar_filme(genero_usuario)
