import hashlib
import sys

rockyou = open('output.txt', 'r', encoding='utf-8' ) #output has the first 33000 words of the rockyou.txt, strings must be encoded in utf 8 before hashing
hash_sha1_dict ={}

for i in rockyou.read().splitlines(): #converting the wordlist into hash SHA1
    c_hash = hashlib.sha1()
    c_hash.update(i.encode('utf-8')) # ye karega hash in utf 8, nahi kiya toh nahi chalega
    q = c_hash.hexdigest() #ye karega hash in hexadecimal to match the file 
    modified_hash ='00000' +q[5:].strip()
    hash_sha1_dict[modified_hash] = i #key value pair key is hash , value is word from rockyou

out = open('SHA1.txt','r', encoding='utf-8')
sha1list=[]
for i in out.read().splitlines(): #ab list padho and banao
    sha1list.append(i)                             

sys.stdout = open('Password_Cracked.txt', 'a', encoding='utf-8') 
c=0
for i in sha1list:
    if i in hash_sha1_dict and c<100: #compare v v fast
        print(i,':',hash_sha1_dict[i])
        c=c+1 # 100 hogaye toh niklo
sys.stdout.close()

