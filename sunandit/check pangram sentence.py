def isPangram(s):
    alphabetList = 'abcdefghijklmnopqrstuvwxyz'
    alphabetCount = 0
    if len(s) < 26:
        return False
    else:
        s = re.sub('[^a-zA-Z]','',s).lower()
				for i in range(len(alphabetList)):
            if alphabetList[i] in s:
                alphabetCount = alphabetCount + 1
        if alphabetCount == 26:
            return True
        else:
            return False
