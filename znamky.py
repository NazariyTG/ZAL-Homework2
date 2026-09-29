



def read_lines(filename:list[str]) -> list[str]:

    with open(filename, encoding="utf-8") as f:
        lines:list[str] = f.readlines()
        

        for line in lines:
            if( line != ""):
                print(parse_line(line.strip()))
            
        


    return 1

def parse_line(line:list[str]) -> tuple(str,str):
    subjeck, scores = line.split(":")
    return subjeck, scores

def average(values:list[int]):
    
    sum = 0
    for i in values:
        sum += i

    return sum / len(values)



read_lines("znamky.txt")
