class FooBar {
private:
    int n;
    mutex mfoo;
    mutex mbar;
public:
    FooBar(int n) {
        this->n = n;
        mbar.lock();
    }

    void foo(function<void()> printFoo) {
        
        for (int i = 0; i < n; i++) {
            mfoo.lock();
        	// printFoo() outputs "foo". Do not change or remove this line.
        	printFoo();
            mbar.unlock();
        }
    }

    void bar(function<void()> printBar) {
        
        for (int i = 0; i < n; i++) {
            mbar.lock();
        	// printBar() outputs "bar". Do not change or remove this line.
        	printBar();
            mfoo.unlock();
        }
    }
};