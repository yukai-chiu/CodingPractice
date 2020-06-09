class Solution:
    def backTracking(self, origin, route):
        if len(route) == self.flights+1:
            self.result = route
            return True
        
        for i, nextDest in enumerate(self.flightMap[origin]):
            if not self.visited[origin][i]:
                self.visited[origin][i] = True
                ret = self.backTracking(nextDest, route + [nextDest])
                if ret:
                    return True
                #if we didn't return True, means it's not a valid route
                #so we reset the visited
                self.visited[origin][i] = False
        return False
    
    
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from collections import defaultdict
        self.flightMap = defaultdict(list)
        self.visited = {}
        self.flights = len(tickets)
        self.result = []
        
        for ticket in tickets:
            origin, dest = ticket[0], ticket[1]
            self.flightMap[origin].append(dest)
    
        
        for depart, destination in self.flightMap.items():
            destination.sort()
            self.visited[depart] = [False] * len(destination)
        
        
        
        route = ['JFK']
        self.backTracking('JFK', route)
        return self.result