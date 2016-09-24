studentencijfers = [
    [95, 92, 86],
    [66, 75, 54],
    [89, 72, 100],
    [34, 0, 0]
];

"""
Calculate the average in a two dimentional list

@param {List(List(Int))} studenten - Two dimentional list of Ints
@return {list(Float)} One dimentional list of the average of the input
"""
def gemiddelde_per_student(studenten):
    gemiddelde = [];
    for student in studenten:
        gemiddelde.append(float(sum(student)) / max(len(student), 1));

    return gemiddelde;

"""
Calculate the average of a list

@param {List(Float)} studenten - List of average marks
@return {Int} Total average.
"""
def gemiddelde_van_alle_studenten(studenten):
    gemiddelde = gemiddelde_per_student(studenten);
    return float(sum(gemiddelde)) / max(len(gemiddelde), 1);

print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))
