// most_frequent_int.cpp
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int mostFrequent_pythonic(vector<int> nums){
    int result;
    int maxcount = 0; 
    unordered_map<int,int> counts;
    for (int x : nums){
        if (counts.find(x) != counts.end()){
            counts[x]++;
        }
        else counts.insert({x,1});
        if (counts[x] > maxcount){
            maxcount = counts[x];
            result = x;
        }
    }
    return result; 
}

int mostFrequent_cppy(vector<int> nums){
    int result;
    int maxcount = 0; 
    unordered_map<int,int> counts;
    
    for (int x : nums){
        counts[x]++; // if x notin `counts`, inserts new element and initializes to 0. Increment in any case
        if (counts[x] > maxcount){
            maxcount = counts[x];
            result = x;
        }
    }
    return result;
}


int main(){
    vector<int> nums = {1, 2, 2, 5, 5, 5, 5};
    cout << mostFrequent_cppy(nums) << endl;
}