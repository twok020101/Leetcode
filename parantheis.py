class solution:
    def check_square(self,s):
        x=s.count("[")
        y=s.count("]")
        if x==y:
            return True
        else:
            return False

    def check_flower(self,s):
        x=s.count("{")
        y=s.count("}")
        if x==y:
            return True
        else:
            return False

    def check_bracket(self,s):
        x=s.count("(")
        y=s.count(")")
        if x==y:
            return True
        else:
            return False

    def main(self,s: str)->bool:
        if s.find("["):
            x=check_square(self,s)
            print("here")
            if not x:
                return False
        if s.find("{"):
            z=check_flower(self,s)
            if not z:
                return False
        if s.find("("):
            y=check_bracket(self,s)
            if not y:
                return False
        return True

if __name__=="__main__":
    obj=solution()
    print(obj.main("[]()}"))