from texttonumber import findlet


def decrypt():
    message = open('message', 'r')
    privateKey = open('privateKey', 'r')

    decrypted = message.read()   # ** int(privateKey.readline()) % int(privateKey.readline())
    nums = decrypted.split()

    decrypt_num = []
    d = privateKey.readline()
    n = privateKey.readline()

    for items in nums:

        decrypt_num.append((int(items) ** int(d)) % int(n))

    message.close()
    privateKey.close()

    return decrypt_num


print(decrypt())

for items in decrypt():
    print(findlet(items))
