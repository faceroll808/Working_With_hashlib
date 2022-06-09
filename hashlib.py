import hashlib
pass_hash= input("Enter md5 Hash: ")
wordlist=input("file name: ")
try:
    pass_file=open(wordlist,"r")

except:
    print("no file found!")
    quit()
for wor in pass_file:
    enc_wrd = word.encode('UTF-8')
    digest = hashlib.md5(enc_wrd.strip()).hexdigest()

    if digest==pass_hash:
        print("password found")
        print("password is "+ word)
        flag=1
        break

if flag ==0:
    print("password is not in the list")