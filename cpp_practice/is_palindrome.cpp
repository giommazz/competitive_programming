// is_palindrome.cpp
#include <iostream>
#include <string>
using namespace std;

template <typename T>
void print(T elem){ // printing a single elementy
    cout << elem << endl;
}

bool is_palindrome(const string& s){
        int left = 0; int right = s.length()-1;
        
        while (left < right)
            if (s[left++] != s[right--]) return false;
        return true;    
}

int main(){
    string s("hallah");
    print(s);
    print("is \"" + s + "\" palindrome?");
    print(is_palindrome(s) ? "yes" : "no");
}
