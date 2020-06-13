# Chorus.ai
#### How to run the script?
Activate virtual env and install requirements.
```shell script
$ python -m venv .
# Linux 
$ source bin/activate
# Windows 
$ Scripts/activate.bat
$ pip install -r requirements.txt
```
Last, just run the script.
```shell script
(venv)$ python main.py
```

| File          | Short Description | 
| ------------- |:-------------:|
| `config.py`      | URLs and headers |
| `run.py`      | Just call the functions/classes      |
| `scraper.py` | `Scrape` class, we handle everything here(BS4)|
| `serializer.py` | 2 functions, structuring the JSON and saving it |
| `data/chorus.json` | Result is saved here |