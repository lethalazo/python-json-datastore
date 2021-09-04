"""
Author: Arsalan Azmi
Description: JSON Datastore
Package: python-json-datastore
Python Version: 3.9
Year: 2021
Version: 2
"""
# ---- IMPORTS ----
import json_datastore as _jsd

# -----------------
# Class Definitions
# -----------------
class Main():
    """
    Main runner class.
    """
    def __init__(self):
        self.datastore = _jsd.JSONDatastore()
        self.queries = []
    
    # Public API
    def run(self):
        self.__readInput()
        result = self.__parseAndExecuteQueries()
        for doc in result:
            print(doc)
        
    # Private API
    def __getCommand2Action(self):
        datastore = self.datastore
        return {
            "add": datastore.add,
            "get": datastore.get,
            "delete": datastore.delete
        }
    
    def __parseAndExecuteQueries(self):
        datastore = self.datastore
        result = []
        queries = self.queries

        for query in queries:
            seperatorIndex = query.index(' ')
            command = query[0:seperatorIndex]
            doc = query[seperatorIndex+1:]
            
            command2action = self.__getCommand2Action()
            val = command2action[command](doc)
            if command == "get":
                result.extend(val)
        return result
                
    def __readInput(self):
        queries = self.queries
        line = input()
        while line:
            try:
                queries.append(line)
                line = input()
            except EOFError:
                break

# =============
# Main
# =============
runner = Main()
runner.run()