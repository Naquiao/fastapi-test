# **FASTAPI test**

## **Python API with FASTAPI**

• a POST request with a boolean parameter that returns the current date in yyyy-mm-dd hh:ii:ss format if the parameter is true and returns the date in yyyy-dd-mm format if the parameter is false.


• a GET request that obtains the value of a counter of times that one of the two endpoints was called

### First Step
  
Disclaimer : FASTAPI need Python 3.6 version or beyond
 ```diff
 + pip install -r requirements.txt
```

Whenever you are ready to run the live server:
 ```diff
 + uvicorn main:app --reload
```
The results are showed here:

**1 - Landing page of Swagger**
![image](https://github.com/Naquiao/marvik-technical-test/blob/main/docs/Swagger-landing.png)

**2 - PUT - true test**
![image](https://github.com/Naquiao/marvik-technical-test/blob/main/docs/put-test-true.png)

**3 - PUT - false test**
![image](https://github.com/Naquiao/marvik-technical-test/blob/main/docs/put-test-false.png)

**4 - GET - counter test**
![image](https://github.com/Naquiao/marvik-technical-test/blob/main/docs/get-test-counter.png)


