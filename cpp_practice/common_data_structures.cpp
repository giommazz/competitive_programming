#include <unordered_set>
#include <vector>
#include <iostream>
using namespace std;

int main(){
    unordered_set<int> seen;
    seen.insert(2);
    seen.insert(3);
    if (seen.find(2) != seen.end()){
        cout << "Found x!" << endl;
    }
    for (int elem : seen){
        cout << elem << " ";
    }
    cout << endl;
}