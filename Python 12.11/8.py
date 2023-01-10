def szo_tisztitas(szo):
    spkak = "\'\"+!%/=()~ˇ^˘°˛`˙´,.-?:_;>*>#&@\\{}łŁ$ß÷đĐ[]€"
    spkak = [*spkak]
    for s in spkak:
        szo = "".join(szo.split(s))
    return szo

print(szo_tisztitas("hogyan?"))
print(szo_tisztitas("'most!'"))
print(szo_tisztitas("?+='s-z-a-v!a,k@$()'"))