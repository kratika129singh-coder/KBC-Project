print("=============Welcome to Kaun Banega CrorePati=============")
questions=[{ "question" :"Who was india's first woman lead in political field",
             "option" :["A. Pratibha Patel","B.Indra Gandhi","C.Rani LaxmiBai","Sarojini Naidu"],
             "answer":"B",
             "prize":1000
           },
           {
             "question" :"what is the captial of India ",
             "option" :["A. Mumbai", "B. Kolkata", "C. New Delhi", "D. Chennai"],
             "answer":"C",
             "prize":1000
          },
         {
            "question":"what is the famous Mathura's Sweet",
            "option" : ["A. Lassi","B. Pede","C. laduu","D. Barfi"],
            "answer":"B",
            "prize":1000
         }
  ]
total_prize=0

print("="*40)
print("Welcome To Kaun Banega CrorePati")
print("="*40)

for q in questions:
    print(f"Question:-{q['question']}")
    
    for op in q["option"]:
        print(f"{op}")

    user_ans=input("Select your Answer(A/B/C/D) : ").strip().upper()

    if user_ans==q["answer"]:
       total_prize+=q["prize"]
       print(f"Correct Answer! you won ${total_prize}")
       print("="*40) 
    else:
       print("Ohhh Wrong Answer! Khel khatam bro ")
       print(f"Game Over! you are taking this prize {total_prize} to your home")
else:
   print(f"congratsyou selected all the ansewer correct { total_prize}")