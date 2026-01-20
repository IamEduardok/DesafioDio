import csv


usuarios = []
with open("usuarios.csv", "r", encoding="utf-8") as arquivo_csv:
    leitor = csv.DictReader(arquivo_csv)
    for linha in leitor:
        usuarios.append(linha)


def gerar_mensagem(usuario):
    return (
        f"Olá, {usuario['Nome']}! 👋\n"
        f"Sua conta {usuario['Conta']} foi analisada com sucesso.\n"
        f"Cartão final {usuario['Cartao']}.\n"
        f"Aproveite nossos benefícios exclusivos!"
    )

mensagens = []
for usuario in usuarios:
    mensagens.append({
        "Nome": usuario["Nome"],
        "Mensagem": gerar_mensagem(usuario)
    })


with open("mensagens_usuarios.csv", "w", newline="", encoding="utf-8") as arquivo_saida:
    campos = ["Nome", "Mensagem"]
    escritor = csv.DictWriter(arquivo_saida, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(mensagens)

print("ETL finalizado com sucesso! Arquivo 'mensagens_usuarios.csv' criado.")

