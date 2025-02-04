
#Access the value of key history

sample_dict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}

print(sample_dict['class']["student"]["marks"]["history"])


###################

student_info = {
    'name': 'John',
    'age': 25,
    'hobbies': ['reading', 'gaming', 'cycling'],
    'city': 'New York'
}

# Tasks:
# 1 - Change the value of 'age' from 25 to 30.
# 2 - Add a new entry with the key 'occupation' and the value 'Engineer'.
# 3 - Remove the entry with the key 'city'.
# 4 - check if the key 'email' is on the dictionary, if not, add it with value 'name@gmail.com'
# 5 - Loop through the values in the 'hobbies' list and print each hobby on a new line.

student_info['age'] =30
student_info["occupation"] = "Engineer"
del student_info["city"]
print('email' in student_info)
student_info["email"] = "name@gmail.com"
for i in student_info["hobbies"]:
    print(i)

###################



# Delete set of keys from Python Dictionary

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}

keys_to_remove = ["name", "salary"]
for i in keys_to_remove:
    del sample_dict[i]