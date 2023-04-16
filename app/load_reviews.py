def load_reviews(reviews):
    if len(reviews) < 6:
        return reviews
    else:
        first_two = reviews[:3]
        last_two = reviews[-3:]
        combined = first_two + last_two
        return combined