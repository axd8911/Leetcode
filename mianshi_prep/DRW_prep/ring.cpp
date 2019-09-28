// Return longest size of a ring
// create a set to save all numbers that already saved
//

#include <iostream>
#include <vector>
#include <string>
#include <array>
#include <unordered_set>
#include <algorithm>
using namespace std;

int solution(vector<int> &A){
    unordered_set<int> counted;
    vector<vector<int>> rings;
    for (size_t i=0;i<A.size();++i){
        if (counted.find(A[i]) == counted.end()){
            cout<<endl;
            cout<<i;
            int idx = i;
            rings.push_back({});
            while (counted.find(idx) == counted.end()){
                cout<<"  locA  "<<idx;
                rings[rings.size()-1].push_back(idx);
                counted.insert(idx);
                idx = A[idx];
            }
        }
    }
    int largest = 0;
    for (size_t i=0;i<rings.size();++i){
        int curr = rings[i].size();
        //cout<<largest<<"  "<<curr<<endl;
        largest = max(largest, curr);
    }
    return largest;
};

int main(){
    int output;
    vector<int> myArr {4,2,9,6,7,5,3,1,0,8};
    output = solution(myArr);
    cout<<output;
    return output;
};
