#include <iostream>
#include <algorithm>
using namespace std;

int solution(int N,int K){
    if (N<0 || K<0 || N-K<0){
        return -1;
    }
    if (N == 0 || K == 0){
        return 1;
    }

    int small = min(K,N-K);
    int large = max(K,N-K);
    int init = 1;
    double total = 1;
    for (int i=N; i>large; --i){
        total *= (i/init);
        if (total > 1000000000){
            return -1;
        }
        init += 1;
    }
    int output = 1;
    for (int i=large+1;i<=N;++i){
        output *= i;
    }
    for (int i=1;i<=small;++i){
        output /=i;
    }
    return output;
};

int main(){
    int n = 40;
    int k = 35;
    int output = solution(n,k);
    cout<<output;
    return output;
};
