//duplicate_int_list.cpp

#include <vector>
#include <unordered_set>
#include <iostream>
using namespace std;


bool hasDuplicate(vector<int>& nums) {
        
    unordered_set<int> seen;

    if (nums.size() > 1){
        for (int x : nums){
            if (seen.count(x)){
                return true;
            }
            else{
                seen.insert(x);
            }
        }
    }
    return false;
}

int main(){
    vector<int> nums = {1, 2, 3, 5};
    cout << boolalpha << hasDuplicate(nums) << endl; // `boolalpha` prints booleans as "false"/"true" instead of 0/1
}