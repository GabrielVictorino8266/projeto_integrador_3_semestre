import hashlib

def get_hash_password(password):
    """Gera o hash SHA-256 de uma senha."""
    return hashlib.sha256(password.encode()).hexdigest()

# Exemplo de uso
if __name__ == "__main__":
    password = input("Digite a senha que deseja hashear: ")
    hashed_password = get_hash_password(password)
    print(f"Senha original: {password}")
    print(f"Hash SHA-256: {hashed_password}")