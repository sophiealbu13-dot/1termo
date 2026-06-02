# Logica de programação 
# Aula: Lógica de Programação com Python e Boas Práticas

## 1. Introdução à Lógica com Python
A lógica de programação é a base para criar algoritmos. O **Python** é utilizado aqui por sua sintaxe limpa e próxima da linguagem humana.

### Conceitos Fundamentais:
*   **Variáveis e Tipos:** `int`, `float`, `string` e `boolean`.
*   **Estruturas Condicionais:** `if`, `elif`, `else`.
*   **Laços de Repetição:** `for` e `while`.

---

## 2. Clean Code (Código Limpo)
Programar não é apenas fazer o computador entender, mas sim fazer outros humanos entenderem.

### Princípios Básicos:
*   **Nomes Significativos:** Evite variáveis como `a` ou `x1`. Use `preco_total` ou `usuario_logado`.
*   **Funções Pequenas:** Uma função deve fazer apenas uma coisa e fazê-la bem.
*   **Comentários Necessários:** O código deve ser claro o suficiente para não precisar de excesso de comentários.
*   **DRY (Don't Repeat Yourself):** Não repita código; use funções ou classes.

---

## 3. Versionamento com Git
O **Git** é o sistema que controla o histórico de alterações dos seus arquivos.

### Comandos Essenciais para Projetos:
1.  `git init`: Inicia um novo repositório local.
2.  `git add .`: Adiciona as mudanças para a "área de espera" (staging).
3.  `git commit -m "mensagem"`: Salva as alterações com uma nota explicativa.
4.  `git status`: Verifica o estado atual dos arquivos.

---

## 4. GitHub e Colaboração
O **GitHub** é a plataforma na nuvem que hospeda seus repositórios Git.

*   **Repositório Remoto:** Onde o código fica salvo online.
*   **Push:** Envia seu código local para o GitHub (`git push origin main`).
*   **Pull:** Baixa as atualizações da nuvem para sua máquina.
*   **Social Coding:** Portfólio para desenvolvedores e colaboração em projetos open-source.

---

## 5. Exemplo Prático: Unindo Tudo
Um pequeno script Python seguindo padrões de Clean Code para ser versionado:

```python
def calcular_media(notas):
    """Calcula a média aritmética de uma lista de notas."""
    soma_total = sum(notas)
    quantidade = len(notas)
    return soma_total / quantidade

# Dados de exemplo
notas_aluno = [8.5, 7.0, 9.2]
media_final = calcular_media(notas_aluno)

print(f"A média do aluno é: {media_final:.2f}")
```

---

## 6. Desafio da Aula
1. Crie um script Python que resolva um problema simples (ex: conversor de moedas).
2. Aplique as regras de **Clean Code** nos nomes das variáveis.
3. Crie um repositório no **GitHub**.
4. Faça o **Git Commit** e o **Push** do seu código para o repositório criado.
                                                                                                                                       