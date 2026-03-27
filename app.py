# Student Grade Management System

# This function takes the average score as input
# and returns the corresponding grade
def calculate_grade(avg):
    if avg >= 80:
        return "A"   # Return grade A if average is 80 or above
    elif avg >= 70:
        return "B"   # Return grade B if average is between 70–79
    elif avg >= 60:
        return "C"   # Return grade C if average is between 60–69
    elif avg >= 50:
        return "D"   # Return grade D if average is between 50–59
    else:
        return "Fail"  # Return Fail if average is below 50


# This loop keeps the program running until the user chooses to exit
while True:
    # Display program title/menu
    print("\n--- Student Grade System ---")
    
    marks = []  # Create an empty list to store subject marks
    
    # Ask user how many subjects they want to enter
    subjects = int(input("Enter number of subjects: "))

    # Loop through each subject and collect marks
    for i in range(subjects):
        # Ask user to enter marks for each subject
        score = int(input(f"Enter marks for subject {i+1}: "))
        
        # Add the entered score to the marks list
        marks.append(score)

    # Calculate the average by dividing total marks by number of subjects
    average = sum(marks) / len(marks)

    # Call the function to determine grade based on average
    grade = calculate_grade(average)

    # Display the calculated average
    print("\nAverage Score:", average)
    
    # Display the final grade
    print("Final Grade:", grade)

    # Ask user if they want to run the program again
    choice = input("\nDo you want to continue? (yes/no): ").lower()
    
    # If user types anything other than 'yes', exit the loop
    if choice != "yes":
        print("Exiting program...")  # Display exit message
        break  # Stop the program
