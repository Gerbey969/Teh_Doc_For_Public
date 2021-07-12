# Teh_Doc_For_Public
Website for using inside the company.

To install packages:<br>
```python
pip install -r requirements.txt
```
To apply all migrations:<br>
```python
python manage.py makemigrations
python manage.py migrate
```

To make translation records:
```python
python manage.py makemessages -l en
```

To apply:
```python
python manage.py compilemessages
```
