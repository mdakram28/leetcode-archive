inline int BitCount(unsigned int u)                         
{
    unsigned int uCount;
    uCount = u - ((u >> 1) & 033333333333) - ((u >> 2) & 011111111111);
    return ((uCount + (uCount >> 3)) & 030707070707) % 63;
}

static const char LogTable256[256] = 
{
#define LT(n) n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n
    -1, 0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3,
    LT(4), LT(5), LT(5), LT(6), LT(6), LT(6), LT(6),
    LT(7), LT(7), LT(7), LT(7), LT(7), LT(7), LT(7), LT(7)
};

inline int log2(unsigned int v)
{
    unsigned int r;     // r will be lg(v)
    unsigned int t, tt; // temporaries

    if (tt = v >> 16)
    {
        r = (t = tt >> 8) ? 24 + LogTable256[t] : 16 + LogTable256[tt];
    }
    else 
    {
        r = (t = v >> 8) ? 8 + LogTable256[t] : LogTable256[v];
    }

    return r;
}

class Solution {
public:
    int minOperations(vector<int>& nums) {
        int a=0, b=0, t;
        for(int num: nums)
        {
            if (num == 0) continue;
            a += BitCount(num);
            t = log2(num);
            // cout << "num=" << num << ", a=" << a << ", t=" << t << endl;
            if (t>b)
            {
                b = t;
            }
        }
        return a+b;
    }
};