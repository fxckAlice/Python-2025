def get_new_student_data():
    student_data = {
        "full_name": input("Enter your full name: "),
        "age": input("Enter your age: "),
        "location": input("Enter your location: "),
        "university": input("Enter your university: "),
        "group": input("Enter your group`s number: "),
        "number": input("Enter your student number: ")
    }
    return student_data.copy()

def get_additional_student_data():
    add_student_data = {
        "state": input("Tell me how is it going?: "),
        "feeling": input("How do you feel?: "),
        "time_to_get_home": input("How long do you need to get home?: "),
        "exam_result": input("What is your External Independent Evaluation result in Ukrainian?: "),
        "sunny": input("Is it sunny today?: "),
        "to_quarantine": input("When do you think we should go to quarantine?: "),
        "friend_name": input("What is your friend name?: "),
        "wants_to_be_master": input("Do you want to get master`s degree?: "),
        "notebook_color": input("What color is your notebook?: "),
        "mood": input("What's your mood?: ")
    }
    return add_student_data.copy()

def print_student_data(student_data, add_student_data):
    print("\nStudent data:")
    for key, value in student_data.items():
        print(f"{key}: {value}")
    print("\nAdditional student data:")
    for key, value in add_student_data.items():
        print(f"{key}: {value}")

def main():
    student_data = get_new_student_data()
    add_student_data = get_additional_student_data()
    print_student_data(student_data, add_student_data)

main()