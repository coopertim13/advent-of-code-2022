def unique(s):
    return len(set(s)) == len(s)

signals = open('6.txt', 'r')
signal = signals.readlines()[0].strip()
i = 0
while i <= len(signal) - 4:
    sig = signal[i] + signal[i+1] + signal[i+2] + signal[i+3]
    if(unique(sig)):
        print(i+4)
        break
    i+=1