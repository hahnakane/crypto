# Simple Substitution Cipher
import sys, random


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    myMessage = 'If a man is offered a fact which goes against his instincts, he will scrutinize it closely, and unless the evidence is overwhelming, he will refuse to believe it. If, on the other hand, he is offered something which affords a reason for acting in accordance to his instincts, he will accept it even on the slightest evidence. The origin of myths is explained in this way. -Bertrand Russell'    
    myMode = 'encrypt' # set to 'encrypt' or 'decrypt'
    myKey = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'
    #myKey = getRandomKey()

    checkValidKey(myKey)

    if myMode == 'encrypt':
        result = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        result = decryptMessage(myKey, myMessage)
    print('Using key %s' % (myKey))
    print('The new message is:')
    print(result)

#check to make sure the letters have a 1-to-1 mapping
def checkValidKey(key):
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()
    if keyList != lettersList:
        sys.exit('There is an error in the key or symbol set.')


def encryptMessage(key, message):
    return transformMessage(key, message, 'encrypt')


def decryptMessage(key, message):
    return transformMessage(key, message, 'decrypt')


def transformMessage(key, message, mode):
    result = ''
    charsA = LETTERS
    charsB = key
    if mode == 'decrypt':
        # For decrypting, we can use the same code as encrypting. We
        # just need to swap where the key and LETTERS strings are used.
        charsA, charsB = charsB, charsA

    # loop through each symbol in the message
    for symbol in message:
        if symbol.upper() in charsA:
            # encrypt/decrypt the symbol
            symIndex = charsA.find(symbol.upper())

            #check and maintain letter casing
            if symbol.isupper():
                result += charsB[symIndex].upper()
            else:
                result += charsB[symIndex].lower()
                
        else:
            # symbol is not in LETTERS, just add it
            result += symbol

    return result


#This function generates a random key rather than hardcoding it
#def getRandomKey():
#    key = list(LETTERS)
#    random.shuffle(key)
#    return ''.join(key)


if __name__ == '__main__':
    main()


#encrypted message resutlt: myMessage = 'Sy l nlx sr pyyacao l ylwj eiswi upar lulsxrj isr sxrjsxwjr, ia esmm rwctjsxsza sj wmpramh, lxo txmarr jia aqsoaxwa sr pqaceiamnsxu, ia esmm caytra jp famsaqa sj. Sy, px jia pjiac ilxo, ia sr pyyacao rpnajisxu eiswi lyypcor l calrpx ypc lwjsxu sx lwwpcolxwa jp isr sxrjsxwjr, ia esmm lwwabj sj aqax px jia rmsuijarj aqsoaxwa. Jia pcsusx py nhjir sr agbmlsxao sx jisr elh. -Facjclxo Ctrramm'
