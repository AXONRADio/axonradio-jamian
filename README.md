# axonradio-jamian
my section of the code for the CSUN senior project AXONRADio
### To run backend code:
* install anaconda
* `conda create --name myenv --file spec-file.txt`</ol>
* `conda activate myenv`</ol>
* `python predictions.py` to run script to classify youtube links</ol>
* `python restful_test.py` to run restful flask server</ol>


### Install and run mongodb
* Make sure mongo db is installed
* start server with:
```
sudo service mongod start
```
* to access the shell
```
mongo --host 127.0.0.1:27017
```

### Run vue app
* to run vue app in debug mode
```
cd frontend
npm run dev
```
* flask app redirects to dev server if `debug=true`
* else it will redirect to `backend/build/template`
