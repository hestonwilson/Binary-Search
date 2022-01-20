def search(l, x, i, k):
    """Searches for an occurrence of x in list l, from position i to position k - 1 inclusive,
    using recursion. Code attempts to minimize accesses to run as efficiently as possible"""
  

    if k <= i:
      return None
    else:
      
      #j is the midpoint of the list
      j = i + (k - i) // 2
      lj = l[j]
    
      if k == i + 1:
        if lj == x:
          return j
        else:
          return None
          
      if lj == x:
        s = search(l, x, i, j)
        
        if (s is None):
          return j
        else:
          return s
  
      elif lj > x:
        return search(l, x, i, j)
      else:
        return search(l, x, j, k)

    return None
    
