# code by Edwin Saul @Saul11235

def problem_strings(string,calculate=False):
    content=list(filter( lambda x:x!="",str(string).split(" ")))

    print(content)
    return ["k","k"]





def arithmetic_arranger(problems,calculate=False):
    list_strings=[ problem_strings(x) for x in problems]

    arranged_problems=str(list_strings)

    return arranged_problems

if __name__=="__main__":
    print(problem_strings(" 1 + 3 "))
    print(arithmetic_arranger([1,2,3]))
