class Idea:

    def __init__(self, prompt, rating, tags):
        self.prompt = prompt
        self.rating = rating
        self.tags = tags
        self.my_rating = None

    def set_my_rating(self, rating: int):
        self.my_rating = rating

    def hasTag(self, tag: str):
        for idea_tag in self.tags:
            if (idea_tag == tag):
                return True

        return False
    