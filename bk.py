import json
from bottle import run, post, get, request

LOGIN_DATA = {
    "sample_login": "sample_password"
}


@post('/add')
def add_login_info():
    try:
        req_data = json.loads(request.body.read())
        username = req_data["username"]
        password = req_data["as_password"]
        data = {}
        with open("login.json", "r") as r_file:
            data = json.load(r_file)
            data.update({username: password})
        with open("login.json", "w") as w_file:
            json.dump(data, w_file)
        return "SUCCESS"
    except Exception as e:
        msg = f"FAILED\n {str(e)}"
        return msg


@post('/login')
def login_check():
    try:
        req_data = json.loads(request.body.read())
        with open("login.json", "r") as read_file:
            data = json.load(read_file)
            username = req_data.get("username", None)
            password = req_data.get("as_password", None)
            # Input check
            if not username:
                msg = "Username must be provided"
                raise Exception(msg)
            if not password:
                msg = "Password must be provided"
                raise Exception(msg)
            if not data[username]:
                return "FALSE"

            password_from_dict = data[username]
            if password != password_from_dict:
                return "FALSE"
            return "TRUE"

    except Exception as e:
        msg = f"FAILED\n {str(e)}"
        return msg


if __name__ == "__main__":
    run(host='localhost', port=8080, debug=True)