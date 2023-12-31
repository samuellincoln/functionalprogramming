is_leaf = lambda ttree : "list" in str (type (ttree))
branch = lambda f, el : str (el if not is_leaf (el) else f (el))
in_order = lambda ttree : branch (in_order, ttree [0]) + " " + str (ttree [1]) + " " + branch (in_order, ttree [2])
pre_order = lambda ttree : str (ttree [1]) + " " + branch (pre_order, ttree [0]) + " " + branch (pre_order, ttree [2])
post_order = lambda ttree : branch (post_order, ttree [0]) + " " + branch (post_order, ttree [2]) + " " + str (ttree [1])
print(in_order ([[1, 3, 2], 5, [7, 10, 9]]))
print(pre_order ([[1, 3, 2], 5, [7, 10, 9]]))
print(post_order ([[1, 3, 2], 5, [7, 10, 9]]))
