dict1={"name":"sam","marks":[90,85,80]}
for key,value in dict1.items():
    marks_values=dict1.get("marks")
    avg=(sum(marks_values))/len(marks_values)
print(avg)