#starting the program
print("Small note: 1 is start. and 0 symbolises as dont start")
start_story = int(input("Start? type 1 or 0 : "))
#Logic code
if start_story == 0:
    print("Ok then play again soon")


if start_story == 1:
    print("You just waken up eh?")
    print("Im Xander that guy who always end his dialogue with eh is Tom")
    print("By the way who is your name eh?")
    name = input("Enter your name :")
    print(name, "You got a nice name alright get some backpack there's 2 pick one")
    backpack = int(input(" Backpack 1 = food 5.water 6.axe 1.or Backpack 2 = food 3.water 7.axe 2 : "))
    #backpack choosing time
    if backpack == 1:
        print("Wise choice lets head to the camp and we will gather some supplies")
        print("1 Hour later......")
        print("You finally there comrade xavier!")
        print("Wait who the hell is in the wagon!!!!")
        print("Oi oi oi Dimitri we just rescued him eh")
        print("Ooo i see Ivan,Sergey,Vlad come over here also tell the chief we just got some member Sergey")
        print("Oi mate we gotta go get some woods eh")
        print("Aight you go there wth xavier and let us stay with this new guy")
    if backpack == 2:
        print("Good choice lets get some meat and woods after that we will head to the camp")
        print("1 Hour later......")
        print("Arghh! damnit there's a group of Ogres")
        #answering time and there's going to be alot 
        answering = int(input(" option 1 lets fight em up!. option 2 : lets offer them some alliance. choose one : "))
        if answering == 1:
            print("Aight grab some axe we are going to fight em eh")
            print("You have killed 3 ogres Tom you have killed 6 ogres and I have killed 3 ogres nice Tom you got some gud skills")
            print("Yeah lets go we need to go get some meats eh")
        if answering == 2:
            print("You must be kidding me they always raid our stuff!")
            answering1 = int(input("Option 1 : Screw it! there's must be a reason why they raid our stuff. Option 2 : Sorry i dont know. choose one : "))
            if answering1 == 1:
                print("Arghhhh!! Fine go there Tom has told em to stop and tell em to talk with ya")
                answering2 = int(input("Option 1 : Hello fellow ogres i awant to make a alliance because why you guys raid us? Option 2 : Here sign that thing now! choose one : "))
                if answering2 == 1:
                    print("Im Kaldagerusw the leader of this raid corp why we raid you all? because our food is low and we are heavily opressed of becaause of the Wizardous Death clan")
            if answering1 == 2:
                print("Ah! run they got some more friends there")
                print("Euh.... xander they bring a big cannon in there giant wagon eh")     
        if answering < 2:
            print("You have died")
    if backpack >2:
        print("Sorry we got only 2 backpack. Pick again eh")
if start_story >2:
    print("euh.. read the small note again and you can only choose 1 and 0")
if start_story == 2:
    print("Well well here you are")
    print('\n')
    print("You are now currently in a boss fight right now you have :")
    print("Dragon armor = 50000 health when equiped")
    print("Sword of the Legends = Damage : 200,High damage : 1200")
    print("Shield of protection = Block possibility : 89% when enemy hit damage reduced : 67")
    print("Potion of healing = heals 50% of your health")
    print("Potion of strength = buff 10% of the damage")
    print("Boot of Hermes = speed = 1000km/2 Hour dodging possibility = 97%")
    print("The dragon knife = damage = 100")

    
                        
                   




    
    
    
