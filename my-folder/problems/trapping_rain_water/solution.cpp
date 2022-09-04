class Solution {
public:
    int trap(vector<int> &height) {
        vector<int> tops(height.size());
        int maxIndexLeft = 0;
        int maxValueLeft = height[0];
        auto size = height.size();

        for (int i = 0; i < size; i++) {
            if (height[i] > maxValueLeft) {
                maxIndexLeft = i;
                maxValueLeft = height[i];
            }
            tops[i] = maxValueLeft;
        }

        int i = size - 1;
        int maxValueRight = height[i];
        while (maxValueRight < maxValueLeft) {
            if (height[i] > maxValueRight) {
                maxValueRight = height[i];
            }
            tops[i] = maxValueRight;
            i--;
        }

        int trap = 0;
        for (i = 0; i < size; i++) {
            trap += tops[i] - height[i];
        }
        return trap;
    }
};