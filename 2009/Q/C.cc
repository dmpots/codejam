#include <string>
#include <iostream>

using namespace std;

const char* target = "welcome to code jam";
const int tsize = 20;
char s[20] = {};

int solve(const string& line) {
  int len = line.size();
  int count = 0;
  uint32_t max = 1 << len;

  for(uint32_t config = 0; config <= max; config++) {
    if(__builtin_popcount(config) != 19) continue;
    
    bool good = true;
    for(int i = 0, j = 0; i < len; i++) {
      if((config >> i) & 1) {
	if(target[j++] != line[i]) {good = false; break;}
	//s[j++] = line[i];
      }
    }
    if(good) {count++; if(count == 10000) count = 0;}
  }
  
  return count;
}


int solve2(const string& line) {
  const int len = line.size();
  const int tsize = 19;
  int count = 0;
  for(int w = 0; w < len; w++) {
    if(line[w] != 'w' || len-w < tsize ) continue;
    for(int e = w+1; e < len; e++) {
      if(line[e] != 'e' || len-e < tsize) continue;
      for(int l = e+1; l < len; l++) {
	if(line[l] != 'l' || len-l < tsize) continue;
	for(int c = l+1; c < len; c++) {
	  cout << c << endl;
	  if(line[c] != 'c' || len-c < tsize) continue;
	  for(int c = c+1; c < len; c++) {
	    cout << " " << c << endl;
	    if(line[c] != 'o' || len-c < tsize) continue;
	    for(int c = c+1; c < len; c++) {
	      cout << "  " << c << endl;
	      if(line[c] != 'm' || len-c < tsize) continue;
	      for(int c = c+1; c < len; c++) {
		if(line[c] != 'e' || len-c < tsize) continue;
		for(int c = c+1; c < len; c++) {
		  if(line[c] != ' ' || len-c < tsize) continue;
		  for(int c = c+1; c < len; c++) {
		    if(line[c] != 't' || len-c < tsize) continue;
		    for(int c = c+1; c < len; c++) {
		      if(line[c] != 'o' || len-c < tsize) continue;
		      for(int c = c+1; c < len; c++) {
			if(line[c] != ' ' || len-c < tsize) continue;
			for(int c = c+1; c < len; c++) {
			  if(line[c] != 'c' || len-c < tsize) continue;
			  for(int c = c+1; c < len; c++) {
			    if(line[c] != 'o' || len-c < tsize) continue;
			    for(int c = c+1; c < len; c++) {
			      if(line[c] != 'd' || len-c < tsize) continue;
			      for(int c = c+1; c < len; c++) {
				if(line[c] != 'e' || len-c < tsize) continue;
				for(int c = c+1; c < len; c++) {
				  if(line[c] != ' ' || len-c < tsize) continue;
				  for(int c = c+1; c < len; c++) {
				    if(line[c] != 'j' || len-c < tsize) continue;
				    for(int c = c+1; c < len; c++) {
				      if(line[c] != 'a' || len-c < tsize) continue;
				      for(int c = c+1; c < len; c++) {
					if(line[c] != 'm' || len-c < tsize) continue; 
					else {count++; if(count > 10000)count=0;}
				      }
				      
				    }

				  }

				}

			      }
	    
			    }

			  }

			}

		      }

		    }
	    
		  }

		}
	      }
	    }
	  }
	}
      }
    }
  }


  return count;
}


int main() {
  int N;
  string input;
  
  cin >> N;
  getline(cin, input);
  for(int i = 1; i <= N; ++i) {
    getline(cin, input);

    int count = solve(input);
    cout << "Case #" << i << ": ";
    if(count < 1000) cout << '0';
    if(count < 100)  cout << '0';
    if(count <  10)  cout << '0';
    cout << count << endl;
  }
  
}
