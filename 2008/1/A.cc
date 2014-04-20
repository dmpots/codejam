
#include <iostream>
using namespace std;

int64_t solve( int64_t *x,  int64_t *y, int n) {
  sort(x, x+n);
  sort(y, y+n, greater<int>());

  int64_t dotp = 0;
  for(int i = 0; i < n; i++) {
    dotp += x[i] * y[i];
  }
    
  return dotp;
}



int main(int argc, char** argv) {

  int T;
  cin >> T;

  int64_t x[800];
  int64_t y[800];

  for(int t = 1; t <= T; t++) {
    int n;
    cin >> n;

    for(int i = 0; i<n; i++) {
      cin >> x[i];
    }
    for(int i = 0; i<n; i++) {
      cin >> y[i];
    }

    int64_t sol = solve(x, y, n);
    cout << "Case #" << t << ": " << sol << endl;
  }
}
