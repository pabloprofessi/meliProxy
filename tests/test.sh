max=99
for i in `seq 2 $max`
do
curl -X GET 127.0.0.1:8888/categories/MLA97994
curl -X GET 127.0.0.1:8888/categories/MLA
curl -X GET 127.0.0.1:8888/
done
