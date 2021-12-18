
class Check:

  def check_match(input):

    open = ('({[')
    close = (')}]')
    map = dict(zip(open, close))
    queue = []

    for i in input:
        if i in open:
            queue.append(map[i])
        elif i in close:
            if not queue or i != queue.pop():
                return False
    if not queue:
        return True
    else:
        return False
