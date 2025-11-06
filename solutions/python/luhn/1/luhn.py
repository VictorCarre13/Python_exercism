class Luhn:
    def __init__(self, card_num):
        self.card_num=card_num.replace(" ","").strip()

    def valid(self):
        try:
            if int(self.card_num)<=1 and len(self.card_num)==1:
                return False
            count=1
            result=""
            number=0
            for digit in reversed(self.card_num):
                if count % 2 == 0:
                    number=int(digit)*2
                    if number > 9:
                        number-=9
                    result+=f"{number}"
                else:
                    result+=f"{digit}"
                count+=1
        except ValueError:
            return False
        return sum(int(total) for total in result)%10==0