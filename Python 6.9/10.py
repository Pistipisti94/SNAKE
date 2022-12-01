teszt = print
teszt(3 % 4 == 0) #ez lesz sikertelen azért mert 3 maradékosan osztva 4-el az 3 és nem 0
teszt(3 % 4 == 3) 
teszt(3 / 4 == 0) #ez lesz sikertelen azért mert 3 osztva 4-el az 0,75 és nem 0
teszt(3 // 4 == 0)
teszt(3+4*2 == 14) #ez lesz sikertelen azért mert a python először a (*)-t végzi el
teszt(4-2+2 == 0) #ez lesz sikertelen azért mert a (+)-t és (-)-t eggyenrangúként kezeli a pythonban
teszt(len("helló, világ!") == 13)

teszt(3 % 4)
teszt(3 % 4)
teszt(3 / 4)
teszt(3 // 4)
teszt(3+4*2)
teszt(4-2+2)
teszt(len("helló, világ!"))