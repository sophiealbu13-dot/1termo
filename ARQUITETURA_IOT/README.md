# Arquitetura IOT     
# Aula: Arquitetura IoT e Dispositivos de Borda

## 1. Introdução à Arquitetura IoT
A arquitetura de Internet das Coisas (IoT) geralmente é dividida em camadas:
*   **Camada de Percepção (Dispositivos):** Sensores e atuadores (Ex: Arduino).
*   **Camada de Rede (Conectividade):** Protocolos como Wi-Fi, LoRa, MQTT.
*   **Camada de Aplicação:** Dashboards, análise de dados e armazenamento em nuvem.

## 2. O Ecossistema Arduino
O Arduino atua na **Camada de Percepção**. É uma plataforma de prototipagem eletrônica de código aberto baseada em hardware e software flexíveis.

### Principais Componentes:
*   **Microcontrolador:** O "cérebro" do dispositivo (ex: ATmega328P no Arduino Uno).
*   **Pinos de I/O:** Entradas e saídas digitais e analógicas.
*   **IDE Arduino:** Ambiente de desenvolvimento para escrever e carregar o código.

---

## 3. Linguagens de Programação na IoT

Na arquitetura IoT, a escolha da linguagem depende da capacidade de processamento do hardware.

### 3.1 C++ (O padrão para Microcontroladores)
O C++ é a linguagem nativa do ecossistema Arduino. 

*   **Vantagens:** Alta performance, baixo consumo de memória e controle direto sobre o hardware.
*   **Estrutura Básica:**
    ```cpp
    void setup() {
      pinMode(13, OUTPUT); // Configura o pino 13 como saída
    }

    void loop() {
      digitalWrite(13, HIGH); // Liga o LED
      delay(1000);           // Espera 1 segundo
      digitalWrite(13, LOW);  // Desliga o LED
      delay(1000);
    }
    ```

### 3.2 Python (IoT em Camadas Superiores)
Embora o Arduino clássico use C++, versões modernas (como Arduino Nano RP2040) e o Raspberry Pi utilizam **MicroPython** ou **Python**.

*   **Vantagens:** Desenvolvimento rápido, sintaxe simples e excelente para processamento de dados e integração com APIs.
*   **Exemplo (MicroPython):**
    ```python
    from machine import Pin
    import time

    led = Pin(13, Pin.OUT)

    while True:
        led.value(1) # Liga
        time.sleep(1)
        led.value(0) # Desliga
        time.sleep(1)
    ```

---

## 4. Comparativo: C++ vs Python na IoT


| Característica | C++ (Arduino) | Python (MicroPython/Linux) |
| :--- | :--- | :--- |
| **Performance** | Muito Alta | Média |
| **Consumo de Memória** | Baixíssimo | Significativo |
| **Curva de Aprendizado** | Moderada | Fácil |
| **Uso Comum** | Sensores, Atuadores, RTOS | Gateways, Processamento de Dados, IA |

---

## 5. Exercício Prático
1. Identifique os sensores necessários para um sistema de monitoramento de umidade.
2. Escreva a lógica em pseudocódigo para ler o sensor a cada 5 segundos.