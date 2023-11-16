# Creating a "choose your own adventure" game in Python. 

name = input("Type your name: ")
print("Welcome", name, "to this magical adventure! Are you ready?")

answer = input("You find yourself on an ancient road in the middle of a market. Foods, handmade objects, fabrics, and more are being traded and sold. On your left you see a table full of magical potions, each with its distinct use. On the right, you see a table full of powerful stones with magical properties. You've got enough money in your pocket for either one magical potion or one magical stone. Which do you choose to purchase? Type in 'left' for the potions, or 'right' for the stones. ").lower()

if answer == "left":
    answer = input("At the magical potion table, there are three potions that catch your eye. Potion One is a bubbling, tasteless, clear potion, meant for enternal glory, power, fame, and money. Potion Two is warm chocolatey drink with the most delightful smell, with a promise that true love will come to you soon. Potion Three is a green cold liquid smelling of cucumber and lemon, promising enternal youth and immortality. Which potion do you purchase? Type 'potion one', 'potion two', or 'potion three'. ")
    
    if answer == "potion one":
        print("Power, fame, and money isn't everything. Soon after buying this potion, you became the most infamous person in history. However, this path of fame and glory led you to an untimely death. You died only two weeks after purchasing this potion, in a freak accident. You journey has come to an end.")
    elif answer == "potion two":
        answer = input("You chose potion two. Immediately after drinking the potion, you feel an electric shock as you bump into the person next to you: your soulmate. As two souls collide, you are transported into a serene forest, where the only sounds the two of you can hear are the sound nature... and a giant. You are your soulmate must get away from the giant. Do you fight against the giant together, or distract the giant and run away? Type 'fight' or 'distract'. ")
        if answer == "fight":
            print("You are your partner are no match for the giant, who destroys you both. This is how your journey ends.")
        elif answer == "distract":
            print("You and your soulmate decide to team up to distract the giant. Your collaboration is full of cleverness, and the giant walks away, defeated. You and your partner continue on your journey, together, willing to work together as your journey ends.")
        else:
            print("Not a valid option. Your journey has ended.")
    elif answer == "potion three":
        answer = input("After drinking potion three at the market, your gray hair is immediately replaced with your natural color. A glow appears on your face. Any wrinkle or blemish disappears. You feel the healthiest you've ever been. All of a sudden, a woman nearby you collaspes. Her skin seems to be rotting. The plague arrives in town. Everyone around you as at risk... but yourself. A healing mage arrives and asks for help to transport the woman to the apothecary. Do you assist the healer, or continue on your way? Type 'help' or 'ignore'. ")
        if answer == "help":
            print("You decide to help the ill woman. You use your new powers to help others and take a job with the healer. You help the entire village to get better. This is how your journey ends.")
        elif answer == "ignore":
            print("After refusing to help the ill woman, you realize your true nature and become a wicked villain. This is how your journey ends.")
        else: 
            print("Not a valid option. Your journey has ended.")
    else:
        print("Not a valid option. Your journey has ended.")
    
elif answer == "right":
    answer = input("At the magical stone table, there are three stones that catch your eye. One is a burning hot stone that appears to sizzle in the heat, but when you touch it, turns cold; it promises the magical ability to withold any temperature, making you immune to fire and ice. Stone Two is a small, blue glowing crystal, which promises the end of loneliness, and the start of forever love. Stone three is a sparkling black stone that fits in the palm of your hand, and when touched, keeps you safe from any harm. Which stone do you choose? Type 'stone one', 'stone two', or 'stone three'. ")
    
    if answer == "stone one":
        answer = input("You chose stone one. You keep the cold stone in your pocket, forgetting about it while you tour the market. Yet a flame appears and spreads as it engulfs the entire market. You are immune to the flames, but a child is lost within the market, crying for help. Do you rescue the child from the flames, or leave the burning market? Type 'rescue' or 'leave'. ")
        if answer == "rescue":
            answer = input("After rescuing the child, you are applauded as a hero by the townspeople. The child's parents appear, thanking you for your good deed. They are acquainted with the king and will convince his Royal Highness to grant you title of Knight. Do you accept the honor, or leave without reward? Type 'accept' or 'leave'. ")
            if answer == "accept":
                print("Congratulations! You are now a knight of the kingdom. You are cheered on by the king and the townspeople as a hero. This is how your journey ends.")
            if answer == "leave":
                print("You left without a reward. You may not be a knight, but maybe you have become something better. With the stone, you continue saving others in times of need. This is how your journey ends.")
            else:
                ("Not a valid option. Your journey has ended.")
        elif answer == "leave":
            print("You may be immune to fire and ice, but blades can still harm you. After the fire, you are robbed of your magical stone and die during a struggle. This is the end of your journey.")
        else:
            print("Not a valid option. Your journey has ended.")
    elif answer == "stone two":
        print ("You chose stone two. You've kept the stone with you, forever, sometimes completely forgetting about it, but always knowing you are never alone. Your life is filled with love and friendship and abundance. Your journey in this adventure has come to an end, because you are already living it.  ")
    elif answer == "stone three":
        answer = input("You choose stone three. All of a sudden, a large group of bandits with a large cart drawn by a horse arrive at the market. Armed with weapons and torches, they demand all the goods or they will burn down and destroy anything in their sight, which includes people. After an intense struggle, the people of the market are murdered, but the stone helps you stay alive. The bandits are impressed by your ability to stay unhurt. They ask you to join their gang. Do you join the bandits, or leave? Type 'join' or 'leave'. ")
        if answer == "join":
            print("You join the bandits... and thrive. You become the leader of the gang and are known across the kingdom as the most dangerous of all. Your journey ends as a villain.")
        elif answer == "leave":
            print("You decide to keep your integrity. Instead, you become a vigiliante who fights against both the bandits and the king. You meet a group of link-minded individuals and decide to steal from the rich to give to the poor... the rest is history. This is how your journey ends.")
        else: 
            print("Not a valid option. Your journey has ended.")
else:
    print("Not a valid option. Your journey has ended.")


