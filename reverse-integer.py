
def reverse(self, x: int) -> int:
        no = x
        rev_no = 0

        is_neg = False
        if no < 0:
            is_neg = True
            no *= -1

        while no > 0:
            rem = no % 10
            rev_no = rev_no*10+rem
            no = no // 10

        if -2**31 < rev_no and rev_no > 2**31-1:
            return 0
        
        if is_neg:
            new_rev = rev_no*-1
            return new_rev
        else:
            return rev_no
        









