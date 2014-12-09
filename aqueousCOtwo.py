                                                # SOLVING AQUEOUS CO2 SYSTEM VOLUME


# Authored by : 10GG20017 
# Current Version : 0.1     ( Final expected version : 1.0 )

#Python 2.7.6 (default, Nov 10 2013, 19:24:24), 64 bit (AMD64) on win32
#If using Windows machine, run the code on CMD (Command Prompt) : ' python new_code.py   '

#Don't play with indentation. Whole code will break down if indentation is not properly followed

############################### DON'T PLAY WITH CODE HERE ####################################################

import math                         #import math package

def mrk_equation(pressure,temperature,fxCo2,volume,TOL):                                    #Function for mrk_equation
    bH2o,bCo2=14.6,29.7
    a_not_h2o=35.0
    a_not_co2=46.0
    n,nMAX=1,100000
    celsius_temperature = temperature-273.15
    r=83.12
    k_dash=-11.07+(5953/temperature)-(2746000/pow(temperature,2))+ 464.6*pow(10,6)/pow(temperature,3)
    k=math.exp(k_dash)
    fxH2o = 1 - fxCo2
    b=fxCo2*bCo2+fxH2o*bH2o
    a=math.sqrt(a_not_h2o*a_not_co2) + 0.5*r*r*pow(celsius_temperature,2.5)*k

    while n<=nMAX:
        volume_equation = pow(volume,3)*pressure*pow(temperature,0.5) - pow(volume,2)*r*pow(temperature,1.5) - volume*(pressure*b*b*pow(temperature,0.5) - r*b*pow(temperature,1.5) + a) - a*b
        differential_of_volume_equation = 3*pow(volume,2)*pressure*pow(temperature,0.5) - 2*volume*r*pow(temperature,1.5) - pressure*b*b*pow(temperature,0.5) - r*b*pow(temperature,1.5)
        new_volume = volume - (volume_equation/differential_of_volume_equation)
        
        print str(volume_equation)
        
        if abs(volume_equation)<TOL:
            print str(volume_equation)
            print "we are in the if statement at the " + str(n) + " th step with volume " + str(new_volume)

            a_cubic = pressure*pow(temperature,0.5)
            b_cubic = -1.0*r*pow(temperature,1.5)

            discriminant = (b_cubic + 2*new_volume)*(b_cubic + 2*new_volume) - 4*a_cubic*new_volume*(b_cubic + 2*new_volume)
            print str(discriminant)
            minus_b_term = -1.0*(b_cubic + 2*new_volume)
            print "-b term is " + str(minus_b_term)
            print "in the 2a term, a is " + str(a_cubic)
            quad_volume1 = (minus_b_term + math.sqrt(discriminant))/(2*a_cubic)
            print "1st quadratic volume is " + str(quad_volume1)
            quad_volume2 = (minus_b_term - math.sqrt(discriminant))/(2*a_cubic)
            print "1st quadratic volume is " + str(quad_volume2)
            return (new_volume, quad_volume1, quad_volume2)
        else:
            volume = new_volume
            print str(volume_equation)
            print "we are in the else statement at the " + str(n) + " th step with volume " + str(volume)
        n=n+1

########################################################################################################################################################

## MAIN FUNCTION ########################### CHANGE THE VALUES ACCORDING TO YOUR REQUIREMENTS IN THIS CODE BLOCK ###########################################################
## for this function 

chosen_pressure = 100.0 #in bars
chosen_temperature_in_celsius = 100.0 
chosen_Co2_composition = 0.2
estimated_volume = 20 #in cm cube
# when volume is 140.0, 1.0  roots are 109.646, 194.083, -70
# 14,0.1 roots 11, 134, -10
tolerance_value = 0.00001                            # It is difficult to converge to an actual zero value. So, chose a tolerance_value that is very close to 0

#################################################################################################################################################################

################### DON'T PLAY WITH CODE NOW ####################################################################################################################

chosen_temperature = chosen_temperature_in_celsius + 273.15
req_volume, quad_volume1, quad_volume2  = mrk_equation(chosen_pressure,chosen_temperature,chosen_Co2_composition,estimated_volume,tolerance_value)

# Final PRINT statement #################################################################################################################################

print "VALUE OF VOLUME FROM THE MAIN FUNCTION IS " + str(req_volume) + " , " + str(quad_volume1) + " and " + str(quad_volume2)

############ END ###########################################################################################################################################
