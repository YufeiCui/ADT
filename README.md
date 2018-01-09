# ADT

Some simple ADTs implemented with [Nodes] for [CSCA48] 
* [Queue] - An ADT that behaves in a FIFO manner
* [Stack] - An ADT that behaves in a LIFO manner

### Behaviours
Queue:
``` python
enqueue(self: 'Queue', data: object) -> None 
dequeue(self: 'Queue') -> object
is_empty(self: 'Queue') -> bool
peak(self: 'Queue') -> object
```

Stack:
``` python 
push(self: 'Stack', data: object) -> None 
pop(self: 'Stack') -> object
is_empty(self: 'Stack') -> bool
peak(self: 'Stack') -> object
```

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [Queue]: <https://github.com/YufeiCui/ADT/blob/master/queue.py>
   [Stack]: <https://github.com/YufeiCui/ADT/blob/master/queue.py>
   [Nodes]: <https://github.com/YufeiCui/ADT/blob/master/node.py>
   [CSCA48]: <https://mathlab.utsc.utoronto.ca/courses/csca48/>
