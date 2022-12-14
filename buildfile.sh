#buildfile.sh
echo "hello world"
pip3 install -r music_controller/requirements.txt
python3.9 music_controller/manage.py makemigrations 
python3.9 music_controller/manage.py migrate 
python3.9 music_controller/manage.py runserver 