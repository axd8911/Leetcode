#include <iostream>
#include <vector>

using namespace std;
// non negative, add up
// negative, update current maximum, return zero

int solution(vector<int> &A){
    int total = 0;
    int largest = -1;
    int count = 0;
    for (size_t i=0;i<A.size();i++){
        if (A[i]<0){
            largest = max(total,largest);
            total = 0;
            count += 1;
        }
        else{
            total += A[i];
        }
    }
    largest = max(total,largest);
    if (count == int(A.size())){
        return -1;
    }
    return largest;
};
int main(){
    vector<int> myVec {-8,3,0,5,-3,12};
    int output;
    output = solution(myVec);
    cout<<output;
    return output;
};
