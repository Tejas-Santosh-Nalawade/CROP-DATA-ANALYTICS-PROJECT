# IMPORTING LIBRARIES

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importing CSV
Top_10_crop="D:/PBL PROJECT FIRST YEAR/crops.csv"
Production="D:/PBL PROJECT FIRST YEAR/production_crop.csv"
Primary="D:/PBL PROJECT FIRST YEAR/primary_crop.csv"
Avg_growth="D:/PBL PROJECT FIRST YEAR/average cost.csv"
Returns="D:/PBL PROJECT FIRST YEAR/returns.csv"

# LOGIN FUNCTION

def login():
    login_d={'Amit':'Amit123','Rahul':'Rahul256','Seema':'Seema897'}
    print("                     *************************************************** ")
    print("                     *                                                                       * ")
    print("                     *     FARMERS CROP DATA ANALYSIS      *")
    print("                     *                                                                       * ")
    print("                     *************************************************** ")
    print()  
    while True:
        print("""
=====================================

        1. LOGIN
        2. CREATE ACCOUNT
        3. EXIT
        
=====================================""")
        print()

        choice=int(input("Enter your choice:"))
        if choice==1:
            id=input("Enter your username:")
            if id in login_d:
                pwd=input("Enter your password:")
                if pwd==login_d[id]:
                    print()
                    print("                              ************************************")
                    print("                              *                                                  *")
                    print("                              *     LOGIN SUCCESFULLY     *")
                    print("                              *                                                  *")
                    print("                              ************************************")
                    print()
                    mainmenu()
                    
                
                else:
                    print()
                    print("**********INVALID PASSWORD**********")
                    sys.exit()
            else:
                print()
                print("""********INVALID USER NAME**********""")
                sys.exit()
                
        elif choice==2:
            newuser=input("Enter your preferred username:")
            newpwd=input("Enter your preferred password:")
            login_d[newuser]=newpwd
            print()
            print("                    ***************************************************** ")
            print("                    *                                                                          *  ")
            print("                    *     ACCOUNT CREATED SUCCESFULLY    *  ")
            print("                    *                                                                          *  ")
            print("                    ***************************************************** ")
            print()
            continue
        else:   
            sys.exit()
# MAINMENU FUCTION

def mainmenu():
    ans=True
    while ans:
        print("         1. DATA VISUALIZATION")
        print("         2. DATA ANALYSIS") 
        print("         3. READ CSV FILE AND DISPAY DATAFRAME")
        print("         4. EXIT")
        print()
        inp=int(input("Enter Your Choice:"))
        print()
        if inp==1:
            submenu1()
        elif inp==2:
            submenu2() 
        elif inp==3:
            submenu3()
        else:
            sys.exit()
# FUNCTION FOR PLOTTING GRAPH

def submenu1():
    ans=True
    while ans:
        print("        1. TOP 10 CROPS GROWN IN INDIA")
        print("        2. CROPS ANALYSIS")
        print("        3. PRIMARY CROPS OF INDIA")
        print("        4. AVERAGE GROWTH OF KHARIF CROPS")
        print("        5. PERCENTAGE OF CROPS")
        print("        6. BACK TO MAIN MENU")
        print()
        ans=int(input("Enter Your Choice:"))
        print()
        if ans==1:
             print()
             top()             
        if ans==2:
            crop_analysis()
        if ans==3:
            primary_crop()
        if ans==4:
            avg_growth()
        if ans==5:
            percent_crop()
        if ans==6:
             mainmenu()

# DISPLAYING TOP 10 CROPS GROWN IN INDIA

def top():
    df1=pd.read_csv(Top_10_crop)
    x=np.arange(len(df1))
    Crop=df1['Crops']
    year1=df1['2016-17']
    year2=df1['2017-18']
    year3=df1['2018-19']
    year4=df1['2019-20']
    plt.bar(x+0.15,year1,width=.15,label='2016-2017',color='gold')
    plt.bar(x+0.30,year2,width=.15,label='2017-2018',color='red')
    plt.bar(x+0.45,year3,width=.15,label='2018-2019',color='green')
    plt.bar(x+0.60,year4,width=.15,label='2019-2020',color='blue')
    plt.xticks(x,Crop,rotation=45)
    plt.title('TOP 10 CROPS GROWN IN INDIA',color='blue',fontsize=20)
    plt.xlabel('CROPS',fontsize=20,color='red')
    plt.ylabel('QUANTITY',fontsize=20,color='red')
    plt.grid()
    plt.legend()
    plt.show()


# PLOTTING LINE CHARTS

