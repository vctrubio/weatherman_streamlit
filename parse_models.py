from models import *


def parse_location_data(data):
    location_json = {
        'latitude': data['latitude'],
        'longitude': data['longitude'],
        'address': data['resolvedAddress'],
        'days': [Day(**ptr) for ptr in data['days']]
    }
    location = Location(**location_json)
    return location


def parse_location_db(location, SessionLocal):
    locations = []
    with SessionLocal() as db:
        location_dict = location.model_dump()
        locatation_ptr = location_dict.copy()
        location_dict['days'] = [DayDB(**day.model_dump())
                                 for day in location.days]
        existing_location = db.query(LocationDB).filter_by(
            address=location_dict['address']).first()

        if existing_location is None:
            existing_location = LocationDB(**location_dict)
            db.add(existing_location)
            print(f'{location.address} | + Added')
        else:
            print(f'{location.address} | - Exists')

        for day in location.days:
            existing_day = db.query(DayDB).filter_by(
                datetime=day.datetime).first()
            if existing_day is None:
                day_db = DayDB(**day.model_dump())
                existing_location.days.append(day_db)
                print(f'day {day.datetime} | + Added')
            else:
                print(f'day {day.datetime} | - Exists')
        locations.append(locatation_ptr)
        db.commit()
        print(f'-----------------------------------------------\n')
    return locations
