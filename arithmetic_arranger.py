# code by Edwin Saul @Saul11235

def problem_strings(string,calculate=False):
    content=list(filter( lambda x:x!="",str(string).split(" ")))
    anchor=0
    for x in content: anchor=max(anchor,len(x))
    lista=[]
    for x in content: lista.append(str(x))
    lista.append("-"*(anchor+2))
    if calculate:
        lista.append("xxxx")
    return lista



def arithmetic_arranger(problems,calculate=False):
    list_strings=[ problem_strings(x,calculate) for x in problems]
    arranged_problems=str(list_strings)
    return arranged_problems



if __name__=="__main__":
    # dev test
    print(problem_strings(" 1 + 3 "))
    print(arithmetic_arranger(["1 + 2","23 - 11"],True))
