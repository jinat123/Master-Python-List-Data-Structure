# List storing product data
product_id_list = [1,2,3,4,5]
product_name_list = ["Laptop", "Desk Chair", "Smartwatch","Notebook", "Running Shoes"]
product_category_list = ["Electronics", "Furniture", "Electronics", "Stationery", "Apparel"]
product_price_list = [750, 100, 200, 5, 80]
product_stock_list = [50, 200, 150, 500, 100]
product_supplier_email_list = ["supplier1@gmail.com", "supplier2@gmail.com", "supplier3@gmail.com", "supplier4@gmail.com", "supplier5@gmail.com"]

# print product data
print("Product List:")
for i in range(len(product_id_list)):
    print(f"ID: {product_name_list[i]}, {product_category_list[i]}, {product_price_list[i]}, {product_stock_list[i]}, {product_supplier_email_list[i]}")

# List storing employee data
employee_id_list = [1,2,3,4,5]
employee_name_list = ["John Doe", " Jane Smith", "Mark Johnson", "Lisa Wong", "Paul Mcdonald"]
employee_department_list = ["Sales", "Human Resources", "IT", "Marketing", "Finance"]
employee_age_list = [30, 25, 40, 28, 35]
employee_email_list = ["john.doe@company.com", "jane.smith@company.com", "mark.johnson@company.com", "lisa.wong@company.com", "paul.mcdonald@company.com"]

# Print employee data
print("Employee List:")
for i in range(len(employee_id_list)):
    print(f"ID: {employee_name_list[i]}, {employee_department_list[i]}, {employee_age_list[i]}, {employee_email_list[i]}")

# List storing books data
book_id_list = [1,2,3,4,5]
book_Title_list = ["The Great Gatsby", "To Kill A Mockingbird", "1984", "The Catcher In The Rye", "A Brief History of Time"]
book_author_list = ["F. Scott Fitzgerald", "Harper Lee", "George Orwell", "J.D. Salinger", "Stephen Hawking"]
book_genre_list = ["Fiction", "Fiction", "Dystopian", "Fiction", "Non-Fiction"]
book_published_year_list = [1925, 1960, 1949, 1951, 1988]
book_isbn_list = ["978-0743273565", "978-0060935467", "978-0451524935", "978-0316769488", "978-0553380163"]
book_stock_list = [20, 35, 40, 25, 10]
book_price_list = [15.99, 10.99, 9.99, 8.99, 18.99]

# Print books data
print("Book List:")
for i in range(len(book_id_list)):
    print(f"ID: {book_Title_list[i]}, {book_author_list[i]}, {book_genre_list[i]}, {book_published_year_list[i]}, {book_isbn_list[i]}, {book_stock_list[i]}, {book_price_list[i]}")

# List storing universities data
university_id_list = [1,2,3,4,5]
university_name_list = ["University of the Philippines", "Ateneo de Manila University", "De La Salle University", "University of Santo Tomas", "Polytechnic University of the Philippines"]
university_location_list = ["Quezon City", "Quezon City", "Manila", "Manila", "Manila"]
university_established_year_list = [1908, 1859, 1911, 1611, 1904]
university_type_list = ["Public", "Private", "Private", "Private", "Public"]
university_website_list = ["www.up.edu.ph", "www.ateneo.edu", "	www.dlsu.edu.ph", "www.ust.edu.ph", "www.pup.edu.ph"]

# Print universities data
print("University List:")
for i in range(len(university_id_list)):
    print(f"ID: {university_name_list[i]}, {university_location_list[i]}, {university_established_year_list[i]}, {university_type_list[i]}, {university_website_list[i]}")

# List storing restaurants data
restaurant_id_list = [1,2,3,4,5]
restaurant_name_list = ["Vikings Luxury Buffet", "Antonio's Restaurant", "Mesa Filipino Moderne", "Manam Comfort Filipino", "Ramen Nagi"]
restaurant_location_list = ["Pasay City", "Tagaytay", "Makati City", "Quezon City", "Various Locations"]
restaurant_Cuisine_type_list = ["Buffet", "Fine Dining", "Filipino", "Filipino", "Japanese"]
restaurant_established_year_list = [2011, 2002, 2009, 2013, 2013]
restaurant_website_or_contact_list = ["www.vikings.ph", "www.antoniosrestaurant.ph", "www.mesa.ph", "www.manam.ph", "www.ramennagi.com.ph"]

# Print restaurants data
print("Restaurant List:")
for i in range(len(restaurant_id_list)):
    print(f"ID: {restaurant_name_list[i]}, {restaurant_location_list[i]}, {restaurant_Cuisine_type_list[i]}, {restaurant_established_year_list[i]}, {restaurant_website_or_contact_list[i]}")
