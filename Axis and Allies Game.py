import sys
import random

def speak_out():

    ch_yes = ['yes', 'y', 'yeah', 'yer', 'ja']
    ch_no = ['no', 'n', 'nah', 'nein']

    response = input("Today is the fifth night in a row where you have stayed awake until daybreak toiling over the idea of deserting your squad. Do you try to persuade some of your men to go with you? Answer: Yes or No? \n").lower()
    
    while response not in ch_yes and response not in ch_no:
    
        response = input("You don't have much more time to think this over, the sun is already peaking through your window. Answer: Yes or No? \n").lower()
        
    if response in ch_yes:
        return True

    else: 
        return False
        

def persuasion_attempt():
    
    ch_yes = ['yes', 'y', 'yeah', 'yer', 'ja']
    ch_no = ['no', 'n', 'nah', 'nein']

    response = input("During breakfast you realize it is now or never to get your squad on your side. You have the idea to stand on the table and denounce the Nazis along with Hitler. You also plan to invite your men to join you in leaving the Nazi Army, and heading to Switzerland, but you also realize the danger of this choice. Do you go through with your idea? Answer: Yes or No? \n").lower()
    
    while response not in ch_yes and response not in ch_no:
    
        response = input("Now is the best timeto do it, if you're going to do it at all. Yes or No? \n").lower()
    
    if response in ch_yes:
            return True
    
    else:
        return False


def when_leave_alone():

    ch_yes = ['night']
    ch_no = ['day']

    response = input("You have chosen to keep your plan to youself. Do you leave during the day or the night? \n").lower()
    
    while response not in ch_yes and response not in ch_no:
        
        response = input("You ARE leaving today, do you leave during the day or at night? \n").lower()
    
    if response in ch_yes:
        return True
    
    else:
        return False


def escape_day():

    ch_yes = ['kill']
    ch_no = ["run"]

    response = input("You have been found trying to leave the barracks with your bag and rifle by one of your Pvts. He questions where you are going and why you have all of your equipment, but your anxiety causes you to studder which kills any chance of lying to him. Do you kill him or run away? \n").lower()
    
    while response not in ch_yes and response not in ch_no:        
        
        response = input("You have to do something! The Pvt is starting to get alarmed. Do you kill him or run?!? \n").lower()
    
    if response in ch_yes:
        return True    
    
    else:
        return False



def how_leave_group():

    ch_yes = ['a truck', 'truck', 'the truck']
    ch_no = ['on foot', 'walk', 'leave on foot']
    
    response = input("Your electrifying speech and your position as a general convince your men to join and aid you on your escape to Switzerland. Do you leave on foot or in a truck? \n").lower()
    
    while response not in ch_yes and response not in ch_no:
        
        response = input("Your men are fired up and ready to leave now. It wouldn't be good to let them think on what they have just agreed to. Do you take the truck, or leave on foot? \n").lower()
    
    if response in ch_yes:
        return True
    
    else:
        return False


def air_strip(): 

    ch_yes = ['ram', 'ram the fence']
    ch_no = ['pass', 'pass the air-strip', 'drive']

    response = input("On your way to Switzerland you come across an air strip with a pristine bomber left unattended at one end of the runway. Do you ram the fence or pass the air-strip? \n").lower()
    
    while response not in ch_yes and response not in ch_no:
        
        response = input("Hurry up and choose! You are going to reach a turn in the road. Do you ram the fence or pass the air-strip? \n").lower()

    if response in ch_yes:
        return True
    
    else:
        return False


def fly_plane():
    
    ch_yes = ['yes', 'y', 'yeah', 'yer', 'ja']
    ch_no = ['no', 'n', 'nah', 'nein']

    response = input("You decided to ram the fence and are inside the air strip. Soon you will be pulling alongside the bomber, but right now you are really rethinking your decision. The alarm has been sounded but one of your Pvts, Pvt Seth says that she can fly. Do you let her fly? Answer: Yes or No? \n").lower()
    
    while response not in ch_yes and response not in ch_no:
       
        response = input("Hurry up and choose! The guards are assembling and closing in on your position! Answer: Yes or No? ").lower()
  
    if response in ch_yes:
        return True
  
    else:
        return False


def make_it():

    ch_yes = ['yes', 'y', 'yeah', 'yer', 'ja']
    ch_no = ['no', 'n', 'nah', 'nein']

    response = input("You let Pvt. Seth fly the plane. She got the plane into the air, luckily, but it is apparent she in over her head. Do you relieve them of their position and fly the bomber youself? Answer: Yes or No? \n").lower()
    
    while response not in ch_yes and response not in ch_no:
        
        response = input("Your men are looking to you for an answer, they don't want to crash. Do you take over? Answer: Yes or no? \n").lower()

    if response in ch_yes:
        return True
    
    else:
        return False


print ("Greetings player!!! Thank you for playing my game!!! This game is very simple, answer each question in an attempt to flee the Nazis.\n")
print ("   \n")
print ("Your name is Hanz Frankfurter and you are a general in the Nazi army. There are many men like you, but unlike all of them, you hold a burning hatred for the Nazis and the atrocities committed against the Jewish people.\n")
print ("   \n")
print ("You are stationed in a village on the outskirts of Berlin with a squad of five men under you. You suspect that some or all of your men share your hatred of the Nazis, however you have been too scared of the punishment for treason.\n")
print ("   \n")
print ("For the past year you have dreamt of deserting your post and fleeing to the snowcapped mountains of neutral Switzerland. However, you realize that your plan is impossible without help.\n")
print ("   \n")


ch_speak = speak_out()
if ch_speak:

    ch_rally = persuasion_attempt()
    if ch_rally:

        print("Your men are moved by your passionate speech and decide to join you.\n")

        ch_Gleave = how_leave_group()
        if ch_Gleave:

            print ("You and your squad drive for an hour or so and come upon an air-strip where someone has left a pristine bomber out.\n")

            ch_plane = air_strip()
            if ch_plane:

                ch_fly = fly_plane()
                if ch_fly:

                    print ("You are sailing through the skies, only hitting a small amount of turbulence. Pvt. Seth does far better than you expected. You make it to Switzerland with a rough landing, but you are so relieved. You and your men are taken to a jail and questioned, but once the MP's hear your story they give you a medal of Honor!!! Congratulations you made it out alive!!!\n")

                else: 

                    print ("You try to fly the bomber but are not nearly skilled enough and fly into a thicket of trees. You end up as a Nazi kabab.\n")

            else: 

                print ("You continue down the road for a little until you come upon a road block. All of the guns are trained right through your windows and in that moment you realize someone has noticed your absence and the turd on the Nazi flag. You and your squad are turned into red mashed potatoes by the MG42's\n")

        else: 

            print ("While walking down the road your squad sees a path through the woods that looks to be a shortcut. You take the path and a group of children jump from the trees and kill you.\n")

    else: 

        print ("As you are proclaiming your hate for the Nazis, a stray artillery shell hits you and turns you into a fine red mist. Was it God? Sadly it was not, it was Marcus playing with mortars.\n")

else:   

    ch_Aleave = when_leave_alone()
    if ch_Aleave:

        print("While walking in the dark you walk into a minefield and become the first Nazi astronaut.\n")

    else: 

        ch_day = escape_day()
        if ch_day:

            print ("Your comrades hear you kill the Pvt. who found you. They surround you and beat you to death with comically large german sausages.\n")
        
        else: 

            print ("In your haste to leave you run behind the firing range and get turned into Swiss Cheese, karma has never been so fair.")
