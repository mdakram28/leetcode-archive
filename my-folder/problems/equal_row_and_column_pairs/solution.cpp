std::size_t hashRow(std::vector<std::vector<int>> const& grid, int r) {
  std::size_t seed = grid.size();
  for(auto& i : grid[r]) {
    seed ^= i + 0x9e3779b9 + (seed << 6) + (seed >> 2);
  }
  return seed;
}

std::size_t hashCol(std::vector<std::vector<int>> const& grid, int c) {
  std::size_t seed = grid.size();
  for(int r=0; r<grid.size(); r++) {
    seed ^= grid[r][c] + 0x9e3779b9 + (seed << 6) + (seed >> 2);
  }
  return seed;
}

class Solution {
public:
    int equalPairs(vector<vector<int>>& grid) {
        std::unordered_map<size_t, int> hashCount;
        int ans = 0;
        for(int r=0; r<grid.size(); r++) {
            hashCount[hashRow(grid, r)]++;
        }
        for(int c=0; c<grid.size(); c++) {
            ans += hashCount[hashCol(grid, c)];
        }
        return ans;       
    }
};