def crop_analysis():
    df=True
    while df:  
       print("         1. PRODUCTION VS YEAR OF RICE") 
       print("         2. PRODUCTION VS YEAR OF CEREALS")      
       print("         3. PRODUCTION VS YEAR OF JOWAR")
       print("         4. PRODUCTION VS YEAR OF GROUNDNUTS")
       print("         5. PRODUCTION VS YEAR OF COTTON")
       print("         6. PRODUCTION VS YEAR OF OILSEEDS")
       print("         7. PRODUCTION VS YEAR OF TEA")
       print("         8. PRODUCTION VS YEAR OF COFFEE")
       print("         9. BACK TO MAIN MENU")
       print()
       inp=int(input("Enter Your Choice:"))
       print()
       if inp==1:
           print()
           Rice()
       elif inp==2:
           Cereals() 
       elif inp==3:
           Jowar()
       elif inp==4:
           Groundnuts()
       elif inp==5:
           Cotton()
       elif inp==6:
           Oilseeds()
       elif inp==7:
           Tea()
       elif inp==8:
           Coffee()
       elif inp==9:
           print()
           submenu1()
       else:
           sys.exit
           

def Rice():    
    df=pd.read_csv(Production)
    df=df.tail(5)
    year= df.Year
    rice = df.Rice
    plt.plot(year,rice,marker="*",markersize='8',markeredgecolor='g',color='r',linewidth='1')
    plt.xlabel("YEARS",fontsize=16,color='black')
    plt.ylabel("PRODUCTION",fontsize=16,color='black')
    plt.title("PRODUCTION VS YEAR OF RICE",color='blue',fontsize=18)
    plt.xticks(year)
    plt.show()
    
def Cereals():
    df=pd.read_csv(Production)
    df=df.tail(5)
    year= df.Year
    cereals = df.Cereals
    plt.plot(year,cereals,marker='*',markeredgecolor='r',markersize='8',color='g',linewidth='1')
    plt.xlabel("YEARS",fontsize=16,color='black')
    plt.ylabel("PRODUCTION",fontsize=16,color='black')
    plt.title("PRODUCTION VS YEAR OF CEREALS",color='blue',fontsize=18)
    plt.xticks(year)
    plt.show()
    
def Jowar():
    df=pd.read_csv(Production)
    df=df.tail(5)
    year= df.Year
    jowar = df.Jowar
    plt.plot(year,jowar,marker='+',markeredgecolor='r',markersize='10',color='c',linewidth='1')
    plt.xlabel("YEARS",fontsize=16,color='k')
    plt.ylabel("PRODUCTION",fontsize=16,color='k')
    plt.title("PRODUCTION VS YEAR OF JOWAR",color='blue',fontsize=18)
    plt.xticks(year)
    plt.show()
    
def Groundnuts():
    df=pd.read_csv(Production)
    df=df.tail(5)
    year= df.Year
    groundnuts = df.Groundnuts
    plt.plot(year,groundnuts,marker='d',markeredgecolor='olive',markersize='10',color='firebrick',linewidth='1')
    plt.xlabel("YEARS",fontsize=16,color='k')
    plt.ylabel("PRODUCTION",fontsize=16,color='k')
    plt.title("PRODUCTION VS YEAR OF GROUNDNUTS",color='blue',fontsize=18)
    plt.xticks(year)
    plt.show()
    
def Cotton():
    df=pd.read_csv(Production)
    df=df.tail(5)
    year= df.Year
    cotton = df.Cotton
    plt.plot(year,cotton,marker='*',markeredgecolor='tomato',markersize='10',color='teal',linewidth='1')
    plt.xlabel("YEARS",fontsize=16,color='k')
    plt.ylabel("PRODUCTION",fontsize=16,color='k')
    plt.title("PRODUCTION VS YEAR OF COTTON",color='blue',fontsize=18)
    plt.xticks(year)
    plt.show()
    
def Oilseeds():
    df=pd.read_csv(Production)
    df=df.tail(5)
    year= df.Year
    oilseeds = df.Oilseeds
    plt.plot(year,oilseeds,marker='*',markeredgecolor='darkorange',markersize='10',color='grey',linewidth='1')
    plt.xlabel("YEARS",fontsize=16,color='k')
    plt.ylabel("PRODUCTION",fontsize=16,color='k')
    plt.title("PRODUCTION VS YEAR OF OILSEEDS",color='blue',fontsize=18)
    plt.xticks(year)
    plt.show()
    
def Tea():
    df=pd.read_csv(Production)
    df=df.tail(5)
    year= df.Year
    tea = df.Tea
    plt.plot(year,tea,marker='.',markeredgecolor='black',markersize='12',color='crimson',linewidth='2')
    plt.xlabel("YEARS",fontsize=16,color='k')
    plt.ylabel("PRODUCTION",fontsize=16,color='k')
    plt.title("PRODUCTION VS YEAR OF TEA",color='blue',fontsize=18)
    plt.xticks(year)
    plt.show()
        
