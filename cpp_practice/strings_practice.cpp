// strings_practice.cpp
#include <string>
#include <vector>
#include <iostream>
using namespace std;

template <typename SC>
void printsy(SC sc){ // prints strings and characters
    cout << sc << endl;
}

template <typename N>
void printsy(vector<N> v){ // prints vectors
    for (int i=0; i < v.size(); ++i){
        cout << v[i] << " ";
    }
    cout << endl;
}

string reverse(string s){
    int left=0; int right = s.length()-1;
    while (left < right){
        swap(s[left++], s[right--]);
    }
    return s;
}   

int main(){
    string s = "pallone";
    
    printsy(reverse(s));
}