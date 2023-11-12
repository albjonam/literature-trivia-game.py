print("Welcome to the literature trivia game!")

playing = input("Would you like to play? ")

if playing.lower() != "yes":
    quit()

print("Alright, let's go!")
score = 0 

answer = input("Arthur Conan Doyle is known writing which famous detective? ")
if answer.lower() == "sherlock holmes":
    print("Correct! You are a rock star! Let's keep going...")
    score += 1
else: 
    print("Wrong! You need to read more.")

answer = input("Sun Tzu is known for which classic book of military strategy? ")
if answer.lower() == "the art of war":
    print("Correct! Wow, you must read a lot!")
    score += 1
else: 
    print("Wrong! What a disappointment.")

answer = input("The sentence 'So we beat on, boats against the current, borne back ceaselessly into the past.' is the ending line of which 1920s novel? ")
if answer.lower() == "the great gatsby":
    print("Congratulations! You really know your literature.")
    score += 1
else: 
    print("Incorrect! You need to read more.")

answer = input("What author wrote Frankenstein? ")
if answer.lower() == "mary shelley":
    print("Correct! You're doing so well!")
    score += 1
else: 
    print("Wrong! How do you not know Mary Shelley?")

answer = input("In 1988, Toni Morrison won the Pultizer Prize for which novel? ")
if answer.lower() == "beloved":
    print("Amazing! Well done!")
    score += 1
else: 
    print("Incorrect. That is disappointing.")

answer = input("What French author is known for writing the novels 'The Count of Monte Cristo' and 'The Three Musketeers'? ")
if answer.lower() == "alexandre dumas":
    print("I see you also know your French literature. Well done!")
    score += 1
else: 
    print("Wrong!")

answer = input("What Haruki Murakami novel is also the title of a Beatles song? ")
if answer.lower() == "norwegian wood":
    print("Another win for you!")
    score += 1
else: 
    print("Incorrect. Wow, that's sad.")

answer = input("What author is known for writing the plays 'Romeo and Juliet', 'Hamlet' and 'Macebeth'? ")
if answer.lower() == "william shakespeare":
    print("Wow, you're doing so great!")
    score += 1
else: 
    print("Incorrect. You lost. Who doesn't know Shakespeare?") 

print("You got " + str(score) + "/8 questions correct! Congratulations!")
print("You got " + str((score / 8) * 100) + "% answers correct! Oh wow!") 