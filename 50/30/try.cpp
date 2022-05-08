#include <iostream>
#include <cmath>
using namespace std;
int main(){
    int a,b,x;
    cin >> x;
    for (a = -1000;a<1000;a++){
        for(b = -1000;b<1000;b++){
            if(pow(a,5)-pow(b,5) == x){
                cout << a <<" "<< b << endl;
                return 0;
            }
        }
    }
}