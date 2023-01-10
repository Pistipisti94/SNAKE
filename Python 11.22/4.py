ez = ["Én", "nem", "vagyok", "egy", "csodabogár"]
az = ["Én", "nem", "vagyok", "egy", "csodabogár"]
print("Test 1:{0}".format(ez is az))
ez = az
print("Test 2:{0}".format(ez is az))
#Az első False mert nem ugyan az 
#A másodiknál viszont már ugyan az lesz ezért az eredmény True