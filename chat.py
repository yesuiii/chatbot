import streamlit as st
import pickle

# Load the scraped AUM data
with open("aum_data.pkl", "rb") as f:
    aum_data = pickle.load(f)

# AUM page links
pages = {
    'home': 'https://aum.edu.mn/',
    'academics': 'https://aum.edu.mn/en/academics/',
    'why_aum': 'https://aum.edu.mn/en/why-aum/',
    'admission': 'https://aum.edu.mn/en/admission/',
    'international_students': 'https://aum.edu.mn/en/international-students/',
    'study_abroad': 'https://aum.edu.mn/en/study-abroad/',
    'enrollment_exam': 'https://aum.edu.mn/en/enrollment-exam/',
    'graduate_degrees': 'https://aum.edu.mn/en/graduate-degrees/',
    'study_in_usa': 'https://aum.edu.mn/en/study-in-usa/',
    'extraccuricular_activities': 'https://aum.edu.mn/en/extraccurricular-activities/',
    'faculty': 'https://aum.edu.mn/en/faculty/',
    'data_science': 'https://aum.edu.mn/data-science/',
    'masters_in_data_science': 'https://aum.edu.mn/en/masters-in-data-science/',
    'mba': 'https://aum.edu.mn/en/mba/'
}

# Set up the page title and chatbot
st.set_page_config(page_title="AUM Chatbot", page_icon="🎓")
st.title("🎓 American University of Mongolia Chatbot")
st.write("Hello! I'm here to help with any questions you have about AUM. Please ask away.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input (chat input box)
user_input = st.chat_input("How can I assist you today?")

import re

unwanted_phrases = [
    "info@aum.edu.mn", "Instagram", "Facebook", "© American University of Mongolia",
    "Phone:7272-2626", "Home", "Academics", "Course catalog", "Study in USA",
    "Extracurricular activities", "Faculty", "Data Science", "Why AUM", "Admission",
    "International students", "Study Abroad", "Enrollment Exam", "Graduate Degrees",
    "Masters in Data Science", "MBA", "Submit new student application", "Reserve your seat by submitting reservation fee",
    "Complete student interview", "Sign new student contract and submit documents",
    "(OPTIONAL) Submit scholarship application"
]


def clean_answer(answer):
    for phrase in unwanted_phrases:
        answer = answer.replace(phrase, "")
    # Optionally remove extra spaces after the cleaning process
    answer = re.sub(r'\s+', ' ', answer).strip()
    return answer

def get_relevant_answer(question):
    question = question.lower()

    # Define keywords to match question categories and provide detailed, polite responses

    if "admission" in question or "apply" in question:
        admission_info = aum_data.get('admission', 'No specific admission details found.')
        return (
            f"Thank you for your interest in applying to AUM. Here's the information about the admission process:\n\n"
            f"{admission_info}\n\n"
            f"For more information, please visit the [Admission Page](https://aum.edu.mn/en/admission/)."
        )
    
    elif "academic" in question or "program" in question or "major" in question:
        academics_info = aum_data.get('academics', 'No specific academic details found.')
        return (
            f"At AUM, we offer a range of academic programs designed to provide a well-rounded education. Here's some information about our academics:\n\n"
            f"{academics_info}\n\n"
            f"To explore all available programs, please visit our [Academics Page](https://aum.edu.mn/en/academics/)."
        )
    
    elif "why aum" in question or "choose aum" in question:
        why_aum_info = aum_data.get('why_aum', 'No specific reasons found.')
        return (
            f"We are delighted you're considering AUM! Here's why AUM stands out:\n\n"
            f"{why_aum_info}\n\n"
            f"Learn more about why AUM is a great choice by visiting our [Why AUM Page](https://aum.edu.mn/en/why-aum/)."
        )
    
    elif "international students" in question:
        international_students_info = aum_data.get('international_students', 'No specific details found for international students.')
        return (
            f"Here's some important information for our international students:\n\n"
            f"{international_students_info}\n\n"
            f"Please refer to our [International Students Page](https://aum.edu.mn/en/international-students/) for more details."
        )
    
    elif "enrollment exam" in question or "exam" in question:
        enrollment_exam_info = aum_data.get('enrollment_exam', 'No specific enrollment exam details found.')
        return (
            f"Thank you for your inquiry about the enrollment exam. Here's what you need to know:\n\n"
            f"{enrollment_exam_info}\n\n"
            f"To learn more, please visit our [Enrollment Exam Page](https://aum.edu.mn/en/enrollment-exam/)."
        )
    
    elif "graduate" in question or "masters" in question or "phd" in question:
        graduate_degrees_info = aum_data.get('graduate_degrees', 'No specific graduate degree details found.')
        return (
            f"We offer a variety of graduate degree programs. Here's more information about our graduate degrees:\n\n"
            f"{graduate_degrees_info}\n\n"
            f"To explore graduate programs further, please visit our [Graduate Degrees Page](https://aum.edu.mn/en/graduate-degrees/)."
        )
    
    elif "study abroad" in question:
        study_abroad_info = aum_data.get('study_abroad', 'No specific study abroad details found.')
        return (
            f"Interested in studying abroad? Here's what you need to know:\n\n"
            f"{study_abroad_info}\n\n"
            f"Find out more by visiting our [Study Abroad Page](https://aum.edu.mn/en/study-abroad/)."
        )
    
    elif "faculty" in question:
        faculty_info = aum_data.get('faculty', 'No specific faculty details found.')
        return (
            f"AUM is proud to have a distinguished faculty. Here's more information about our faculty:\n\n"
            f"{faculty_info}\n\n"
            f"To learn more about our faculty, please visit our [Faculty Page](https://aum.edu.mn/en/faculty/)."
        )

    # Additional pages and sections can be added as needed

    # Default response if no match is found
    else:
        return (
            "I'm sorry, I wasn't able to find an answer to that specific question. "
            "Please feel free to ask about admissions, academics, or any general AUM-related topics. "
            "I'm here to help!"
        )

# Process user input and generate response
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Call function to get the relevant answer
    response = get_relevant_answer(user_input)

    # Add bot's response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

    # Display the bot's response in the chat
    with st.chat_message("assistant"):
        st.markdown(response)

