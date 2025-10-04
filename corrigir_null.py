arquivo = "Analise_dados_Pousada.py"

with open(arquivo, "r", encoding="utf-8") as f:
    conteudo = f.read()

# Substituições de JSON -> Python
conteudo_corrigido = (
    conteudo.replace("null", "None")
            .replace("true", "True")
            .replace("false", "False")
)

with open(arquivo, "w", encoding="utf-8") as f:
    f.write(conteudo_corrigido)

print("Substituição concluída: null/true/false foram corrigidos para Python.")
