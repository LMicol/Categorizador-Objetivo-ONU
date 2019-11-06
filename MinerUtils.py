class MinerUtils:
    def removeall(raw):
        raw = raw.replace('\'', ' ')
        raw = raw.replace('.', ' ')
        raw = raw.replace(',', ' ')
        raw = raw.replace('+', ' ')
        raw = raw.replace('-', ' ')
        raw = raw.replace(';', ' ')
        raw = raw.replace('\"', ' ')
        raw = raw.replace('{', ' ')
        raw = raw.replace('}', ' ')
        raw = raw.replace('[', ' ')
        raw = raw.replace(']', ' ')
        raw = raw.replace('/', ' ')
        raw = raw.replace('\\', ' ')
        raw = raw.replace(':', ' ')
        raw = raw.replace('>', ' ')
        raw = raw.replace('<', ' ')
        raw = raw.replace('(', ' ')
        raw = raw.replace(')', ' ')
        raw = raw.replace('?', ' ')
        raw = raw.replace('!', ' ')
        raw = raw.replace('%', ' ')
        raw = raw.replace('#', ' ')
        raw = raw.replace('&', ' ')
        raw = raw.replace('*', ' ')
        raw = raw.replace('  ', ' ')
        raw = raw.replace('   ', ' ')
        
        return raw
        
    def counter(string):
        counter = dict()
        s = string.split()
        
        for word in s:
            try:
                counter[word]+=1
            except:
                counter[word] = 1
    
        return counter