from data.data_types.idea import Idea

class StoredData:
    # All the tags that are currently on the app
    # User-created tags are add to the list
    tags = ["sports", "movies", "books"]
    
    # All the ideas that are currently on the app
    # follow ups are created and tied to the ideas
    # User-created ideas are add to the list
    ideas = [Idea("Do you still play soccer?", [4, 4, 4, 4, 5], ["sports"],
                  [Idea("Why don't you play anymore?", [3, 5], ["sports"], []),
                   Idea("How'd your latest game go?", [3, 3, 4, 4, 4], ["sports"], [])]),
             Idea("Did you see the game last Sunday?", [4, 4, 4, 4, 5, 5, 3], ["sports"], []),
             Idea("What's your favorite team lately?", [3, 4], ["sports"], []),
             Idea("Have you seen the FNAF movie?", [4, 3, 5, 5], ["movies"] , []),
             Idea("What movies are you interested in seeing soon?", [4, 4, 5, 3], ["movies"], []),
             Idea("Read any good books lately?", [2, 5, 5], ["books"], []),
             Idea("What's the worst book you've ever read?", [2, 4, 4, 3], ["books"], []),
             Idea("Do you have a cat?", [4, 5, 4, 5], ["general"], []),
             Idea("Do you like video games?", [4, 3, 5, 5, 4], ["general"], []),
             Idea("Seen any good movies?", [3, 3, 5, 4, 3, 4], ["general"], []),
             Idea("Learned any interesting facts lately?", [4, 3, 4, 3, 4], ["general"], []),
             Idea("What's changed since I last heard from you?", [3, 3, 3, 4, 4], ["general"], []),
             Idea("If you could be any animal, what would you be?", [1, 5, 2, 3, 3, 4], ["general"], [])]

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

    # All the texts you've made - key = recipient name, value = list of tuples (text, color)
    message_history = {}

    # Who is currently set to receive messages on the message screen
    message_recipient = None
