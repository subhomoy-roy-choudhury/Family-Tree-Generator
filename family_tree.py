class FamilyTree:

    def __init__(self,value,name):
        self.root = value
        self.name = name
        self.nodes = []

    def insert_member(self,value,name):
        self.nodes.append(FamilyTree(value,name))

    def find_member_DFS(self,tree,value):
        self.key = None
        self.finder(tree,value)
        return self.key

    def find_member_by_name_generation_DFS(self,tree,name,generation):
        self.key = None
        self.finder_by_name_generation(tree,name,generation)
        print(self.key)
        return self.key

    def finder_by_name_generation(self,tree,name,generation):
        if self.name == name and generation==generation :
            self.key = self
        elif tree.nodes != []:
            for i in tree.nodes:
                if name == i.name and generation==generation:
                  self.key = i
                else :
                  self.finder_by_name_generation(i,name,generation=generation+1)

    def finder(self,tree,value):
        if self.root == value :
          return self
        elif tree.nodes != []:
          for i in tree.nodes:
            if value == i.root:
              self.key = i
            else :
              self.finder(i,value)

    def structure(self,tree,length=0):
        line = u'\u2500'
        generation = length//2
        if self.root == tree.root :
          print(f'{tree.root}({tree.name},{generation})')
        elif length == 2 :
          print(f'{" "*(length-2)}|{line*2} {tree.root}({tree.name},{generation})')
        else :
          print(f'{" "*(length-2)}{" "*(length-2)}|{line*2} {tree.root}({tree.name},{generation})')
        if tree.nodes != [] :
          for i in tree.nodes :
            self.structure(i,length=length+2)

        def __repr__(self):
            return f"FamilyTree({self.root},{self.name}): {self.nodes}"

if __name__ == '__main__' :

  tree = FamilyTree(5,'ANIL')
  tree.insert_member(2,"Sunil")
  tree.insert_member(3,'AMAN')
  tree.insert_member(4,'SHAH')
  tree.nodes[1].insert_member(19,"MANKU")
  tree.find_member_DFS(tree,3).insert_member(1,'ABC')
  tree.find_member_DFS(tree,4).insert_member(0,'DEF')
  tree.find_member_DFS(tree,0).insert_member(11,'GHI')
  tree.find_member_DFS(tree,0).insert_member(13,'MNM')
  tree.find_member_DFS(tree,13).insert_member(15,'LOL')
  tree.find_member_DFS(tree,4).insert_member(25,'LaL')
  tree.structure(tree)
  # print(tree)
