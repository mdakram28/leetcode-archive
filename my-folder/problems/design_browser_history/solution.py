class BrowserHistory:

    def __init__(self, homepage: str):
        self.q = [None] * 5000
        self.curr = 0
        self.top = 0
        self.q[0] = homepage
        

    def visit(self, url: str) -> None:
        self.curr += 1
        self.q[self.curr] = url
        self.top = self.curr

    def back(self, steps: int) -> str:
        self.curr -= min(steps, self.curr)
        return self.q[self.curr]

    def forward(self, steps: int) -> str:
        self.curr += min(steps, self.top-self.curr)
        return self.q[self.curr]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)