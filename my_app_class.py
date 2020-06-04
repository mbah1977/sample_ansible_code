#!/bin/env python3
class my_app():
    """"""
    def __init__(self,central_ac,client_ac,kiosk,MTN_ac,agence_ac,app_ac,price,service_fee):
        self.central_ac = central_ac
        self.client_ac = client_ac
        self.kiosk = kiosk
        self.MTN_ac = MTN_ac
        self.agence_ac = agence_ac
        self.app_ac = app_ac
        self.price = price # To be retrieved from database for agency selected by passenger
        self.service_fee = service_fee
    def cash_collection(self):
        """"""   
        active=True
        while active:
            method=input("What is the payment method? Cash or debit or enter 'q' to quit? :    ")
            if method == 'debit':
                self.client_ac -= (self.price + self.service_fee)
                self.central_ac += (self.price + self.service_fee)
                self.agence_ac += self.price 
                self.app_ac += (0.75 * self.service_fee)
                self.MTN_ac += (0.25 * self.service_fee)
            if method == 'cash':
                self.kiosk -= (self.price + self.service_fee)
                self.central_ac += (self.price + self.service_fee)
                self.agence_ac += self.price 
                self.app_ac += (0.75 * self.service_fee)
                self.MTN_ac += (0.25 * self.service_fee)
            if method == 'q':
                active = False
        print("central_ac :", self.central_ac)
        print("client     :", self.client_ac)
        print("kiosk      :", self.kiosk) 
        print("agency     :", self.agence_ac)
        print("app_ac     :", round(self.app_ac))
        print("MTN_ac     :", self.MTN_ac)
        
    def passenger_cancellations(self, cancellation_fee):
        """"""
        self.cancellation_fee=cancellation_fee
        
        active=True
        while active:
            method=input("What is the refund method? Cash or debit or enter 'q' to quit? :    ")
            if method == 'debit':
                self.central_ac -= (self.price + self.service_fee)
                self.client_ac += (self.price - self.cancellation_fee )
                self.agence_ac -= (self.price - (0.5 * self.cancellation_fee))
                self.app_ac += (0.5 * self.cancellation_fee)
            if method == 'cash':
                self.central_ac -= (self.price + self.service_fee)
                self.client_ac += (self.price - self.cancellation_fee)
                self.agence_ac -= (self.price - (0.5 * self.cancellation_fee))
                self.app_ac += (0.5 * self.cancellation_fee)   
            if method == 'q':
                active = False
                
        print("central_ac :", self.central_ac)
        print("client     :", self.client_ac)
        print("kiosk      :", self.kiosk) 
        print("agency     :", self.agence_ac)
        print("app_ac     :", self.app_ac)
        
    def agency_cancellations(self):
        """"""       
        active=True
        while active:
            method=input("What is the refund method? Cash or debit or enter 'q' to quit? :    ")
            if method == 'debit':
                self.central_ac -= self.price 
                self.client_ac += self.price 
                self.agence_ac -= (self.price + self.service_fee) 
                self.app_ac += self.service_fee 
                                            
            if method == 'cash':
                self.central_ac -= self.price
                self.agence_ac -= (self.price + self.service_fee)
                self.kiosk += self.price + (0.25 * self.service_fee) # 100frs penalty charged to agency.
                self.app_ac += (0.75 * self.service_fee)
            if method == 'q':
                active = False

        print("central_ac :", self.central_ac)
        print("client     :", self.client_ac)
        print("kiosk      :", self.kiosk) 
        print("agency     :", self.agence_ac)
        print("app_ac     :", self.app_ac)        
      
print("What service do you want?: select from the list below")
print("Payment, Passenger_cancellation, or agency_cancellation?")   
response=input(":")  
if response == 'payment':
     call=my_app(0,15600,15600,0,0,0,5000,200)
     call.cash_collection()
elif response == 'passenger_cancel':
    call=my_app(15600,0,0,150,15000,450,5000,200)
    call.passenger_cancellations(500)
elif response == 'agency_cancel':
    call=my_app(15600,0,0,150,15900,450,5200,100)
    call.agency_cancellations()

