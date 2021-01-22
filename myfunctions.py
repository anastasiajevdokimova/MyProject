def loe_fail(f):
    fail=open(f,'r',encoding="utf-8-sig")
    mas=[] 
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    print(mas)
    return mas

def kontroll (event):
    w=ent.get()
    while w not in EST:
        lbla=Label(win, text="Пожалуйста, введи текст \nна эстонском языке!")
        lbla.pack(anchor=E)
    except:
        TypeEror
        
    if w(ind)==wrd(ind):
        lbla=Label(win, text="Правильно!")
        lbla.pack(anchor=E)
    else:
        lbla=Label(win, text="Ой, попробуй ещё раз!")
        lbla.pack(anchor=E)

def olv ():
    listitem=random.randint(0,len(estv))
    wrd=estv[listitem]
    lbl=Label(win, text="str(wrd)")
    ent=Entry(win, width=5)
    lbl.pack(anchor=W)
    ent.pack(anchor=CENTER)
    ent.bind('<Return>', kontroll)
