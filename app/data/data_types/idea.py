class Idea:

    def __init__(self, prompt, rating, tags):
        self.prompt = prompt
        self.rating = rating
        self.tags = tags
        self.my_rating = None

    def set_my_rating(self, rating: int):
        self.my_rating = rating
    