# WhetherMonitor
This project is based on SPACE WEATHER MONITORING FOR A VIRTUAL REALITY SIMULATION OF A MARTIAN SETTLEMENT project by Italian Mars City(a sub organization under python.org). Project is expected to carried out with GSOC 2017

Basic architecture of the project carries 3 modules.
1) Python interface for moddeling(the project)
2) NOAA, PREDICCS , FORSPE services (Online web services which give whether data)
3) Tensorflow library (Calculations and prediction support in Mashine learning and Neural Network perspective)

This project carries implementing the module 1 and connecting it with other mentioned Libraries and web services.

1 st will have a 3 tier architecture. Purposes of three layers will be as follows.

1) Communicate with the user.
(API for the outside/ invoking internal functions )
2) Communicate  with external services.
Includes
  i) Token management with web portals
  ii) Requesting data from the portals
  iii) extract and convert recieved json data into a useble format. 
3) Comuputational works and comunicating with tensorflow.

In this case 3 rd tier should inplement following tasks.

1) Getting data from the 2nd tier.
2) train tensorflow models with acquired data.
3) Generate predictions (probabilistic or statistical )
4) compare the results recieved from NOAA and  and FORSPEF.
Desition on choosing both or one will be able to manage. An algorithm would have to develop to combine results. 
5) Present the predictions.


Information flow through the tiers will be as follows.

Invoke function from API
1st layer invokes appropriate  interal functions of the 3rd layer depending on what is adressesed through the API.
Collecting data from web portals is handed to 2 nd tier. Results are sent to second tier. Invoking tensorflow functions and generating results.
Then present data.

Expected Functions to be added to the API,

1) instant CME level ( time- optional parameter)
    This will return the instant CME level of mars. Or function will be able to predict the CME level after a given time period then the input would be a time period.

2) instant SEP level(time - optional parameter)
 This will return the instant SEP level of mars. Or function will be able to predict the SEP level after a given time period then the input would be a time period.

3) CME monitor(hazardous level of CME- optional)
  This function will continuously predict the CME level at MARS and send responses like "danger", "warning", "safe", "return to base in *time-period" optional parameter is to introduce the hazardous levels. When the value is not passed default values will be used.

4) SEP monitor(hazardous level of SEP- SEP)
  This function will continuously predict the SEP level at MARS and send responses like "danger", "warning", "safe", "return to base in *time-period" optional parameter is to introduce the hazardous levels. When the value is not passed default values will be used.
5)Speed Of Particles(particle type - optional)
This function will return the average speed of the particles specified in the function input. Where it is not specified function will return a chart of speeds of all the particle types.

6) Equivalent radiation doses(radiation type - optional)
 This function will return the predicted radiation dose on the Mars surface for specified radiation type. Where it is not given radiation doses of all the available radiation types will be returned.
