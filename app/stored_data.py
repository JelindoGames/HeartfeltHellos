from data.data_types.idea import Idea

class StoredData:
    # All the tags that are currently on the app
    # User-created tags are add to the list
    tags = ["academic", "animals", "books", "movies", "music", "sports", "technology", "videogames"]
    
    # All the ideas that are currently on the app
    # follow ups are created and tied to the ideas
    # User-created ideas are add to the list
    ideas = [Idea("Do you still play soccer?", [4, 4, 4, 4, 5], ["sports"], "Yeah, I do! What's up?",
                  [Idea("Why don't you play anymore?", [3, 5], ["sports"], "Idk, schedule stuff. I probably should get back into it.", []),
                   Idea("How'd your latest game go?", [3, 3, 4, 4, 4], ["sports"], "Not bad, I still got it!", [])]),
             Idea("Did you see the game last Sunday?", [4, 4, 4, 4, 5, 5, 3], ["sports"], "Yeah, could you believe that ending!?",
                  [Idea("What was your favorite play?", [3, 5], ["sports"], "Totally that crazy one at the very beginning!", []),
                   Idea("You happy about the results?", [3, 4], ["sports"], "Well, tbh I was rooting for the other team", [])]),
             Idea("What's your favorite team lately?", [3, 4], ["sports"], "Probably the Steelers, I think they're cool.",
                  [Idea("Why are they your favorite?", [3, 3, 3], ["sports"], "Well, I've loved them since childhood!", []),
                   Idea("What could change your mind?", [4, 5], ["sports"], "Lol, not a fan of them?", [])]),
             Idea("Have you seen the FNAF movie?", [4, 3, 5, 5], ["movies"] , "Yessss! I loved the MatPat cameo!", 
                  [Idea("What was your favorite scene?", [3, 3, 3], ["movies"], "I loved the fort building scene! So wholesome and adds to the story.", []),
                   Idea("Have you played any of the FNAF games?", [4, 5], ["movies"], "Not really, they scared me as a kid", [])]),
             Idea("What movies are you interested in seeing soon?", [4, 4, 5, 3], ["movies"], "Whenever they make the Morbius sequel, I'll be there.", []),
             Idea("Read any good books lately?", [2, 5, 5], ["books"], "I read this great book about boredom just now.", 
                  [Idea("Would you recommend the book?", [3, 3, 3], ["books"], "Yes! I learned so much from it.", []),
                   Idea("Who's your favorite author?", [4, 5], ["books"], "Definitely would be Elina Tochilnikova. She is such a great writer and backs up her theories with research!", [])]),
             Idea("What's the worst book you've ever read?", [2, 4, 4, 3], ["books"], "Probably the textbook for my math class.", 
                  [Idea("What's your least favorite genre?", [3, 3, 3], ["books"], "I bet it would have to be romance. I cringe everytime I try to read them.", [])]),
             Idea("Do you have a cat?", [2, 2, 3, 4], ["general"], "Yes, his name is Fluffy and I love him <3", 
                  [Idea("What's their favorite toys?", [3, 3, 3], ["books"], "The love to chase laser beams. It helps to tire them out before bedtime, too!", [])]),
             Idea("Do you like video games?", [4, 3, 5, 5, 4], ["general"], "Mostly... I stay away from the farming sim games though. Those bore me out!", 
                  [Idea("What's your favorite gaming genre?", [4, 3, 5, 5, 4], ["general"], "Definitely first-person shooters! Those keep me on my toes.", []),
                   Idea("What do you like to do in your spare time?", [4, 3, 5, 5, 4], ["general"], "I like to knit and read on top of playing video games.", [])]),
             Idea("Seen any good movies?", [3, 3, 5, 4, 3, 4], ["general"], "Well, I saw Morbius the other day.", 
                  [Idea("What's your favorite actor from the movie?", [4, 3, 5, 5, 4], ["general"], "Jared Leto played the lead role so well! Looking forward to the next one.", [])]),
             Idea("Learned any interesting facts lately?", [4, 3, 4, 3, 4], ["general"], "Nothing I can think of, how about you?", []),
             Idea("What's changed since I last heard from you?", [3, 3, 3, 4, 4], ["general"], "Not a ton tbh, how about you?", []),
             Idea("If you could be any animal, what would you be?", [1, 5, 2, 3, 3, 4], ["general"], "Hmm, maybe a cat. That sounds kinda fun.", [])]

    # All the friends you currently have on the app
    friends = []

    # For Idea creation form
    temp_prompt = ""

    # For friend creation form
    temp_friend_name = ""

    # For selection of person from friend list
    temp_selected_person = None

    # For selection of tag under a friend
    temp_selected_tag = None

    temp_selected_idea = None

    # type of ideas that user has recently been looking at
    idea_screen_history = []

    # ideas that the user has used
    idea_history = []

    previous_friend_list_screen = ""

    # ideas that the user has seen
    # preserves the chronological order a which user has seen the idea
    viewed_ideas = []

    # All the texts you've made - key = recipient name, value = list of tuples (text, color)
    message_history = {}

    # Who is currently set to receive messages on the message screen
    message_recipient = None
