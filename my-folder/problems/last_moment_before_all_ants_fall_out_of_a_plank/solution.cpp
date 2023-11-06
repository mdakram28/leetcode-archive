
#include <immintrin.h>

int fastMax16(int* start, int* end)
{
#define STRIDE 16
#define STRIDE_ELEM 16/sizeof(int)

    const int* firstAddr = (const int*)((((uint64_t)start / STRIDE) * STRIDE));
    if (firstAddr < start)
        firstAddr += STRIDE;
    const int* lastAddr = (const int*)(((uint64_t)end / STRIDE) * STRIDE);

    int* it = start;
    int ret = 0;

    for (it = start; it < firstAddr && it < end; it++)
    {
        if (*it > ret)
            ret = *it;
    }

    if (it < lastAddr)
    {
        // __m512i val;
        __m128i maxval = _mm_load_si128((__m128i*) it);
        it += STRIDE_ELEM;
        while (it < lastAddr)
        {
            // Load STRIDE and store max
            maxval = _mm_max_epi16(maxval, _mm_load_si128((__m128i*) it));
            it += STRIDE_ELEM;
        }
        alignas(32) uint16_t tmp[8];
        _mm_store_si128((__m128i*)tmp, maxval);
        ret = max(ret, (int) max({tmp[0], tmp[2], tmp[4], tmp[6] }));
    }

    while (it < end)
    {
        if (*it > ret)
            ret = *it;
        it++;
    }

    return ret;
}

int fastMin16(int* start, int* end)
{
#define STRIDE 16
#define STRIDE_ELEM 16/sizeof(int)

    const int* firstAddr = (const int*)((((uint64_t)start / STRIDE) * STRIDE));
    if (firstAddr < start)
        firstAddr += STRIDE;
    const int* lastAddr = (const int*)(((uint64_t)end / STRIDE) * STRIDE);

    int* it = start;
    int ret = INT_MAX;

    for (it = start; it < firstAddr && it < end; it++)
    {
        if (*it < ret)
            ret = *it;
    }

    if (it < lastAddr)
    {
        __m128i maxval = _mm_loadu_si128((__m128i*) it);
        it += STRIDE_ELEM;
        while (it < lastAddr)
        {
            // Load STRIDE and store max
            maxval = _mm_min_epi16(maxval, _mm_loadu_si128((__m128i*) it));
            it += STRIDE_ELEM;
        }
        alignas(32) uint16_t tmp[8];
        _mm_store_si128((__m128i*)tmp, maxval);
        ret = min(ret, (int)min({ tmp[0], tmp[2], tmp[4], tmp[6] }));
    }

    while (it < end)
    {
        if (*it < ret)
            ret = *it;
        it++;
    }

    return ret;
}

class Solution {
public:
    
    int getLastMoment(int n, vector<int>& left, vector<int>& right) {
        int l = fastMax16(left.data(), left.data() + left.size());
        int r = fastMin16(right.data(), right.data() + right.size());

        return max(l, n-r);
    }
};