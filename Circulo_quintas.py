
import random
                  #Escalas Mayores
#Notas Naturales
esc_CM = ['Do', 'Re', 'Mi' ,'Fa', 'Sol', 'La', 'Si']
esc_DM = ['Re', 'Mi', 'Fa#', 'Sol', 'La', 'Si','Do#']
esc_EM = ['Mi', 'Fa#', 'Sol#', 'La', 'Si','Do#', 'Re#']
esc_FM = ['Fa', 'Sol', 'La', 'Sib','Do', 'Re', 'Mi']
esc_GM = ['Sol', 'La', 'Si', 'Do', 'Re', 'Mi' ,'Fa#']
esc_AM = ['La', 'Si', 'Do#', 'Re', 'Mi' ,'Fa#', 'Sol#']
esc_BM = ['Si','Do#', 'Re#', 'Mi' ,'Fa#', 'Sol#', 'La#']
#Notas Alteradas
esc_Csost = ['Do#', 'Re#', 'Mi#', 'Fa#', 'Sol#', 'La#', 'Si#']
esc_Dsost = ['Re#', 'Mi#', 'Fa##', 'Sol#', 'La#', 'Si#','Do##']
esc_Fsost = ['Fa#', 'Sol#', 'La#', 'Si','Do#', 'Re#', 'Mi#']
esc_Gsost = ['Sol#', 'La#', 'Si#', 'Do#', 'Re#', 'Mi#' ,'Fa##']
esc_Asost = ['La#', 'Si#', 'Do##', 'Re#', 'Mi#' ,'Fa##', 'Sol##']
esc_Db = ['Reb', 'Mib', 'Fa', 'Solb', 'Lab', 'Sib', 'Do']
esc_Eb = ['Mib', 'Fa', 'Sol', 'Lab', 'Sib', 'Do', 'Re']
esc_Gb = ['']
esc_Ab = esc_Gsost
esc_Bb = ['Sib', 'Do', 'Re', 'Mib', 'Fa', 'Sol', 'La']


                 #Escalas Menores
#Notas Naturales
esc_Cm= ['Do', 'Re', 'Mib' ,'Fa', 'Sol', 'Lab', 'Sib']
esc_Dm= ['Re', 'Mi' ,'Fa', 'Sol', 'La', 'Sib','Do']
esc_Em = ['Mi' ,'Fa#', 'Sol', 'La', 'Si','Do', 'Re']
esc_Fm = ['Fa', 'Sol', 'Lab', 'Sib', 'Do', 'Reb', 'Mi']
esc_Gm = ['Sol', 'La', 'Sib', 'Do', 'Re', 'Mib' ,'Fa']
esc_Am = ['La', 'Si', 'Do', 'Re', 'Mi' ,'Fa', 'Sol']
esc_Bm = ['Si', 'Do#', 'Re', 'Mi' ,'Fa#', 'Sol', 'La']
#Notas Alteradas
esc_Csost_m = ['Do#', 'Re#', 'Mi', 'Fa#', 'Sol#', 'La', 'Si']
esc_Dsost_m = ['Re#', 'Fa', 'Fa#', 'Sol#', 'La#', 'Si', 'Do#']
esc_Fsost_m = ['Fa#', 'Sol#', 'La', 'Si', 'Do#', 'Re', 'Mi']
esc_Gsost_m = ['Sol#', 'La#', 'Si', 'Do#', 'Re#', 'Mi', 'Fa#']
esc_Asost_m = ['La#', 'Do', 'Do#', 'Mi#', 'Fa', 'Fa#', 'Sol#']
esc_Db_m = esc_Csost_m
esc_Eb_m = esc_Dsost_m
esc_Gb_m = esc_Fsost_m
esc_Ab_m = esc_Gsost_m
esc_Bb_m = esc_Asost_m


          #Acordes Mayores
#Acordes C Mayor
ACORDE_CM_1 = esc_CM[0:5:2]
ACORDE_CM_2 = esc_Dm[0:5:2]
ACORDE_CM_3 = esc_Em[0:5:2]
ACORDE_CM_4 = esc_FM[0:5:2]
ACORDE_CM_5 = esc_GM[0:5:2]
ACORDE_CM_6 = esc_Am[0:5:2]
ACORDE_CM_7 = ['Si', 'Re', 'Fa']
def menu_CM():
    print(f'''
    Acordes de C Mayor:     septimas:            Grados:

CM: {ACORDE_CM_1}     Sib          I, III, VI/TONO: C, Em, Am
Dm: {ACORDE_CM_2}      Do
Em: {ACORDE_CM_3}     Re           II, IV/SEMI TONO: Dm, F
FM: {ACORDE_CM_4}      Mib
GM: {ACORDE_CM_5}     Fa           V, VII/DOMINANTE: G, B0
Am: {ACORDE_CM_6}      Sol
B0: {ACORDE_CM_7}      La

    Escala:
    {esc_CM}
    ''')

