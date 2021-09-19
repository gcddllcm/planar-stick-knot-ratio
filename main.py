from fractions import Fraction as fr


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



def generateAllLinearEq(listOfAllPoints):
    listOfAllLinearEq = [];
    for i in range(0, len(listOfAllPoints), 1):
        for j in range(0, len(listOfAllPoints), 1):
            if (j - i == 1) or (i == 0 and j == len(listOfAllPoints)-1):
                listOfAllLinearEq.append(
                    constructLinearEq(listOfAllPoints[i], listOfAllPoints[j])
                    );
    
    return listOfAllLinearEq;
                
                
    
    

if __name__ == '__main__':
    listOfPoints = addPoints();
    print(generateAllLinearEq(listOfPoints));