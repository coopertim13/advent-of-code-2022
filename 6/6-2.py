def unique(s):
    return len(set(s)) == len(s)

signals = open('6.txt', 'r')
signal = signals.readlines()[0].strip()
i = 0
while i <= len(signal) - 14:
    sig = ""
    j = i
    while j < i+14:
        sig = sig + signal[j]
        j+=1
    if(unique(sig)):
        print(i+14)
        break
    i+=1