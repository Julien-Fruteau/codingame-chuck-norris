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

message = "Hi"


def binEncoded(message):
    for charac in message:
        chrToBinStr = bin(ord(charac))[2:]
        yield chrToBinStr


# result = [ " ".join(encodeBinSeq()) ]
binEncodedMessage = "".join(binEnc for binEnc in binEncoded(message))
unaireMessage = " ".join(
    unaireMessage for unaireMessage in splitUnaireSeq(binEncodedMessage))

for binEnc in binEncoded(message):
    for unaireSeq in splitUnaireSeq(binEnc):
        unaireEncode(unaireSeq)


def unaireSeqValidation(f):
    def hasOnlyBinaries(seq):
        binCount = seq.count('0') + seq.count('1')
        return len(seq) == binCount

    def wrapped(seq):
        if not hasOnlyBinaries(seq):
            raise ValueError('seq does not contain only binaries')
        r = f(seq)
        return r
    return wrapped


@unaireSeqValidation
def splitUnaireSeq(message):
    unaireSeq = message[0]
    for i in message[1:]:
        if i == unaireSeq[0]:
            unaireSeq += i
        else:
            yield unaireSeq
            unaireSeq = i
    yield unaireSeq


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


@seqValidation
def unaireEncode(unaireSeq):
    result = '0 ' if unaireSeq[0] == '1' else '00 '
    result += '0' * len(unaireSeq)
    return result


# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print("answer")
