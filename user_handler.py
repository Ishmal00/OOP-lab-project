class FileHandler:
    def __init__(self, user_file="users.txt", data_file="data.txt"):
        self.user_file = user_file
        self.data_file = data_file
        open(self.user_file, 'a').close()
        open(self.data_file, 'a').close()

    def sign_up(self, username, password):
        if self._user_exists(username):
            return False, "User already exists!"
        with open(self.user_file, 'a') as f:
            f.write(f"{username},{password}\n")
        return True, "Signed up successfully!"

    def login(self, username, password):
        with open(self.user_file, 'r') as f:
            for line in f:
                u, p = line.strip().split(",")
                if u == username and p == password:
                    return True, "Login successful!"
        return False, "Invalid credentials!"

    def _user_exists(self, username):
        with open(self.user_file, 'r') as f:
            return any(line.startswith(f"{username},") for line in f)

    def add_record(self, username, data):
        with open(self.data_file, 'a') as f:
            f.write(f"{username}:{data}\n")

    def get_user_data(self, username):
        with open(self.data_file, 'r') as f:
            return [line.strip().split(":", 1)[1] for line in f if line.startswith(f"{username}:")]

    def update_record(self, username, index, new_data):
        lines = open(self.data_file, 'r').readlines()
        count = -1
        for i, line in enumerate(lines):
            if line.startswith(f"{username}:"):
                count += 1
                if count == index:
                    lines[i] = f"{username}:{new_data}\n"
                    break
        with open(self.data_file, 'w') as f:
            f.writelines(lines)

    def delete_record(self, username, index):
        lines = open(self.data_file, 'r').readlines()
        count = -1
        for i, line in enumerate(lines):
            if line.startswith(f"{username}:"):
                count += 1
                if count == index:
                    lines.pop(i)
                    break
        with open(self.data_file, 'w') as f:
            f.writelines(lines)
