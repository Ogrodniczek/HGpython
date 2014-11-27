# encoding: utf-8
"""List of users and their default directory"""


def user_list():
    """getting list of users from file"""
    users = []
    handler = open('/etc/passwd')
    for lines_in_passwd in handler:
        users.append(lines_in_passwd.split(":"))
    n = 0
    while n+1 <= len(users):
        print(users[n][0], " : ", users[n][5])
        n += 1


if __name__ == '__main__':
    user_list()