from fractions import Fraction as fr;
import math as m;



def calculateSlope(point1, point2):
    slope = fr(
        fr(point2[1] - point1[1]).limit_denominator(), 
        fr(point2[0] - point1[0]).limit_denominator()
        );
    
    return slope;



def constructLinearEq(point1, point2):
    # y-y1 = m (x-x1) => y = mx - mx1 + y1 => -mx + y = -mx1 + y1
    m = calculateSlope(point1, point2);
    xCoeff = -m * m.denominator;
    yCoeff = m.denominator;
    rhs = (-m * point1[0] + point1[1]) * m.denominator;
    linearCoeff = [xCoeff, yCoeff, rhs];
    
    # to get rid of /1 in fraction
    for i in range(0, 3, 1):
        if linearCoeff[i].denominator == 1:
            linearCoeff[i] = linearCoeff[i].numerator;
            
    return linearCoeff;



# to bring the last line to the end of the list
def sortingListOfAllLinearEqs(listOfAllLinearEqs):
    listOfAllLinearEqs_sorted = [];
    for i in range(0, len(listOfAllLinearEqs), 1):
        if i != 1:
            listOfAllLinearEqs_sorted.append(listOfAllLinearEqs[i]);
    listOfAllLinearEqs_sorted.append(listOfAllLinearEqs[1]);
    
    return listOfAllLinearEqs_sorted;



def generateAllLinearEqs(listOfAllPoints):
    listOfAllLinearEq = [];
    for i in range(0, len(listOfAllPoints), 1):
        for j in range(0, len(listOfAllPoints), 1):
            if (j - i == 1) or (i == 0 and j == len(listOfAllPoints)-1):
                listOfAllLinearEq.append(
                    constructLinearEq(listOfAllPoints[i], listOfAllPoints[j])
                    );
                
    listOfAllLinearEq = sortingListOfAllLinearEqs(listOfAllLinearEq);
    
    return listOfAllLinearEq;

      
    
def solutionOf2Lines(line1, line2):
    # will be solved by Cramer's Rule
    det = line1[0]*line2[1] - line2[0]*line1[1];
    detX = line1[2]*line2[1] - line2[2]*line1[1];
    detY = line1[0]*line2[2] - line2[0]*line1[2];
    x = fr(
        fr(detX).limit_denominator(), det
    );
    y = fr(
        fr(detY).limit_denominator(), det
    );
    
    return (x, y);



def pointDistance(point1, point2):
    x1, y1 = point1[0], point1[1];
    x2, y2 = point2[0], point2[1];
    d = m.sqrt(
        (y2-y1)**2 + (x2-x1)**2
    );
    d = fr(d).limit_denominator();
    
    return d;



def lengthRatio(point1, point2, point3):
    # point1 := initial point, point2 := internal point, point3 := terminal point
    net_length = pointDistance(point1, point3);
    __1to2 = pointDistance(point1, point2);
    __2to3 = pointDistance(point2, point3);
    
    return (fr(__1to2, net_length).limit_denominator(), fr(__2to3, net_length).limit_denominator());



def inequalityGenerator(listOfAllEqs, listOfCrossingTuple, listOfPoints):
    listOfPoints.append(listOfPoints[0]); # append the first point to the last position to avoid index out of range and in a planar stick knot, we always connect the first point with the last point
    listOfIne = [];
    
    for i in range(0, len(listOfCrossingTuple), 1):
        line1 = listOfAllEqs[listOfCrossingTuple[i][0]-1];
        line2 = listOfAllEqs[listOfCrossingTuple[i][1]-1];
        
        # first and second points of line1
        fpLine1 = listOfPoints[listOfCrossingTuple[i][0]-1];
        spLine1 = listOfPoints[listOfCrossingTuple[i][0]];
        
        # first and second points of line2
        fpLine2 = listOfPoints[listOfCrossingTuple[i][1]-1];
        spLine2 = listOfPoints[listOfCrossingTuple[i][1]];
        
        solution = solutionOf2Lines(line1, line2);
        
        # ratio1_1 := ratio of the line number 1 and for the first var
        (ratio1_1, ratio1_2) = lengthRatio(fpLine1, solution, spLine1);
        (ratio2_1, ratio2_2) = lengthRatio(fpLine2, solution, spLine2);
        
        
        if listOfCrossingTuple[i][0] == len(listOfPoints)-1:
            lhs = f"{ratio1_1} z{listOfCrossingTuple[i][0]} + {ratio1_2} z{1}";
        else: lhs = f"{ratio1_1} z{listOfCrossingTuple[i][0]} + {ratio1_2} z{listOfCrossingTuple[i][0]+1}";
        
        if listOfCrossingTuple[i][1] == len(listOfPoints)-1:
            rhs = f"{ratio2_1} z{listOfCrossingTuple[i][1]} + {ratio2_2} z{1}";
        else: rhs = f"{ratio2_1} z{listOfCrossingTuple[i][1]} + {ratio2_2} z{listOfCrossingTuple[i][1]+1}";
        
        inequality = lhs + " > " + rhs;
        
        listOfIne.append(inequality);
        print(listOfIne[i]);



# add knot vertices along with the direction
def addPoints(): 
    z1 = (0, 0);
    z2 = (9, 4);
    z3 = (5, 8);
    z4 = (2, 5);
    z5 = (1, 7);
    z6 = (9, 7);
    z7 = (5, 1);
    z8 = (0, 6);
    z9 = (2.39, 6.39);
    listOfPoints = [z1, z2, z3, z4, z5, z6, z7, z8, z9];
    
    return listOfPoints;



def addCrossing():
    # (starting point of line1, starting point of line2) and 
    listOfCrossingTuple = [(1, 7), (6, 1), (2, 6), (5, 2), (3, 5), (9, 4), (4, 8), (7, 9)];
    
    return listOfCrossingTuple;



if __name__ == '__main__':
    __listOfPoints = addPoints();
    __listOfCrossingTuple = addCrossing();
    __listOfAllLinearEq = generateAllLinearEqs(__listOfPoints);
    print(__listOfAllLinearEq);
    print(__listOfCrossingTuple);
    print(__listOfPoints);
    inequalityGenerator(__listOfAllLinearEq, __listOfCrossingTuple, __listOfPoints);