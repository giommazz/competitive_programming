// https://neetcode.io/problems/two-integer-sum?list=neetcode150
#include <vector>
#include <unordered_map>
using namespace std;


vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> complements;
    // `complements`: each key is a complement wrt `target`, each value is an index
    complements[target - nums[0]] = 0; // add first element

    for (int i=1; i < nums.size(); i++){
        int key = nums[i]; // get current key
        if (complements.find(key) != complements.end()){ // if `key` in `complements`
            return {complements[key], i};
        }
        complements[target - key] = i; // add current element
    }   
}

