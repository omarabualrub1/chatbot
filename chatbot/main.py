import tkinter as tk
from tkinter import scrolledtext
import json
import re
import nltk
import random
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Load the data from the JSON file
with open('data.json', 'r') as file:
    data = json.load(file)

# Download NLTK resources (if not already downloaded)
nltk.download("punkt")
nltk.download("stopwords")


greetings = ["Hello! How can I assist you today?", "Hi there! What can I do for you?", "Greetings! How may I help you?"]
than_k = ["ok thank you !", "Good Bye !", "Have a nice day :)"]

department_mandatory_requirements = [
    "AI 484", "AI 240", "AI 244", "AI 249", "AI 328", "AI 342", "AI 350",
    "AI 484", "AI 452", "AI 453", "AI 454", "AI 455", "AI 457", "AI 471",
    "AI 474", "AI 477", "AI 481", "AI 482", "AI 483", "AI 484", "AI 485",
    "AI 490", "AI 491", "AI 492", "AI 495-I", "AI 495-II", "AI 495-III"
]

# Create a simple chatbot
faculty_requirements = [
    "MATH 101", "MATH 102", "MATH 241", "CS 101", "SE 103", "SE 112", "CS 211", "MATH 241", "CIS 221"
]
first_year_courses = """
{{1st Semester}}
Course Number || Course Name || # CH || Prerequisite
CS 101 || Introduction to Programming || 3 || CIS 99 (or concurrent)
CS 101 || (Practical) Introduction to Programming || 0 || Concurrent with CS101
SE 103 || Introduction to IT || 3 || CS 101 (or concurrent)
Math 101 || Calculus I || 3 || -
Math 241 || Discrete Mathematics || 3 || -
HSS 110 || Leader and Social Responsibility || 3 ||  -
LG 101 || Communication Skills in English || 3 || Pass LG 099 or passing English exam
Total : 18

{{2nd Semester}}
SE 112 || Introduction to Object-Oriented Programming || 3 || Passing CS 102
SE 112 ||(Practical)Introduction to Object-Oriented Programming || 0  ||  Concurrent with SE 112
CS 211 || Data Structures || 3 ||  Math 241 and passing SE 112
Math 140 ||  Linear Algebra || 3 || Math 101
Math 102 || Calculus 2 || 3  || Math 101
CIS 203 || Communication and Professional Ethics || 2 ||  -
Total : 14
"""
second_year_courses = """
## 2 Year - 1st Semester

CS 284: Analysis and Design of Algorithms: 3 :CS 211 + Math 233
Math 233 : Probability & Statistics (for CS students): 3 : Math 102
CIS 201: Introduction to Web Design: 1 : SE 112 
CIS 221: Fundamentals of Database Systems: 3 : CS 211 
ARB 102: Communication Skills in Arabic: 3  : -
University Elective: 3 :-
 **Total** | 16 |

## 2 Year - 2nd Semester

| Course Number|Course Name| # CH | Prerequisite|

AI 240: Introduction to Artificial Intelligence: 3 :CS 284  
AI 244: Artificial Intelligence Programming: 3 : CS 101  
AI 244: Artificial Intelligence Programming(Practical): 0  : Concurrent with AI 244 
MS 100: Military Science: 3 :  -   
AI 249: Machine Learning: 3 : AI 244  
LG 103: Life Skills: 2 : -   
University Elective : 3 : -   
 **Total** | 17  |
"""
third_year_courses = """
## 3rd Year - 1st Semester

Course Number | Course Name | # CH | Prerequisite                

AI 375: Operating Systems : 3 : CS 284
AI 328: Big Data Processing: 3  : CIS 221
AI 375: Digital Image Processing: 3 : CS 284 + Math 140
AI 380: Optimization Algorithms: 3 : CS 284 + AI 244 
HSS 119: Entrepreneurship and Innovation: 2  : - 
University Elective : 3 : - 

 **Total**  | 17  |                              

## 3rd Year - 2nd Semester

Course Number | Course Name | # CH | Prerequisite

AI 350: Data Science: 3 : AI 328
AI 342: Deep Learning: 3 : AI 249
AI 356: Information Retrieval: 3  : AI 249
AI 378: Smart Systems: 3 : CS 375
Department Elective : 3 : - 

 **Total** | 15  |

## 3rd Year - 3rd Semester (Summer)

Course Number | Course Name | # CH | Prerequisite

AI 490: Internship: 3 : Passing 90 CHs or department approval 

 **Total**| 3 |
"""
fourth_year_courses = """
## 4th Year - 1st Semester

Course Number | Course Name | # CH | Prerequisite

AI 445: Natural Language Processing: 3 : AI 342
AI 447: Computer Vision: 3  : AI 342 + AI 375
AI 471: Artificial Intelligence for Games: 3  : AI 342
AI 477: Robotics: 3 : AI 342
AI 491: Graduation Project (1): 2 : Passing 90 CHs 
Department Elective: 3 : - 

 **Total** | 17 |

## 4th Year - 2nd Semester

Course Number | Course Name | # CH | Prerequisite

AI 446: Audio and Speech Processing: 3 : AI 342
AI 448: Deep Reinforcement Learning: 3 : AI 342
AI 474: Extended Reality: 3 : AI 447
AI 492: Graduation Project (2): 3 : AI 491
Department Elective: 3 : -

 **Total**| 15 |
"""
objectives = """
       The objective of the B.Sc. in AI program is to produce graduates that will be able to:
       1. PEO1 (Problem Solving): Gain in-depth knowledge of Computing and Artificial Intelligence
          principles and techniques and apply them effectively and proficiently to solve real-life problems.
       2. PEO2 (Self-Motivated and Life-Long Learning): Promote sustainable learning by developing
          transferable skills and knowledge to keep up with the evolving Artificial Intelligence
          technologies, meet the demands of the rapidly changing labor market, and pursue higher degrees
          in different subfields of Artificial Intelligence.
       3. PEO3 (Leadership and Teamwork): Improve the ability to work effectively and productively as a
          leader or a team member toward accomplishing common goals.
       4. PEO4 (Community Support): Maintain strong relationships with the local, regional, and
          international communities by contributing to economic growth and social development.
       """
