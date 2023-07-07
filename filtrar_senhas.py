import subprocess

# Função para executar comandos no terminal e retornar a saída
def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

# Obtendo as portas abertas
open_ports = run_command("netstat -tuln | grep 'LISTEN'")

# Obtendo o tempo de atividade
uptime = run_command("uptime -p")

# Obtendo o nome do processador
processor = run_command("cat /proc/cpuinfo | grep 'model name' | uniq | cut -d ':' -f 2")

# Obtendo a quantidade de memória RAM
memory = run_command("free -h | awk '/Mem:/ {print $2}'")

# Exibindo as informações
print("Portas abertas:\n", open_ports)
print("Tempo ligado:", uptime)
print("Nome do processador:", processor)
print("Quantidade de memória RAM:", memory)

