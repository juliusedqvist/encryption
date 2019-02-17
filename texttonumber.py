from encrypt import encrypt, clearMes


letters = [" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


def findlet(n):

    """ Translate nums to letters """

    for i in letters:
        if letters[n] == i:
            return i


def findnum(a):

    """Finds the number corresponding to a letter"""

    x = 0
    for i in letters:
        if a == i:
            return x
        x += 1


def splitsen(n):

    """Splits the sentence into letters"""

    letter = list(n)

    return letter


def translate(n):

    """ Sends all the letters into findnum and then returns the nums """

    holder = []

    for items in list(n):
        holder.append(findnum(items))

    return holder


def encryptmess(n):

    """ Encrypts the entire string by using encrypt function"""

    for i in translate(list(n)):
        encrypt(int(i))


clearMes()
encryptmess("hello there")
