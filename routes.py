import sys

class Routes:
    def __init__(self, routesTable={}):
        self.routesTable = routesTable
    
    def distanceBetween(self, cities=[]):
        distance = 0
        for i in range(len(cities)):
            root_node = cities[i]
            if i + 1 < len(cities):
                next_node = cities[i+1]
                if next_node in self.routesTable[root_node]:
                    distance = distance + self.routesTable[root_node][next_node]
                else: 
                    return "There is no route"
        return distance
    
    def numStops(self, start, end, maxStops):
        return self.findRoutes(start, end, 0, maxStops)
    
    def findRoutes(self, start, end, depth, maxStops):
        visited =[]
        routes = 0
        
        if start in self.routesTable and end in self.routesTable:
            depth = depth + 1
            if depth > maxStops:
                return 0
            visited.append(start)

            for adj in self.routesTable[start]:
                if adj == end:
                    routes = routes + 1
                
                if adj not in visited and adj != end:
                    depth = depth - 1
                    routes += self.findRoutes(adj, end, depth, maxStops)
        else:
            return "No Such route"
        
        if start in visited:
            visited.remove(start)
        return routes
    

    def shortestRoute(self, start, end):
        return self.findShortestRoute(start, end, 0, 0)

    def findShortestRoute(self, start, end , weight, shortestRoute, visited=[]):
        if start in self.routesTable and end in self.routesTable:
            visited.append(start)

            for adj in self.routesTable[start]:
                if(adj == end or adj not in visited):
                    weight += self.routesTable[start][adj]
                    
                if adj == end:
                    if shortestRoute == 0 or weight < shortestRoute:
                        shortestRoute = weight
                    visited.remove(start)
                    return shortestRoute
                
                if adj not in visited:
                    shortestRoute = self.findShortestRoute(adj, end, weight, shortestRoute, visited)
                    weight -= self.routesTable[start][adj]
        
        else:
            return "No such route exists"

        if start in visited:
            visited.remove(start)
        
        return shortestRoute

    def numberOfRoutesWithin(self, start, end, maxDistance):
        return self.findNumberOfRoutesWithin(start, end, 0, maxDistance)
    
    def findNumberOfRoutesWithin(self, start, end , weight, maxDistance, routes=0):
        if start in self.routesTable and end in self.routesTable:
            for adj in self.routesTable[start]:
                weight += self.routesTable[start][adj]
                if weight <= maxDistance:
                    if adj == end:
                        routes = routes + 1
                        routes += self.findNumberOfRoutesWithin(adj, end, weight, maxDistance)
                    else:
                        routes += self.findNumberOfRoutesWithin(adj, end, weight, maxDistance)
                        weight -= self.routesTable[start][adj]
                else:
                    weight -= self.routesTable[start][adj]
        else:
            print("No such route")
        
        return routes

    def findPathWithExactStops(self, start, finish, exact):
        count = 0
        visited = []
        path = []

        path.append(start)
        visited.append(start)

        for adjacent_node in self.routesTable[start]:
            if adjacent_node not in visited:
                count = self.printAllPathsUtil(adjacent_node, finish, visited, path, exact, count)
        
        return count

    def printAllPathsUtil(self, start, finish, visited, path, exact, count):
        visited.append(start)
        path.append(start)

        if start == finish:
            if len(path) < exact:
                count = self.findCycle(finish, path, exact, count)
            
            if len(path) == exact + 1:
                print(path)
                count = count + 1
        
        else:
            for adjacent_node in self.routesTable[start]:
                if adjacent_node not in visited:
                    count = self.printAllPathsUtil(adjacent_node, finish, visited, path, exact, count)
        
        path.pop()
        visited.remove(start)

        return count


    def findCycle(self, start, path, exact, count):
        visited = []

        for adj_node in self.routesTable[start]:
            if adj_node not in visited:
                count = self.findCycleUtil(adj_node, start, path, visited, exact, count)
        return count
    

    def findCycleUtil(self, start, end, path, visited, exact, count):
        visited.append(start)
        path.append(start)

        if start == end:
            if len(path) == exact + 1:
                count = count + 1
                print(path)
        else:
            for adj_node in self.routesTable[start]:
                if adj_node not in visited:
                   count = self.findCycleUtil(adj_node, end, path, visited, exact, count)

        path.pop()
        visited.remove(start) 

        return count