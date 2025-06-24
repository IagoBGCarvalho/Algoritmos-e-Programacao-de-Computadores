# --- Dados Auxiliares (Definidos Fora do Loop) ---

# Mapeia o dígito do dia da semana para o índice da lista (0=Seg, 1=Ter, ..., 5=Sab)
dias_map = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5}
dias_semana_nomes = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab"]

# Mapeia o código do horário para a string de tempo a ser exibida
horarios_map = {
    "M1": "08:00 - 08:55", "M2": "08:55 - 09:50", "M3": "10:00 - 10:55",
    "M4": "10:55 - 11:50", "M5": "12:00 - 12:55", "T1": "12:55 - 13:50",
    "T2": "14:00 - 14:55", "T3": "14:55 - 15:50", "T4": "16:00 - 16:55",
    "T5": "16:55 - 17:50", "T6": "18:00 - 18:55", # <<< CORREÇÃO APLICADA AQUI
    "N1": "19:00 - 19:50", "N2": "19:50 - 20:40", "N3": "20:50 - 21:40", "N4": "21:40 - 22:30",
}

# Ordem cronológica de todos os horários possíveis para impressão ordenada
ordem_slots = [
    "M1", "M2", "M3", "M4", "M5", "T1", "T2", "T3", "T4", "T5", "T6",
    "N1", "N2", "N3", "N4"
]

# --- Estrutura de Dados Principal ---
# Inicializa a grade com todos os horários vazios
grade = {slot: [""] * 6 for slot in ordem_slots}


# --- Loop Principal do Programa ---
while True:
    try:
        instrucao_completa = input()
        if instrucao_completa == "Hasta la vista, beibe!":
            break

        partes = instrucao_completa.split()
        comando = partes[0]

        if comando == "?":
            # IMPRIMIR GRADE
            horarios_com_aula = []
            for slot, aulas in grade.items():
                if any(aula != "" for aula in aulas):
                    horarios_com_aula.append(slot)

            # Ordena os horários a serem impressos
            horarios_ordenados = sorted(horarios_com_aula, key=lambda s: ordem_slots.index(s))

            # Imprime o cabeçalho
            print("+---------------+----------+----------+----------+----------+----------+----------+")
            print("|               | Seg      | Ter      | Qua      | Qui      | Sex      | Sab      |")
            print("+---------------+----------+----------+----------+----------+----------+----------+")

            # Imprime cada linha de aula
            for slot in horarios_ordenados:
                horario_str = horarios_map[slot]
                aulas = grade[slot]
                print(f"| {horario_str:^13} | {aulas[0]:^8} | {aulas[1]:^8} | {aulas[2]:^8} | {aulas[3]:^8} | {aulas[4]:^8} | {aulas[5]:^8} |")
                print("+---------------+----------+----------+----------+----------+----------+----------+")

        elif comando == "+" or comando == "-":
            # ADICIONAR OU REMOVER DISCIPLINA
            cod_disciplina = partes[1]
            cods_dth = partes[2:]
            
            # Decodifica todos os DTHs em uma lista de tuplas (índice_dia, slot)
            slots_para_alterar = []
            for dth in cods_dth:
                dias_str = ""
                horas_str = ""
                turno = ''
                for char in dth:
                    if char.isdigit():
                        if not turno:
                            dias_str += char
                        else:
                            horas_str += char
                    else:
                        turno = char
                
                for dia in dias_str:
                    for hora in horas_str:
                        slot = f"{turno}{hora}"
                        slots_para_alterar.append((dias_map[dia], slot))
            
            # Lógica de Adicionar (+)
            if comando == "+":
                conflito = False
                for dia_idx, slot in slots_para_alterar:
                    if grade[slot][dia_idx] != "":
                        conflito = True
                        break
                
                if conflito:
                    print(f"!({instrucao_completa})")
                else:
                    for dia_idx, slot in slots_para_alterar:
                        grade[slot][dia_idx] = cod_disciplina
            
            # Lógica de Remover (-)
            elif comando == "-":
                nao_existe = False
                for dia_idx, slot in slots_para_alterar:
                    if grade[slot][dia_idx] != cod_disciplina:
                        nao_existe = True
                        break

                if nao_existe:
                    print(f"!({instrucao_completa})")
                else:
                    for dia_idx, slot in slots_para_alterar:
                        grade[slot][dia_idx] = ""

    except EOFError:
        break