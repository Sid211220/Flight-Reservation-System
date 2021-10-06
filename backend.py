from tkinter import *
import sqlite3
from tksheet import *


connection = sqlite3.connect('flight_reservation_system.db')
cursor = connection.cursor()


def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS USER(Email TEXT Primary Key, First_Name TEXT, Last_Name TEXT, Password "
                   "TEXT, DOB TEXT)")

    cursor.execute("CREATE TABLE IF NOT EXISTS USER_PHONENO(Email TEXT, PhoneNo INTEGER, PRIMARY KEY(Email,PhoneNo), "
                   "FOREIGN KEY(Email) references USER(Email) on delete cascade on update cascade)")

    cursor.execute("CREATE TABLE IF NOT EXISTS FLIGHTS(flight_number INTEGER PRIMARY KEY, origin TEXT, destination "
                   "TEXT, Date_depart TEXT, Date_arrival TEXT, Time_depart TEXT, Time_arrival TEXT, "
                   "seats_booked INTEGER, seats_available INTEGER,price REAL)")

    cursor.execute("create table if not exists BOOKINGS(PNR REAL PRIMARY KEY, SP TEXT, totalamt REAL, no_of_passengers "
                   "INTEGER, email TEXT, flight_number INTEGER, FOREIGN KEY (email) REFERENCES USER(email) on DELETE "
                   "CASCADE on UPDATE CASCADE, FOREIGN KEY (flight_number) REFERENCES flights(flight_number) on DELETE "
                   "CASCADE on UPDATE CASCADE)")

    cursor.execute("create table if not exists PASSENGERS(Ticket_no REAL PRIMARY KEY, Name VARCHAR(20), DOB TEXT, AGE "
                   "VARCHAR(20), Gender VARCHAR(10), Nationality VARCHAR(20), PNR REAL, FOREIGN KEY(PNR) references "
                   "Bookings(PNR)on DELETE CASCADE ON UPDATE CASCADE)")


def data_entries_pass():
    cursor.execute("INSERT INTO Passengers VALUES(1001, 'Viraj', '9/2/01', 19, 'Male', 'India', 101)")
    cursor.execute("INSERT INTO Passengers VALUES(1002, 'Divya', '12/5/00', 20, 'Female', 'India', 101)")
    cursor.execute("INSERT INTO Passengers VALUES(1003, 'Sumedha', '4/3/01', 20, 'Female', 'India', 101)")


def data_entries_user():
    cursor.execute("INSERT INTO USER VALUES ('virsanap@gmail.com', 'Viraj', 'Sanap', 'virajsanap', '09/02/2001')")
    connection.commit()