def Coffee():
    df=pd.read_csv(Production)
    df=df.tail(5)
    year= df.Year
    coffee = df.Coffee
    plt.plot(year,coffee,marker='>',markeredgecolor='green',markersize='10',color='red',linewidth='2')
    plt.xlabel("YEARS",fontsize=16,color='k')
    plt.ylabel("PRODUCTION",fontsize=16,color='k')
    plt.title("PRODUCTION VS YEAR OF COFFEE",color='blue',fontsize=18)
    plt.xticks(year)
    plt.show()


# DISPLAYING PRIMARY CROPS OF INDIA

def primary_crop():
    df= pd.read_csv("D:\PBL PROJECT FIRST YEAR\IP PROJECT\primary_crop.csv")
    df.plot(kind='barh',x='Crop',title='PRIMARY CROPS OF INDIA')
    plt.xlabel('Rate')
    plt.show()


# DISPLAYING AVERAGE GROWTH OF KHARIF CROPS

def avg_growth():
    df=pd.read_csv(Avg_growth)
    df.plot(kind='line',x='Kharif Crops',title='AVERAGE GROWTH OF KHARIF CROPS')
    plt.ylabel("Rate")
    plt.show()


# DISPLAYING PERCENTAGE OF CROPS

def percent_crop():
    df=pd.DataFrame({'2018-19':[49,63,41,70,87,364,173,101,111,145,99]}
    ,index=['Paddy','Jowar','Bajra','Ragi','Maize','Moong','Urad','Groundnut','Sunflower','Soyabean','Sesamum'])
    df.plot(kind='pie',y='2018-19',title='PERCENTAGE OF CROPS',legend=False)
    plt.show()

             
# FUNCTION FOR ANALYSING DATA

def submenu2():
    print("           1. TO PRINT THE MAXIMUM VALUES OF THE DATARAME")
    print("           2. TO PRINT THE MINIMUM VALUES OF THE DATAFRAME")
    print("           3. TO COUNT THE NUMBER OF RECORDS IN THE DTAFRAME")
    print("           4. TO DISPLAY THE MEAN OF RETURN OVER COST")
    print("           5. TO SUM THE COST OF PRODUCTION")
    print("           6. BACK TO MAIN MENU")
    print()
    choice=int(input("Enter Your Choice"))
    print()
    if choice==1:
          max_value()
          print()
          submenu2()
    if choice==2:
          min_value()
          print()
          submenu2()
    if choice==3:
          count_record()
          print()
          submenu2()
    if choice==4:
          mean_return()
          print()
          submenu2()
    if choice==5:
        sum_cost()
        print()
        submenu2()
    if choice==6:
         mainmenu()


# TO PRINT THE MAXIMUM VALUES OF THE DATARAME

def max_value():
    df= pd.read_csv(Returns)
    print(df.max())

# TO PRINT THE MINIMUM VALUES OF THE DATAFRAME

def min_value():
    df= pd.read_csv(Returns)
    print(df.min())

# TO COUNT THE NUMBER OF RECORDS IN THE DTAFRAME

def count_record():
    df= pd.read_csv(Returns)
    print(df.count())
    

# TO DISPLAY THE MEAN OF RETURN OVER COST

def mean_return():
    df= pd.read_csv(Returns)
    return1=df['Return over cost ( in percent)']
    print(return1.mean())
    
# TO SUM THE COST OF PRODUCTION

def sum_cost():
    df= pd.read_csv(Returns)
    print(df.sum())

    
# READING CSV FILE AND DISPLAYING DATA FRAME

def submenu3():
    print("             1. Top_10_crop ")
    print("             2. Production")
    print("             3. Primary")
    print("             4. Avg_growth")
    print("             5. Returns")
    print("             6. BACK TO MAIN MENU")
    print()
    choice=int(input("Enter your choice:"))
    print()
    if choice==1:
        top_10_crop()
        print()
        submenu3()
    elif choice==2:
        production()
        print()
        submenu3()
    elif choice==3:
        primary()
        print()
        submenu3()
    elif choice==4:
        avg()
        print()
        submenu3()
    elif choice==5:
        returns()
        print()
        submenu3()
    elif choice==6:
        mainmenu()
    else:
        sys.exit()
        
    
# CSV FILES FUNCTIONS

def top_10_crop():
    df1=pd.read_csv(Top_10_crop)
    print(df1)
    
def production():
    df=pd.read_csv(Production)
    print(df)
    
def primary():
    df=pd.read_csv(Primary)
    print(df)

def avg():
    df=pd.read_csv(Avg_growth)
    print(df)

    
def returns():
    df=pd.read_csv(Returns)
    print(df)




    
    
