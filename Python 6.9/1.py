def fordulj_orajarasi_iranyba(teszt):
    teszt = teszt.lower()
    data = ""

    if teszt == "d":
        data = "Nyugat"
    elif teszt == "ny":
        data = "Észak"
    elif teszt == "é":
        data = "Kelet"
    elif teszt == "k":
        data = "Dél"
    else:
        data = "None"

    return data

irany=input("Írj be egy éghajlat Kezdőbetűjét:(É,D,Ny,K) ")
print(irany,"Óramutató járásával megeggyező szomszéda:",fordulj_orajarasi_iranyba(irany))

