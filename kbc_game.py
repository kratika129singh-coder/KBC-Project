print("=============Welcome to Kaun Banega CrorePati=============")
questions=[
   { "question" :"Who was india's first woman lead in political field",
     "option" :["A. Pratibha Patel","B.Indra Gandhi","C.Rani LaxmiBai","Sarojini Naidu"],
     "answer":"B",
     "prize":1000
    },
    {
       "question" :"what is the captial of India ",
       "option" :["A. Mumbai", "B. Kolkata", "C. New Delhi", "D. Chennai"],
       "answer":"C",
       "prize":1000
    }
  ]
total_won=0
for q in questions:
    print("/n" +q["question"])
    for op in q["option"]:
        print(op)

user_ans=input("Select your Answer(A/B/C/D) : ").upper()
if user_ans==q["answer"]:
    total_won=q["prize"]
    print(f"Correct Answer! you won ${total_won}") 
else:
    print("Ohhh Wrong Answer! Khel khatam bro ")