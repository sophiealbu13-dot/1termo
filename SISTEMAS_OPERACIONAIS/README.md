# Sistemas operacionais
# Aula: Fundamentos de Sistemas Operacionais (S.O.)

## 1. O que é um Sistema Operacional?
O **S.O.** é o software fundamental que gerencia o hardware do computador e fornece serviços para os programas aplicativos. Ele atua como o intermediário entre o usuário e o hardware.

### Principais Funções:
*   Gerenciamento de Processos (CPU).
*   Gerenciamento de Memória (RAM).
*   Gerenciamento de Arquivos e Armazenamento.
*   Interface com o Usuário.

---

## 2. Windows vs. Linux

### Windows
*   **Proprietário:** Desenvolvido pela Microsoft.
*   **Foco:** Facilidade de uso (Interface Gráfica - GUI).
*   **Ecossistema:** Amplamente utilizado em ambientes corporativos e jogos.

### Linux
*   **Código Aberto:** Gratuito e colaborativo.
*   **Kernel:** O coração do sistema.
*   **Versatilidade:** Utilizado em servidores, supercomputadores e dispositivos IoT.

---

## 3. CLI (Command Line Interface)
A **CLI** ou Interface de Linha de Comando é a interação com o S.O. através de comandos de texto, sem o uso de mouse.

*   **Linux:** Utiliza o Terminal (BASH, ZSH).
    *   `ls`: Listar arquivos.
    *   `sudo`: Executar como administrador.
*   **Windows:** Utiliza o CMD ou PowerShell.
    *   `dir`: Listar arquivos.
    *   `ipconfig`: Verificar rede.

---

## 4. Sistemas Operacionais de Tempo Real (RTOS) e Arduino
Diferente de um PC, dispositivos como o **Arduino** geralmente não rodam um S.O. completo como Windows ou Linux.

*   **Arduino:** Executa um "Bare Metal" ou um **RTOS** (Real-Time Operating System) simples.
*   **Controle:** O código é executado diretamente no microcontrolador para garantir que tarefas críticas aconteçam no tempo exato.

---

## 5. Arquitetura AIOS (All-In-One System)
O conceito de **AIOS** refere-se a sistemas integrados onde hardware e software são otimizados para funcionar como uma única unidade coesa, comum em sistemas embarcados modernos e dispositivos móveis.

*   **Integração:** Maximiza a eficiência energética e performance.
*   **Uso:** Tablets, sistemas automotivos e automação industrial.

---

## 6. Atividade Prática de Comparação
1.  **Exploração CLI:** Abra o terminal do seu sistema (CMD no Windows ou Terminal no Linux) e execute o comando para listar diretórios.
2.  **Identificação:** Liste 3 periféricos que o S.O. precisa gerenciar ao conectar um Arduino no computador.
3.  **Reflexão:** Por que o Linux é preferido para servidores e o Windows para usuários domésticos?
