// top_k_frequent.cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>
using namespace std;

unordered_map<int, int> _getFrequencies(const vector<int>& nums){
    unordered_map<int, int> frequencies; // initialize dictionary containing array elements and their frequencies
    for (int x : nums){
        frequencies[x]++; // update frequency for each unique array element
    }
    return frequencies;
}

vector<int> topKFrequent(const unordered_map<int, int>& frequencies, int k){
    priority_queue<unordered_map<int, int>> most_freq = {}; // initialize queue
    for (int x : frequencies){
        if (most_freq.size() <= k){    
            most_freq.push(x, frequencies[x]);
        }
        else{

        }
    }
}


int main(){
    vector<int> nums = {1,1,1,2,2,3};
    int k = 2;
    vector<int> top = topKFrequent(nums, k);
    for (int x : top) cout << x << " ";
}