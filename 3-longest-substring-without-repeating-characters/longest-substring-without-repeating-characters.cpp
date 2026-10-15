#include <string>
#include <vector>
#include <algorithm>

class Solution {
public:
    int lengthOfLongestSubstring(std::string s) {

        std::vector<int> charIndex(128, -1);
        int maxLength = 0;
        int left = 0;

        for (int right = 0; right < s.length(); ++right) {
            char currentChar = s[right];

            if (charIndex[currentChar] >= left) {
                left = charIndex[currentChar] + 1;
            }

            charIndex[currentChar] = right;

            maxLength = std::max(maxLength, right - left + 1);
        }

        return maxLength;
    }
};