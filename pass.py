import random, time
# Funções
def gerar_a_z():
  result = chr(random.randint(97,122))
  return result
def gerar_A_Z():
  result = chr(random.randint(65,90))
  return result
def gerarSimbolos():
  result = chr(random.randint(58,64))
  return result
def gerar_numeros():
  result = chr(random.randint(48,57))
  return result
def caractere():
  rangex = [
    random.randint(33, 47), # Faz um range de do sinal de -> ! até o sinal de barra -> / [!-/]
		random.randint(58, 64),
		random.randint(91, 96),
		random.randint(123, 126),
  ]
  return chr(random.choice(rangex))

def criar(upper=True,lenght=20,lower=True,numbers=True,chars=True):
  senha = []
  for x in range(lenght):
    if numbers:
        senha.append(gerar_numeros())
        senha.append(caractere())
    if lower:
        senha.append(gerar_a_z())
    if upper:
        senha.append(gerar_A_Z())
    if chars:
        senha.append(caractere())
    senhap = senha[:lenght]
    random.shuffle(senhap)
    return ''.join(senhap)

print("""\033[1;33m
  ____                                                ____                         _                  
 |  _ \    __ _   ___   ___  __      __              / ___|  _ __    ___    __ _  | |_    ___    _ __ 
 | |_) |  / _` | / __| / __| \ \ /\ / /    _____    | |     | '__|  / _ \  / _` | | __|  / _ \  | '__|
 |  __/  | (_| | \__ \ \__ \  \ V  V /    |_____|   | |___  | |    |  __/ | (_| | | |_  | (_) | | |   
 |_|      \__,_| |___/ |___/   \_/\_/                \____| |_|     \___|  \__,_|  \__|  \___/  |_|

                                         versão 1.0                                                      \033[m""")
print("""

Meu GitHub > https://github.com/nano-9

              ----------
Este é um gerador de senhas super fortes
o programa gera senhas baseado em ASCII
              ----------
              
Dê enter para gerar sua senha
""")



input()
while True:
# Mostra a senha criada
  print("Gerando sua senha...\n")
  time.sleep(2)
  print("\033[1;32mSua senha é:\033[m")

  for y in range(5+1):
    print(criar(upper=True,lenght=20,lower=True,numbers=True,chars=True), end='')
  print()
  try:
    stop = str(input("\nQuer outra senha? S ou enter / N: ")).upper().strip().rstrip().lstrip()
  except (ValueError, TypeError):
    print("Tipo de dados inválidos")
  except KeyboardInterrupt:
    print("\nSaiu!")
    break
  else:
    if stop == "S":
      pass
    elif stop == "N":
      break

  print()

print('Volte sempre!')

print()
