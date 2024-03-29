class Movie:

    def __init__(self, title, original_title, duration, release_date, rating='TP'): #define the important features
        self.title = title 
        self.original_title = original_title
        self.duration = duration
        self.rating = rating
        self.release_date = release_date
        
        #less important features and if they are not present on the movie details, the program won't take them
        self.score = None
        self.id = None
        self.actors = []
        self.productors = []
        self.is_3d = None
        self.production_budget = None
        self.marketing_budget = None
        self.imdb_id = None
        self.synopsis = None

    def total_budget(self):# we create a new method for the total budget
        if (self.production_budget == None or self.marketing_budget == None):#or it includes also the and so when both are none
            return None
        #else:#we could omit the else because with return we ended the function
        return self.production_budget + self.marketing_budget

 
