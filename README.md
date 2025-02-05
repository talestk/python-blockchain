**Activate the virtual environment**
```
source blockchain-env/bin/activate
```

**Install all packages**
```
pip install -r requirements.txt
```

**Run the tests**

Make sure to activate the virtual environment.
```
python3 -m pytest backend/tests
```

**Run the application and API**

Make sure to activate the virtual environment.
```
python -m backend.app
```

**File with pubnub keys**

File should be named and be on the backend folder:
```
pubnub_keys.txt
```
Content of the file should respect:
- first line should be the subscriber key from pubnub.com
- second line should be the publisher key

**Run a peer instance**

Make sure to activate the virtual environment.

```
export PEER=True && python -m backend.app
```