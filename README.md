Group22
Contributors:-

Joshal Jain - ec201007,

Akshara Gopakumar - ec201010,

Keerthana Hariharan - ec201035,

Sindhu Javvaji - ec201034,

Nayana Narayan - ec20043

# Cloud_Computing

# Covid-19-API

## Part I - CRUD Operations
## What the API is for?

The API is intended for developers, machines, programs, and other websites to be able to quickly fetch up to date information on the COVID-19 epidemic.
It can be used to build tools and systems that are used for data analysis all the way to websites that act as public dashboards and charts. This API, consist of data of COVID cases from countries all over the world. This project focuses on data from one country (i.e _The United States of America_)

## Using the API
API base:
https://covid-api.mmediagroup.fr/v1

## Crude Operations
1. GET /cases

   __Function__
    This function brings out all the data from the chosen parameters of the given dataset.

   __Parameters__
    Any country name (_here_, United States)
    1.	_State names_
    2.	_Confirmed Cases_
    3.	_Deaths_
    4.	_Updated_  (all states are updated on _31/3/2021_)

2. POST /cases
   
   __Function__
    This function allows to add a particular parameter/data to the existing database. 
   
   __Parameters__
    1.	_State name_ (here _Mississippi_)
    2.	_Confirmed cases_ in Mississippi.
    3.	_Deaths_ in Mississippi
    4.	Date _Updated_ (here, _1/4/2021_)

3. PUT /cases
  
  __Function__
    This function updates a particular parameter/data to the existing database. 
   
   __Parameters__
    1.	Confirmed cases in Mississippi.
    2.	Deaths in Mississippi
    3.	Date Updated (here, 1/4/2021)

4. DELETE /cases
   
   __Function__
    This function updates a particular parameter/data to the existing database. 
   
   __Parameters__
    1.	State names (here Alaska)
    2.	Confirmed cases 
    3.	Deaths 
    4.	Updated 

## Part II - SERVING APPLICATION OVER https
This application uses a python library called pyopenssl to server the application over https.
