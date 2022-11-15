# This two lines reset the database
rm ./../Service_Web/video1.db
cp ./../DB_origin.db ./../Service_Web/video1.db

python3 ./lib_test/main.py

rm ./../Service_Web/video1.db
cp ./../DB_origin.db ./../Service_Web/video1.db