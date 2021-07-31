from Question import Question

question_prompts=["Guess the age of our universe?\na)13.8 billion yrs\nb)25 trillion yrs\nc)100  billion yrs\n","Choose the brightest star outside of solar system?\na)Virgo\nb)Sirius A\nc)Alpha Centauri\n"
]                 
                  
questions = [ 
                   Question(question_prompts[0],"a"),
                   Question(question_prompts[1],"b"),
            ]  
            
    
# win - +1 , wrong answer - -0.25 and invalid option - -0.5
def run_test(questions):
    score = 0
    for question in questions:
        
        answer = input(question.prompt)
        
        if answer == question.answer:
           
           score += 1
           
        elif  answer != question.answer and answer in "abc":
            print("Wrong Guess\n")
            score -= 0.25
        
        else:
            print("Invalid option")
            
            score -= 0.5   
    
    print("Total:")
    print (" You got " + str(score) + "/" + str(len(questions)) + " correct.")       
   
run_test(questions) 
