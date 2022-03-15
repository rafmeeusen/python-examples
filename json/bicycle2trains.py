import sys
import json
import datetime


cycletimes = { 'Bordet':12, 'Diegem':14, 'Zaventem':18 }
DEFAULT_FILE='trains_timetable.json'
DEST='Leuven'
JSTR_TR='train'
JSTR_LI='line'
JSTR_STO='stops'
JSTR_STA='station'
JSTR_TI='time'


''' convert data into connections to get home '''
def data2connections(data):
    connections = []
    for treinrit in data:
        stops = treinrit[JSTR_STO]
        locations = [ s[JSTR_STA] for s in treinrit[JSTR_STO] ]
        try:
            idx_dest = locations.index(DEST)
        except ValueError:
            print('WARNING', DEST, 'not found in train', treinrit[JSTR_TR], ', skipping')
            continue
        nr_stops_before = idx_dest
        for idx_origin in range(nr_stops_before):
            #print('origin', stops[idx_origin])
            #print('destination', stops[idx_dest] )
            c = {}
            c['origin'] = stops[idx_origin]
            c['destination'] = stops[idx_dest]
            connections.append(c)
    return connections

def print_connections(cons):
    for c in cons:
        if len(c)==2:
            print('from', c['origin'] ,'to', c['destination'])
        else:
            print('KKE', c['work'], 'via', c['origin'] ,'to', c['destination'])



'''
    subtract time int_min (integer, minutes)
    from given time string "hh:mm"
    return again as string "hh:mm"
'''
def subtract_time(str_hhmm, int_min):
    h=int(str_hhmm[0:2])
    m=int(str_hhmm[3:5])
    dummydate = datetime.date(1, 1, 1)
    origtime = datetime.datetime.combine(dummydate, datetime.time(h, m, 0))
    minutes =  datetime.timedelta(minutes=int_min)
    newtime = origtime - minutes
    return newtime.strftime('%H:%M')

def addcycletimes(cons, times):
    newcons=[]
    for c in cons:
        traintime = c['origin'][JSTR_TI]
        trainstation = c['origin'][JSTR_STA]
        cycletime = 15
        if not trainstation in times.keys():
            print('warning taking default time of 15 min')
        else:
            cycletime = times[trainstation]
        kke_time = subtract_time( traintime, cycletime )
        kke = { JSTR_STA:'KKE', JSTR_TI:kke_time }
        newc = c
        newc['work'] = kke
        newcons.append(newc)
    return newcons 

def main(fn):
    print("Reading data from", fn)
    fp=open(fn)
    data=json.load(fp)
    print('== connections')
    cons=data2connections(data)
    print_connections(cons)
    cons2=addcycletimes(cons, cycletimes)
    print('== connections 2')
    print_connections(cons2)

if __name__ == "__main__":
    fn = DEFAULT_FILE
    if len(sys.argv) > 1:
        # consider arg as filename:
        fn = sys.argv[1]
    main(fn)



