# Write code below 💖
User=input('Entre dein name ')
print('Ello ' + User + ' Welcome back from dein trip!')
print('It seems you have some shinys left over from your trip, ' + User + '. \nLet"s calculate your left over currency' )

COP=float(input("What do you have left over from your trip to Colombia? enter Pesos: "))
PES=float(input('What do you have left over from your trip to Peru? enter soles: '))
BRR=float(input('What do you have left over from your trip to  Brazil? enter reais: '))

Cpesos_2_usd= (1/4156.91) # COP to usd, 1 usd = 4156.91 cop
Psoles_2_usd =(1/3.62)  # PEN to USD, 1 usd = 3.62 peru soles
Breals_2_usd =(1/5.67)  # BRL to USD, 1 usd = 5.67 Brazil reais
#inverse

usd_frm_cop = COP * Cpesos_2_usd   # 
usd_frm_pen = PES * Psoles_2_usd   #
usd_frm_brl = BRR * Breals_2_usd   # 

print('Your left over cash from your trip to colombia es ' + str(usd_frm_cop)  + ' usd')
print('Your left over cash from your trip to peru es '  + str(usd_frm_pen) +  ' usd')
print('Your left over cash from your trip to brazil es '  + str(usd_frm_brl) + ' usd')


total_usd = usd_frm_cop + usd_frm_pen + usd_frm_brl
print('Und you total amount in dollars left over from all three is ' + str(total_usd))