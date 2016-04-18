delivery_id_confirmations = [2, 5, 4, 2, 4, 5, 7]

def find_unique_id(delivery_ids):

    id_counts = {}

    for delivery_id in delivery_ids:
        if delivery_id in id_counts:
            id_counts[delivery_id] += 1
        else:
            id_counts[delivery_id] = 1

    for delivery_id, count in id_counts.items():
        if count == 1:
            return delivery_id