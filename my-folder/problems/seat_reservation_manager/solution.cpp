class SeatManager {
    priority_queue <int, vector<int>, greater<int>> pq;
    int last = 0;
public:
    SeatManager(int n) {
        // for(int i=1; i<=n; i++)
        // {
        //     pq.push(i);
        // }
    }
    
    int reserve() {
        if (pq.size() == 0)
        {
            return ++last;
        }
        int ret = pq.top();
        pq.pop();
        return ret;
    }
    
    void unreserve(int seatNumber) {
        if (seatNumber == last)
        {
            last--;
        }
        else{
            pq.push(seatNumber);
        }
    }
};

/**
 * Your SeatManager object will be instantiated and called as such:
 * SeatManager* obj = new SeatManager(n);
 * int param_1 = obj->reserve();
 * obj->unreserve(seatNumber);
 */