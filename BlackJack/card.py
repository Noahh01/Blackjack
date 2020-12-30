class card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __add__(self, other, bool = True):
        if bool == False:
            return self.getMaxVal() + other.getMaxVal()

        return self.getMinVal() + other.getMinVal()


    def __eq__(self, other):
        return self.value == other.value and self.suit == other.suit

    def __str__(self):
        return self.value+ self.suit

    def getMinVal(self):

        a = None
        try:
            a = int(self.value)
        except ValueError:
            if self.value in ["J","Q","K"]:
                a = 10
            else:
                a = 1
        return a

    def getMaxVal(self):

        a = None
        try:
            a = int(self.value)
        except ValueError:
            if self.value in ["J","Q","K"]:
                a = 10
            else:
                a = 11

        return a

    def getImage(self):

        suit = ""
        if self.suit == "\u2663":
            suit = "c" ### clubs
        elif self.suit == "\u2660":
            suit = "s" ### spades
        elif self.suit == "\u2666":
            suit = "d" ### dimonds
        else:
            suit = "h" ### heart


        return "pics\\\\"+ self.value +  suit + ".png"
