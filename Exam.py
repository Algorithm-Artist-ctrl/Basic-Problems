'''Q35. Exam Hall Entry
Allow only if hall ticket and ID card both are valid.
'''
def Exam_Hall_Entry(hall_ticket=True,ID_card=True):
    if hall_ticket and ID_card :
        return "Entry"
    else:
        return "Not Entry"
print(Exam_Hall_Entry())

