class StackItemType:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class MyStack:
    def __init__(self):
        """
        Creëert een lege stack.
        Postconditie: een lege stack is gecreëerd.
        """
        self.top = None

    def isEmpty(self):
        """
        Bepaalt of de stack leeg is.
        :return: True als de stack leeg is, anders False.
        Preconditie: geen.
        Postconditie: de staat van de stack is niet gewijzigd.
        """
        return self.top is None

    def push(self, nieuwItem):
        """
        Voegt het element ‘newItem’ toe op de top van een stack.
        :param nieuwItem: Het item om toe te voegen aan de stack.
        :return: True, aangezien het toevoegen altijd succesvol is.
        Preconditie: er is nog plaats op de stack.
        Postconditie: De stack is 1 item groter en de top bevat het toegevoegde item.
        """
        nieuwItem.next = self.top
        self.top = nieuwItem
        return True

    def pop(self):
        """
        Verwijdert het bovenste item van de stack en geeft het terug.
        :return: Een tuple (verwijderd_item, True) als de stack niet leeg is, anders (None, False).
        Preconditie: geen.
        Postconditie: Als de stack niet leeg is, is deze 1 item kleiner.
        """
        if self.isEmpty():
            return (None, False)
        verwijderd = self.top
        self.top = self.top.next
        return (verwijderd.value, True)

    def getTop(self):
        """
        Geeft het bovenste item van de stack terug zonder het te verwijderen.
        :return: Een tuple (bovenste_item, True) als de stack niet leeg is, anders (None, False).
        Preconditie: geen.
        Postconditie: De staat van de stack is niet gewijzigd.
        """
        if self.isEmpty():
            return (None, False)
        return (self.top.value, True)

    def save(self):
        """
        Geeft een lijstweergave van de huidige items in de stack.
        :return: Een lijst van items in de stack.
        Preconditie: geen.
        Postconditie: De staat van de stack is niet gewijzigd.
        """
        elements = []
        huidige = self.top
        while huidige != None:
            elements.insert(0, huidige.value)
            huidige = huidige.next
        return elements

    def load(self, items):
        """
        Laadt een lijst van items in de stack.
        :param items: Een lijst van items om in de stack te laden.
        Preconditie: geen.
        Postconditie: De stack bevat de geladen items, met het laatste item in de lijst als top.
        """
        self.top = None
        for i in items:
            nieuwe_node = StackItemType(i)
            nieuwe_node.next = self.top
            self.top = nieuwe_node


if __name__ == "__main__":
    s = MyStack()
    print(s.isEmpty())
    print(s.getTop()[1])
    print(s.pop()[1])
    print(s.push(StackItemType(2)))
    print(s.push(StackItemType(4)))
    print(s.isEmpty())
    print(s.pop()[0])
    s.push(StackItemType(5))
    print(s.save())

    s.load(['a', 'b', 'c'])
    print(s.save())
    print(s.pop()[0])
    print(s.save())
    print(s.getTop()[0])
    print(s.save())