aci1=float(input("1.açı: "))
aci2=float(input("2.açı: "))
aci3=180-(aci1+aci2)
ucgenTurleri=['ikizkenar üçgen','dik üçgen','eşkenar üçgen','çeşitkenar üçgen']

if (aci1==aci2) and (aci1==aci3):
    print(f'Üçgen türü: {ucgenTurleri[2]}')
elif (aci1==aci2) or (aci1==aci3) or (aci2==aci3):
    print(f'Üçgen türü: {ucgenTurleri[0]}')
elif (aci1==90) or (aci2==90) or (aci3==90):
    print(f'Üçgen türü: {ucgenTurleri[1]}')
else:
    print(f'Üçgen türü: {ucgenTurleri[3]}')