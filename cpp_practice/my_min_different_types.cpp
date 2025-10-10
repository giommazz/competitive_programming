// my_min_different_types.cpp
#include <iostream>
using namespace std;

/* 
`template` allows working with one or more types that will be specified later
`typename`: placeholder for types
`auto`: dynamic inference at compile time
*/
template <typename T, typename U>

// Write a function that takes any two numbers and returns their minimum without using std::min
auto my_min(T a, U b){
    return (a < b) ? a : b;
}

int main() {
    cout << "Hello, Gubi!" << endl;
    cout << my_min(2.9, 3.4);
    return 0;
}