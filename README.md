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