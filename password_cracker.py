import hashlib

def crack_sha1_hash(hash, use_salts = False):
    password_file = "top-10000-passwords.txt"
    salts_file = "known-salts.txt"    
    
    try:
        with open(password_file, 'r') as file:
            passwords = [line.strip() for line in file]
        if use_salts:
            try:
                with open(salts_file, 'r') as file:
                    salts = [line.strip() for line in file]
            except FileNotFoundError:
                return "Salts file not found"
            
            for salt in salts:
                for password in passwords:
                    for salted_password in [salt + password, password + salt]:
                        h = hashlib.sha1(salted_password.encode()).hexdigest()
                        if h == hash:
                            return password
        else:
                        
            for password in passwords:
                
                h = hashlib.sha1(password.encode()).hexdigest()
                if h == hash:
                    return password
        return "PASSWORD NOT IN DATABASE"
    except FileNotFoundError:
        return "Password file not found"
                
    


hash_sammy = "b305921a3723cd5d70a375cd21a61e60aabb84ec"
superman    = "53d8b3dc9d39f0184144674e310185e41a87ffd5"
print(crack_sha1_hash(hash_sammy))
print(crack_sha1_hash(superman, True))