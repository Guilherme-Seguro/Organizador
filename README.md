Organizador de Arquivos 

Script de automação pessoal desenvolvido em Python que organiza os arquivos de uma pasta (ex: Downloads) em subpastas de acordo com o tipo de arquivo.

Problema que resolve:

Pastas como "Downloads" costumam acumular arquivos de tipos diferentes misturados (imagens, PDFs, planilhas, instaladores, etc.), o que dificulta encontrar o que se precisa. Esse script organiza tudo automaticamente em poucos segundos, separando os arquivos por categoria.

Funcionalidades:
Organiza arquivos automaticamente em subpastas por tipo: Imagens, Documentos, Planilhas, Apresentações, Vídeos, Áudios, Compactados, Executáveis e Código;
Arquivos com extensões não mapeadas vão para uma pasta "Outros";
Evita sobrescrever arquivos com nomes repetidos (adiciona um sufixo numérico automaticamente);
Pede confirmação antes de mover qualquer arquivo, evitando acidentes;
Fácil de expandir: basta adicionar novas extensões ao dicionário CATEGORIAS;

Tecnologias utilizadas:
Python 3;
Bibliotecas nativas: os, shutil, pathlib (sem dependências externas).

Recomendado testar primeiro em uma pasta de exemplo (com arquivos que não sejam importantes), antes de rodar em pastas reais como Downloads ou Documentos.

Estrutura do código:
CATEGORIAS — dicionário que mapeia categorias de pastas para as extensões de arquivo correspondentes;
obter_categoria — identifica a categoria de um arquivo a partir da sua extensão;
organizar_pasta — percorre a pasta informada e move cada arquivo para a subpasta correta;
main — controla o fluxo principal, incluindo a confirmação do usuário antes de executar a organização;
Possíveis melhorias futuras;
Adicionar opção de desfazer a organização (undo);
Permitir organização por data de criação/modificação, além do tipo;
Criar uma interface gráfica simples;
Adicionar testes automatizados;
Gerar um log das movimentações realizadas.
