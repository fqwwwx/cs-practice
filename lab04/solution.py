def winner(names: list[str], scores: list[float]) -> str:
    best = 0
    for i in range(1,len(scores)):
        if scores[i] > scores[best]:
            best = i
            
    return names[best]
    
def average(scores: list[float]) -> float:
    if len(scores)== 0:
        return 0.0
        
    return round(sum(scores) / len(scores), 2)
    
def ranking(names: list[str], scores: list[float]) -> list[str]:
    result = []
    
    for i in range(len(names)):
        result.append((scores[i],names[i]))
        
    result.sort(key=lambda x: -x[0])
    return [name for score,name in result]
    
def above_average(names: list[str], scores: list[float]) -> list[str]:
    avg = average(scores)
    result = []
    for i in range(len(scores)):
        if scores[i] > avg:
            result.append(names[i])
            
    return result
    
names =  ["Аня", "Боря", "Вика"]
scores = [7.0,   9.0,    9.0]
print (winner(names,scores))
print (average(scores))
print(ranking(names,scores))
print(above_average(names,scores))