s = "Microsoft libera atualização de emergência no  Windows para corrigir falha de segurança. Empresa enviou correção " \
    "para vulnerabilidade  conhecida como PrintNightmare, revelada há uma semana, para diversas versões do sistema  " \
    "operacional. Recomendação é instalação imediata."

lowcase = s.lower()
print(lowcase)

removeCommaFullStop = s.replace(',', ""), s.replace('.', '')
print(removeCommaFullStop)

split = s.split(' ')
print(split)

comprimento = len(s)
print(comprimento)

ss = "maça pera uva"
dividir = ss.split(' ')
dividir.reverse()
print(" ".join(dividir))
