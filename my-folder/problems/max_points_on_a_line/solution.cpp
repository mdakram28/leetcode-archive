class Fraction {
public:
    int n,d;
    bool pos;
    
    Fraction(int num, int den) {
        n = num>0 ? num : -num;
        d = den>0 ? den : -den;
        pos = (num>0) == (den>0);
        reduce();
    }
    
    void reduce()
    {
        for (int i = min(d,n); i > 1; i--) {  
            if ((d % i == 0) && (n % i == 0)) {  
                d /= i;  
                n /= i;  
            }
        }
        if(d==0 && n!=0){ 
            n=1;
            pos = true;
        }
        else if(n==0 && d!=0){
            d=1;
            pos = true;
        }
    }
    
    bool equals(Fraction &f2) {
        return n==f2.n & d==f2.d && pos==f2.pos;
    }
};

class Solution {
public:
    int maxPoints(vector<vector<int>>& points) {
        vector<Fraction *> mat(points.size(), NULL);
        int max_count = 1;
        
        for(int r=0;r<points.size();r++) {
            for(int c=r+1;c<points.size();c++) {
                
                int x1 = points[r][0];
                int y1 = points[r][1];
                int x2 = points[c][0];
                int y2 = points[c][1];
                Fraction *slope = new Fraction(y2-y1, x2-x1);
                mat[c] = slope;
                
            }
            
            // printf("Mat = ");
            // for(int c=r+1;c<points.size();c++) {
            //     printf("%c%d/%d, ", mat[c]->pos ? '+' : '-',mat[c]->n, mat[c]->d);
            // }
            // printf("\n");
            
            for(int i=r+1; i<points.size();i++) {
                int count = 2;
                if(mat[i]==NULL) continue;
                for(int j=i+1;j<points.size();j++) {
                    if(mat[j]!=NULL && mat[i]->equals(*mat[j])) {\
                        // printf("Matched %d and %d\n", i,j);
                        count++;
                        delete mat[j];
                        mat[j] = NULL;
                    }
                }
                delete mat[i];
                mat[i] = NULL;
                max_count = max(count, max_count);
            }
            
        }
        return max_count;
    }
};