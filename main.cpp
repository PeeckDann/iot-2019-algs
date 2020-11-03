#include <iostream>
#include <math.h>
#include <fstream>

using namespace std;

int solve(int cNum, int cWidth, int cHeight){
    int bigger = (cWidth > cHeight) ? cWidth : cHeight;
    int smaller = cWidth + cHeight - bigger;

    int exceptionSideSize = bigger * cNum;
    int oldTemp = exceptionSideSize;
    int temp = 0;

    if (cNum == 1){
        return bigger;
    }
    if (cWidth == cHeight){
        return ceil(sqrt(cNum)) * cWidth;
    }
    for (int i = 1; i < ceil(cNum/2); ++i){
        if (cNum % i == 0){
            temp = (smaller * (cNum / i) > bigger * i) ? smaller * (cNum / i) : bigger * i;
            exceptionSideSize = (temp < oldTemp) ? temp : oldTemp;
            oldTemp = temp;
        }
    }

    int maxSideSize = 0;
    int finalSideSize = 0;
    int rowNum = 1;

    for (int colNum = cNum; colNum > 1; --colNum){
        if (colNum == cNum / rowNum && rowNum != 1){
            rowNum++;
        }

        maxSideSize = (smaller * colNum > bigger * rowNum) ? smaller * colNum : bigger * rowNum;

        if (finalSideSize > maxSideSize){
            finalSideSize = maxSideSize;
        }

        if (colNum == cNum){
            rowNum++;
            finalSideSize = maxSideSize;
        }
    }

    return (finalSideSize < exceptionSideSize) ? finalSideSize : exceptionSideSize;
}

int main(){
    int cNum, cWidth, cHeight;

    fstream bugtrk_in;
    bugtrk_in.open("bugtrk_in", ios::in);
    if (!bugtrk_in){
        cout << "Does not exist!";
        return 0;
    }
    bugtrk_in >> cNum;
    bugtrk_in >> cWidth;
    bugtrk_in >> cHeight;
    bugtrk_in.close();

    int tSide = solve(cNum, cWidth, cHeight);

    fstream bugtrk_out;
    bugtrk_out.open("bugtrk_out", ios::out);
    if (!bugtrk_out){
        cout << "Does not exist!";
        return 0;
    }
    bugtrk_out << tSide << endl;
    bugtrk_out.close();

    cout << cNum << " " <<  cWidth << " " << cHeight << "\n" << tSide << endl;
    return 0;
}