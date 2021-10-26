# functions
def print_text():
    text = "This is a test!"
    print(text)

print_text()

# functions
def print_text(text1):
    print(text1)
   
# called the function
print_text("Another test!")

# passing values into functions
def age_cal(age,name):
    if age < 5:
        print("Young lad!", name, "is only", age)
    elif age == 5:
        print("Growing up!,", name)
    else:
        print("All grown up!")
age_cal(3,"He")

# getting parameter back from a function
def add_age(sent_age):
    new_age = sent_age + 10
    return new_age

how_old_will_i_be = add_age(3)
print(how_old_will_i_be)