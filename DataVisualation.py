import matplotlib.pyplot as plt 

'''
y = [0,1,4,9,16,25,36,49,64,81,100]
x = [0,1,2,3,4,5,6,7,8,9,10]

plt.plot(x,y)
plt.show()

'''

'''
x = ["mon","tue","web","thr","fri"]
y = [1,2,0.5,0.9,5]

plt.plot(x,y)

plt.title("Shares of company")
plt.xlabel("Days")
plt.ylabel("Money in cr")

plt.show()

'''

'''

x = ["mon","tue","web","thr","fri"]
y = [1,2,0.5,0.9,5]

plt.plot(x,y,color = "red",linestyle = "-",linewidth = 1,marker = 'o',markersize = 3,label = "money")

plt.title("Shares of company")
plt.xlabel("Days")
plt.ylabel("Money in cr")
plt.legend()
plt.grid(color = 'blue',linestyle = ":",linewidth = 0.5)
plt.xlim(0,7)
plt.ylim(0,10)

plt.xticks(["mon","tue","web","thr","fri"],["day-1","day-2","day-3","day-4","day-5"])

plt.show()

'''


'''
x = ["mon","tue","wed","thu","fri"]
height = [100,2000,500,900,500]

plt.bar(x,height,color = "black",label = "money")
plt.legend()

plt.xlabel("Days")
plt.ylabel("Money in cr")

plt.title("Shares of company")
plt.grid(color = 'blue',linestyle = ":",linewidth = 0.5)
plt.show()
'''

