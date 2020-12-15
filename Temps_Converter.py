def temp_conv():
    t_in=float(input("Please enter the temperature you want to convert : "))

    unite = input("If the temperature is in Celsius, please click on 'c' and if it's in Farenheight, please click on 'f' : ")

    print("The temperature you want to convert is : " + str(t_in))
    
    if unite == "f" :
        t_out = (t_in -32)*5/9
        x="Farenheight"
        y="Celcius"
    elif unite  == "c" :
        t_out = ((t_in*9/5) +32)
        x="Celcius"
        y="Farenheight"
    else :
        print("Well you should have done a mistake !")

    print("The temperature " + str(t_in) + " in " + x + " is equal to " + str(t_out) + " in " + y)
    print("end")
    print("V Temps_Converter 1.1")

temp_conv()
temp_conv()


