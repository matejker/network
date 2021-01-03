# Network
Network is a simple pure Python package for generating, modifying and playing with (even complex) networks. The motivation 
was to create a very small network framework which offers reasonable many attributes and operates relatively fast. It is 
meant to run smoothly for stochastic simulations on networks, unlike a famous [NetworkX](https://github.com/networkx/networkx) 
package.

## Structure
The package itself lives in [/network](./network) folder where is the main *Network* object. All generative network 
models are in [/network/models](./network/models). 

## Installation 
The Network package was developed on Python 3.6.9 and the required packages can be find in [requirements](./requirements)
folder. To install the package from this GitHub repo using `pip`:
```
pip install git+https://github.com/matejker/network.git@0.0.2
``` 

## Usage
Feel more that free to use, modify and copy the code, just follow the [licence](./LICENSE.txt) and cite it:

```tex
@misc{Kerekrety2020,
  author = {Kerekrety, M},
  title = {Network},
  year = {2020},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/matejker/network}}
}
```

## References
[1] Newman, M. E. J. (2010), _Networks: an introduction_, Oxford University Press, Oxford; New York  
[2] Diestel, R. (2002), _Graph Theory_, Springer, Volume 173 of Graduate texts in mathematics, ISSN 0072-5285  
[3] Geeks For Geeks, A computer science portal for geeks, _Depth First Search or DFS for a Graph_, 
https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/  
[4] Geeks For Geeks, A computer science portal for geeks, _Breadth First Search or BFS for a Graph_, 
https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/  
[5] 
