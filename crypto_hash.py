import hashlib
import json


def crypto_hash(*args):
    """
    Return a sha-256 hash of the given arguments
    """

    # here we are sorting for arguments that may come in different order
    # This way we can get the same hash for the same parameters in different  order
    # Note the use of lambda to to get the string representation of each argument
    stringified_args = sorted(map(lambda data: json.dumps(data), args))
    print(f'stringified_args: {stringified_args}')

    joined_data = ''.join(stringified_args)

    print(f'joined_data: {joined_data}')

    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()

def main():
    print(f"crypto_hash('foo'): {crypto_hash('foo')}")
    print(f"crypto_hash(1): {crypto_hash(1)}")
    print(f"crypto_hash([2, 3]): {crypto_hash([2, 3])}")
    print(f"crypto_hash('one', 'two', 'three'): {crypto_hash('one', 'two', 'three')}")
    print(f"crypto_hash(1, 'two', [2,4]): {crypto_hash(1, 'two', [2,4])}")
    print(f"crypto_hash(1, [2,4], ): {crypto_hash(1, 'two', [2,4])}")
    print(f"crypto_hash(1, [2,4], 'two'): {crypto_hash(1, [2,4], 'two')}")


if __name__ == '__main__':
    main()
