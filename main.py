from dbs import init_db
from parse_json import init_json
from parse_models import parse_location_data, parse_location_db
from ploty_with_pandas import plot


def load_data_into_db(json_data, db):
    locations = []
    for data in json_data:
        location = parse_location_data(data)
        locations.append(parse_location_db(location, db))
    return locations


def setting_up():
    enginge, session = init_db()

    json_data = init_json()
    location_ptr = load_data_into_db(json_data, session)

    plot(location_ptr)


if __name__ == '__main__':
    setting_up()
