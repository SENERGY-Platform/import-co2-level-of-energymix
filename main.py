# https://api.co2signal.com/v1/latest?countryCode=DE

import CO2DataFetcher, sched, time
from import_lib.import_lib import ImportLib

def bla(lib, scheduler):
    lib.put(*CO2DataFetcher.co2DataFetcher())
    scheduler.enter(60, 0, bla, (lib, scheduler))

if __name__ == '__main__':
    lib = ImportLib()
    scheduler = sched.scheduler(timefunc=time.time)
    bla(lib, scheduler)

    while True:
        scheduler.run()
        time.sleep(10)


