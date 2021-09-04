"""
Author: Arsalan Azmi
Description: JSON Datastore
Package: python-json-datastore
Python Version: 3.9
Year: 2021
Version: 2
"""
# ---- IMPORTS ----
import json as _json

# -----------------
# Class Definitions
# -----------------        
class JSONDatastore():
    """
    Class for JSON Datastore.
    """
    def __init__(self):
        self.store = []
    
    # Public API
    def get(self, docQuery):
        """
        Get matching documents.
        
        Parameters
        ----------
        docQuery : str
            A JSON example query document.
            
        Returns
        -------
        list of str
            A list of matching JSON documents.
        """        
        docQueryDict = _json.loads(docQuery)
        matching = self.__findMatching(docQueryDict)
        
        return matching
        
    def add(self, doc):
        """
        Parameters
        ----------
        doc : str
            JSON document.
        """
        store = self.store
        
        documentDict = _json.loads(doc)
        store.append((doc, documentDict))
    
    def delete(self, docQuery):
        """
        Delete matching documents.
        
        Parameters
        ----------
        docQuery : str
            A JSON example query document.
        """
        store = self.store
        docQueryDict = _json.loads(docQuery)
        
        matchingIndices = self.__findMatchingIndices(docQueryDict)
        
        deleted = 0
        for idx in matchingIndices:
            # Subtracting 'deleted' from index as deleting shifts list to the left.
            del store[idx - deleted]
            deleted += 1
        
    # Private API
    def __findMatching(self, docQueryDict):
        store = self.store
        
        matching = []
        for doc, documentDict in store:
            if matchDict(docQueryDict, documentDict):
                matching.append(doc)
        
        return matching
    
    def __findMatchingIndices(self, docQueryDict):
        store = self.store
        
        matching = []
        for idx, documentDictTuple in enumerate(store):
            if matchDict(docQueryDict, documentDictTuple[1]):
                matching.append(idx)
        
        return matching
 
# -----------------------
# Public Helper Functions
# -----------------------
def matchDict(a, b):
    """
    Helper function to see if dict "a" is a 'subset' of dict "b".
    
    Parameters
    ----------
    a : dict
        A dictionary.
    b : dict
        A dictionary.

    Returns
    -------
    bool
        True is dict "a" is a 'subset' of dict "b",
        False otherwise.
    """
    matching = True
    for key in a:
        if key in b:
            valA = a[key]
            valB = b[key]
            
            if type(valA) in (str, int, float, bool):
                matching = valA == valB
            # If value is list, chech if it subsets.
            elif type(valA) is list:
                matching = set(valA) <= set(valB)
            # Recur if nested dict.
            else:
                matching = matchDict(valA, valB)
                
            if not matching:
                break
        else:
            return False
    return matching