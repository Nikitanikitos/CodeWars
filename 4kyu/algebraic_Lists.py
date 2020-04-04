class Cons:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

    def to_array(self):
        return [self.head] + (self.tail.to_array() if self.tail is not None else [])

    @classmethod
    def from_array(cls, arr):
        if arr:
            head = arr.pop(0)
            return Cons(head=head, tail=cls.from_array(arr))

    def filter(self, fn):
        while self.tail:
            if fn(self.head):
                return Cons(head=self.head, tail=self.tail.filter(fn))
            else:
                self = self.tail
        else:
            if fn(self.head):
                return Cons(head=self.head, tail=None)

    def map(self, fn):
        head = fn(self.head)
        if self.tail:
            return Cons(head=head, tail=self.tail.map(fn))
        else:
            return Cons(head=head, tail=None)

print(Cons.from_array([1,2,3,4,5]))
print(Cons.from_array([1,2,3,4,5]).filter(lambda n: n > 3).to_array())
print(Cons.from_array(["1","2","3","4","5"]).map(int).to_array())