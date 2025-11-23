# Sistema Inteligente de Recomendação de Filmes
# Simula um algoritmo de IA baseado em pontuação, preferências e perguntas ao usuário

import time

# Base de filmes com características
filmes = [
    {"titulo": "Matrix", "acao": 5, "drama": 1, "comedia": 0, "terror": 0, "ficcao": 5, "romance": 0},
    {"titulo": "Interestelar", "acao": 2, "drama": 4, "comedia": 0, "terror": 0, "ficcao": 5, "romance": 1},
    {"titulo": "John Wick", "acao": 5, "drama": 1, "comedia": 0, "terror": 0, "ficcao": 1, "romance": 0},
    {"titulo": "As Branquelas", "acao": 0, "drama": 0, "comedia": 5, "terror": 0, "ficcao": 0, "romance": 1},
    {"titulo": "Hereditário", "acao": 0, "drama": 2, "comedia": 0, "terror": 5, "ficcao": 0, "romance": 0},
    {"titulo": "O Exorcista", "acao": 0, "drama": 1, "comedia": 0, "terror": 5, "ficcao": 0, "romance": 0},
    {"titulo": "Clube da Luta", "acao": 2, "drama": 5, "comedia": 0, "terror": 0, "ficcao": 0, "romance": 0},
    {"titulo": "Diário de uma Paixão", "acao": 0, "drama": 4, "comedia": 1, "terror": 0, "ficcao": 0, "romance": 5},
]

preferencias_usuario = {
    "acao": 0,
    "drama": 0,
    "comedia": 0,
    "terror": 0,
    "ficcao": 0,
    "romance": 0
}

def resposta_sim_nao(pergunta):
    while True:
        resp = input(pergunta + " (s/n): ").lower()
        if resp in ["s", "n"]:
            return resp
        print("Resposta inválida. Digite 's' ou 'n'.")

def perguntar_preferencias():
    print("\n=== Sistema Inteligente de Recomendação ===")
    time.sleep(0.5)

    perguntas = {
        "acao": "Você gosta de filmes com muita ação?",
        "drama": "Você gosta de histórias profundas e dramáticas?",
        "comedia": "Você prefere filmes engraçados?",
        "terror": "Você gosta de filmes assustadores?",
        "ficcao": "Você gosta de ficção científica?",
        "romance": "Você gosta de histórias de amor?"
    }

    print("\nResponda algumas perguntas para calibrar o sistema:")
    time.sleep(0.5)

    for categoria, pergunta in perguntas.items():
        resp = resposta_sim_nao(pergunta)
        if resp == "s":
            preferencias_usuario[categoria] += 3
        else:
            preferencias_usuario[categoria] -= 1

def pontuar_filmes():
    for filme in filmes:
        score = 0
        for categoria in preferencias_usuario:
            score += filme[categoria] * preferencias_usuario[categoria]
        filme["score"] = score

def recomendar():
    print("\n🔍 Analisando suas preferências...", end="")
    time.sleep(1)
    print(" pronto!\n")

    filmes_ordenados = sorted(filmes, key=lambda x: x["score"], reverse=True)
    melhor = filmes_ordenados[0]

    print(f"🎬 Filme recomendado: **{melhor['titulo']}**")
    print("\n🧠 Motivos da recomendação:")
    for categoria in preferencias_usuario:
        if melhor[categoria] > 0:
            print(f"- Combina bem com seu gosto por **{categoria}** ({melhor[categoria]} pontos)")

    print(f"\n📌 Score total: {melhor['score']}")

def main():
    perguntar_preferencias()
    pontuar_filmes()
    recomendar()

main()
