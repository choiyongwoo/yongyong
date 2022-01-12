#파이썬으로 큐를 구현
class Queue(object):
    def __init__(self):
        self.items= []
        
    def isEmpty(self):
        return not bool(self.items)
    
    def enqueue(self, item):
        #insert(i, x): array의 원하는 위치 i에 x 삽입
        self.items.insert(0, item)
        
    def dequeue(self):
        value= self.items.pop()
        if value is not None:
            return value
        else:
            print('Queue is empty')
            
    def size(self):
        return len(self.items)
    
    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            print('queue is empty')
            
    def __repr__(self):
        return repr(self.items)
    
if __name__== '__main__':
    queue= Queue()
    print('큐가 비었나요? {0}'.format(queue.isEmpty()))
    print('큐에 숫자 0~9를 추가')
    for i in range(10):
        queue.enqueue(i)
    print('큐 크기: {0}'.format(queue.size()))
    print('peek: {0}'.format(queue.peek()))
    print('dequeue: {0}'.format(queue.dequeue()))
    print('peek: {0}'.format(queue.peek()))
    print('큐가 비었나요?{0}'.format(queue.isEmpty()))
    print(queue)
    
#이 코드에서는 리스트의 insert()메서드를 썼지만, 이는 모든 요소가 메모리에서 이동될 수 있으므로 비효율적