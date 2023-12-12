class Idea:

    def __init__(self, prompt, ratings: list, tags, followup=[]):
        self.prompt = prompt
        self.ratings = ratings
        self.tags = tags
        self.my_rating = None
        self.followup = followup

    def set_my_rating(self, rating: int):
        if self.my_rating is None:
            self.my_rating = rating
            self.ratings.append(rating)
        else:
            self.ratings.remove(self.my_rating)
            self.my_rating = rating
            self.ratings.append(rating)

    def get_rating(self):
        return sum(self.ratings) / len(self.ratings)

    def hasTag(self, tag: str):
        for idea_tag in self.tags:
            if (idea_tag == tag):
                return True

        return False
    