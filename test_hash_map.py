from hash_map import h_map


if __name__ == "__main__":
     numeric = [
        ('1', 'one'),
        ('2', 'two'),
        ('3', 'three'),
        ('4', 'four')
    ]
hashtable = h_map(numeric)
print('\n Все значения \n')
print(hashtable)
print(f"1 {hashtable.give_value('1')}")