def data_entries_flights():
    cursor.execute("INSERT INTO flights VALUES(101,'Delhi','Mumbai','4/5/21','4/5/21','7:30:15','9:30:00',5,95,4398)")
    cursor.execute(
        "INSERT INTO flights VALUES(102,'Delhi','Mumbai','4/7/21','4/7/21','10:30:15','12:30:00',0,100,5670)")
    cursor.execute("INSERT INTO flights VALUES(103,'Mumbai','Delhi','4/6/21','4/6/21','5:00:00','6:30:10',10,90,2396)")
    cursor.execute("INSERT INTO flights VALUES(104,'Mumbai','Delhi','4/8/21','4/8/21','6:30:15','8:00:00',30,70,3890)")
    cursor.execute("INSERT INTO flights VALUES(105,'Delhi','Pune','4/5/21','4/5/21','11:15:00','13:00:00',2,98,2894)")
    cursor.execute("INSERT INTO flights VALUES(106,'Delhi','Pune','4/7/21','4/5/21','15:30:15','17:15:20',50,50,6739)")
    cursor.execute("INSERT INTO flights VALUES(107,'Pune','Delhi','4/6/21','4/6/21','6:30:15','8:30:00',6,94,5000)")
    cursor.execute("INSERT INTO flights VALUES(108,'Pune','Delhi','4/8/21','4/8/21','19:00:30','21:00:15',70,30,3600)")
    cursor.execute(
        "INSERT INTO flights VALUES(109,'Delhi','Hyderabad','4/5/21','4/5/21','8:10:15','11:30:13',20,80,7200)")
    cursor.execute(
        "INSERT INTO flights VALUES(110,'Delhi','Hyderabad','4/7/21','4/7/21','20:00:00','22:20:25',1,99,2540)")
    cursor.execute(
        "INSERT INTO flights VALUES(111,'Mumbai','Hyderabad','4/6/21','4/6/21','13:00:15','15:50:40',20,80,4370)")
    cursor.execute(
        "INSERT INTO flights VALUES(112,'Hyderabad','Mumbai','4/7/21','4/7/21','18:00:00','20:30:15',40,60,2350)")
    cursor.execute("INSERT INTO flights VALUES(113,'Mumbai','Pune','4/7/21','4/7/21','10:15:00','11:00:00',9,91,2500)")
    cursor.execute("INSERT INTO flights VALUES(114,'Pune','Mumbai','4/8/21','4/8/21','9:30:15','9:45:20',16,84,1900)")
    cursor.execute(
        "INSERT INTO flights VALUES(115,'Mumbai','Hyderabad','4/6/21','4/6/21','21:00:15','23:30:00',6,94,4000)")
    cursor.execute(
        "INSERT INTO flights VALUES(116,'Hyderabad','Mumbai','4/8/21','4/8/21','12:15:00','2:45:15',45,55,4250)")
    cursor.execute(
        "INSERT INTO flights VALUES(117,'Pune','Hyderabad','4/5/21','4/5/21','8:10:15','11:30:13',0,100,3530)")
    cursor.execute(
        "INSERT INTO flights VALUES(118,'Hyderabad','Pune','4/7/21','4/7/21','20:00:00','22:20:25',3,97,3240)")
    cursor.execute("INSERT INTO flights VALUES(119,'Delhi','Mumbai','4/5/21','4/5/21','9:30:15','11:30:00',4,96,5490)")
    cursor.execute("INSERT INTO flights VALUES(120,'Delhi','Mumbai','4/5/21','4/5/21','10:30:15','12:30:00',1,99,5543)")
    cursor.execute("INSERT INTO flights VALUES(121,'Delhi','Mumbai','4/5/21','4/5/21','22:00:15','24:00:00',7,93,6512)")
    cursor.execute(
        "INSERT INTO flights VALUES(122,'Delhi','Mumbai','4/6/21','4/6/21','11:30:15','13:30:00',0,100,3400)")
    cursor.execute("INSERT INTO flights VALUES(123,'Delhi','Mumbai','4/6/21','4/6/21','17:00:15','19:00:30',9,91,3200)")
    cursor.execute(
        "INSERT INTO flights VALUES(124,'Delhi','Mumbai','4/6/21','4/6/21','22:00:15','24:00:00',10,90,4590)")
    cursor.execute(
        "INSERT INTO flights VALUES(125,'Delhi','Mumbai','4/7/21','4/7/21','13:30:15','15:30:00',12,88,5500)")
    cursor.execute("INSERT INTO flights VALUES(126,'Delhi','Mumbai','4/7/21','4/7/21','16:00:00','18:00:30',8,92,2500)")
    cursor.execute(
        "INSERT INTO flights VALUES(127,'Delhi','Mumbai','4/7/21','4/7/21','20:00:15','22:00:00',25,75,2560)")
    cursor.execute(
        "INSERT INTO flights VALUES(128,'Delhi','Mumbai','4/8/21','4/8/21','13:00:15','15:00:00',11,89,5490)")
    cursor.execute("INSERT INTO flights VALUES(129,'Delhi','Mumbai','4/8/21','4/8/21','18:00:00','20:00:30',5,95,5570)")
    cursor.execute("INSERT INTO flights VALUES(130,'Delhi','Mumbai','4/8/21','4/8/21','20:30:15','22:30:00',2,98,3270)")
    cursor.execute("INSERT INTO flights VALUES(131,'Mumbai','Delhi','4/6/21','4/6/21','5:00:00','6:30:10',55,45,5409)")
    cursor.execute(
        "INSERT INTO flights VALUES(132,'Mumbai','Delhi','4/6/21','4/6/21','22:00:15','24:00:00',28,72,4432)")
    cursor.execute("INSERT INTO flights VALUES(133,'Mumbai','Delhi','4/6/21','4/6/21','4:00:00','6:00:10',69,31,7843)")
    cursor.execute(
        "INSERT INTO flights VALUES(134,'Mumbai','Delhi','4/5/21','4/5/21','13:30:15','15:00:00',43,57,4390)")
    cursor.execute("INSERT INTO flights VALUES(135,'Mumbai','Delhi','4/5/21','4/5/21','5:00:00','6:30:10',10,90,3209)")
    cursor.execute(
        "INSERT INTO flights VALUES(136,'Mumbai','Delhi','4/5/21','4/5/21','13:30:15','15:30:00',30,70,2390)")
    cursor.execute("INSERT INTO flights VALUES(137,'Mumbai','Delhi','4/7/21','4/7/21','5:00:00','6:30:10',11,89,3480)")
    cursor.execute(
        "INSERT INTO flights VALUES(138,'Mumbai','Delhi','4/7/21','4/7/21','14:30:15','16:00:00',35,65,2370)")
    cursor.execute("INSERT INTO flights VALUES(139,'Mumbai','Delhi','4/5/21','4/7/21','2:00:00','5:30:10',2,98,3790)")
    cursor.execute("INSERT INTO flights VALUES(140,'Mumbai','Delhi','4/8/21','4/8/21','4:30:15','6:30:30',30,70,4580)")
    cursor.execute("INSERT INTO flights VALUES(141,'Mumbai','Delhi','4/8/21','4/8/21','10:00:00','12:00:10',8,92,6700)")
    cursor.execute(
        "INSERT INTO flights VALUES(142,'Mumbai','Delhi','4/8/21','4/8/21','18:00:15','20:00:40',20,80,2580)")
    cursor.execute("INSERT INTO flights VALUES(143,'Delhi','Pune','4/5/21','4/5/21','13:15:00','15:00:00',2,98,3490)")
    cursor.execute("INSERT INTO flights VALUES(144,'Delhi','Pune','4/5/21','4/5/21','10:30:15','12:15:20',50,50,3260)")
    cursor.execute("INSERT INTO flights VALUES(145,'Delhi','Pune','4/6/21','4/6/21','15:15:00','17:00:00',2,98,5044)")
    cursor.execute("INSERT INTO flights VALUES(146,'Delhi','Pune','4/6/21','4/6/21','5:30:15','7:15:20',50,50,3260)")
    cursor.execute("INSERT INTO flights VALUES(147,'Delhi','Pune','4/7/21','4/7/21','11:15:00','13:00:00',2,98,5077)")
    cursor.execute("INSERT INTO flights VALUES(148,'Delhi','Pune','4/7/21','4/7/21','20:30:15','22:15:20',50,50,6807)")
    cursor.execute("INSERT INTO flights VALUES(149,'Delhi','Pune','4/8/21','4/8/21','4:15:00','6:00:00',2,98,4680)")
    cursor.execute("INSERT INTO flights VALUES(150,'Delhi','Pune','4/8/21','4/8/21','12:30:15','14:15:20',50,50,5770)")
    cursor.execute("INSERT INTO flights VALUES(151,'Pune','Delhi','4/5/21','4/5/21','6:30:15','8:30:00',2,98,2680)")
    cursor.execute("INSERT INTO flights VALUES(152,'Pune','Delhi','4/5/21','4/5/21','19:00:30','21:00:15',60,40,4580)")
    cursor.execute("INSERT INTO flights VALUES(153,'Pune','Delhi','4/5/21','4/5/21','6:30:15','8:30:00',6,94,4560)")
    cursor.execute("INSERT INTO flights VALUES(154,'Pune','Delhi','4/6/21','4/6/21','19:00:30','21:00:15',75,25,1980)")
    cursor.execute("INSERT INTO flights VALUES(155,'Pune','Delhi','4/6/21','4/6/21','6:30:15','8:30:00',6,94,3000)")
    cursor.execute("INSERT INTO flights VALUES(156,'Pune','Delhi','4/8/21','4/8/21','19:00:30','21:00:15',2,98,5670)")
    cursor.execute("INSERT INTO flights VALUES(157,'Pune','Delhi','4/6/21','4/6/21','6:30:15','8:30:00',6,94,6700)")
    cursor.execute("INSERT INTO flights VALUES(158,'Pune','Delhi','4/7/21','4/7/21','19:00:30','21:00:15',10,20,4570)")
    cursor.execute("INSERT INTO flights VALUES(159,'Pune','Delhi','4/7/21','4/7/21','6:30:15','8:30:00',40,60,2469)")
    cursor.execute("INSERT INTO flights VALUES(160,'Pune','Delhi','4/7/21','4/7/21','19:00:30','21:00:15',70,30,3579)")
    cursor.execute(
        "INSERT INTO flights VALUES(161,'Delhi','Hyderabad','4/5/21','4/5/21','8:10:15','11:30:13',44,56,5790)")
    cursor.execute(
        "INSERT INTO flights VALUES(162,'Delhi','Hyderabad','4/7/21','4/7/21','20:00:00','22:20:25',60,40,2409)")
    cursor.execute(
        "INSERT INTO flights VALUES(163,'Delhi','Hyderabad','4/6/21','4/6/21','8:10:15','11:30:13',20,80,4769)")
    cursor.execute(
        "INSERT INTO flights VALUES(164,'Delhi','Hyderabad','4/6/21','4/6/21','20:00:00','22:20:25',2,98,6590)")
    cursor.execute(
        "INSERT INTO flights VALUES(165,'Delhi','Hyderabad','4/8/21','4/8/21','8:10:15','11:30:13',18,82,4580)")
    cursor.execute(
        "INSERT INTO flights VALUES(166,'Delhi','Hyderabad','4/8/21','4/8/21','20:00:00','22:20:25',1,99,6754)")
    cursor.execute(
        "INSERT INTO flights VALUES(167,'Hyderabad','Delhi','4/5/21','4/5/21','8:10:15','11:30:13',20,80,3380)")
    cursor.execute(
        "INSERT INTO flights VALUES(168,'Hyderabad','Delhi','4/5/21','4/5/21','20:00:00','22:20:25',1,99,2280)")
    cursor.execute(
        "INSERT INTO flights VALUES(169,'Hyderabad','Delhi','4/6/21','4/6/21','8:10:15','11:30:13',22,78,6590)")
    cursor.execute(
        "INSERT INTO flights VALUES(170,'Hyderabad','Delhi','4/7/21','4/7/21','20:00:00','22:20:25',2,98,2890)")
    cursor.execute(
        "INSERT INTO flights VALUES(171,'Hyderabad','Delhi','4/7/21','4/7/21','8:10:15','11:30:13',10,90,1870)")
    cursor.execute(
        "INSERT INTO flights VALUES(172,'Hyderabad','Delhi','4/8/21','4/8/21','20:00:00','22:20:25',21,79,5432)")
    cursor.execute("INSERT INTO flights VALUES(173,'Mumbai','Pune','4/5/21','4/5/21','12:15:00','14:00:00',40,60,2500)")
    cursor.execute("INSERT INTO flights VALUES(174,'Mumbai','Pune','4/5/21','4/5/21','21:15:00','23:00:12',23,77,2652)")
    cursor.execute("INSERT INTO flights VALUES(175,'Mumbai','Pune','4/7/21','4/7/21','8:00:00','10:10:00',30,70,3456)")
    cursor.execute("INSERT INTO flights VALUES(176,'Mumbai','Pune','4/6/21','4/6/21','12:10:00','14:10:10',2,98,2673)")
    cursor.execute("INSERT INTO flights VALUES(177,'Mumbai','Pune','4/6/21','4/6/21','14:15:00','16:00:00',5,95,1599)")
    cursor.execute("INSERT INTO flights VALUES(178,'Mumbai','Pune','4/8/21','4/8/21','18:15:00','20:05:10',80,20,8723)")
    cursor.execute("INSERT INTO flights VALUES(179,'Mumbai','Pune','4/8/21','4/8/21','4:15:00','6:00:30',12,88,4976)")
    cursor.execute("INSERT INTO flights VALUES(180,'Pune','Mumbai','4/8/21','4/8/21','13:30:15','15:45:20',50,50,2523)")
    cursor.execute(
        "INSERT INTO flights VALUES(181,'Mumbai','Hyderabad','4/6/21','4/6/21','6:00:00','8:00:30',10,90,2490)")
    cursor.execute(
        "INSERT INTO flights VALUES(182,'Hyderabad','Mumbai','4/8/21','4/8/21','4:00:10','6:45:15',30,70,3250)")
    cursor.execute(
        "INSERT INTO flights VALUES(183,'Pune','Hyderabad','4/5/21','4/5/21','10:00:15','12:20:13',47,53,4700)")
    cursor.execute(
        "INSERT INTO flights VALUES(184,'Hyderabad','Pune','4/7/21','4/7/21','6:30:00','9:20:10',10,90,2876)")
    cursor.execute("INSERT INTO flights VALUES(185,'Pune','Mumbai','4/5/21','4/5/21','12:30:15','14:45:00',17,83,5600)")
    cursor.execute(
        "INSERT INTO flights VALUES(186,'Mumbai','Hyderabad','4/5/21','4/5/21','4:00:15','6:00:00',10,90,3000)")
    cursor.execute(
        "INSERT INTO flights VALUES(187,'Hyderabad','Mumbai','4/5/21','4/5/21','12:15:00','2:45:15',45,55,3450)")
    cursor.execute(
        "INSERT INTO flights VALUES(188,'Pune','Hyderabad','4/6/21','4/6/21','8:10:15','11:30:13',0,100,6530)")
    cursor.execute(
        "INSERT INTO flights VALUES(189,'Hyderabad','Pune','4/5/21','4/5/21','20:00:00','22:20:25',3,97,2560)")
    cursor.execute("INSERT INTO flights VALUES(190,'Pune','Mumbai','4/5/21','4/5/21','9:30:15','9:45:20',16,84,1900)")
    cursor.execute(
        "INSERT INTO flights VALUES(191,'Mumbai','Hyderabad','4/5/21','4/5/21','21:00:15','23:30:00',6,94,4000)")
    cursor.execute(
        "INSERT INTO flights VALUES(192,'Hyderabad','Mumbai','4/5/21','4/5/21','12:15:00','2:45:15',45,55,4250)")
    cursor.execute(
        "INSERT INTO flights VALUES(193,'Pune','Hyderabad','4/6/21','4/6/21','14:00:15','16:00:00',0,100,3530)")
    cursor.execute("INSERT INTO flights VALUES(194,'Hyderabad','Pune','4/5/21','4/5/21','5:30:00','7:20:25',3,97,3240)")
    cursor.execute("INSERT INTO flights VALUES(195,'Pune','Mumbai','4/6/21','4/6/21','9:30:15','9:45:20',16,84,1900)")
    cursor.execute(
        "INSERT INTO flights VALUES(196,'Mumbai','Hyderabad','4/7/21','4/7/21','21:00:15','23:30:00',6,94,4000)")
    cursor.execute(
        "INSERT INTO flights VALUES(197,'Hyderabad','Mumbai','4/6/21','4/6/21','12:15:00','2:45:15',45,55,4250)")
    cursor.execute(
        "INSERT INTO flights VALUES(198,'Pune','Hyderabad','4/7/21','4/7/21','8:10:15','11:30:13',0,100,3530)")
    cursor.execute(
        "INSERT INTO flights VALUES(199,'Hyderabad','Pune','4/7/21','4/7/21','20:00:00','22:20:25',3,97,3240)")
    cursor.execute("INSERT INTO flights VALUES(200,'Pune','Mumbai','4/6/21','4/6/21','12:00:45','14:00:30',20,80,2570)")
    cursor.execute(
        "INSERT INTO flights VALUES(201,'Mumbai','Hyderabad','4/7/21','4/7/21','5:30:00','8:50:10',45,55,3460)")
    cursor.execute(
        "INSERT INTO flights VALUES(202,'Hyderabad','Mumbai','4/6/21','4/6/21','5:40:00','7:40:45',23,77,6320)")
    cursor.execute(
        "INSERT INTO flights VALUES(203,'Pune','Hyderabad','4/7/21','4/7/21','20:30:15','22:30:00',30,70,2390)")
    cursor.execute(
        "INSERT INTO flights VALUES(204,'Hyderabad','Pune','4/7/21','4/7/21','6:15:00','9:10:25',50,50,2500)")
    cursor.execute("INSERT INTO flights VALUES(205,'Pune','Mumbai','4/7/21','4/7/21','9:30:15','9:45:20',16,84,1900)")
    cursor.execute(
        "INSERT INTO flights VALUES(206,'Mumbai','Hyderabad','4/8/21','4/8/21','21:00:15','23:30:00',6,94,4000)")
    cursor.execute(
        "INSERT INTO flights VALUES(207,'Hyderabad','Mumbai','4/7/21','4/7/21','12:15:00','2:45:15',45,55,4250)")
    cursor.execute(
        "INSERT INTO flights VALUES(208,'Pune','Hyderabad','4/8/21','4/8/21','8:10:15','11:30:13',0,100,3530)")
    cursor.execute(
        "INSERT INTO flights VALUES(209,'Hyderabad','Pune','4/8/21','4/8/21','20:00:00','22:20:25',3,97,3240)")
    cursor.execute("INSERT INTO flights VALUES(210,'Pune','Mumbai','4/7/21','4/7/21','17:15:45','19:30:20',20,80,5400)")
    cursor.execute(
        "INSERT INTO flights VALUES(211,'Mumbai','Hyderabad','4/8/21','4/8/21','8:00:00','10:00:00',80,20,2600)")
    cursor.execute(
        "INSERT INTO flights VALUES(212,'Hyderabad','Mumbai','4/7/21','4/7/21','10:15:30','12:30:15',12,88,6510)")
    cursor.execute(
        "INSERT INTO flights VALUES(213,'Pune','Hyderabad','4/8/21','4/8/21','19:00:00','22:00:40',10,90,4210)")
    cursor.execute(
        "INSERT INTO flights VALUES(214,'Hyderabad','Pune','4/8/21','4/8/21','5:30:00','7:00:25',30,70,4320)")
    connection.commit()


def data_entries_bookings():
    cursor.execute("INSERT INTO Bookings VALUES ('101', 'Student', 1000, 3, 'virajsanap@gmail.com', 101)")
    connection.commit()


def reading():
    cursor.execute("SELECT * FROM USER")
    for row in cursor.fetchall():
        print(row)
    connection.commit()
    print("\n")
    cursor.execute("SELECT * FROM FLIGHTS")
    for row in cursor.fetchall():
        print(row)
    print("\n")
    cursor.execute("SELECT * FROM Bookings")
    for row in cursor.fetchall():
        print(row)
    print("\n")
    cursor.execute("SELECT * FROM Passengers")
    for row in cursor.fetchall():
        print(row)
    print("\n")
    cursor.execute("SELECT * FROM User_PhoneNo")
    for row in cursor.fetchall():
        print(row)
    connection.commit()

create_table()
# data_entries_user()
# data_entries_flights()
# data_entries_bookings()
# data_entries_pass()
# reading()

# cursor.execute("DROP TABLE USER")
# cursor.execute("DROP TABLE Flights")
# cursor.execute("DROP TABLE Bookings")
# cursor.execute("DROP TABLE Passengers")
# cursor.execute("Drop table user_phoneno")

cursor.close()
connection.close()

