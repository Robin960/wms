#How to run this application
1. This application requires the installation of Python and some dependencies on your machine. 
2. Please make sure the all the files placed on the same directory.
3. All the requirements are installed based on 'requirements.txt' file.
   If dependencies are not installed on your machine, use this command on your console 
   
   'pip install -r requirements.txt' 
4. Just execute the 'run.py' on your command line console.

#Endpoints
1.  run on localhot: 127.0.0.1:5100/

2.  127.0.0.1:5100/warehouse --> Home Page

    127.0.0.1:5100/warehouse/orders?customer_name = ''  --> Order Information

    127.0.0.1:5100/warehouse/add/orders/'id'/'customer_name' --> Add order but pass the id and customer_name mentioned on quotes.
    
    127.0.0.1:5100/warehouse/delete/orders/'id'

    127.0.0.1:5100/warehouse/update/orders/'id'/'update value'   --> 'update value' = customer_name = 'abc'

    127.0.0.1:5100/warehouse/sku/'id'
    
    127.0.0.1:5100/warehouse/storage/'id'
    
    127.0.0.1:5100/warehouse/orderline/'id'

#Technologiey Stack
1. Python3: It's an open source, light weight and fast prograaming language. 
            It's easier to learn and requires lee lines of code to implement the solutions a scompare to other programming languages.
            It's flexible and have good frameworks for web development and good for buiding prototypes and start up tech companies.

2. Flask:   It's a light weight web development framework for python and also known as micro-framework.
            It provides the pluggable approch to develop the functionalities and supports restful api's.

3. SQLAlchemy: It can be used with or without the ORM(Object Relational Mapping).
               It provides the way to write create, read and other databse operations without writing SQL queries on database.
             


#Models.py
1. The model file contains the logic of model classes which are orders, sku, storage and orderline.
2. From the routes, we can send the request to our model and model will execute the requested parameter 
   and send back the response to the requested route.
3. The relationship can be added or enhanced on these models for future work. So, we can ensure the data inetegrity and consistency.


#Routes.py
1. This file holds all the routes which are required for the warehouse management system. The end user can add, delete
   insert and update the Orders. But at the moment for other classes user can just read the data.
2. The same logic can be implemented to perform the CUD operations on other classes.

#site.db
1. This file holds the data for all the classes/models.
2. For the demonstration of this case study, there is already some data available. So, you can perform some basic operations.

#Future Work
1.  Order Fulfillment 
2.  GUI for all the classes
3.  CRUD operations on all the classes
4.  Ipmrove order searching parameters
5.  Security Implementation
6.  API validation