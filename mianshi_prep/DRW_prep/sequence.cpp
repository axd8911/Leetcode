#include <iostream>
#include <vector>
#include <array>
#include <algorithm>

using namespace std;

int solution(int A[],int length){
    if (length <= 2){
        return 0;
    }
    int seq = 1;
    int total = 0;
    int diff = 2^31-1;
    for (int i=1;i<length;++i){
        if (A[i]-A[i-1]==diff){
            seq += 1;
            //cout<<"yes1"<<" "<<seq<<"  "<<diff<<endl;
            if (i==length-1){
                total += (seq-2)*(seq-1)/2;
            }
        }
        else{
            //cout<<"yes2"<<" "<<seq<<endl;
            total += (seq-2)*(seq-1)/2;
            seq = 2;
            diff = A[i]-A[i-1];
        }
        //cout<<A[i]<<"  "<<A[i-1]<<"  "<<total<<endl;
    }

    return total;

};

int main(){
    int output;
    int myVec[10000] {0};
    int length = sizeof(myVec)/sizeof(myVec[0]);
    output = solution(myVec,length);
    cout<<output<<"  "<<sizeof(myVec)/sizeof(myVec[0]);
    return output;
};
