class RecentCounter {
    queue<int> times;
public:
    RecentCounter() {
        
    }
    
    int ping(int t) {
        times.push(t);
        while((t-times.front()) > 3000) times.pop();
        return times.size();
    }
};

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter* obj = new RecentCounter();
 * int param_1 = obj->ping(t);
 */