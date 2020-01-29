import sys:

ch_yes = ["1."]
ch_no = ["2."]


def speak_out():

    response = input("After your fifth sleepless night toiling with the idea of deserting your country and going AWOL, you have broken. Do you try to persuade some of your men to go with you, Yes or No?\n").lower()
    
    while response not in ch_yes and response not in ch_no:
        
        response = input("You don't have much time to think this over, the sun is already peaking through your window, answer Yes or No\n").lower()
        
        if response in affirm_resp:
            return True
        
        else:
            return False

def persuasion_attempt():

     response = input("During breakfast you decide it is now or never to get your men on your side. You want to stand on the table and proclaim your hatred of the Nazis and your plan to head to Switzerlad, but you also realize the danger of this. Do you go through with your idea, Yes or No?\n").lower()

    while response not in ch_yes and response not in ch_no:
        
        response = input("Now is the best time if you're going to do it. Yes or No?\n").lower()

    if response in ch_yes:
        return True
    
    else:
        return False


ch_yes = ['night']
ch_no = ['day']
def when_leave_alone():

     response = input("You have chosen to keep your disdain for Hitler to youself. Do you leave during the day or the night?\n").lower()

    while response not in ch_yes and response not in ch_no:
        
        response = input("You ARE leaving today, do you leave during the day or at night?\n").lower()

    if response in ch_yes:
        return True
    
    else:
        return False

ch_yes = ['kill']
ch_no = ["run"]
def escape_day():

    response = input("You have been found trying to leave with your bag by one of your Privates. He questions where you are going but your anxiety kills any chance of lying. Do you kill him or run away?\n").lower()

    while response not in ch_yes and response not in ch_no:
        
        response = input("You have to do something! The private is starting to get alarmed. Do you kill him or run?\n").lower()

    if response in ch_yes:
        return True
    
    else:
        return False


ch_yes = ['a truck', 'truck']
ch_no = ['on foot', 'walk']
def when_leave_group():

    response = input("Your electrifying speech and your position as a general convince your men to aid and join your escape to Switzerland. Do you leave on foot or in a truck?\n").lower()

    while response not in ch_yes and response not in ch_no:
        
        response = input("Your men are fired up and ready to leave now, it wouldn't be good to let them think about what they are doing. Do you take the truck, or leave on foot?\n").lower()

    if response in ch_yes:
        return True
    
    else:
        return False

ch_yes = ['ram', 'ram the fence']
ch_no = ['pass', 'pass the air-strip']
def air_strip(): 
    
    response = input("On your way to Switzerland you come across an air strip with a pristine bomber left unattended at one end of the runway. Do you ram the fence or pass the air-strip?/n")
    while response not in ch_yes and response not in ch_no:
        
        response = input("Hurry up and choose! You are going to reach a turn in the road. Do you ram the fence or pass the air-strip?").lower()

    if response in ch_yes:
        return True
    
    else:
        return False



print ("Greetings player!!! Thank you for playing my game!!! The instructions are simple, answer each question in an attempt to save yourself from the horrors of Nazi enlistment.")
print ("Your name is General Hanz Frankfurter and you are a general in the Nazi army. Unlike most people in your position, you have a deep resentment for the Nazis and the terrible actions they have devoted themselves to.")
print ("You are stationed in an outer villige of Berlin with a squad of five men. You suspect that your men may share your hatred of the Nazis, however you have been too scared of the punishment for treason.")
print ("You dream of deserting your post and fleeing to the snowcapped mountains of neutral Switzerland. You realize that this is only but a fanstasy.")

ch_speak = speak_out()

if ch_speak:

