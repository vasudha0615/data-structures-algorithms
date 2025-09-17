class DetectCapital:
    def detectcapital(self,word):
        count = 0
        length = len(word)
        for i in range(length):
            if word[i] >= chr(65) and word <=chr(91):
                count+=1

        if count == length:
            return True
        if count == 0:
            return True
        if count == 1 and word[i] >= chr(65) and word[i] <= chr(91):
            return True
        else:
            return False