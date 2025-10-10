// arrays_practice.cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> create_anytype_array(int len){
    vector<int> v = {};
    for (int i = 0; i < len; i++){
        v.push_back(i);
    }
    return v;
}

void print_array(vector<int> v){
    for (int elem : v){
        cout << elem << " ";
    }
    cout << endl;
}



int main(){
    cout << "Hello!" << endl;
    int a[2] = {1, 2};
    int sa = sizeof(a);
    int sa0 = sizeof(a[1]);
    int len = sa / sa0;
    cout << "sizeof(a[0]): " << sa0 << "; sizeof(a): " << sa << "; length: " << len << endl;

    vector<int> v = create_anytype_array(5);
    print_array(v);
}
