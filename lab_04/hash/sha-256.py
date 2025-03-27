import hashlib

def calculate_sha256_hash(data):
    """Hàm tính toán giá trị hash SHA-256 cho chuỗi đầu vào."""
    sha256_hash = hashlib.sha256()  
    sha256_hash.update(data.encode('utf-8'))  
    return sha256_hash.hexdigest()  

data_to_hash = input("Nhập dữ liệu để hash bằng SHA-256: ")

hash_value = calculate_sha256_hash(data_to_hash)

print("Giá trị hash SHA-256 của chuỗi '{}' là: {}".format(data_to_hash, hash_value))
