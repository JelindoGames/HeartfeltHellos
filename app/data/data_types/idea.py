class Idea:

    def __init__(self, prompt, rating, tags, followup=[]):
        self.prompt = prompt
        self.rating = rating
        self.tags = tags
        self.my_rating = None
        self.followup = followup

    def set_my_rating(self, rating: int):
        self.my_rating = rating

    def update_rating(self, new_rating: int):
        if(self.rating == None):
            self.rating = new_rating
            return
        self.rating = (self.rating + new_rating) / 2

    def hasTag(self, tag: str):
        for idea_tag in self.tags:
            if (idea_tag == tag):
                return True

        return False
    