import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()

# get the bin code of the ASCII code of each letter in message
# 'h' = '11010000'
# for each uniq seq in binEncoded(Char), chuckEncode(Seq)
# 001011100 => 00 1 0 111 00
#              00 00 0 0 0 000 00 00


def binEncodedRange(message):
    for charac in message:
        chrToBinStr = bin(ord(charac))[2:]
        yield chrToBinStr


# result = [ " ".join(encodeBinSeq()) ]
for binEnc in binEncodedRange(message):
    for unaireSeq in unaireSeqRange(binEnc):
        unaireEncode(unaireSeq)



@unaireSeqValidation
def unaireSeqRange(binEncodedChar):
    pass


def unaireSeqValidation(f):
    def wrapped(seq):
        r = f(seq)
    return wrapped


@seqValidation
def unaireEncode(unaireSeq):
    result = '0 ' if unaireSeq[0] == '1' else '00 '
    result += '0' * len(unaireSeq)
    return result


def seqValidation(f):
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
        r = f(seq)
        return r
    return wrapped


# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print("answer")
