#buildfile.sh
echo "hello world erik"
pip3 install -r music_controller/requirements.txt
python3 music_controller/manage.py makemigrations 
python3 music_controller/manage.py migrate 
python3 music_controller/manage.py runserver 