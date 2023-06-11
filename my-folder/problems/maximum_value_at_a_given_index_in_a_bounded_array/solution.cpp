class Solution {
public:
    int maxValue(int n, int index, int maxSum) {
        long left = 1;
        long right = maxSum;
        int result = -1;

        while (left <= right) {
            long mid = left + (right - left) / 2;

            if (check(n, index, maxSum, mid)) {
                result = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return result;
    }

    bool check(int n, int index, int maxSum, long num) {
        long leftSum = 0;
        long rightSum = 0;

        // Calculate the sum of elements on the left side
        if (num > index) {
            long diff = num - index;
            leftSum = (diff + num) * (index + 1) / 2;
        } else {
            leftSum = (1 + num) * num / 2 + index - num + 1;
        }

        // Calculate the sum of elements on the right side
        if (num > (n - index - 1)) {
            long diff = num - (n - index - 1);
            rightSum = (diff + num) * (n - index) / 2;
        } else {
            rightSum = (1 + num) * num / 2 + n - index - num;
        }

        long sum = leftSum + rightSum - num;

        return sum <= maxSum;
    }
};