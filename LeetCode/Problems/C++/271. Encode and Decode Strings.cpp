class Codec {
public:

    // Encodes a list of strings to a single string.
    string encode(vector<string>& strs) {
        stringstream ss;
        
        for(int i=0; i<strs.size();i++){
            ss << setw(4) << setfill('0') << strs[i].size();
            ss << strs[i];       
        }
        return ss.str();
    }

    // Decodes a single string to a list of strings.
    vector<string> decode(string s) {
        vector<string> output;
        int i = 0;

        while(i <s.size()){
            int chunk = stoi(s.substr(i,4));
            i = i+4;
            output.push_back(s.substr(i,chunk));
            i = i + chunk;
        }     
        return output;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.decode(codec.encode(strs));