"""
Desafio Módulo Git

Neste arquivo você encontrará funções **incompletas** que representam
tarefas relacionadas ao aprendizado de Git e GitHub.

Seu objetivo é:
- Criar uma issue para cada função.
- Implementar a função em uma branch específica.
- Fazer commit, criar tag e abrir Pull Request.
- Repetir o processo até concluir todas as funções.

Boa sorte e bons commits! 🚀
"""

def mostrar_mensagem_inicial():
    """
    Exibe uma mensagem de boas-vindas ao desafio.
    Retorno esperado: string com a mensagem "Bem-vindo ao Desafio de Git!"
    """
    mensagem = "Bem-vindo ao Desafio de Git!"    
    return mensagem


def listar_comandos_git_basicos():
    """
    Retorna uma lista com os principais comandos básicos do Git.
    Exemplo de saída:
    ["git init", "git add", "git commit", "git status", "git push"]
    """
    comandos = ["git init", "git add", "git commit", "git status", "git push"]
    return comandos

def criar_mensagem_commit(funcao_nome):
    """
    Recebe o nome de uma função e retorna uma mensagem de commit padronizada.
    Exemplo:
    criar_mensagem_commit("listar_comandos_git_basicos") ->
    "Implementa função listar_comandos_git_basicos"
    """
    return f"Implementa função {funcao_nome}"

def verificar_tag_valida(tag):
    """
    Verifica se uma tag está no formato 'vX.Y' (ex: v1.0, v2.1).
    Retorna True se o formato for válido, caso contrário False.
    """
    # Verifica se começa com 'v' e o restante segue o padrão numérico
    if not isinstance(tag, str):
        return False

    if tag.startswith("v"):
        partes = tag[1:].split(".")  # remove o 'v' e separa em duas partes
        if len(partes) == 2 and all(p.isdigit() for p in partes):
            return True
    return False

def gerar_relatorio_final(funcoes_concluidas):
    """
    Recebe uma lista com os nomes das funções implementadas
    e retorna uma mensagem final do desafio.

    Exemplo:
    gerar_relatorio_final(["mostrar_mensagem_inicial", "listar_comandos_git_basicos"])
    ->
    "Desafio concluído! 2 funções implementadas com sucesso."
    """
    if not isinstance(funcoes_concluidas, list):
        return "Erro: o parâmetro deve ser uma lista."

    total = len(funcoes_concluidas)

    if total == 0:
        return "Nenhuma função implementada ainda. Continue praticando!"
    elif total == 1:
        return "Desafio em andamento! 1 função implementada com sucesso."
    else:
        return f"Desafio concluído! {total} funções implementadas com sucesso."

#Inicio   
print(mostrar_mensagem_inicial(), "\n")

comandos = listar_comandos_git_basicos()
print("Comandos Git básicos:")
for cmd in comandos:
    print("-", cmd), 

print("\n", criar_mensagem_commit("listar_comandos_git_basicos"), "\n")

print("Verifiaca Tag Válida")
print(verificar_tag_valida("v1.0"))   # ✅ True
print(verificar_tag_valida("v2.3"))   # ✅ True
print(verificar_tag_valida("1.0"))    # ❌ False (não começa com v)
print(verificar_tag_valida("v2"))     # ❌ False (não tem ponto)
print(verificar_tag_valida("v2.a"), "\n")   # ❌ False (parte não numérica)

print(gerar_relatorio_final([]))
# ➜ "Nenhuma função implementada ainda. Continue praticando!"

print(gerar_relatorio_final(["mostrar_mensagem_inicial"]))
# ➜ "Desafio em andamento! 1 função implementada com sucesso."

print(gerar_relatorio_final(["mostrar_mensagem_inicial", "listar_comandos_git_basicos", "criar_mensagem_commit"]))
# ➜ "Desafio concluído! 3 funções implementadas com sucesso."

