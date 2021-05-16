 ################################################################################
#
#   Lab #9
#
#   Purpose: The purpose of this program is to provide a user with access
#               to three dictionaries. The Room Number, Instructor, and Meeting
#               will be available to the user through these dictionaries.
#   Author: Tigris Mendez
#   Date Written: March 4th, 2021
#   Version: 1.7
#
################################################################################

#Create three dictionaries

#Course Number/ Room Number
CNumber_Room = {'CS101': 3004, 'CS102': 4501,'CS103': 6755,'NT110': 1244,'CM241': 1411}

#Course Number/ Instructor
Cnumber_Instructor = {'CS101': 'Haynes','CS102': 'Alvarado','CS103': 'Rich','NT110': 'Burke','CM241': 'Lee'}

#Course Number/ Meeting Time
CNUmber_Meeting = {'CS101': '8:00am','CS102': '9:00am','CS103': '10:00am','NT110': '11:00am','CM241': '11:00pm'}

#define mainline logic of the program
#class_name = 'input(Enter a class name: ')
print('Welcome to the class directory')
print('To recieve the Room #, Instructor, and Meeting time of a class, please enter a class as follows:')
print('\nCS101, CS102, CS103, NT110, CM241')
print('^^^type as given to avoid errors^^^')
class_name = input('\nEnter a class name:')


#if the class_name IS in dictionaries
if __name__ == '__main__':

        #if class_name is in CNumber_Room
    if class_name in CNumber_Room:
        # print 'Room' + Room Number
        print(CNumber_Room[class_name])

    #if class_name is in CNumber_Instructor
    if class_name in Cnumber_Instructor:
        #print 'Instructor' + Instructor
        print(Cnumber_Instructor[class_name])

    #if class_name is is CNumber_Meeting
    if class_name in CNUmber_Meeting:
        #print 'Time' + Meeting Time
        print(CNUmber_Meeting[class_name])

    #if the class_name IS NOT in dictionaries

    if class_name not in CNumber_Room:
        # print 'Room' + Room Number
        print("No room number available for " + class_name)

    #if class_name is in CNumber_Instructor
    if class_name not in Cnumber_Instructor:
        #print 'Instructor' + Instructor
        print("No Instructor Name available for " + class_name)

    #if class_name is is CNumber_Meeting
    if class_name not in CNUmber_Meeting:
        #print 'Time' + Meeting Time
        print("No Meeting Time available for " + class_name)
main()