max=10
for i in `seq 2 $max`
do
curl -X GET 127.0.0.1:8080/categories/MLA97994
curl -X GET 127.0.0.1:8080/categories/ML
curl -X GET 127.0.0.1:8080/
done
