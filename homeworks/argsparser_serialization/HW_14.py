import json
import argparse


def create_file():
    file = open("users_info.json", 'w')
    file.write(json.dumps([]))
    file.close()
    return open("users_info.json", 'r')


def create_user(users):
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", help="username")
    parser.add_argument("-e", "--email", help="email")
    parser.add_argument("-s", "--status", help="status")
    args = parser.parse_args()
    try:
        users["username"] = args.username
        users["email"] = args.email
        users["status"] = args.status
    except IndexError:
        raise Exception("Error")


def check_user(user, users_info):
    for users in users_info:
        if user["username"] == users["username"] or user["email"] == users["email"]:
            return True
    return False


def add_user(user):
    try:
        read_files = open("users_info.json", "r")
    except FileNotFoundError:
        read_files = create_file()
    try:
        users_info = json.loads(read_files.read())
    except ValueError:
        with open("users_info.json", 'w') as w_file:
            w_file.write(json.dumps([]))
        users_info = []
    read_files.close()

    if not check_user(user, users_info):
        users_info.append(user)
        with open("users_info.json", "w") as w_file:
            w_file.write(json.dumps(users_info, indent=4, sort_keys=True))
    else:
        raise "User with user or email already"


if __name__ == "__main__":
    new_user = {}
    create_user(new_user)
    add_user(new_user)
