from os import listdir
from os.path import isfile, join

from collections import defaultdict


def main():
    my_path = 'list/'
    files = [f for f in listdir(my_path) if isfile(join(my_path, f))]
    schema = defaultdict(list)
    for owner in files:
        schema[owner] = [dict([('ip', s.replace('\n', '').split(':')[0]),
                               ('login', s.replace('\n', '').split(':')[1]),
                               ('password', s.replace('\n', '').split(':')[2])]) for s in
                         open(join(my_path, owner)).readlines()]
    print('\nList of owners: %s' % [i for i in schema.keys()])
    print('\nList of server by owner: %s' % schema['OWNER1'])
    print('\nList of server info by owner:')
    print(*['\tServer:\n\t\tip: %s\n\t\tlogin: %s\n\t\tpassword: %s\n' % (server['ip'], server['login'], server['password']) for server in
            schema['OWNER1']])
    print('\nWhole schema\n%s' % schema)

if __name__ == '__main__':
    main()
