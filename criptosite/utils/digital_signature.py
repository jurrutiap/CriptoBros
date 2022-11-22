import ecdsa

# Code from:
# https://cryptobook.nakov.com/digital-signatures/ecdsa-sign-verify-examples
# https://stackoverflow.com/questions/34451214/how-to-sign-and-verify-signature-with-ecdsa-in-python
# https://pypi.org/project/ecdsa/

def signECDSAsecp256k1(msg, privKey):
    signature = privKey.sign(msg)
    return signature.hex()

def sign(message):
    message = bytes(message, 'utf-16')
    sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
    vk = sk.get_verifying_key()
    a = signECDSAsecp256k1(message, sk)
    return a, vk.to_string().hex(), sk.to_string().hex()

def verify(signature, vk, message):
    vk = ecdsa.SigningKey.from_string(bytes.fromhex(vk), curve=ecdsa.SECP256k1).get_verifying_key()
    try:
        vk.verify(bytes.fromhex(signature), bytes(message, 'utf-16'))
        #print('Successful')
        return 'SUCCESSFUL AUTHENTICATION. ORIGINAL TEXT'
    except:
        #print('Tampered Text')
        return 'FAILED AUTHENTICATION. ALTERED TEXT'

if __name__ == "__main__":
    message = '星を出ていくのに、王子さまは渡り鳥の旅を利用したのだと思う'
    signature, pk, vk = sign(message)
    print(f'Signature: {signature}')
    print(f'Private key: {pk}')
    print(f'Verification key: {vk}')
    print(verify(str(signature), str(vk), message))
