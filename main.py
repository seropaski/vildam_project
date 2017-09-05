import re
from collections import defaultdict
from os import listdir
from os.path import isfile, join

PATH = 'list/'
DEFAULT_LOGIN = 'root'
DEFAULT_PASSWORD = 'password'


def get_full_schema(path):
    files = [f for f in listdir(path) if isfile(join(path, f))]

    full_schema = defaultdict(list)
    for owner in files:
        full_schema[owner] = [dict([
            ('desc', s.rstrip().split(':')[0]),
            ('ip', s.rstrip().split(':')[1]),
            ('login', s.rstrip().split(':')[2] if s.rstrip().split(':')[2] else DEFAULT_LOGIN),
            ('password', s.rstrip().split(':')[3] if s.rstrip().split(':')[3] else DEFAULT_PASSWORD),
        ]) for s in
            open(join(path, owner)).readlines()]

    return full_schema


def search_server_by_schema(schema_by_owner, part_of_name):
    try:
        pattern = re.compile(part_of_name)
    except Exception as e:
        return 'Wrong format of pattern: %s' % e

    server_list = [server for server in schema_by_owner if re.search(pattern, server.get('desc'))]

    return server_list


if __name__ == '__main__':

    part_of_name_for_search = 'bulk'
    owner_name = 'OWNER1'

    schema = get_full_schema(PATH)
    print('Full schema: %s\n' % schema)
    found_servers = search_server_by_schema(schema[owner_name], part_of_name_for_search)
    print('Result of search: %s' % found_servers)
