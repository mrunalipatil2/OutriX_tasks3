import random

# Questions stored directly in Python (list of dictionaries)
questions = [
    {
        "question": "What is the capital of India?",
        "options": {"A": "Delhi", "B": "Mumbai", "C": "Chennai", "D": "Kolkata"},
        "answer": "A"
    },
    {
        "question": "Which language is used for Artificial Intelligence?",
        "options": {"A": "Python", "B": "C", "C": "Java", "D": "HTML"},
        "answer": "A"
    },
    {
        "question": "Who developed the C language?",
        "options": {"A": "Dennis Ritchie", "B": "James Gosling", "C": "Bjarne Stroustrup", "D": "Guido van Rossum"},
        "answer": "A"
    },
    {
        "question": "2 + 2 = ?",
        "options": {"A": "3", "B": "4", "C": "5", "D": "6"},
        "answer": "B"
    },
    {
        "question": "Which company developed the Java language?",
        "options": {"A": "Microsoft", "B": "Sun Microsystems", "C": "Apple", "D": "Google"},
        "answer": "B"
    }
]

# Function to run quiz
def run_quiz(questions):
    score = 0
    random.shuffle(questions)  # Randomize question order

    print("\n===== Welcome to the Quiz App =====\n")
    for i, q in enumerate(questions, 1):
        print(f"Q{i}: {q['question']}")
        for option, text in q["options"].items():
            print(f"   {option}. {text}")
        
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()
        
        if user_answer == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! Correct Answer: {q['answer']}\n")
    
    print("===== Quiz Finished =====")
    print(f"Your final score: {score}/{len(questions)}")

# Main Execution
if __name__ == "__main__":
    run_quiz(questions)
