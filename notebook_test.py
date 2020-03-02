from notebook import Notebook, Note


def main():
    n = Note('hello')
    print('Testing of class Note')
    print()
    print(type(n))
    print(dir(n))
    print(n.__str__())
    print(n.__init__)
    print(n.__dict__)
    print(n.tags)
    print(n.memo)
    print(n.creation_date)
    print(n.match('hello'))
    print(n.match('hi'))
    print(n.id)

    nb = Notebook()
    print('Testing of class Notebook')
    print()
    print(type(nb))
    print(dir(nb))
    print(nb.__str__())
    print(nb.__init__)
    print(nb.__dict__)
    print(nb.notes)
    print(nb.new_note('hi'))


if __name__ == "__main__":
    main()
