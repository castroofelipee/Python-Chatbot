import random

R_EATING = "i don't like eating anything beacuse i'm a bot"
R_ADVICE = "if i were you, i would go to the internet and type what you wrote there!"

def unknown():
    response = ["Could you please re-phrase that? ,"
                "...", 
                "Sounds about right."
                "what does that mean?"][
                    random.randrange(4)
                ]
    
    return response 