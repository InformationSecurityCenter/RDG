from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ed25519


private_key = ed25519.Ed25519PrivateKey.generate()
private_key_bytes = private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                              format=serialization.PrivateFormat.PKCS8,
                                              encryption_algorithm=serialization.NoEncryption())
print("Private key: ", repr(private_key_bytes.decode()))

public_key = private_key.public_key()
public_key_bytes = public_key.public_bytes(encoding=serialization.Encoding.OpenSSH,
                                           format=serialization.PublicFormat.OpenSSH)
print("Public key: ", repr(public_key_bytes.decode()))
