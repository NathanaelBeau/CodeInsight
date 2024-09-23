def test(dict0):
    top_three = [('', [0])] 
    
    for key, value in dict0.items():
        total_value = sum(value)
        if total_value > sum(top_three[-1][1]):
            top_three.pop()
            top_three.append((key, value))
            top_three.sort(key=lambda tup: sum(tup[1]), reverse=True)
    
    summary = {}
    for key, value in top_three:
        if key:
            summary[key] = sum(value)
    
    return summary

