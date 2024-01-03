# Yours Truly, Christian Drey S. Abusca
# From DCpET 1-1
import time
seatwork_1 = 1
seatwork_2 = 2
baseball_cost = 1 
boughton_inc = 2 
flower_garden = 3 
itech = 4 
aling_nena = 1
baseball_travel = 2
stock_loss = 3
time_conversion = 4
back = 5
QUIT_AKO = 3
def main():
    menu_display()     
    choice = 0  
    while choice != QUIT_AKO: 
        choice = int(input("Enter Your Choice: "))
        if choice == seatwork_1:
            menu_display2()
            while choice != back:
                choice = int(input("Enter Your Choice: "))
                if choice == baseball_cost:
                    print("\nBaseball Cost")
                    BP=int(input("Enter the number of Baseballs purchased "))
                    COEB=float(input("Enter the cost of each Baseball "))
                    print("Calculating..........\n")
                    time.sleep(2)
                    print("The Little League Baseball Team has spent the total amount to purchase the baseballs: PHP",TASB(BP,COEB), "\n")
                elif choice == boughton_inc:
                    print("\nBoughton Inc.")
                    SPS=float(input("Enter the Salesperson Sales "))
                    CR=0.10
                    print("The Commision Rate = 10%")
                    print("Calculating..........\n")
                    time.sleep(2)
                    print("This is the Amount of a Salespersons Commission in Boughton Inc.", ASPC(SPS, CR), "\n")
                elif choice == flower_garden:
                    print("\nFlower Garden")
                    COS=float(input("Enter the Cost of the Soil "))
                    COFS=float(input("Enter the Cost of the Flower Seeds "))
                    COF=float(input("Enter the Cost of the Fence "))
                    print("Calculating..........\n")
                    time.sleep(2)
                    print("The Garden Center spent the Total Amount to make a Flower Garden Display ",TAS(COS, COFS, COF), "\n")
                elif choice == itech:
                    print("\nITech")
                    nose=int(input("Enter the Number of Students Enrolled "))
                    note=int(input("Enter the Number of Teachers Employed "))
                    print("Calculating..........\n")
                    time.sleep(2)
                    print("This is the Average number of Students per Teacher employed at the Institute of Technology ",ANST(nose, note), "\n")
                elif choice == back:
                    print("\nGoing Back to the Menu\n")
                    return main()
                else:          
                    print("Error: Invalid selection") 
        elif choice == seatwork_2:
            menu_display3()
            while choice != back:
                choice = int(input("Enter Your Choice: "))
                if choice == aling_nena:
                    print("\nAling Nena")
                    print("She sells: ")
                    print("    Banana Cue = 50pcs \n    Turon = 25pcs \n    Maruya = 45pcs")
                    print("Banana Sales: ")
                    print("    Banana Cue Sales = 0.417\n    Turon Sales = 0.208\n    SALMAR = 0.375")
                    print("Calculating for Amount Sold..........\n")
                    time.sleep(2)
                    BATOTE = BATUMA()
                    print("Total Amount of Banana Cue Sold: ", BATOTE[3])
                    print("Total Amount of Turon Sold: ", BATOTE[4])
                    print("Total Amount of Maruya Sold: ", BATOTE[5])
                    print("Calculating for Total Sales..........\n")
                    time.sleep(2)
                    print("Total Sales: ", BATOTE[6])
                    print("Calculating for Amount Contributed Sales per Type of Banana..........\n")
                    time.sleep(2)
                    print("The percentage of the total sales that the BANANA CUE contributed is : ", BATOTE[0], "%")
                    print("The percentage of the total sales that the TURON contributed is : ", BATOTE[1],"%")
                    print("The percentage of the total sales that the MARUYA contributed is : ", BATOTE[2],"%", "\n")
                elif choice == baseball_travel:
                    print("\nBaseball Travel")
                    SECS = no_seconds_()
                    print("Calculating..........\n")
                    time.sleep(2)
                    print("The amount of time that the baseball travelled is", SECS , "seconds", "\n") 
                elif choice == stock_loss:
                    print("\nStock Loss")
                    print("Given: \n    Total Share of Stocks = 750 \n    Share Price = 35.00 \n    Share Tradecost = 31.15")
                    print("Calculating..........\n")
                    time.sleep(2)
                    print("The total amount paid per stock is : ",STOCK[0])
                    print("The total amount received from the sold stock is : ",STOCK[1])
                    print("The total amount money lost on the stock is : ",STOCK[2], "\n")
                elif choice == time_conversion:
                    print("\nTime Conversion")
                    seconds = int(input("Enter the desired number of seconds to convert it to Hours, Minutes and Seconds : "))
                    (hour, minutes, secondsss) = time_conversion_(seconds)
                    print("Converting..........\n")
                    time.sleep(2)
                    print(hour," hours ", minutes," minutes and ", secondsss, " seconds", "\n")
                elif choice == back:
                    print("\nGoing Back to the Menu\n")
                    return main()
                else:          
                    print("Error: Invalid selection") 
        elif choice == QUIT_AKO:             
            print("Exiting the program")         
        else:          
            print("Error: Invalid selection") 
def TASB(BP,COEB):
    return BP * COEB
def ASPC(SPS,CR):
    return SPS*CR
def TAS(COS, COFS, COF):
    return COS + COFS + COF
def ANST(nose, note):
    return nose/note
def BATUMA():
    BAC = 50
    TUR = 25
    MAR = 45
    SALBAC = 0.417
    SALTUR = 0.208
    SALMAR = 0.375
    TOSALBAC = int(SALBAC * BAC)
    TOLSALTUR = int(SALTUR * TUR)
    TOLSALMAR = int(SALMAR * MAR)
    TOLSAL = TOSALBAC+TOLSALTUR+TOLSALMAR
    AMCOMBAC = round((TOSALBAC / TOLSAL)*100)
    AMCOMTUR = round((TOLSALTUR / TOLSAL)*100)
    AMCOMMAR = round((TOLSALMAR / TOLSAL)*100)
    return [AMCOMBAC, AMCOMTUR, AMCOMMAR, TOSALBAC, TOLSALTUR, TOLSALMAR, TOLSAL]
def no_seconds_():
    DIFE=float(input("What is the travel specified distance in feet of the baseball? : "))
    DIME= DIFE *(1/5280)
    SPEMPH=float(input("What is the travel specified speed in mph of the baseball? : "))
    TIME= DIME/SPEMPH
    NUMS = int(TIME * 3600)
    return NUMS
def stock_loss_():
    TOSHA = 750
    SHAPRI= 35.00
    SHATRA = 31.15
    TAPS = TOSHA * SHAPRI
    TARSS = TOSHA * SHATRA
    TAML = TAPS - TARSS
    return [TAPS, TARSS, TAML]
STOCK = stock_loss_()
def time_conversion_(seconds):
    hour = seconds // 3600
    minutes = (seconds % 3600) // 60
    secondsss = seconds % 60
    return (hour, minutes, secondsss)
def menu_display():     
    print("Menu") 
    print("1) Seatwork No. 1")    
    print("2) Seatwork No. 2")
    print("3) Quit")  
def menu_display2():
    print("\nSeatwork No. 1") 
    print("1) Baseball Cost")    
    print("2) Boughton Inc")
    print("3) Flower Garden")    
    print("4) ITech")
    print("5) Back")
def menu_display3():
    print("\nSeatwork No. 2") 
    print("1) Aling Nena")    
    print("2) Baseball Travel")
    print("3) Stock Loss")    
    print("4) Time Conversion")
    print("5) Back")
main()