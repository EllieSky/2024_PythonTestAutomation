def count_occ(input1,input2):
  input1= "cucumber"
  input2 = "u"
  return input1.count(input2)


count_occ("Cucumber", "u")


# Advanced level
def counting_occ_adv(inp1, inp2, case_sensitive=True):
    if(case_sensitive != True):
        countss = inp1.lower().count(inp2.lower())
    print(countss)
    return countss


counting_occ_adv("Cucumber", "c", False)


# Expert Level

def counting_occ_expert(inp1, inp2):
    countsss = str(inp1).count(str(inp2))
    print(countsss)
    return countsss


counting_occ_expert("The boy is 5 years old", "5")
counting_occ_expert(532, 3)