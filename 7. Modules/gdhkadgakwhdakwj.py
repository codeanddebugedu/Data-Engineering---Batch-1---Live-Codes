# Modules
def db_connect(connection: str, port: int):
    return f"{connection} connection is connecting at port {port}"


def login(username, password):
    return f"{username} user is login using password = {password}"


def logout(username):
    return f"User {username} is logout now"
