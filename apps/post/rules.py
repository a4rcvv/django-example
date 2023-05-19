import rules


@rules.predicate
def is_author(user, post):
    if post.user == user:
        print("OK")
        return True
    else:
        print("NG")
        return False


rules.add_perm("post.can_update", is_author)
