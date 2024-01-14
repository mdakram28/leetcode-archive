class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        int i=0;
        for(int a: asteroids) {
            if (a > 0) {
                asteroids[i++] = a;
                continue;
            }
            bool dest = false;
            while (i > 0 && asteroids[i-1]>0) {
                // cout << "last=" << asteroids[i-1] << endl;
                if (asteroids[i-1] > -a) {
                    dest = true;
                    break;
                } else if (asteroids[i-1] == -a) {
                    // cout << "dest last" << endl;
                    i--;
                    dest = true;
                    break;
                } else {
                    // cout << "dest last" << endl;
                    i--;
                }
            }
            // cout << "a=" << a << ", dest=" << dest << endl;
            if (!dest) {
                asteroids[i++] = a;
            }
        }
        asteroids.resize(i);
        return asteroids;
    }
};