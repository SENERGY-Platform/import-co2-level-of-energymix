# https://api.co2signal.com/v1/latest?countryCode=DE

import CO2DataFetcher, sched, time
from import_lib.import_lib import ImportLib, get_logger

logger = get_logger(__name__)

def co2DataScheduler(lib, scheduler):
    try:
        lib.put(*CO2DataFetcher.co2DataFetcher())
    except Exception as e:
        logger.error(str(e))
    scheduler.enter(600, 0, co2DataScheduler, (lib, scheduler))

if __name__ == '__main__':
    lib = ImportLib("github.com/SENERGY-Platform/import-co2-level-of-energymix")
    scheduler = sched.scheduler(timefunc=time.time)
    co2DataScheduler(lib, scheduler)

    while True:
        scheduler.run()
        time.sleep(10)