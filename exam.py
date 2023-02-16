class star_cinema:
    hall_list = []
    def __init__(self):
        pass

    def entry_hall(self):
        pass


class Hall(star_cinema):
    def __init__(self,hall_no, rows=5, Cols=3):
        self.seats = {}
        self.show_list = {}
        self.rows = rows
        self.cols = Cols
        self.hall_no = hall_no
        super().hall_list.append(self)

    def entry_show(self, id, movie_name, time):
        self.show_list[id]= movie_name ,time
        l =[]

        for i in range(self.rows):
            index = 65
            index_char= chr(index)
            l2=[]
            index1 = 0
            for j in range(self.cols):
                char = ''
                char = index1 
                l2.append(char)
                index1+=1
            l.append(l2)
            # index+=1
        self.seats[id]= l
            
    

    def book_seats(self,name,phone,id, t1,t2):
        self.seats[id][t1][t2] = 'boking'
                         
                            

    def view_show_list(self):
        print(str(f'Movie name: {self.show_list[22][0]}              Show Id: {22}                      Time: {self.show_list[22][1]} '))
        print(str(f'Movie name: {self.show_list[23][0]}          Show Id: {23}                      Time: {self.show_list[23][1]} '))

    def movie_name (self,id):
        return self.show_list[id][0]

    def movie_time (self,id):
        return self.show_list[id][1]

    def view_available_seats(self,id):
        for key in self.seats.keys():
            if key == id:
                for i in self.seats[id]:
                    print(i)
                    for j in i:
                        pass
                    


my_cinema = Hall(42)
my_cinema.entry_show(22,'Thank God', ' feb 15 2023 11:30pm')
my_cinema.entry_show(23,'KGF Chapter 2', 'feb 15 2023 04:30am')

while True:
    print('1: View All Show Today')
    print('2: View Available Seats')
    print('3: Book Ticket')
    val = input('Enter Option: ')
    print('\n')
    if  val == '1':
        print('-----------------------------------------------------------------------------------------\n')
        my_cinema.view_show_list()
        print()
        print('-----------------------------------------------------------------------------------------\n \n')
    
    if val == '2':
        condition = True
        while condition == True:
            show = int (input('Enter Show ID: '))
            if show == 22 or show==23:
                condition = False
            else:
                print('wrong id try again')
        print()
        print('-----------------------------------------\n')
        my_cinema.view_available_seats(show)
        print()
        print('-----------------------------------------\n')
            

    if val == '3':
        # my_cinema.book_seats('anuj','01646267167',22,1,1)
        name = input('Enter Name: ')
        phone = input('Enter Phone Number: ')
        condition2 = True
        while condition2 == True:
            ID = int (input('Enter Movie ID: '))
            if ID == 22 or ID == 23:
                condition2= False
            else:
                print('Wrong ID Try Again')
        en = int(input('Enter Number Of Ticket: '))
        for i in range (en):
            r = int (input('Enter row for seats booking: '))
            c = int (input('Enter Collam for seats booking: '))
            my_cinema.book_seats(name,phone,ID, r,c)
        print()
        print('\t\tTicket Booked Successfully!..')
        print('-----------------------------------------------------------------------------------------\n')
        print(f'Name:{name}')
        print(f'Phone Number:{phone}')
        print()
        result =my_cinema.movie_name(ID)
        result2 = my_cinema.movie_time(ID)
        print(f'Movie name: {result} \t\t   Movie Time: {result2}')
        print(f'your booking {en} ticket ')
        print('Hall No: 450')
        print  ()
        print('-----------------------------------------------------------------------------------------\n')
