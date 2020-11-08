def init_database(hotel_name):
    '''
    (Task 3.1)
    '''
    # Implement your code here
    hotel_review_database = []

    for i in range(len(hotel_name)):
        hotel_review_dict = {
            'hotel_name':hotel_name[i],
            'review': {
                'very bad': 0,
                'bad': 0,
                'soso': 0,
                'good': 0,
                'very good': 0
            },
            'average_rating': None,
            'number_of_reviews': 0
        }

        if hotel_review_dict not in hotel_review_database:
            hotel_review_database.append(hotel_review_dict)

    return hotel_review_database

    
def add_review(hotel_review_database, hotel_name, review):
    '''
    (Task 3.2)
    '''

    # check if there's a record for the hotel name
    existing_hotel_review_dict = None # dictionary hotel
    existing_hotel_review_index = None # index

    # find the hotel in list
    # if found break immediately the loop
    for i, hotel_review_dict in enumerate(hotel_review_database):
        if hotel_review_dict['hotel_name'] == hotel_name:
            existing_hotel_review_dict = hotel_review_dict
            existing_hotel_review_index = i
            break

    # check if review is valid item
    # it will check if review belongs to the valid list of review
    valid_review = review in ['very bad', 'bad', 'soso', 'good', 'very good']

    if not valid_review:
        # the review is invalid
        # therefore do nothing and just return the database
        return hotel_review_database

    # if existing_hotel_review_dict contains the hotel dictionary
    # then it is an existing hotel therefore don't create a new instance of it
    if not existing_hotel_review_dict:
        # the hotel does not exist but the review is valid
        # therefore add the hotel with the corresponding review
        hotel_review_dict = {
            'hotel_name': hotel_name,
            'review': {
                'very bad': 0,
                'bad': 0,
                'soso': 0,
                'good': 0,
                'very good': 0
            },
            'average_rating': None,
            'number_of_reviews': 0
        }

        hotel_review_dict['review'][review] = 1
        hotel_review_dict['number_of_reviews'] = 1

        # calculate sum of review
        sum_review = (1 * hotel_review_dict['review']['very bad']) + (2 * hotel_review_dict['review']['bad']) + (3 *  hotel_review_dict['review']['soso']) + (4 * hotel_review_dict['review']['good']) + (5 * hotel_review_dict['review']['very good'])
        # calculate the average rating
        avg_rating = sum_review / hotel_review_dict['number_of_reviews']
        hotel_review_dict['average_rating'] = avg_rating

        # append the hotel to the database
        hotel_review_database.append(hotel_review_dict)
        return hotel_review_database

    # this means here that the hotel does exists and we have a valid review
    # therefore update the hotel accordingly
    existing_hotel_review_dict['review'][review] += 1
    existing_hotel_review_dict['number_of_reviews'] += 1

    # calculate sum of review
    sum_review = (1 * hotel_review_dict['review']['very bad']) + (2 * hotel_review_dict['review']['bad']) + (3 *  hotel_review_dict['review']['soso']) + (4 * hotel_review_dict['review']['good']) + (5 * hotel_review_dict['review']['very good'])
    avg_rating = sum_review / existing_hotel_review_dict['number_of_reviews']
    existing_hotel_review_dict['average_rating'] = avg_rating

    # replace the existing record with the updated one
    hotel_review_database[existing_hotel_review_index] = existing_hotel_review_dict
    return hotel_review_database

def sort_hotels(database, criteria, reverse):
    # Implement your code here
    pass

def extract_hotels(hotel_review_database, conditions):
    hotels = []

    for hotel_review_dic in hotel_review_database:
        # check if the current hotel fulfills the conditions
        if hotel_review_dic['average_rating'] >= conditions['average_rating'] and hotel_review_dic['number_of_reviews'] >= conditions['number_of_reviews']:
            hotels.append(hotel_review_dic['hotel_name'])

    return hotels

def main():
    hotel_name = ['Apple Hotel']
 
    hotel_review_database = init_database(hotel_name)
    print("Initialized hotel review database:\n", hotel_review_database)
    
    hotel_review_database = add_review(hotel_review_database, 'Apple Hotel', 'good')
    print("Updated hotel review database:\n", hotel_review_database)
    
    hotel_review_database = add_review(hotel_review_database, 'Apple Hotel', 'very bad')
    print("Updated hotel review database:\n", hotel_review_database)
    
    hotel_review_database = add_review(hotel_review_database, 'Apple Hotel', 'great')
    print("Updated hotel review database:\n", hotel_review_database)
    
    hotel_review_database = add_review(hotel_review_database, 'Banana Hotel', 'soso')
    print("Updated hotel review database:\n", hotel_review_database)

    # Creating the example hotel list
    # hotel_name = ['Apple Hotel', 'Banana Hotel', 'Cherry Hotel', 'Date Hotel']
    # hotel_review_database = init_database(hotel_name)

    # apple_reviews = ['very bad'] * 0 + ['bad'] * 1 + ['soso'] * 3 + ['good'] * 5 + ['very good'] * 3
    # for review in apple_reviews:
    #     hotel_review_database = add_review(hotel_review_database, 'Apple Hotel', review)
    
    # print(hotel_review_database[0])

    # banana_reviews = ['very bad'] * 3 + ['bad'] * 3 + ['soso'] * 1 + ['good'] * 1 + ['very good'] * 0
    # for review in banana_reviews:
    #     hotel_review_database = add_review(hotel_review_database, 'Banana Hotel', review)
    
    # cherry_reviews = ['very bad'] * 0 + ['bad'] * 0 + ['soso'] * 1 + ['good'] * 1 + ['very good'] * 2
    # for review in cherry_reviews:
    #     hotel_review_database = add_review(hotel_review_database, 'Cherry Hotel', review)
        
    # date_reviews = ['very bad'] * 0 + ['bad'] * 1 + ['soso'] * 1 + ['good'] * 2 + ['very good'] * 2
    # for review in date_reviews:
    #     hotel_review_database = add_review(hotel_review_database, 'Date Hotel', review)
    
    # Test your implementations
    # criteria = ['reviews']
    # criteria = ['average_rating', 'number_of_reviews']
    # criteria = ['number_of_reviews', 'average_rating']

    # sorted_list = sort_hotels(hotel_review_database, criteria, True)
    # print(sorted_list)

if __name__ == "__main__":
    main()
