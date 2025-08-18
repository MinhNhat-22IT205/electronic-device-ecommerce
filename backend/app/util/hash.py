import hashlib
import os
from datetime import datetime

def generate_object_key(filename: str) -> str:
    # Create a unique hash using timestamp + filename
    name, ext = os.path.splitext(filename)
    unique_str = f"{datetime.utcnow().timestamp()}_{filename}"
    file_hash = hashlib.md5(unique_str.encode()).hexdigest()
    
    # Store under <hash><ext>
    return f"{file_hash}{ext}"

