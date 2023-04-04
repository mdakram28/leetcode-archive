class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        ret = []
        trans_by_name = collections.defaultdict(list)
        ret = set()
        for i, t in enumerate(transactions):
            name, time, amount, city = t.split(',')
            time = int(time)
            amount = int(amount)

            if amount > 1000:
                ret.add(i)
                
            invalid = False
            for t2 in trans_by_name[name]:
                if abs(t2[1]-time) <= 60 and t2[2] != city:
                    ret.add(t2[0])
                    invalid = True
            if invalid:
                ret.add(i)


            trans_by_name[name].append((i, time, city))
        
        return [transactions[i] for i in ret]

