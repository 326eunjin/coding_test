#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

int main() {
    std::string num1, num2;
    std::cin >> num1 >> num2;

    std::string min, max;
    int left = 0;

    if (num1.length() > num2.length()) {
        min = num2;
        max = num1;
        left = num1.length() - num2.length();
    } else {
        min = num1;
        max = num2;
        left = num2.length() - num1.length();
    }

    // 앞부분에 0 추가
    min = std::string(left, '0') + min;

    std::vector<int> result;
    int tmp = 0;

    // 덧셈 진행 (뒤에서부터)
    for (int i = max.length() - 1; i >= 0; --i) {
        tmp += (min[i] - '0') + (max[i] - '0');
        if (tmp >= 10) {
            result.push_back(tmp % 10);
            tmp /= 10;
        } else {
            result.push_back(tmp);
            tmp = 0;
        }
    }

    if (tmp > 0) {
        result.push_back(tmp);
    }

    std::reverse(result.begin(), result.end());

    for (int i : result) {
        std::cout << i;
    }
    std::cout << std::endl;

    return 0;
}
