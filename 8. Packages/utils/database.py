def db_connect(connection: str, port: int):
    return f"{connection} connection is connecting at port {port}"


def db_disconnect(connection: str, port: int):
    return f"{connection} connection is disconnecting at port {port}"
