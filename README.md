# covid-vaccine-finder-delhi
A script I created to alert me when a slot becomes available so that I can go to cowin site and book it

Make sure Python3 is installed on your machine. Update the date at the top in the file `vaccine_slot_finder.py` to match current date

For example, if you're running the script on May 15, use this:
```
# Update the process date here
process_date = '15-05-2021'
```

Create a python3 virtual env (this needs to be done only once):

```
python3 -m venv venv
source venv/bin/activate
pip install requests
```


Execute the script:
```
python vaccine_slot_finder.py
```



If you need to run the script again in future,

```
source venv/bin/activate
python vaccine_slot_finder.py
```