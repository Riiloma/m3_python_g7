recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
                ['2021-05-01', "15:00", "No trabajar"],
                ['2021-07-15', "13:00", "No hacer nada es feriado"],
                ['2021-09-18', "16:00", "Ramadas"],
                ['2021-12-25', "00:00", "Navidad"]]

recordatorios.insert(2,["2012-02-02","06:00","Empezar el Año"])

for recortadorio in recordatorios:
    if recortadorio[0]=='2021-07-15':
        recortadorio[0]='2021-07-16'
        
    if recortadorio[0]=='2021-05-01':
        recordatorios.remove(['2021-05-01', "15:00", "No trabajar"])

recordatorios.insert(-1,['2021-12-24','22:00', 'Cena de Navidad'])
recordatorios.append(['2021-12-31','22:00', 'Cena de Año Nuevo'])

print(f"recordatorios despues de la modificacion:\n {recordatorios}")