mission = """To realize our mission, the CS department works to:
Emphasize high-quality teaching and research, dedication to community services, and partnership with industry.
Maintain high-quality undergraduate and graduate programs that deliver advanced knowledge in computer science while 
allowing prompt response to the needs of the local community."""
outcomes = """
        Graduates of the AI program will have the ability to:
        1. Analyze a complex computing problem and to apply principles of computing and other relevant
           disciplines to identify solutions.
        2. Design, implement, and evaluate a computing-based solution to meet a given set of computing
           requirements in the context of the program’s discipline.
        3. Communicate effectively in a variety of professional contexts.
        4. Recognize professional responsibilities and make informed and equitable judgments in computing
           practice based on legal and ethical principles.
        5. Function effectively as a member or leader of a team engaged in activities appropriate to the
           program’s discipline.
        6. Apply computer science and artificial intelligence theory and software development fundamentals
           to produce computing-based solutions.
        """
university_requirements = {
    "Mandatory": 16,
    "Elective": 9,
    "Total": 25
}
math = """Math 233:Probability & Statistics 
          Math 140:Linear Algebra
          Math 101:Calculus 1 
          Math 102:Calculus 2
          Math 241:Discrete Mathematics"""

it = """CS-101:An introduction to programming concepts using a high-level language. Topics include algorithm development
         , debugging, and problem-solving. Laboratory exercises provide hands-on experience in programming."""
oop = """SE-112:Introduction to Object-Oriented Programming introduces object-oriented programming concepts. 
        Topics include classes, objects, inheritance, polymorphism, and basic software design principles."""
features = """Entering the field of artificial intelligence (AI) provides several advantages,
              including involvement in cutting-edge technology
              and innovation, diverse applications across industries, high demand for skills leading to competitive salaries,
              a wide range of career opportunities, global impact potential, continuous learning opportunities, 
              flexibility for remote work, interdisciplinary collaboration, and possibilities for entrepreneurship. 
              The dynamic nature of AI offers an intellectually stimulating environment with the chance to contribute
               to solving real-world problems."""


total_hours_ai_major = 132


class ChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Course Chatbot")
        self.root.geometry("850x435")

        self.robot_image = tk.PhotoImage(file="chatbot-image.png")  # Replace with your image file path

        robot_label = tk.Label(self.root, image=self.robot_image)
        robot_label.place(x=0, y=0)

        self.text_area = scrolledtext.ScrolledText(self.root, width=60, height=15, wrap=tk.WORD,bg="white",
                                                   font=('Helvetica', 15, 'bold'))
        self.text_area.place(x=10, y=10)



        self.user_input = tk.Entry(self.root , width=40)
        self.user_input.place(x=10, y=400)

        self.submit_button = tk.Button(self.root, text="Send", command=self.submit_message, fg="black",
                                       font=('Helvetica', 9, 'bold'))
        self.submit_button.place(x=275, y=395)


        self.initialize_chat()

    def initialize_chat(self):
        self.display_message("           Hello! How can I help you with your AI courses?")

    def submit_message(self):
        user_message = self.user_input.get()
        self.display_message(f"User: {user_message}")

        # Process user input and generate a response
        response = self.process_user_input(user_message)

        # Display the chatbot's response
        self.display_message(f"*Chatbot*: {response}")

        # Clear the user input field
        self.user_input.delete(0, tk.END)

    def process_user_input(self, user_message):
        # Tokenize the user's input
        tokens = word_tokenize(user_message)

        # Remove stopwords
        stop_words = set(stopwords.words('english'))
        filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

        # Create a regular expression pattern for course codes
        course_code_pattern = re.compile(r'\b[A-Za-z]+\s*\d{3}\b')

        # Look for a course code in the filtered tokens
        course_code_matches = course_code_pattern.findall(' '.join(filtered_tokens))

        # Check if the query is about faculty requirements

        if "faculty requirements" in user_message.lower() or "faculty courses" in user_message.lower():
            total_hours_faculty_requirements = 24
            return (f"Faculty Requirements: {', '.join(faculty_requirements)}\nTotal Hours:"
                    f" {total_hours_faculty_requirements} hours")

        # Check if the query is about department mandatory requirements
        elif "department mandatory requirements" in user_message.lower():
            total_hours_department_mandatory_requirements = 74
            return (f"Department Mandatory Requirements: {', '.join(department_mandatory_requirements)}\nTotal Hours:"
                    f" {total_hours_department_mandatory_requirements} hours")

        # Check if the query is about the "Vision" course
        elif "vision" in user_message.lower():
            return ("The Vision course focuses on staying at "
                    "the top of computer science departments in Jordan and moving toward a world-class distinguished"
                    " department through high-quality teaching and research.")
        elif "university requirements" in user_message.lower():
            return (f"University Requirements:\nMandatory: {university_requirements['Mandatory']} hours\nElective:"
                    f" {university_requirements['Elective']} hours\nTotal: {university_requirements['Total']} hours")

            # Check if the query is about the total hours for University Requirements
        elif "how many hours" in user_message.lower() and "university requirements" in user_message.lower():
            total_hours_university_requirements = university_requirements["Total"]
            return f"Total Hours for University Requirements: {total_hours_university_requirements} hours"

        elif ("ai major" in user_message.lower() or "AI major" in user_message.lower() or "Ai major"
              in user_message.lower()):
            return f"Total Hours for AI Major: {total_hours_ai_major} hours"
        elif ("first year" in user_message.lower() or "1st year" in user_message.lower() or "year one"
              in user_message.lower()):
            return first_year_courses
        elif ("2nd year" in user_message.lower() or "year two" in user_message.lower() or "second year"
              in user_message.lower()):
            return second_year_courses
        elif ("3rd year" in user_message.lower() or "year three" in user_message.lower() or "third year"
              in user_message.lower()):
            return third_year_courses
        elif ("4th year" in user_message.lower() or "year four" in user_message.lower() or "fourth year"
              in user_message.lower()):
            return fourth_year_courses
        elif "objectives" in user_message.lower():
            return f"Objectives: {objectives}"
        elif "mission" in user_message.lower():
            return f"Mission: {mission}"
        elif "outcomes" in user_message.lower():
            return f"Outcomes: {outcomes}"
        elif "math" in user_message.lower():
            return f"Math : {math}"
        elif "C++" in user_message.lower() or "c++" in user_message.lower():
            return f"C++ : {it}"
        elif "oop" in user_message.lower() or "Oop" in user_message.lower() or "OOp" in user_message.lower():
            return f"Oop : {oop}"
        elif ("no" in user_message.lower() or "thank you" in user_message.lower() or "thanks" in user_message.lower() or
              "ok" in user_message.lower()):
            return random.choice(than_k)
        elif ("advantages" in user_message.lower() or "advantage" in user_message.lower() or "features"
              in user_message.lower()):
            return features
        elif user_message.lower() == "hi":
            return "Hi there! What can I do for you?"


        elif any(word in user_message.lower() for word in ["hello", "how are you"]):
            return random.choice(greetings)



        if course_code_matches:
            # Extract the first course code found
            course_code = course_code_matches[0].upper()

            # Look up the course information in the JSON data
            for course in data["courses"]:
                if course["code"].upper() == course_code:
                    # Check if the user is asking for the title
                    if any(word in filtered_tokens for word in ["title", "name"]):
                        return course["title"]

                    # Check if the user is asking for the credit hours
                    elif any(word in filtered_tokens for word in ["credit", "hours", "hour"]):
                        return f"{course['title']} Credit Hours: {course['credit_hours']}"

                    # Check if the user is asking for prerequisites
                    elif any(word in filtered_tokens for word in ["prerequisite", "Prerequisite", "requirement",
                                                                  "Requirement"]):
                        prerequisite = course.get("prerequisite", "None")
                        return f"{course['title']} Prerequisite: {prerequisite}"

                    # Default response with full information
                    else:
                        title = course["title"]
                        credit_hours = course["credit_hours"]
                        prerequisite = course.get("prerequisite", "None")

                        response = f"{title} ({credit_hours}): {course['description']}\nPrerequisite: {prerequisite}"
                        return response

        return "I'm sorry, but I couldn't find information ."


    def display_message(self, message):
        self.text_area.insert(tk.END, f"{message}\n")
        self.text_area.yview(tk.END)

# Main part of the code
if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotApp(root)
    root.mainloop()
