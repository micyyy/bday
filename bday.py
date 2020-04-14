import json
import sys
from datetime import datetime, timedelta

_HOLIDAY_FILE = 'bday.json'

def str_to_datetime(sdate: str) -> datetime:
    return datetime.today() if sdate == '' else datetime.strptime(sdate, "%Y%m%d")


def datetime_to_str(dt: datetime) -> str:
    return dt.strftime('%Y%m%d')


class FindBDay():
    def __init__(self, dt:datetime):
        self.dt = dt

    def is_bday(self, dt:datetime) -> bool:
        if dt.weekday() in (5, 6):
            return False

        with open(_HOLIDAY_FILE) as jfile:
            bday = json.load(jfile)

            if dt.strftime('%Y/%m/%d') in bday['Holiday']:
                return False

        return True

    def get_last_bday(self, ndays:int) -> list:
        bdays = list()
        date = self.dt
        count = 0
        while count < ndays:
            if self.is_bday(date):
                bdays.append(datetime_to_str(date))
                count += 1
            
            date -= timedelta(days=1)

        return bdays


def main(sdate):
    dt = str_to_datetime(sdate)

    fbd = FindBDay(dt)
    print('get_last_bday {}'.format(fbd.get_last_bday(2)))

if __name__ == '__main__':
    if len(sys.argv) >= 2 and len(sys.argv[1]) == 8 and sys.argv[1].isdigit():
        sdate = sys.argv[1]
    elif len(sys.argv) == 1:
        sdate = ''
    else:
        exit('Usage: {} YYYYMMDD').format(sys.argv[0])

    main(sdate)
