"""
problem:

extend the program so that it determines and displays the longest sequence of consecutive result increases

"""

results= [39,32,62,88,51,62,64,81,77]

def uwu(result):
    mean=0
    grade=0
    lowest=0
    highest=0
    scores_under40=0
    score50to79=0
    longest=0
    
    #calculate mean
    for i in results:
        mean+=i
    mean=mean/(len(results))
    
    #calculate if grade is lower or higher merit
    if mean<70:
        grade="lower merit"
    elif mean>70:
        grade="higher merit"
    elif mean<=0:
        grade="failed, this idiot didnt even get a 1/100"
    
    #calculate lowest grade
    lowest=(sorted(results))[0]

    #calculate highest grade
    highest=(sorted(results))[len(results)-1]
    
    #scores under 40
    #calculate number of grades between 50 to 70
    for i in results:
        if i<40:
            scores_under40+=1
        if i in range(50,79):
            score50to79+=1
        

    

    #calculate longest run
    """will implement this"""

    







    explanation= print(f"the mean percentage mark is {mean}\n the grade for the average result is {grade} \n the lowest score is {lowest} \n the highest score is {highest} \n the number of scores below 40 is {scores_under40} \n the number of scores between 50 and 79 is {score50to79}\n the longest run of result incrases is {longest}")


    return explanation

uwu(results)