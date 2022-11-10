class Robot {
    int w,h;
    int perimeter;
    int s;
    bool isFirst;
public:
    Robot(int width, int height) {
        w=width;
        h=height;
        perimeter = 2*w + 2*h - 4;
        s=0;
        isFirst=true;
    }
    
    void step(int num) {
        s = (s + num) % perimeter;
        isFirst = false;
    }
    
    vector<int> getPos() {
        int ts = s;
        if (ts < (w-1)) {
            return {ts, 0};
        }
        ts -= w-1;
        if (ts < (h-1)) {
            return {w-1, ts};
        }
        ts -= h-1;
        if (ts < (w-1)) {
            return {w-1-ts, h-1};
        }
        ts -= w-1;
        return {0, h-1-ts};
    }
    
    string getDir() {
        if(isFirst) {
            return "East";
        } else if(s == 0) {
            return "South";
        }
        int ts = s;
        if (ts <= (w-1)) {
            return "East";
        }
        ts -= w-1;
        if (ts <= (h-1)) {
            return "North";
        }
        ts -= h-1;
        if (ts <= (w-1)) {
            return "West";
        }
        ts -= w-1;
        return "South";
    }
};

/**
 * Your Robot object will be instantiated and called as such:
 * Robot* obj = new Robot(width, height);
 * obj->step(num);
 * vector<int> param_2 = obj->getPos();
 * string param_3 = obj->getDir();
 */