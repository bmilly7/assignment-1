from product_data import products
# TODO: Step 1 - Print out the products to see the data that you are working with.

#print(products)

# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.

customer_preferences = []
response = ""
while response != "N":
    print("Input a preference:")
    preference = input()
    # Add the customer preference to the list
    customer_preferences.append(preference)
    response = input("Do you want to add another preference? (Y/N): ").upper()
  

# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.
customer_preferences_set = set(customer_preferences)


# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
converted_products = []
for i in products:
    tag_set =  set(i['tags'])
    converted_products.append(tag_set)



# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(converted_products, customer_preferences_set):
    
    count = 0
    for index, tags in enumerate(converted_products):
        matching_tags = tags & customer_preferences_set 
        
        if matching_tags:
            count += 1
            #print(f"index: {index} : {matching_tags}")
        
    
    print(f"There are {count} products with matching preference")



    '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
    '''
    pass




# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_preferences_set):
    list_of_matches = []
    for i in products:
        matches = set(i['tags']) & customer_preferences_set
        if matches:
            list_of_matches.append ([i['name'],matches, len(matches)])
        
        
        
    sorted_list = sorted(list_of_matches, key=lambda x: x[2], reverse=True)

    for name, matches, match_count in sorted_list:
        print(f"- {name} --{match_count}")



    '''
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        list: A list of products containing product names and their match counts.
    '''
    pass



# TODO: Step 7 - Call your function and print the results

count_matches(converted_products, customer_preferences_set)
recommend_products(products, customer_preferences_set)


# DESIGN MEMO (write below in a comment):
# 1. What core operations did you use (e.g., intersections, loops)? Why?
# 2. How might this code change if you had 1000+ products?
'''
Some core operation I took advantage of were loops and also intersections. Loops were valuable in looping through
the list of products and also accessing specific elements. For example, to acess the nested list of tags, I used a loop
to acess the index of the row and then the tags by i['tags'] to convert the nested list of tags into a set. Then I appended the set to a new list that i named converted_products.
This converted products list now holds the nested list of tags in the original products list but as a set for quick comparison.
I used the & operator to find matches between the customers preferences and the product tags since I was now comparig two sets. This found the matches of the users prefernces and the products with the same tags.

I am not to sure how my code would handle larger inputs of data. If you have any corrections or insights, please let me know because I am not too sure.
I also had to make some changes to the functions. I changed one of the parameters to accept "customers_preference_set" becasuse that what made since for me.
I tried to assign the original parameter: customer_tags to my customer_preference_set but it did not work and was undefined. But they represent the same data so I changed the parameter to my variable!
'''