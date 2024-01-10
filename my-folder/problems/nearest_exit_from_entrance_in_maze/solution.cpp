class Solution {
public:
    int nearestExit(vector<vector<char>>& maze, vector<int>& entrance) {
        int m = maze.size();
        int n = maze[0].size();

        std::queue<std::tuple<int, int, int>> q;
        std::vector<std::vector<bool>> seen(m, std::vector<bool>(n));

        int r = entrance[0], c = entrance[1];
        q.push({0, r, c});
        seen[r][c] = true;
        maze[r][c] = '+';

        std::vector<std::pair<int, int>> diff = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        while (q.size() > 0) {
            auto [d, r, c] = q.front();
            q.pop();

            // printf("r=%d, c=%d\n", r, c);

            if (maze[r][c] != '+' && (r == 0 || r == m-1 || c == 0 || c == n-1)) {
                return d;
            }

            for(auto [dr, dc]: diff) {
                int nr = r+dr;
                int nc = c+dc;
                // printf("nr=%d, nc=%d\n", nr, nc);
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && !seen[nr][nc] && maze[nr][nc] == '.') {
                    seen[nr][nc] = true;
                    q.push({d+1, nr, nc});
                }
            }
        }

        return -1;
    }
};