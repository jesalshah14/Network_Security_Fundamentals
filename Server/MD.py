import hashlib

class MDAlgorithm:
    def create_hash(self, plain_text :str) -> str:
        hash = hashlib.sha256(plain_text.encode()).hexdigest()
        return hash
    
    def verify_integrity(self, message:str, hash:str):
        new_hash = self.create_hash(message)
        
        if new_hash == hash:
            return True
        else:
            return False

