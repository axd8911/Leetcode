#include <iostream>
#include <unordered_map>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int solution(string &A, string &B){
    unordered_map<char,vector<int>> count;
    for (char i:A){
        if (count.find(i)==count.end()){
            count.insert({i,{1,0}});
        }
        else{
            count[i][0] += 1;
        }
    }
    for (char i:B){
        if (count.find(i)==count.end()){
            count.insert({i,{0,1}});
        }
        else{
            count[i][1] += 1;
        }
    }
    int total = 0;
    for (auto i=count.begin();i!=count.end();++i){
        total += abs(i->second[0] - i->second[1]);
    }
    return total;

};

int main(){
    string A = "rather";
    string B = "harder";
    int output;
    output = solution(A,B);
    cout<<output;
    return output;
};
