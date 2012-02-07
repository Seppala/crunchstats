rm crunch/crunch.db
rm -r crunch/main/migrations
python crunch/manage.py syncdb
python crunch/manage.py convert_to_south main


