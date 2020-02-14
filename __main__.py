import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()

chr(99)
bin(67)

# for each letter in string
# get the ASCII code of the charater
# get the bin code of the ASCII code
# 001011100 => 00 1 0 111 00
#              00 00 0 0 0 000 00 00

encodeSeq(000)


# generateur
def generateur(l, o, i=-1):
    while True:
        try:
            i = l.index(o, i+1)
            yield i
        except ValueError:
            return
        

splitInput("1001")
for c in splitInput("1001"):
    print(c)

def splitInput(message):
    for charac in message:
        chrToStr = bin(ord(charac))[2:]
        yield chrToStr

def splitCharTo(seq):

    pass


@checkSeq
def encodeSeq(seq):
    result = '0 ' if seq[0] == '1' else '00 '
    result += '0' * len(seq)
    return result


def checkSeq(toWrap):
    def getCharCount(seq):
        return {i: seq.count(i) for i in ['0', '1']}

    def hasUniqueValue(seq):
        return 0 in getCharCount(seq).values()

    def wrapped(seq):
        if type(seq) != str:
            raise TypeError("seq argument is not of type string")
        if not hasUniqueValue(seq):
            raise ValueError(
                "Only '0' OR '1' are accepted in sequence {}".format(seq))
        r = toWrap(seq)
        return r
    return wrapped


encodeSeq('10111')
seq = '000'


def getCharCount(seq):
    return {i: seq.count(i) for i in ['0', '1']}


for value in :
    print(value)

0 in getCharCount(seq).values()

bin(99)
bin(int.from_bytes("a".encode(),'big'))
"a".encode()
str(11101)


def bloc1(charSeq):
    what = "has1" if "1" in charSeq else "has0"
    res = {"has1": "0",
           "has0": "00"}
    return res[what]

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print("answer")
