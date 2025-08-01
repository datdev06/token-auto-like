ADMIN_PASSWORD = "123456"

def load_tokens():
    try:
        with open("tokens.txt", "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []

def save_tokens(tokens):
    with open("tokens.txt", "w") as f:
        f.write("\n".join(tokens))

def load_log_uid():
    try:
        with open("log_uid.txt", "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []

def save_log_uid(logs):
    with open("log_uid.txt", "w") as f:
        f.write("\n".join(logs))