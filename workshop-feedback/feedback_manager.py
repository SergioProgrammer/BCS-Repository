# Question 1

raw_feedback = " THE SPEAKER WAS GREAT but THE ROOM WAS COLD "

s = raw_feedback.strip().lower()

s = s.replace("speaker", "presenter")

s = " ".join(s.split())

cleaned_feedback = s.title()

print(f"Cleaned feedback: {cleaned_feedback}")

 

# Question 2

feedback_list = [

    cleaned_feedback,

    "The Workshop Was Useful And Well Organized",

    "Great Examples Made The Topic Easy To Understand"

]

with open("feedback.txt", "w", encoding="utf-8") as file:

    for feedback in feedback_list:

        file.write(feedback + "\n")

print("\nInitial feedback:")

with open("feedback.txt", "r", encoding="utf-8") as file:

    for line in file:

        print(line.rstrip("\n"))

with open("feedback.txt", "a", encoding="utf-8") as file:

    file.write("The Activities Were Great And Engaging\n")

print("\nUpdated feedback:")

with open("feedback.txt", "r", encoding="utf-8") as file:

    for line in file:

        print(line.rstrip("\n"))

 

# Question 3

# Call this function separately to test a missing file.

def read_feedback_safely():

    try:

        with open("feedback.txt", "r", encoding="utf-8") as file:

            for line in file:

                print(line.rstrip("\n"))

    except FileNotFoundError:

        print("File not found. Please create feedback.txt first.")

    except PermissionError:

        print("Permission denied. Close the file and try again.")

    finally:

        print("Operation completed.")

print("\nSafe reading:")

read_feedback_safely()

 

# Question 4

try:

    with open("feedback.txt", "r", encoding="utf-8") as file:

        feedback_lines = file.readlines()

    total_feedback = len(feedback_lines)

    great_mentions = 0

    for feedback in feedback_lines:

        if "great" in feedback.lower():

            great_mentions += 1

    summary = (

        f"=== Workshop Feedback Summary ===\n"

        f"Total Feedback: {total_feedback}\n"

        f"Mentions of 'Great': {great_mentions}\n"

    )

    with open("summary.txt", "w", encoding="utf-8") as file:

        file.write(summary)

    print(f"\n{summary}", end="")

except FileNotFoundError:

    print("File not found. Please create feedback.txt first.")

except PermissionError:

    print("Permission denied. Close the file and try again.")

