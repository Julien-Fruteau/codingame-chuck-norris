import sys
import math

# ================== FUNCTIONS


def binEncode(message):
    for charac in message:
        chrToBinStr = bin(ord(charac))[2:]
        yield chrToBinStr


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


# ================== MAIN

message = input()

binMessage = "".join(eachBinEncodedChar for eachBinEncodedChar in binEncode(message))

unaireMessage = " ".join(
    unaireEncode(eachUnaireSeq) for eachUnaireSeq in splitUnaireSeq(binMessage)
)

print(unaireMessage)
