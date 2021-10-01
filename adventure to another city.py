print("================================")
print(" | adventure to another city |  *<|:‑) ")
print("credit to Lume #0001 <== Lume's discord tag")
print("================================")
city = input("put city name : ")

print("||Someone just made a big party while you are going to another city||")
print("0 : go to the party")
print("1 : ignore the party")
print("2 : ignore and speed up")
print("")
r1 = int(input(" what will you do ? : "))
if r1 == 0:
    print("you go to the party but you forgot to go to another city")
    print("Game over")
    print("(ノ °益°)ノ 彡 (\﻿ .o.)")
elif r1 == 1:
    print("you chose to ignore them but they drag you into the party")
    print("Game over")
    print("(ノ °益°)ノ 彡 (\﻿ .o.)")
elif r1 == 2:
    print("you chose to ignore them and speeds up")
    print("stage completed")
    print(" (👍ᐛ )👍")
    print("|| You are going to the toll and you saw someone running beside your car ||")
    print("0 : ask him")
    print("1 : ignore him keep going")
    r2 = int(input("\n What will you do ? : "))
    if r2 == 0:
        print("You asked him but he dissapears and you crashed your car while knowing it was a mirage")
        print("Game over")
        print("(ノ °益°)ノ 彡 (\﻿ .o.)")
    elif r2 == 1:
        print("You ignored him and how lucky it was actually a mirage")
        print("stage completed")
        print(" (👍ᐛ )👍")
        print("==========================")
        print("|| You are in a toll and the road is queit no one is there ||")
        print("0 : speed up like using the whole spedometer")
        print("1 : keep in the normal spedometer")
        print("==========================")
        print("")
        r3 = int(input("What will you do ? : "))
        
        if r3 == 0:
            print("you speeds up like crazy and you cant stop it and you accidentally crashed in a huge rock")
            print("Game over")
            print("(ノ °益°)ノ 彡 (\﻿ .o.)")
        elif r3 == 1:
            print("You chose to not speeds up and you saw a huge rock and you avoided it")
            print("stage completed")
            print(" (👍ᐛ )👍")
            print("======================================")
            print("You saw a big truck coming in front of you very fast")
            print("0 : Stops")
            print("1 : Keep going")
            print("==============")
            print("")
            r4 = int(input("What will you do ? : "))
            if r4 == 0:
                print("You chose to stop and it actually was a mirage again and you got fined by the police")
                print("Game over")
                print("(ノ °益°)ノ 彡 (\﻿ .o.)")
                print("=======================")
                print("When you got fined by the police something weird is happening")
                print("0 : check it")
                print("1 : run")
                print("2 : do nothing and hide ")
                print("")
                r5 = int(input("What will you do ? : "))
            
                if r5 == 0:
                    print("theres a dragon and it burst it flame to you")
                    print("Game over")
                    print("(ノ °益°)ノ 彡 (\﻿ .o.)")
                elif r5 == 1:
                    print("You ran and the dragon steps on you and the result is you broke alot of bones")
                    print("Game over")
                    print("(ノ °益°)ノ 彡 (\﻿ .o.)")
                elif r5 == 2:
                    print("You chose to do nothing and hide. the dragon has been killed and you still got fined")
                    print("Achievement achieved!")
                    print(" (👍ᐛ )👍")
                    print("")
                    a = int(input("Do you want to see the achivement's name? 0 : no | 1 : yes | : "))
                    if a == 0:
                        print("Kinda game over")
                    elif a == 1:
                        print("===============")
                        print("==============================================================")
                        print("( Achievement name : Hey i survived but why do i still got fined :‑| )")
                        print("==============================================================")
                        print("Kinda game over")
                        print("But hey thats kinda cool y know")
                        print(" (👍ᐛ )👍")
                        print("================")
                    else:
                        print("try again")
                else:
                    print("try again")
                    
            elif r4 == 1:
                print("======================================================================================")
                print("You chose to keep going and wow it was a mirage again how lucky and how crazy was that")
                print("stage completed")
                print("==========================================")
                print("You reached to ", city," epic")
                print("You win")
                print(" (👍ᐛ )👍")
            else:
                print("try again")

        else:
            print("try again")
    
    else:
        print("try again")
 
else:
    print("try again")

        


    

                          
                          
                        
                          
