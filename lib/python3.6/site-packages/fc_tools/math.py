import numpy as np
import itertools

def perms(V):
  """ P=perms(V)
  Generate all permutations of V, one row per permutation. The lexicographical 
  order is choosen. The result is a numpy array with size N!-by-N, where N 
  is the length of V. 
  
  Parameters
  ----------
  V : list or array of N scalars
  
  Returns
  -------
  P : (N!,N) shaped ndarray
  
  As an example, 'perms ([1, 2, 3])' returns the numpy array
  
  >>> P=perms([1, 2, 3])
  >>> P
  array([[1, 2, 3],
         [1, 3, 2],
         [2, 1, 3],
         [2, 3, 1],
         [3, 1, 2],
         [3, 2, 1]])    
          
  """
  return np.array([x for x in itertools.permutations(V,len(V))])

def combs(V,k):
  """
  C=combs(V,k)
  
  Generate all combinations of V taken k at a time, one row per combination. 
  The lexicographical order is choosen. The result is a numpy array with 
  size N!/(k!(n-k)!)-by-k, where N is the length of V and 1<=k<=N.
  
  Parameters
  ----------
  V : list or array of N scalars
  k : integer (0<=k<=N)
  
  Returns
  -------
  C : (N!/(k!(n-k)!),k) shaped ndarray
  
  As an example:
  
  >>> C=combs([1,2,3,4],2)
  >>> C  
  array([[1, 2],
         [1, 3],
         [1, 4],
         [2, 3],
         [2, 4],
         [3, 4]])
    
  """
  assert (len(V)>=k) and (k>=1)
  return np.array([x for x  in itertools.combinations(V,k)])
