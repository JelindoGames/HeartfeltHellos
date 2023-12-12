from data.data_types.idea import Idea

class StoredData:
    # All the tags that are currently on the app
    # User-created tags are add to the list
    tags = ["sports", "movies", "books", "general"]
    
    # All the ideas that are currently on the app
    # follow ups are created and tied to the ideas
    # User-created ideas are add to the list
    ideas = [Idea("Do you still play soccer?", 4.2, ["sports"], 
                  [Idea("Why don't you play anymore?", 4.0, ["sports"], []),
                   Idea("How'd your latest game go?", 3.6, ["sports"], [])]), 
             Idea("Did you see the game last Sunday?", 3.9, ["sports"], []),
             Idea("What's your favorite team lately?", 3.5, ["sports"], []),
             Idea("Have you seen the FNAF movie?", 4.1, ["movies"] , []),
             Idea("What movies are you interested in seeing soon?", 3.8, ["movies"], []),
             Idea("Read any good books lately?", 3.7, ["books"], []),
             Idea("What's the worst book you've ever read?", 3.2, ["books"], []),
             Idea("Do you have a cat?", 4.5, ["general"], []),
             Idea("Do you like video games?", 4.1, ["general"], []),
             Idea("Seen any good movies?", 3.8, ["general"], []),
             Idea("Learned any interesting facts lately?", 3.6, ["general"], []),
             Idea("What's changed since I last heard from you?", 3.4, ["general"], []),
             Idea("If you could be any animal, what would you be?", 2.8, ["general"], [])]

    # All the friends you currently have on the app
    friends = []

    # For Idea creation form
    temp_prompt = ""

    previous_idea_screen = ""

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

    # All the texts you've made (tuple: (text, color))
    message_history = []

    # Who is currently set to receive messages on the message screen
    message_recipient = None
