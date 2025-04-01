import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get(server_address, end_point, cert_path, headers = None):
    import requests
    try:
        response = requests.get(f"https://{server_address}{end_point}", headers = headers, verify = cert_path)
        return response.json()
    except:
        return {"status": "error", "message": f"Can't access server at {server_address}"}

def post(server_address, end_point, cert_path, data, headers = None):
    import requests
    try:
        response = requests.post(f"https://{server_address}{end_point}", json = data, headers = headers, verify = cert_path)
        return response.json()
    except:
        return {"status": "error", "message": f"Can't access server at {server_address}"}

def login(server_address, cert_path, username, password):
    data = {"username": username, "password": password}
    res = post(server_address, "/login", cert_path, data)

    return res

def logout(server_address, cert_path, username):
    data = {"username": username}
    res = post(server_address, "/logout", cert_path, data)

    return res

def register(server_address, cert_path, username, password):
    data = {"username": username, "password": password}
    res = post(server_address, "/register", cert_path, data)

    return res

def get_user_info(server_address, cert_path, token):
    headers = {"Authorization": f"Bearer:{token}"}
    res = get(server_address, "/me", cert_path, headers = headers)

    return res