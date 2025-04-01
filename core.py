from json import loads, dumps
import connector as conn

def open_file(mode, data_in = None):
    """Access securely the settings file"""

    path = "user_data.json"

    if mode == "read":
        try:
            f = open(path, "r")
            data = f.read()
            f.close()
        except:
            open_file("create")
            return open_file("read")
        else:
            return data
    elif mode == "write":
        f = open(path, "w")
        if data_in:
            f.write(data_in)
        f.close()
    elif mode == "create":
        f = open(path, "w")
        f.write("{}")
        f.close()

def save(key, data):
    """Saves key, data couple in settings"""

    file = open_file("read")

    saved_data = loads(file)
    saved_data[key] = data

    open_file("write", data_in = dumps(saved_data))

def delete(key):
    """Daletes key, data couple"""

    file = open_file("read")

    saved_data = loads(file)
    if get(key):
        del(saved_data[key])

    open_file("write", data_in = dumps(saved_data))

def get(key):
    """Returns data associated with key"""

    file = open_file("read")

    saved_data = loads(file)

    return saved_data.get(key)

def get_time():
    """Returns current timestamp"""

    import time

    return time.time()

def get_server_address():
    """Returns saved server address"""

    if get("dev_settings"):
        return "127.0.0.1:4443"
    else:
        return f"{get("server_address")}:{get("server_port")}"

def get_cert_path():
    """Returns saved server address or default one"""

    path = get("cert_path")
    if path:
        return path
    else:
        return "cert.pem"

def login(username, password):
    """Logs the user in, and saves relevent data"""

    if not get("connected"):
        res = conn.login(get_server_address(), get_cert_path(), username, password)
        if res["status"] == "success":
            save("username", username)
            save("password", password)
            save("token", res["token"])
            save("expiration", res["expiration"])
            save("connected", True)

            return True, res["message"]
        elif res["status"] == "error":
            return False, res["message"]
    else:
        return False, "User already connected"

def logout():
    """Logs the user out and deletes useless data"""

    if get("connected"):
        username = get("username")
        res = conn.logout(get_server_address(), get_cert_path(), username)
        if res["status"] == "success":
            delete("password")
            delete("token")
            delete("expiration")
            save("connected", False)

            return True, res["message"]
        elif res["status"] == "error":
            return False, res["message"]
    else:
        return False, "No account connected"

def register(username, password):
    """Creates a new account"""

    res = conn.register(get_server_address(), get_cert_path(), username, password)
    if res["status"] == "success":
        return True, res["message"]
    elif res["status"] == "error":
        return False, res["message"]

def account_info():
    """Gets the information related to the
    logged in account"""

    if get("connected"):
        token = get("token")
        expiration = get("expiration")
        if expiration > get_time():
            res = conn.get_user_info(get_server_address(), get_cert_path(), token)
            if res["status"] == "success":
                return True, res["message"]
            elif res["status"] == "error":
                return False, res["message"]
        else:
            login(get("username"), get("password"))
            return account_info()
    else:
        return False, "No account connected"