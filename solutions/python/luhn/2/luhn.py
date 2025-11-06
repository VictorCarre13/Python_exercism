class Luhn:
    def __init__(self, card_num):
        self.card_num=card_num.replace(" ","").strip()

    def valid(self):
        if not self.card_num.isnumeric() or int(self.card_num)==0 and len(self.card_num)==1:
            return False
        total=0
        for index, digit in enumerate(reversed(self.card_num)):
            number=int(digit)
            if index % 2 == 1:
                number*=2
                if number > 9:
                    number-=9
            total+=number
        return total%10==0