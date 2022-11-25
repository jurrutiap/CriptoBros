from Crypto.PublicKey import ECC
import Crypto.Random
from Crypto.Signature import eddsa

def EC25519Sing(message):

    if isinstance(message,str):
        message = message.encode()

    key = ECC.generate(curve = "Ed25519")
    signer = eddsa.new(key, mode = 'rfc8032')
    signature = signer.sign(message)

    key = key.export_key(format = "DER")



    return signature.hex(),key.hex()

def EC25519Verify(message,key,signature):
    key = bytes.fromhex(key)
    key = ECC.import_key(key)
    if isinstance(message,str):
        message = message.encode()
    signature = bytes.fromhex(signature)

    signer = eddsa.new(key, mode = 'rfc8032')
    try:
        signer.verify(message, signature)
        return "Clave valida"
    except:
        return "Clave o mensaje han sido alterados"


message = """Dies irae, dies illa,
Solvet saeclum in favilla
Teste David cum Sibylla.

Quantus tremor est futurus,
Quando iudex est venturus,
Cuncta stricte discussurus!

Tuba mirum spargens sonum
Per sepulchra regionum
Coget omnes ante thronurn.

Mors stupebit et natura,
Cum resurget creatura
Iudicanti responsura.

Liber scriptus proferetur,
In quo totum continetur,
Unde mundus iudicetur.

Iudex ergo cum censebit,
Quidquid latet apparebit:
Nil inultum remanebit.

Quid sum miser tunc dicturus,
Quem patronum rogaturus,
Cum vix iustus sit securus?"""

signature, key = EC25519Sing(message)
print(EC25519Verify(message,key,signature))