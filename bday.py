import json
import sys
import datetime

_FILE = 'bday.json'

def str_to_datetime(sdate: str) -> datetime:
    if sdate == '':
        dt = datetime.datetime.today()
    else:
        dt = datetime.datetime.strptime(sdate, "%Y%m%d")
    
    return dt 

def datetime_to_str(dt: datetime) -> str:
    return dt.strftime('%Y%m%d')


class FindBDay():
    def __init__(self, sdate: str):
        self.in_date = sdate
        self.file = _FILE
    
    def is_bday(self, dt:datetime) -> bool:
        if dt.weekday() in (5, 6):
            return False

        with open(self.file) as jfile:
            bday = json.load(jfile)

            if dt.strftime('%Y/%m/%d') in bday['Holiday']:
                return False

            return True

    def get_bday(self, dt:datetime) -> datetime:
        bday = dt
        while True:
            if self.is_bday(bday):
                break

            bday = bday - datetime.timedelta(days=1)
        
        return bday

    def get_lday(self, dt:datetime) -> datetime:
        bday = self.get_bday(dt)
        bday = bday - datetime.timedelta(days=1)
        lday = self.get_bday(bday)

        return lday

def main(sdate):
    print('sdate:{}'.format(sdate))
    dt = str_to_datetime(sdate)
    print('dt:{}'.format(dt))

    fbd = FindBDay(sdate)
    print('{} is bday: {}'.format(datetime_to_str(dt), fbd.is_bday(dt)))

    print('the lastest bday is {}'.format(datetime_to_str(fbd.get_bday(dt))))

    print('the lastest lday is {}'.format(datetime_to_str(fbd.get_lday(dt))))

    

if __name__ == '__main__':
    if len(sys.argv) >= 2 and len(sys.argv[1]) == 8 and sys.argv[1].isdigit():
        sdate = sys.argv[1]
    elif len(sys.argv) == 1:
        sdate = ''
    else:
         exit('Usage: {} YYYYMMDD').format(sys.argv[0])

    main(sdate)