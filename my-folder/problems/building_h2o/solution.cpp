class H2O {
    mutex mh;
    mutex mo;
    atomic<int> nh = 0;
public:
    H2O() {
        mo.lock();
    }

    void hydrogen(function<void()> releaseHydrogen) {
        mh.lock();
        // releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen();
        nh++;
        if(nh.load()%2) {
            mh.unlock();
        } else {
            mo.unlock();
        }
    }

    void oxygen(function<void()> releaseOxygen) {
        mo.lock();
        // releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen();
        mh.unlock();
    }
};