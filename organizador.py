import os
import shutil
from pathlib import Path

# Mapeia categorias de pastas para as extensões de arquivo correspondentes
CATEGORIAS = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documentos": [".pdf", ".doc", ".docx", ".txt", ".odt", ".rtf"],
    "Planilhas": [".xls", ".xlsx", ".csv", ".ods"],
    "Apresentacoes": [".ppt", ".pptx", ".odp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "Audios": [".mp3", ".wav", ".flac", ".aac", ".ogg"],
    "Compactados": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Executaveis": [".exe", ".msi", ".apk", ".dmg"],
    "Codigo": [".py", ".js", ".html", ".css", ".java", ".c", ".cpp", ".json"],
}


def obter_categoria(extensao):
    """Retorna o nome da categoria correspondente à extensão, ou
    'Outros' se não estiver mapeada."""
    extensao = extensao.lower()
    for categoria, extensoes in CATEGORIAS.items():
        if extensao in extensoes:
            return categoria
    return "Outros"


def organizar_pasta(caminho_pasta):
    pasta = Path(caminho_pasta)

    if not pasta.is_dir():
        print(f"Erro: '{caminho_pasta}' não é uma pasta válida.")
        return

    arquivos_movidos = 0

    for item in pasta.iterdir():
        # Ignora subpastas (inclusive as que o próprio script cria)
        if item.is_dir():
            continue

        categoria = obter_categoria(item.suffix)
        pasta_destino = pasta / categoria
        pasta_destino.mkdir(exist_ok=True)

        destino = pasta_destino / item.name

        # Evita sobrescrever arquivos com o mesmo nome
        if destino.exists():
            contador = 1
            novo_nome = f"{item.stem}_{contador}{item.suffix}"
            while (pasta_destino / novo_nome).exists():
                contador += 1
                novo_nome = f"{item.stem}_{contador}{item.suffix}"
            destino = pasta_destino / novo_nome

        shutil.move(str(item), str(destino))
        print(f"Movido: {item.name} -> {categoria}/")
        arquivos_movidos += 1

    if arquivos_movidos == 0:
        print("Nenhum arquivo para organizar. A pasta já está organizada.")
    else:
        print(f"\n✅ {arquivos_movidos} arquivo(s) organizado(s) com sucesso!")


def main():
    print("===== ORGANIZADOR DE ARQUIVOS =====\n")
    caminho = input(
        "Digite o caminho da pasta que deseja organizar "
        "(ex: /home/usuario/Downloads): "
    ).strip()

    if not caminho:
        print("Nenhum caminho informado. Encerrando.")
        return

    confirmacao = input(
        f"Tem certeza que deseja organizar os arquivos em '{caminho}'? (s/n): "
    ).strip().lower()

    if confirmacao == "s":
        organizar_pasta(caminho)
    else:
        print("Operação cancelada.")


if __name__ == "__main__":
    main()
