
weighttp -n 50000 -c 20 -t 20 -k  "http://127.0.0.1:8080/categories/MLA97994"



#n ........ number of HTTP requests
#c ........ number of concurrent connections (default: 1)
#k ........ enable HTTP keep-alives (default: none)
#t ......... number of threads of the test (default: 1, use one thread per CPU Core)