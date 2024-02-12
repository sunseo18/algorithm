def toMinute(time):
    hour, min = time.split(":")
    return int(hour) * 60 + int(min)

def toDiff(start_t, end_t):
    return toMinute(end_t) - toMinute(start_t)

def toFullEm(minute, em):
    length = len(em)
    if minute == length:
        return em
    elif minute < length:
        return em[:minute]
    else:
        hae = minute // length
        mod = minute % length
        return em * hae + em[:mod]
    
def solution(m, musicinfos):
    m = m.replace("C#", "c").replace("D#", "d").replace("F#","f").replace("G#", "g").replace("A#", "a")
    answer = ''
    length = len(musicinfos)
    for i in range(length):
        start_t, end_t, title, em  = musicinfos[i].split(",")
        musicinfos[i] = [toDiff(start_t, end_t), title, em.replace("C#", "c").replace("D#", "d").replace("F#","f").replace("G#", "g").replace("A#", "a")]
        
    musicinfos = sorted(musicinfos, key = lambda x : -x[0])
    
    for i in range(length):
        musicinfos[i][2] = toFullEm(musicinfos[i][0], musicinfos[i][2])
        if m in musicinfos[i][2]:
            return musicinfos[i][1]
            
    return "(None)"