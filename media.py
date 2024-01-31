import pandas as pd

# using pandas to read the excel spreadsheet
table = pd.read_excel('planilha_alunos.xlsx')
print('=== table inicial ===\n')
print(table, '\n')

# converts integers (grades) into float
int_to_float = table[['P1', 'P2', 'P3']] / 10
print('=== Notas convertidas (float) ===\n')
print(int_to_float, '\n')

# calculates and prints the student's name and grade
m = int_to_float.mean(axis=1)
# added the column 'Média Final' so it could be displayed on the terminal
table['Média Final'] = m.round()
print('=== Média Final === \n')
print(table[['Aluno', 'Média Final']])

# variables used in the functions
semester_classes = 60
missed_classes_limit = 0.25 * semester_classes

# naf --> Nota para Aprovação final
approved = 7
naf = 5
naf_calc = (m + naf) / 2

# says the result based on the students final grade
def student_situation():
    table['Situação'] = 'Aprovado'

    table.loc[(m < naf), 'Situação'] = 'Reprovado'

    table.loc[(m < approved) & (m >= naf), 'Situação'] = 'Exame Final'
student_situation()

# calculate the student attendance to the classes and gives the result
def failed_attendance():
    semester_classes = 60
    missed_classes_limit = 0.25 * semester_classes

    table.loc[table['Faltas'] > missed_classes_limit, 'Situação'] = 'Reprovado por Falta'

failed_attendance()

# calculates the points the student needs in the final exam
def final_exam_calc():
    table.loc[(table['Situação'] == 'Exame Final'), 'Nota para Aprovação Final'] = approved - m.round()

    table.loc[(table['Situação'] == 'Aprovado') | (table['Situação'] == 'Reprovado') | (table['Situação'] == 'Reprovado por Falta'), 'Nota para Aprovação Final'] = 0

final_exam_calc()

print('\n=== Updated Table ===\n')
print(table)




