studentHousingPref = {
    'Cedric Diggory': ['Hufflepuff', 'Ravenclaw', 'Slytherin', 'Gryffindor'],
    'Draco Malfoy': ['Slytherin', 'Ravenclaw', 'Hufflepuff', 'Gryffindor'],
    'Harry Potter': ['Hufflepuff', 'Ravenclaw', 'Gryffindor', 'Slytherin'],
    'Luna Lovegood': ['Hufflepuff', 'Ravenclaw', 'Slytherin','Griffindor']
}

housesStudentRanking = {
     'Gryffindor': ['Harry Potter',
                    'Cedric Diggory',
                    'Luna Lovegood',
                    'Draco Malfoy'],
     'Hufflepuff': ['Cedric Diggory',
                    'Luna Lovegood',
                    'Harry Potter',
                    'Draco Malfoy'],
     'Ravenclaw': ['Luna Lovegood',
                   'Harry Potter',
                   'Cedric Diggory',
                   'Draco Malfoy'],
     'Slytherin': ['Draco Malfoy',
                   'Harry Potter',
                   'Luna Lovegood',
                   'Cedric Diggory']
}

def stable_matching(studentPref, housePref):
    # Initialize data structures
    free_students = list(studentPref.keys())
    proposals = {student: 0 for student in studentPref}   
    houses_matched = {}  # This will store the matches

    while free_students:
        student = free_students.pop(0)  # Get the next free student
        # Find the next house to propose to
        if proposals[student] < len(studentPref[student]):
            house = studentPref[student][proposals[student]]
            proposals[student] += 1  # Move to the next house for next round
            
            # If the house is free, engage
            if house not in houses_matched:
                houses_matched[house] = student
            else:
                current_student = houses_matched[house]
                # Check if the house prefers the new student
                if housePref[house].index(student) < housePref[house].index(current_student):
                    houses_matched[house] = student
                    free_students.append(current_student)  # Current student becomes free
                else:
                    free_students.append(student)  # This student remains free

    return houses_matched



print("STUDENTS WITH HOUSING PREFERENCE")
print(studentHousingPref)

print("HOUSES WITH STUDENT RANKING")

print (housesStudentRanking)

print("COMPLETE LIST OF HOUSING ASSIGNMENTS")

print(stable_matching(studentHousingPref, housesStudentRanking))