class dp:
    def __init__(self, X, Y):

        self.X, self.Y = X, Y
        self.m, self.n = len(X), len(Y)
        self.dp = [[0]*(self.n+1) for _ in range(self.m+1)]

    def lcs(self):
        for i in range(1, self.m+1):
            for j in range(1, self.n+1):
                if self.X[i-1] == self.Y[j-1]:
                    self.dp[i][j] = self.dp[i-1][j-1] + 1
                else:
                    self.dp[i][j] = max(self.dp[i-1][j], self.dp[i][j-1])
                    
        return self.dp[self.m][self.n]

    def displaytable(self):
        print("-------DP-TABLE-------\n   ", end="")
        for i in " "+self.Y:
            print(i, end="  ")
        print("\n ", end="")
        for i in range(0, len(self.dp)):
            print(self.X[i-1:i] ,self.dp[i])
        

print("-----LCS FINDER-----")
X = input("Enter the first string : ")
Y = input("Enter the second string : ")
table = dp(X, Y)

print("Length of LCS =", table.lcs())

table.displaytable()