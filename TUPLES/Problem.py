# CONVERT THE FOLLOWING DICTIONARY INTO JSON FORMAT
# import json
# student_data = {"name": "David", "age": 13, "marks": 87}
# data = json.dumps(student_data)
# print(data)

## Access the value of age from the given data
# import json
# student_data = """{"name": "David", "age": 13, "marks": 87}"""
# data = json.loads(student_data)
# print(data["age"])



#PRETY PRINT FOLLOWING JSON DATA
# import json
# student_data = {"name": "David", "age": 13, "marks": 87}
# data = json.dumps(student_data, indent=4, separators=(",","="))
# print(data)



### Sort the following JSON keys and write them into a file
# student_data = """{"name": "David", "age": 13, "marks": 87}"""
import json
student_data = {"name": "David", "age": 13, "marks": 87}
print(type(student_data))
f = open("demo.json","w")
data = json.dumps(student_data,indent=4, sort_keys=True)
f.write(data)
print("jahah")
