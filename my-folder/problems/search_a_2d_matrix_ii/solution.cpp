class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size(), n = matrix[0].size();
        // printf("---------------------\n");
        // for (int r=0; r<m; r++) {
        //     for (int c=0; c<n; c++) {
        //         printf("%d\t", matrix[r][c]);
        //     }
        //     printf("\n");
        // }
        // printf("target = %d\n", target);
        int top = 0;
        int left = 0;
        int right = matrix[0].size();
        int bottom = matrix.size();

        while ((right-left) > 1 || (bottom-top)>1) {
            int t = top, b = bottom;
            while (t<b) {
                int mid = (t+b)/2;
                if (matrix[mid][left] <= target) {
                    t = mid+1;
                } else {
                    b = mid;
                }
            }
            bottom = b;

            int l = left, r = right;
            while (l < r) {
                int mid = (l+r)/2;
                if (matrix[top][mid] <= target) {
                    l = mid+1;
                } else {
                    r = mid;
                }
            }
            right = r;

            t = top, b = bottom;
            while (t<b) {
                int mid = (t+b) / 2;
                if (matrix[mid][right-1] < target) {
                    t = mid+1;
                } else {
                    b = mid;
                }
            }
            top = t;

            l = left, r = right;
            while (l<r) {
                int mid = (l+r)/2;
                if (matrix[bottom-1][mid] < target) {
                    l = mid+1;
                } else {
                    r = mid;
                }
            }
            left = l;

            // printf("top=%d, bottom=%d, left=%d, right=%d \n", top, bottom, left, right);
            if (left>=n || top>=m || right<=0 || bottom<=0) {
                return false;
            }
            if (
                matrix[top][left] == target 
                || matrix[top][right-1] == target
                || matrix[bottom-1][left] == target
                || matrix[bottom-1][right-1] == target)
                return true;
        }
        return left<n && top<m && matrix[top][left] == target;
    }
};