from selenium import webdriver

#Using Firefox Browser
Drivers = webdriver.Firefox()
Drivers.get("https://web.whatsapp.com/")
Drivers.maximize_window()
print("NOTE:You Must Scan the QR Before entering Details")
Name = input("Enter name to whom you want to send(Contact/Group): ")
Msg = input("Type Your Message: ")

user = Drivers.find_element_by_xpath("//span[@title='{}']".format(Name))
user.click()
msg_box = Drivers.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
msg_box.send_keys(Msg)
Drivers.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()

print(f'Message sent successfully to Contact/Group "{Name}"')
