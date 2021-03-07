tik_pur =[]
price=int()
inco=[]
class MovieTicket:
   
    
    def __init__(self,rows,seats,seats_disp):
        self.rows= rows
        self.seats= seats
        self.seats_disp= seats_disp
        self.all_user_info = {}                    # this dict is to store all the user info
        
    
    
    def show_seats(self): 
        for i in range(self.rows+1):
            for j in range(self.seats+1):
                if i==0 and j==0:
                    print(' ',end=' ')
                elif i==0:
                    print(j,end=' ')
                elif j==0:
                    print(i, end=' ')
                else:
                    print(self.seats_disp[i][j],end=' ')
            print()
        self.intro()
        
    def intro(self):
        print('Please Select from the Following options ')
        print('1. Show the Seats')
        print('2. Buy a ticket')
        print('3. Statistics')
        print('4. Show booked tickets user info ')
        print('0. Exit')
        option = int(input())
        
        if option == 1:
            self.show_seats()
        elif option == 2:
            self.buy_ticket()
        elif option == 3:
            self.stats()
        elif option == 4:
            self.show_info()
        elif option == 0:
            exit()
        else:
            print("Please try again!!!!!")
       
    

    def buy_ticket(self):
        self.row_no=int(input('Enter the row number: '))
        self.seat_no=int(input('Enter the seat number in that particular row: '))
        
        self.total_seats = self.rows * self.seats
        print('Total seats are: ', self.total_seats)
        global price
        
        if (self.total_seats) < 60:
            price= 10
            inco.append(price)
            self.total_inc = self.total_seats * price         #here for all the seats price will be same
            print("Your price will be $", price)
        if (self.total_seats) > 60:
            self.first_half= self.rows // 2
            self.other_half= self.rows - self.first_half
            if self.rows % 2==0:
                self.total_inc = (self.first_half*10) + (self.other_half*8)    #total income if rows are even
                                                #'if rows are even'
                if self.row_no < self.first_half:
                                                #'if the row is in 1st half'
                    price= 10 
                    inco.append(price)
                    
                    print('Price for the tickets is $',price)
                elif self.row_no > self.first_half and self.row_no < self.rows:
                                                #'if the row is in other half'
                    price = 8
                    inco.append(price)
                    print('Price of your ticket is $', price)
            elif self.row_no %2!=0:                                           #'if rows are odd'
                self.total_inc = (self.first_half*10) + (self.other_half*8)      #total income if seats are odd
                if self.row_no<=self.first_half:
                                                 #'if the row is in 1st half'
                    price = 10
                    inco.append(price)
                    print('Price for the ticket is $', price)
                elif self.row_no > self.first_half and self.row_no <self.rows:
                                             #'if the row is in other half'
                    price = 8 
                    inco.append(price)
                    print('Price of your ticket is $', price)
        
        print('DO U WANT TO BOOK THE TICKET')
        print('1. YES')
        print('2. No')
        ask=int(input())
             
        if ask == 1:
            tik_pur.append(self.seat_no)           #appending the seat number in a list
            
            
            self.user_details(self.row_no,self.seat_no)
        elif ask == 2:
            print("You can choose from the main menu ")
            self.intro()
#         self.intro()
    
    def user_details(self,row_no,seat_no):
        print('To book kindly enter your details ')
        self.name=input('Enter Name ')
        self.age=int(input('Enter Age '))
        self.gender=input('Enter your Gender ')
        self.phone=int(input('Enter your phone number '))
        
        
        dict1={}
        global price
        
        dict1["Name"]=self.name
        dict1["Gender"]=self.gender
        dict1["Age"]=self.age
        dict1["Ticket_Price"]=price
        dict1["Phone_No"]=self.phone
        self.all_user_info[(self.row_no,self.seat_no)] = dict1         #storing the dict1 as a key to the user info
        
        
        
        print('Cinema: ')
       
        if self.seats_disp[self.row_no][self.seat_no]=='S':
            self.seats_disp[self.row_no][self.seat_no]='B'
            for i in range(self.rows+1):
                for j in range(self.seats+1):
                    if i==0 and j==0:
                        print(' ',end=' ')
                    elif i==0:
                        print(j,end=' ')
                    elif j==0:
                        print(i, end=' ')
                    else:
                        print(self.seats_disp[i][j],end=' ')
                print()
        print('Your ticket booked succesfully') 

        self.intro()
    
    def stats(self):
        
        print('Number of tickets purchased: ',len(tik_pur))
        percent =(len(tik_pur) / self.total_seats)* 100
        print('Percentage: ', percent , '%')
        print('Current Income :$',sum(inco))
        
        print('Total Income:$',self.total_inc)
        self.intro()

    
    def show_info(self):
        row_num2 = int(input('Enter the row number you booked: '))
        seat_num2 = int(input('Enter the seat number you booked: '))
        if seats_disp[row_num2][seat_num2]=="B":
            for i in self.all_user_info[(row_num2,seat_num2)]:
                print(i , ': ' , self.all_user_info[(row_num2,seat_num2)][i])
        else:
            print('Seat is not booked')
        self.intro()   
if __name__ == "__main__":
    rows = int(input('Enter the number of rows: '))
    seats = int(input('Enter the number of seats in each row: '))
    print('Cinema: ')
    seats_disp=[['S' for j in range(seats + 1)]for i in range(rows + 1)]
    rohit=MovieTicket(rows,seats,seats_disp)
    rohit.intro()


    

