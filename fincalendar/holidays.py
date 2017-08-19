""" This module exists to allow overrides of calendars since they're so hard to get right
    programaticaly, and sometimes we need to correct a calendar very quickly.
    For now, I make no attempt to replicate a "fixed" version all the functionality in
    workalendar - but rather just create a new 'get holidays for a given year' function. """

from functools import lru_cache
from dateutil.parser import parse

from fincalendar.holiday_mapping import get_calendar

@lru_cache(maxsize=128)
def get_overrides():
    # READ FILE
    results = {"SGP": { 
               "add": {parse("2015-5-27").date(), parse("2016-5-27").date()},
               "subtract": {parse("2015-12-25").date()}
               },
               "HKG": { 
               "add": {parse("2015-5-27").date(), parse("2016-5-27").date()}
               },
               "GBR": { 
               "subtract": {parse("2015-12-25").date()}
               }}
    return results

def holidays_set(alpha_3_country_code, year, state_code=None):
    """ TODO - Add state_code handling """
    overrides = get_overrides().get(alpha_3_country_code) or {}
    calendar = get_calendar(alpha_3_country_code=alpha_3_country_code)
    holidays = calendar.holidays_set(year=year)
    holidays = holidays | overrides.get("add", set()) - overrides.get("subtract", set())
    return holidays
