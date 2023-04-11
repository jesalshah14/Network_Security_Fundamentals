class RC4Cipher:
    
    def change_str_to_unicode(self, string :str) -> list[int]:
        unicode :list[int]= []
        for item in string:
            unicode.append(ord(item))
        
        return unicode
    
    def change_unicode_to_str(self, unicodeList:list[int]) -> str:
        string : str=""

        for i in unicodeList:
            string += chr(i)

        return string
    
    def get_keyScheduling (self, key: str, size :int = 256) -> list[int]:
        
        S = list(range(size))        

        #getting unicode code of the key
        key_unicode :list[int]= self.change_str_to_unicode(key)       
                       
        # incluing unicode key to K list, fitting the lenght of S list     
        K = key_unicode * (size//len(key_unicode)) + key_unicode[:size%len(key_unicode)]

        #Key Scheduling
        j :int = 0 
        for i in range(size):
            j = (j+ S[i] + K[i])% size
            # making diffusion in the S list with the result of j
            temp:int = S[i]
            S[i] = S[j]
            S[j] = temp
        
        return S

    def generate_key_stream(self, plaintext:str, key_schedule: list[int], size:int = 256) -> list[int]:
        
        #getting unicode code of the plaintext
        # plaintext_unicode :list[int]= self.change_str_to_unicode(plaintext)
        
        #making the key stream
        j :int = 0
        key_stream :list[int] = []
        for i in range(1,len(plaintext)+1): #beginning from position 1 in the key_schedule list
            j = (j+ key_schedule[i]) % size
            
            # making diffusion in the key_schedule list with the result of j
            temp:int = key_schedule[i]
            key_schedule[i] = key_schedule[j]
            key_schedule[j] = temp

            #making a diffusion again to then create the key stream 
            t = (key_schedule[i] + key_schedule[j])% size
            key_stream.append(key_schedule[t])
        
        return key_stream
    
    def encryption (self, plain_text :str, key:str):

        #making difusion of a array lenght n and the key
        key_schedule :list[int] = self.get_keyScheduling(key)

        #making the key stream
        key_stream :list[int] = self.generate_key_stream(plain_text,key_schedule)

        #changing the plaintext to unicode        
        plaintext_unicode :list[int]= self.change_str_to_unicode(plain_text)
        
        # making XOR operation between Plaintext and Key Stream
        ciphertext: list[int] = []
        if len(plaintext_unicode) == len(key_stream):    

            for i in range(len(plaintext_unicode)):
                ciphertext.append(plaintext_unicode[i] ^ key_stream[i])
        else:
            print(f"It is not possible to encrypt the text: {plain_text}")
        
        #changing ciphetext from unicode to string
        ct : str = self.change_unicode_to_str(ciphertext)

        return ct
    
    def decryption (self, cipher_text :str, key:str):

        #making difusion of a array lenght n and the key
        key_schedule :list[int] = self.get_keyScheduling(key)

        #making the key stream
        key_stream :list[int] = self.generate_key_stream(cipher_text,key_schedule)

        #changing the cipher text to unicode        
        ciphertext_unicode :list[int]= self.change_str_to_unicode(cipher_text)
        
        # making XOR operation between Ciphertext and Key Stream
        plaintext: list[int] = []
        if len(ciphertext_unicode) == len(key_stream):    

            for i in range(len(ciphertext_unicode)):
                plaintext.append(ciphertext_unicode[i] ^ key_stream[i])
        else:
            print(f"It is not possible to decrypt the ciphertext: {cipher_text}")
        
        #changing plaintext from unicode to string
        pt : str = self.change_unicode_to_str(plaintext)

        return pt

# def main(): 

#     RC4_cipher :RC4Cipher = RC4Cipher()
#     key :str = "brucelee"
#     plain_text :str = "attackatdawn" 

#     print(f"Plaintext: {plain_text}")

#     output :str = RC4_cipher.encryption(plain_text, key)

#     print(f"Ciphertext: {output}")

#     plain_text = RC4_cipher.decryption(output, key)

#     print(f"Plaintext back to original after decryption: {plain_text}")

# if __name__ == '__main__':
#     main()