/**
 * @param {number[]} usageLimits
 * @return {number}
 */
function maxIncreasingGroups(usageLimits) {
    let ans = 1;  // next target length
    let availableLimits = 0;

    usageLimits.sort((a, b) => a - b);  // Sort the usageLimits array in ascending order

    for (const usageLimit of usageLimits) {
        availableLimits += usageLimit;
        // Can create groups 1, 2, ..., ans.
        if (availableLimits >= (ans * (ans + 1)) / 2) {
            ans += 1;
        }
    }

    return ans - 1;
}