#Acordes D Mayor
ACORDE_DM_1 = esc_DM[0:5:2]
ACORDE_DM_2 = esc_Em[0:5:2]
ACORDE_DM_3 = esc_Fsost_m[0:5:2]
ACORDE_DM_4 = esc_GM[0:5:2]
ACORDE_DM_5 = esc_AM[0:5:2]
ACORDE_DM_6 = esc_Bm[0:5:2]
ACORDE_DM_7 = ['Do#','Mi','Sol']
def menu_DM():
    print(f'''
      Acordes de D Mayor:     septimas:            Grados:

D:  {ACORDE_DM_1}                    I, III, VI/TONO: D, Fm# ,Bm
Em: {ACORDE_DM_2}
F#m:{ACORDE_DM_3}                   II, IV/SEMI TONO: Em, G
G:  {ACORDE_DM_4}
A:  {ACORDE_DM_5}                    V, VII/DOMINANTE: A, C0
Bm: {ACORDE_DM_6}
C#0:{ACORDE_DM_7}

    Escala:
    {esc_DM}

''')

#Acordes E Mayor
ACORDE_EM_1 = esc_EM[0:5:2]
ACORDE_EM_2 = esc_Fsost_m[0:5:2]
ACORDE_EM_3 = esc_Gsost_m[0:5:2]
ACORDE_EM_4 = esc_AM[0:5:2]
ACORDE_EM_5 = esc_BM[0:5:2]
ACORDE_EM_6 = esc_Csost_m[0:5:2]
ACORDE_EM_7 = ['Re#','Fa#','La']
def menu_EM():
    print(f'''
      Acordes de D Mayor:     septimas:            Grados:

E:  {ACORDE_EM_1}                   I, III, VI/TONO: E, Gm# ,C#m
F#m:{ACORDE_EM_2}
G#m:{ACORDE_EM_3}                  II, IV/SEMI TONO: F#m, A
A:  {ACORDE_EM_4}
B:  {ACORDE_EM_5}                   V, VII/DOMINANTE: B, D#0
C#m:{ACORDE_EM_6}
D#0:{ACORDE_EM_7}

    Escala:
    {esc_EM}
''')

#Acordes F Mayor
ACORDE_FM_1 = esc_FM[0:5:2]
ACORDE_FM_2 = esc_Gm[0:5:2]
ACORDE_FM_3 = esc_Am[0:5:2]
ACORDE_FM_4 = esc_Bb[0:5:2]
ACORDE_FM_5 = esc_CM[0:5:2]
ACORDE_FM_6 = esc_Dm[0:5:2]
ACORDE_FM_7 = ['Mi', 'Sol', 'Sib']
def menu_FM():
    print(f'''
      Acordes de F Mayor:     septimas:            Grados:

F:  {ACORDE_FM_1}                      I, III, VI/TONO: F, Am ,Dm
Gm: {ACORDE_FM_2}
Am: {ACORDE_FM_3}                      II, IV/SEMI TONO: Gm, Bb
Bb: {ACORDE_FM_4}
C:  {ACORDE_FM_5}                     V, VII/DOMINANTE: C, E0
Dm: {ACORDE_FM_6}
E0: {ACORDE_FM_7}

    Escala:
    {esc_FM}
''')



ACORDE_GM_1 = esc_FM[0:5:2]
ACORDE_GM_2 = esc_Gm[0:5:2]
ACORDE_GM_3 = esc_Am[0:5:2]
ACORDE_GM_4 = esc_Bb[0:5:2]
ACORDE_GM_5 = esc_CM[0:5:2]
ACORDE_GM_6 = esc_Dm[0:5:2]
ACORDE_GM_7 = ['Mi', 'Sol', 'Sib']
def menu_GM():
    print(f'''
      Acordes de F Mayor:     septimas:            Grados:

{n1}: {ACORDE_GM_1}             {s1}          I, III, VI/TONO: {I}, {III} ,{VI}
{n2}: {ACORDE_GM_2}             {s2}
{n3}: {ACORDE_GM_3}             {s3}          II, IV/SEMI TONO: {II}, {IV}
{n4}: {ACORDE_GM_4}             {s4}
{n5}: {ACORDE_GM_5}             {s5}          V, VII/DOMINANTE: {V}, {VII}
{n6}: {ACORDE_GM_6}             {s6}
{n7}: {ACORDE_GM_7}             {s7}

    Escala:
    {esc_GM}
    ''')
I = n1
II = n2
III = n3
VI = n3
V = n5
VI = n6
VII = n7
