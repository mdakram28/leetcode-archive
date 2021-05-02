void swap(int &a,int &b) {
    int t = a;
    a = b;
    b = t;
}

class Line {
public:
    int x1,y1;
    int x2,y2;
    bool horiz;
    
    Line(int x1,int y1,int x2,int y2) {
        horiz = y1==y2;
        if(horiz) {
            if(x1 > x2) swap(x1,x2);
        } else {
            if(y1 > y2) swap(y1,y2);
        }
        this->x1 = x1;
        this->y1 = y1;
        this->x2 = x2;
        this->y2 = y2;
    }
    void print() {
        printf("Line[%d,%d -> %d,%d]\n", x1,y1,x2,y2);
    }
};

class Solution {
    list<Line*> last_lines;
    
    bool intersect(Line *l1, Line *l2) {
        if(l1->horiz == l2->horiz) return false;
        if(l2->horiz) {
            Line *temp = l1;
            l1 = l2;
            l2 = temp;
        }
        if(l1->y1 >= l2->y1 && l1->y2 <= l2->y2 ) {
            if(l2->x1 >= l1->x1 && l2->x2 <= l1->x2) {
                return true;
            }
        }
        return false;
    }
    
    bool check_all_intersects(Line *l1) {
        int i=0;
        for(auto it=last_lines.begin();it!=last_lines.end();it++) {
            if((last_lines.size()-i)%2==0 || i==last_lines.size()-1)continue;
            Line *l2 = *it;
            // printf("Checking intersect with ");
            // l2->print();
            if(intersect(l1,l2)) return true; 
            i++;
        }
        return false;
    }
public:
    bool isSelfCrossing(vector<int>& distance) {
        int cx=0, cy=0;
        int dir_delta[][4] = {
            {0,1},{-1,0},{0,-1},{1,0}
        };
        int cd = 0;
        for(int d: distance) {
            int nx = cx + d*dir_delta[cd][0];
            int ny = cy + d*dir_delta[cd][1];
            Line *l = new Line(cx,cy,nx,ny);
            
            // printf("%d,%d : %d,%d      Moving line ", cx,cy,nx,ny);
            // l->print();
            
            if(check_all_intersects(l)) {
                return true;
            }
            last_lines.push_back(l);
            
            if(last_lines.size()>5){
                Line *del = last_lines.front();
                last_lines.pop_front();
                delete del;
            }
            
            cx=nx;
            cy=ny;
            cd = (cd+1)%4;
        }
        return (cx==0 && cy==0);
    }
};