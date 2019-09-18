# Mapquest-API
Get your directions from point A to point B using **mapquest's API**. Read below to find out how to use the script

To Run: "Main" file (file will run but will not prompt anything out of user, user will just enter what they want) 
  On seperate lines, put the following  
  1. Number of stops
  2. Starting location
  3. Either ending location or mid location
  4. Number of outputs requested fro list ("LATLONG", "STEPS", "TOTALTIME", "TOTALDISTANCE", "ELEVATION")
  5. Which of the five outputs requested.
  
Example:   
3  
Huntington Beach, CA  
1111 Figueroa St, Los Angeles, CA  
3799 S Las Vegas Blvd, Las Vegas, NV  
5  
LATLONG  
STEPS  
TOTALTIME  
TOTALDISTANCE  
ELEVATION  

Supporting files:  
mapquest_api (uses Mapquests API to request information, and converts to Json then reads back. **Uses URLlib and Json packages**)  
output_generator (uses info read from mapquest to give output to user)

